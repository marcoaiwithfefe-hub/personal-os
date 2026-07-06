"""
Fetch and summarize CFTC Commitments of Traders (COT) positioning data.

The CFTC publishes a free weekly report showing how different types of
traders are positioned across U.S. futures markets. This script downloads
the current year's "Legacy Futures Only" annual report, matches the rows
for one contract, and prints a net-positioning summary. No API key or
account is required.

Usage:
    python3 cftc.py                    # defaults to GOLD
    python3 cftc.py "E-MINI S&P 500"

Uses only the Python standard library (urllib, zipfile, csv).
"""
from __future__ import annotations

import csv
import io
import sys
import urllib.request
import zipfile
from datetime import date

_COT_BASE_URL = "https://www.cftc.gov/files/dea/history"
_ZIP_MEMBER = "annualof.txt"
_TIMEOUT = 30

DEFAULT_CONTRACT = "GOLD"

# A handful of well-known, liquid futures contracts, mapped to their exact
# CFTC "Market and Exchange Names" string. Extend this dict with your own
# contracts as needed - use the exact name from the report, not a
# substring, since several contracts share overlapping names (e.g. "GOLD"
# vs "MICRO GOLD").
_CONTRACTS: dict[str, str] = {
    "E-MINI S&P 500": "E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE",
    "GOLD": "GOLD - COMMODITY EXCHANGE INC.",
    "10-YEAR T-NOTE": "UST 10Y NOTE - CHICAGO BOARD OF TRADE",
}

# CSV column names used in the CFTC annual file format (deahistfoYYYY.zip)
_COL_MARKET = "Market and Exchange Names"
_COL_DATE = "As of Date in Form YYYY-MM-DD"
_COL_NC_LONG = "Noncommercial Positions-Long (All)"
_COL_NC_SHORT = "Noncommercial Positions-Short (All)"
_COL_CM_LONG = "Commercial Positions-Long (All)"
_COL_CM_SHORT = "Commercial Positions-Short (All)"

_UA = {"User-Agent": "Mozilla/5.0"}


class ConfigError(Exception):
    """Raised when the CFTC report can't be downloaded or parsed."""


def _year_url(year: int) -> str:
    return f"{_COT_BASE_URL}/deahistfo{year}.zip"


def _fetch_year_rows(year: int) -> list[dict]:
    """Download one annual zip and return its CSV rows."""
    url = _year_url(year)
    req = urllib.request.Request(url, headers=_UA)
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
            raw = resp.read()
    except Exception as exc:
        raise ConfigError(f"Failed to download CFTC COT data from {url}: {exc}") from exc

    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            with zf.open(_ZIP_MEMBER) as member:
                raw_bytes = member.read()
                try:
                    text = raw_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    text = raw_bytes.decode("latin-1")
    except Exception as exc:
        raise ConfigError(f"Failed to unzip CFTC data from {url}: {exc}") from exc

    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def _download_csv_rows() -> list[dict]:
    """Fetch current year + prior year annual zips; return deduplicated rows."""
    today = date.today()
    current_year = today.year
    all_rows: list[dict] = []
    for year in [current_year - 1, current_year]:
        try:
            all_rows.extend(_fetch_year_rows(year))
        except ConfigError:
            if year == current_year:
                raise  # current year is required; prior year is best-effort

    # Deduplicate by (market, date) - protects against year-boundary overlaps
    seen: set[tuple[str, str]] = set()
    deduped: list[dict] = []
    for row in all_rows:
        key = (row.get(_COL_MARKET, ""), row.get(_COL_DATE, ""))
        if key not in seen:
            seen.add(key)
            deduped.append(row)
    return deduped


def _match_contract(market_name: str, exact_name: str) -> bool:
    """Return True if market_name is the target contract (case-insensitive, exact)."""
    return market_name.strip().upper() == exact_name.upper()


def _parse_date(date_str: str) -> date:
    """Parse YYYY-MM-DD format."""
    return date.fromisoformat(date_str.strip())


def _percentile(value: float, population: list[float]) -> float | None:
    """Percentile rank of value within population (0-100). None if too little data."""
    if len(population) <= 1:
        return None
    below = sum(1 for v in population if v < value)
    return round(below / len(population) * 100.0, 1)


def get_positioning_summary(contract: str = DEFAULT_CONTRACT) -> dict:
    """Fetch CFTC COT data and summarize net positioning for one contract."""
    contract_key = contract.upper()
    exact_name = _CONTRACTS.get(contract_key)
    if exact_name is None:
        available = ", ".join(_CONTRACTS)
        raise ValueError(f"Unknown contract '{contract}'. Try one of: {available}")

    all_rows = _download_csv_rows()
    rows = [r for r in all_rows if _match_contract(r.get(_COL_MARKET, ""), exact_name)]
    if not rows:
        return {"contract": contract_key, "_error": "no rows found"}

    def _row_date(r: dict) -> date:
        try:
            return _parse_date(r[_COL_DATE])
        except Exception:
            return date.min

    rows_sorted = sorted(rows, key=_row_date)

    def _int(r: dict, col: str) -> int:
        try:
            return int(r[col].replace(",", "").strip())
        except (ValueError, KeyError):
            return 0

    mm_nets = [float(_int(r, _COL_NC_LONG) - _int(r, _COL_NC_SHORT)) for r in rows_sorted]

    latest = rows_sorted[-1]
    mm_net = _int(latest, _COL_NC_LONG) - _int(latest, _COL_NC_SHORT)
    am_net = _int(latest, _COL_CM_LONG) - _int(latest, _COL_CM_SHORT)
    mm_net_change_wk = int(mm_nets[-1] - mm_nets[-2]) if len(mm_nets) >= 2 else 0

    window = mm_nets[-52:] if len(mm_nets) >= 52 else mm_nets
    pct_52w = _percentile(float(mm_net), window)

    return {
        "contract": contract_key,
        "as_of": _parse_date(latest[_COL_DATE]).isoformat(),
        "mm_net": mm_net,
        "am_net": am_net,
        "mm_net_change_wk": mm_net_change_wk,
        "percentile_52w": pct_52w,
    }


def main() -> int:
    contract = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CONTRACT

    try:
        summary = get_positioning_summary(contract)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except ConfigError as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 1

    if "_error" in summary:
        print(f"No data found for {summary['contract']}.")
        return 0

    print(f"{summary['contract']} - as of {summary['as_of']}")
    print(f"  Noncommercial (large speculator) net position: {summary['mm_net']:+,}")
    print(f"  Change vs prior week:                          {summary['mm_net_change_wk']:+,}")
    print(f"  52-week percentile of net position:             {summary['percentile_52w']}")
    print(f"  Commercial (hedger) net position:               {summary['am_net']:+,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
