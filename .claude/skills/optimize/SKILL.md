---
name: optimize
description: Use when the user types /optimize, or asks for a vault hygiene audit, dead-link check, or stale-notes review.
---

Audit the vault for hygiene problems. Read-only until the user approves a fix, don't edit anything found in step 1.

## 1. Checks

Audit only the user-content folders: `Context/`, `Daily/`, `Knowledge/`, `Projects/`, `memory/` — `docs/`, `examples/`, and root files are shipped scaffolding, not user content.

Run each of these across those folders (grep and Glob over reading every file whole):

- **Dead wikilinks**: `[[Note Name]]` references where no file with that name exists anywhere in the vault. Exempt a link if its target folder doesn't exist yet and the note carries `status: example` or `status: template` frontmatter.
- **Orphan notes**: any note outside `Context/`, `memory/`, `Daily/`, and router files (`CLAUDE.md`, `README.md`) that no other note wikilinks to. `Daily/` is exempt: daily notes link outward by design, nothing links back to them.
- **Misrouted files**: content sitting in the wrong folder per root `CLAUDE.md`'s routing table, or a file sitting at vault root that isn't one of the exempt root files (`CLAUDE.md`, `README.md`, `LICENSE`).
- **Contradicting routers**: two `CLAUDE.md`/`README.md` files giving conflicting instructions for the same kind of content.
- **Missing frontmatter**: notes outside the exempt set (router files, `memory/`) missing `type`, `status`, or `tags`.
- **Stale actives**: notes with `status: active` whose file modification time is 30+ days old.

## 2. Write the report

Create `Projects/os-maintenance/` if it doesn't exist yet. Write `Projects/os-maintenance/optimize-YYYY-MM-DD.md` (today) with frontmatter `type: optimize`, `date`, `status: active`, `tags: [os-maintenance, optimize]`. Order findings by severity: broken links and misrouted files first, stale notes last. Each item names the exact file and a proposed fix, one line each.

## 3. Fix only what's approved

Present the report to the user. Fix only the items they approve, one at a time or as a batch if they say "do all of it". Never delete or move a file the user didn't approve.
