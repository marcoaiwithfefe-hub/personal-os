# Trading: a worked example

Every other example in this repo (`Context/me.md`, the `Daily/` entry) is state you type in yourself. This one is different: it pulls live data from the outside world with two small scripts, then routes what they return into the vault the same way any other note gets routed. It's here to show that "extending the OS to a new domain" isn't limited to writing more markdown by hand, a domain can have a live feed behind it.

Trading is the domain used because it has free, no-nonsense public data sources. Nothing here assumes you trade, or that you use these specific data series. Swap them for whatever a domain of yours actually needs.

## The two scripts

Both live in `examples/trading/data/`.

### `fred.py`: economic data

Pulls a time series from the [FRED](https://fred.stlouisfed.org/) API (Federal Reserve Economic Data): interest rates, inflation, employment, hundreds of other public series.

Setup:

```bash
pip install fredapi
cd examples/trading/data
cp .env.example .env
# edit .env, add a free key from https://fred.stlouisfed.org/docs/api/api_key.html
```

Run from inside `examples/trading/data/` — the script looks for `.env` in the directory you run it from:

```bash
python3 fred.py DGS10       # 10-Year Treasury yield (default)
python3 fred.py CPIAUCSL    # CPI, all items (a monthly series)
```

If you'd rather skip the `.env` file, `export FRED_API_KEY=your_key_here` works from any directory.

Output shape (illustrative, not a live pull, run it yourself for current numbers):

```
DGS10 - last 12 observations:
  2025-01-02  4.51
  2025-01-03  4.48
  2025-01-06  4.55
  ...
  2025-01-17  4.63
```

It fetches the last 400 days so a monthly series like `CPIAUCSL` always has enough history, then prints at most the last 12 observations so a daily series stays readable. No key, no output, it fails loudly with a config error telling you what to fix rather than printing nothing.

### `cftc.py`: futures positioning

Downloads the CFTC's free weekly Commitments of Traders report and summarizes net positioning for one contract. No API key, no account, standard library only.

Run (no `.env` needed, so any directory works — shown from `examples/trading/data/` like above):

```bash
python3 cftc.py                    # defaults to GOLD
python3 cftc.py "E-MINI S&P 500"
python3 cftc.py "10-YEAR T-NOTE"
```

Real output from a live run (CFTC publishes a new report every week, so your numbers will differ):

```
GOLD - as of 2026-06-23
  Noncommercial (large speculator) net position: +172,884
  Change vs prior week:                          -1,501
  52-week percentile of net position:             38.5
  Commercial (hedger) net position:               -197,870
```

Contract names have to match exactly (`_CONTRACTS` in `cftc.py` lists what's available). That's a deliberate choice: substring matching on this data set is a fast way to silently match the wrong contract (`GOLD` vs `MICRO GOLD`, for instance). Ask for something that isn't in the dict and it exits `1` with a clear message on stderr instead of guessing.

## Where the data goes

The scripts only print to stdout. Routing the output into the vault is a session step, not something baked into the script:

1. Run the script.
2. Read the printed summary.
3. Write (or update) a note under `Knowledge/markets/`, e.g. `Knowledge/markets/fred-DGS10.md`, following the same frontmatter and structure any other `Knowledge/` note uses.

A routed note looks like an ordinary vault note, nothing script-specific about its shape:

```markdown
---
type: reference
date: 2025-01-17
status: active
tags: [markets, rates]
---

## DGS10: 10-Year Treasury yield

Pulled via `examples/trading/data/fred.py DGS10`, 2025-01-17.

- Last observation: 4.63 (2025-01-17), up from 4.51 two weeks earlier.
- Tracking this alongside [[Knowledge/markets/cftc-10-year-t-note|10-year T-note positioning]] for the same move.
```

## The pattern

Fetch → summarize → route → build. The script fetches. You (with Claude) summarize what matters into a note that's short enough to reread. Routing puts it under `Knowledge/{domain}/` where every other session can find it. Building means the *next* session doesn't start from zero, it opens the routed note, sees the last reading, and can reason about what changed instead of re-fetching and re-explaining the same context every time.

This is the same loop as everything else in this vault, e.g. session reads state, does work, writes state back. A live-data script is just a faster way to produce the "work" than typing it in by hand.

## Going further: a live broker

If your domain involves an actual brokerage account (not just public reference data), see `examples/trading/broker-bridge.md` for the read-only pattern: a local bridge process plus a snapshot script, with a hard rule that the OS reads positions and prices but never places or modifies an order. This repo doesn't ship a broker-specific script, since every broker's API is different, but the pattern is the same shape as `fred.py` and `cftc.py`.
