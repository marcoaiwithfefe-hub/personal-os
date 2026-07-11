"""
Fetch economic data series from the FRED API into your vault.

FRED (Federal Reserve Economic Data) publishes free time series for
inflation, interest rates, employment, and hundreds of other economic
indicators. This script fetches recent observations for one series ID
and prints them, as a minimal example of pulling public data straight
into a note.

Setup:
    1. Get a free API key: https://fred.stlouisfed.org/docs/api/api_key.html
    2. Copy .env.example to .env and fill in FRED_API_KEY
       (or just `export FRED_API_KEY=your_key_here`)

Usage:
    python3 fred.py DGS10        # 10-Year Treasury yield
    python3 fred.py CPIAUCSL     # CPI, all items

Browse series IDs at https://fred.stlouisfed.org/
"""
from __future__ import annotations

import os
import socket
import sys
from datetime import date, timedelta
from pathlib import Path

from fredapi import Fred

DEFAULT_SERIES_ID = "DGS10"  # 10-Year Treasury Constant Maturity Rate
LOOKBACK_DAYS = 400  # wide enough that monthly series (e.g. CPIAUCSL) always have data
MAX_PRINTED = 12  # cap output so daily series stay tidy
REQUEST_TIMEOUT = 30  # fredapi doesn't expose a timeout, so set it socket-wide


class ConfigError(Exception):
    """Raised when required configuration (e.g. FRED_API_KEY) is missing."""


def _load_dotenv(env_path: Path = Path(".env")) -> None:
    """Minimal .env loader: sets os.environ for KEY=VALUE lines not already set."""
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


def get_recent_observations(series_id: str, lookback_days: int = LOOKBACK_DAYS):
    """Fetch recent observations for a FRED series. Requires FRED_API_KEY."""
    _load_dotenv()
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        raise ConfigError(
            "FRED_API_KEY environment variable is not set. "
            "Copy .env.example to .env and add your free key from "
            "https://fred.stlouisfed.org/docs/api/api_key.html"
        )

    socket.setdefaulttimeout(REQUEST_TIMEOUT)
    fred = Fred(api_key=api_key)
    start = (date.today() - timedelta(days=lookback_days)).isoformat()
    data = fred.get_series(series_id, observation_start=start)
    return data.dropna()


def main() -> int:
    series_id = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SERIES_ID

    try:
        data = get_recent_observations(series_id)
    except ConfigError as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        # Redact the API key in case the upstream error echoes the request URL
        key = os.environ.get("FRED_API_KEY")
        detail = str(exc).replace(key, "***") if key else str(exc)
        print(f"Failed to fetch {series_id}: {detail}", file=sys.stderr)
        return 1

    if len(data) == 0:
        print(f"No observations found for {series_id} in the last {LOOKBACK_DAYS} days.")
        return 0

    recent = data.iloc[-MAX_PRINTED:]
    print(f"{series_id} - last {len(recent)} observations:")
    for observed_date, value in recent.items():
        print(f"  {observed_date.date()}  {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
