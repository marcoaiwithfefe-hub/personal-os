# The Routing Kernel

`CLAUDE.md` at the repo root is the kernel: the one file your agent loads automatically every session, before it does anything else. It has five jobs, in this order: say what to read on session startup, list where each type of information belongs, define the frontmatter standard, define the Obsidian syntax conventions, and state the operating rules and anti-patterns. This doc walks through each piece as it's actually written in that file, not an idealized version of it.

## The routing table

The heart of the kernel is one table:

| Type | Route to |
|------|----------|
| Identity, preferences, style, habits | `Context/me.md` |
| Daily journal, session logs | `Daily/YYYY-MM-DD.md` |
| Domain knowledge (any subject you track) | `Knowledge/{domain}/` |
| Project info | `Projects/{name}/` |
| Long-term facts about you (one fact per file) | `memory/` |
| Rules for assistant behavior | Root `CLAUDE.md` (Rules section) |

The rule underneath the table matters more than the table itself: **every piece of information has a home, no catch-all "misc" or "notes" file.** If something doesn't fit a row, that's a signal to add a row (and probably a folder), not to shove it into whatever file is closest. `docs/04-extending-to-a-domain.md` walks through adding a row for real.

## Per-folder routers

The root kernel stays short by delegating folder-specific detail to a `CLAUDE.md` inside each folder. Your agent reads the relevant one when it's actually working in that folder, so the root file doesn't have to carry every folder's rules up front. In this repo:

- `Context/CLAUDE.md`: what `me.md` holds and why it's the single copy of identity.
- `Daily/CLAUDE.md`: the daily note structure (`Focus` / `Progress` / `Open loops`) and when to write one.
- `Knowledge/CLAUDE.md`: one subfolder per domain, created on demand, not pre-scaffolded.
- `Projects/CLAUDE.md`: the `README.md` + `specs/`/`research/`/`notes/` shape for a project folder.

`memory/README.md` plays the same role for `memory/`, except its schema is different enough (frontmatter of `name`/`description`/`type` instead of `type`/`date`/`status`/`tags`) that the root kernel explicitly exempts it rather than trying to force one schema over both. See `docs/03-memory-protocol.md` for that folder in full.

## The frontmatter standard

Every note outside the exempted files carries this block:

```yaml
---
type: daily-note
date: 2025-01-01
status: active
tags: [example, onboarding]
---
```

`type`, `date`, `status`, `tags` are the standard fields. `status` and at least two specific `tags` are required, generic tags like `misc` defeat the point. Exempt: router files (`CLAUDE.md`, `README.md`), because they describe the system rather than being a piece of content in it, and everything in `memory/`, because it uses its own schema instead.

## Anti-patterns

The kernel's Anti-Patterns section is short on purpose, five things, all failure modes that quietly turn a routed vault back into a junk drawer:

- A `# Title` heading that just repeats the filename, i.e. wasted space that tells the reader nothing.
- Orphan notes with no link from anything else, i.e. findable only by knowing the exact filename.
- Updating vault files in response to casual chat that produced no new information.
- Writing a catch-all "misc" or "notes" file instead of routing.
- Pre-creating empty folders for domains you haven't started yet, folders show up when content does.

None of these are enforced by tooling, they're enforced by your agent actually following the kernel every session. That's the whole bet this repo makes: a small, always-loaded set of rules keeps a system this loose from decaying into an unsorted pile.
