# Memory Protocol

Long-term facts about you that should survive across sessions, i.e. not a project's state (that lives in `Projects/`) and not a day's events (that lives in `Daily/`). One fact per file.

## File format

```yaml
---
name: kebab-case-slug
description: one line, used to decide if this memory is relevant to the current task
type: user | feedback | project | reference
---
```

- `name`: kebab-case slug, matches what the file is about.
- `description`: one line. This is what gets scanned to decide whether the memory is worth opening, so make it specific.
- `type`:
  - `user`: a durable fact about you, i.e. a constraint, a preference that isn't tied to a correction.
  - `feedback`: something you corrected. The body adds two extra lines: **Why** (the reasoning) and **How to apply** (the concrete instruction going forward).
  - `project`: state or a decision tied to a specific project.
  - `reference`: a pointer to something external, i.e. an ID, a location, a tool.
- Body: the fact itself. Short. A feedback entry reads as: what happened, why it mattered, what to do differently.

## MEMORY.md

The index. One line per memory file, loaded every session so the fact is available without opening every file. Update the index line whenever you add, change, or remove a memory.

## Rules

- Update, don't duplicate. If a new memory overlaps an existing one, edit the existing file rather than creating a second one that says almost the same thing.
- Delete memories that turn out to be wrong. A stale or incorrect memory is worse than no memory.
- See `_example_feedback.md` for a fictional worked example.
