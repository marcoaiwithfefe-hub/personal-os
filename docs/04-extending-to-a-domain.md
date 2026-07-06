# Extending to a Domain

The vault ships with the machinery (`CLAUDE.md`, `Context/`, `Daily/`, `Knowledge/`, `Projects/`, `memory/`) and one fictional identity to show the shape of it filled in. It doesn't ship with your domains, those get added as you actually need them. Here's the recipe, using `examples/trading/` as the worked example, plus a second sketch so you can see it isn't trading-specific.

## The recipe

**① Pick the domain.** Name it, and decide what a piece of content in it actually looks like, e.g. a note, a data point, a recurring task. `Knowledge/CLAUDE.md` already says one subfolder per domain, don't create it yet, that comes in step ②.

**② Add routing rows + folders.** The root kernel's table already has a generic row, "Domain knowledge (any subject you track) → `Knowledge/{domain}/`", so most new domains don't need a new table row at all, they just need their subfolder, e.g. `Knowledge/markets/`, created the first time a note actually lands there. Only add a dedicated row to the root table if the domain needs structure the generic `Knowledge/{domain}/` row doesn't cover, i.e. its own top-level folder because one flat subfolder isn't enough for how you use it.

**③ (Optional) a live-data script.** If the domain has a public or private data source worth pulling instead of typing in by hand, write a small script that fetches it and prints a summary. `examples/trading/data/fred.py` and `cftc.py` are the pattern: no framework, a `.env` for whatever credential it needs, one clear function that does the fetch, a `main()` that prints and exits non-zero on failure. The script's job stops at the print, routing the output into a note is a session step, per `examples/trading/README.md`.

**④ (Optional) a skill.** If you find yourself running the same multi-step process in this domain often enough that you're re-explaining it each time, e.g. "fetch this, cross-reference it with that note, update this other note", that's worth capturing as a reusable Claude Code skill instead of a one-off set of instructions typed fresh every session.

Steps ③ and ④ are optional because plenty of domains are just notes: reading, a hobby, a project you're tracking by hand. Nothing about the recipe requires a script or a skill, `Knowledge/spanish/` doesn't need either.

## Worked example: trading

`examples/trading/` runs the full recipe:

① Domain: markets, specifically macro data and futures positioning, since it has free, well-documented public sources.
② Folder: `Knowledge/markets/`, created the first time a script's output gets routed into a note, using the existing generic `Knowledge/{domain}/` row, no new table row needed.
③ Scripts: `fred.py` (economic time series) and `cftc.py` (futures positioning), both read-only, no domain-specific config beyond an API key for the one that needs it.
④ Skill: not built out in this repo, left as an exercise, e.g. a skill that runs both scripts for a watchlist and drafts the routed notes in one pass.

`examples/trading/broker-bridge.md` is a variant of step ③ for when the data source is your own brokerage account rather than a public feed, same shape, with one hard addition: read-only, never execution.

## Sketch: a second domain (Alex's bakery)

To see the recipe generalize, here's the same four steps for a domain that has nothing to do with markets, sketched, not built:

① Domain: supplier costs, since flour and butter prices move and Alex wants to see the trend before the next order.
② Folder: `Knowledge/bakery/`, already implied by the example in `Context/me.md`. No new root table row, "Domain knowledge → `Knowledge/{domain}/`" already covers it.
③ Script: a small script hitting the supplier's price page or emailed price sheet, printing the current price per ingredient, the same shape as `fred.py`, i.e. one fetch function, one `main()`, exit non-zero if the page format changed.
④ Skill: a skill that runs the price check every Monday and flags any ingredient that moved more than a set threshold since the last routed note, rather than Alex re-reading the whole price history by hand each week.

Same four steps, same shape, a completely different subject. That's the point, the recipe doesn't know or care what the domain is.
