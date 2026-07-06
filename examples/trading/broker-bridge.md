# The read-only broker bridge

`fred.py` and `cftc.py` pull public reference data, nobody's money is attached to it. Connecting an actual brokerage account is a different category: now the OS can see what you hold. This note is the pattern for doing that safely, and the only file in this repo that names a specific broker.

## The hard rule

> **Read-only, no exceptions.** The OS may read your positions and prices for context. It never places, modifies, or cancels an order. Execution stays manual, in your broker's own app. There is no automated path from anything Claude reads or writes to an order hitting your account.

This isn't a soft preference, it's the one rule in this whole example that should never bend. A snapshot script that only ever calls read endpoints can't place a bad trade even if a session goes sideways. A script that also wires up write/order endpoints can, the day a prompt or a script bug does something you didn't intend. Keep the two capabilities in different universes: read happens here, execution happens by hand in the broker's app.

## The pattern

1. **A local bridge process.** Several brokers ship a small application you run on your own machine that logs into your account once and then exposes a local API or socket for scripts to query, so a script talks to `localhost`, not to the broker's servers directly with your credentials on every call. [FUTU](https://www.futunn.com/) is one example of a broker with this shape: a local gateway app, plus a Python client library that talks to it.
2. **A snapshot script.** Same shape as `examples/trading/data/fred.py` and `cftc.py`: connect to the local bridge, call the read-only endpoints (positions, quotes, account value), print a summary. No place-order call anywhere in the script, not even commented out, if it isn't in the code it can't accidentally get invoked.
3. **Routed markdown output.** Read the script's output, write it into a note the same way any other domain routes data, e.g. under `Knowledge/markets/`. Same fetch → summarize → route loop as the rest of `examples/trading/`.

Credentials for the bridge (API keys, account tokens) go in a local `.env` file, gitignored, never in the script itself and never in the routed note, exactly like `FRED_API_KEY` in the FRED example. This note doesn't include any real credentials, account numbers, or personal portfolio content, and neither should a real version of it.

## Adapting to a different broker

The pattern only needs two things from a broker's API:

- A way to authenticate once (locally, not per-request) and query positions or prices afterward.
- Read endpoints that are separate from, and don't require enabling, order-placement endpoints.

If a broker's API has both, mirror the three steps above with that broker's own SDK or REST calls in place of the bridge-specific details. If a broker only exposes a combined API where read and write share the same authenticated session, the discipline shifts from "the API can't do it" to "the script never calls it", same hard rule, enforced by what you choose to write into the script rather than by the API's shape.

## What this is not

Not an execution engine. Not a place to automate trade decisions. Not connected, anywhere in this pattern, to a code path that can submit, amend, or cancel an order. If a future version of your own bridge script ever needs to place an order, that's a decision to make deliberately and separately, not something that falls out of extending this pattern.
