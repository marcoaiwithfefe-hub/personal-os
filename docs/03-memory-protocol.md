# The Memory Protocol

`memory/` holds a different kind of fact than the rest of the vault: durable, cross-cutting things about you that aren't tied to a single day (`Daily/`) or a single project (`Projects/`), i.e. a standing preference, a correction you gave once and don't want to repeat. `memory/README.md` is the router for this folder, exempted from the general note frontmatter standard because its schema is purpose-built for this kind of fact.

## One fact per file

Each memory is its own file. Not a running log, not a folder of related facts merged into one document, one file per fact. Splitting them keeps each one short enough that recalling it means reading one small file, not scanning a long one for the paragraph that matters.

## Frontmatter

```yaml
---
name: kebab-case-slug
description: one line, used to decide if this memory is relevant to the current task
type: user | feedback | project | reference
---
```

- `name`: kebab-case, matches what the file is about.
- `description`: one line, specific enough that scanning it alone tells you whether to open the file.
- `type`: `user` (a durable fact or preference not tied to a correction), `feedback` (something you corrected), `project` (state or a decision tied to a specific project), or `reference` (a pointer to something external, i.e. an ID, a location, a tool).

A `feedback` memory's body carries two extra lines beyond the fact itself, **Why** (the reasoning behind the correction) and **How to apply** (the concrete instruction going forward). `memory/_example_feedback.md` is the worked example: Alex correcting recipe units from imperial to metric, with the reasoning (the kitchen scale and supplier packaging are already metric, mid-bake conversion introduces rounding errors) and the instruction (default to metric in `Knowledge/bakery/`, convert old notes to metric next time they're touched, don't leave a note in mixed units).

## `MEMORY.md`: the index

One line per memory, kept in `memory/MEMORY.md`. This is the file that actually gets read, in full, at the start of a session, that's on top of the `Daily/` and `Context/me.md` reads the root kernel already does for every session, so a complete session startup touches three files, not two. Individual memory files only get opened when their one-line description looks relevant to whatever the session is actually doing. That's the whole point of keeping descriptions specific: a vague description means opening the file to find out if it matters, which defeats the reason the index exists.

Update the index line whenever a memory is added, changed, or removed, an index that's out of sync with the files it points to is worse than no index.

## Update, don't duplicate

If a new memory overlaps an existing one, edit the existing file. Don't create a second file that says almost the same thing, that's how a `memory/` folder ends up with three near-duplicate entries and no way to tell which one is current. And when a memory turns out to be wrong, delete it outright, a stale or incorrect memory steering a future session is worse than having no memory of that fact at all.
