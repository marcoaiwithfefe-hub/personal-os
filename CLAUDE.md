# Personal OS

This vault is your operating system. All state, i.e. who you are, what you're working on, what happened today, lives in markdown files. Claude Code reads that state at the start of every session, routes new information to the file where it belongs, and writes session logs back when something worth remembering happens. The vault doesn't just store your notes; it accumulates a memory that compounds.

## Session Startup

On first response in a session:
1. Silently read the latest note in `Daily/` for recent context.
2. Silently read `Context/me.md` for identity, preferences, and current focus.

Never announce loading. Read, absorb, respond.

## Knowledge Routing

Every piece of information has a home. No catch-all "misc" or "notes" file.

| Type | Route to |
|------|----------|
| Identity, preferences, style, habits | `Context/me.md` |
| Daily journal, session logs | `Daily/YYYY-MM-DD.md` |
| Domain knowledge (any subject you track) | `Knowledge/{domain}/` |
| Project info | `Projects/{name}/` |
| Long-term facts about you (one fact per file) | `memory/` |
| Rules for assistant behavior | Root `CLAUDE.md` (Rules section) |

As you extend this system into your own domains, add a row here rather than dumping new content into an existing one. See `docs/04-extending-to-a-domain.md` for a worked example of adding a domain from scratch.

## Frontmatter

```yaml
---
type: daily-note
date: 2025-01-01
status: active
tags: [example, onboarding]
---
```

Standard fields: `type`, `date`, `status`, `tags`. Always include `status:` and 2 or more specific `tags:`. Exempt from frontmatter: router files (`CLAUDE.md`, `README.md`).

## Obsidian Syntax

- **Wikilinks** for every entity, i.e. people, projects, domains, other notes: `[[Note Name]]`, `[[Note|Display Text]]`. Weave them into sentences naturally, don't just append them.
- **Callouts** (`> [!note]`, `> [!tip]`, `> [!warning]`) for visual structure. Sparingly, 1 to 3 per document.
- Never use `[markdown](links)` for internal vault notes. Obsidian's wikilinks resolve and backlink; markdown links don't.

## Rules

1. On first response in a session, read the latest `Daily/` note and `Context/me.md`.
2. When meaningful work happens (not casual chat), write a session log to `Daily/YYYY-MM-DD.md`.
3. Route new information to its canonical home per the table above. Never a catch-all note.
4. When the user corrects something, save it as a permanent rule or fact. Don't ask permission first.
5. Auto-save state changes without asking. Then report what was saved and where.
6. Every note should stand alone and compose with others, a Lego block, not a fragment that only makes sense in context.
7. When a project or piece of work finishes, move it to an archive folder rather than leaving it live.
8. Never create files at vault root. Every note lives inside an existing folder.

## Anti-Patterns

Do not:
- Put a `# Title` heading that just repeats the filename.
- Create orphan notes with no link from any existing note.
- Update vault files in response to casual chat that produced no new information.
- Write a catch-all "misc" or "notes" file instead of routing.
- Pre-create empty folders for domains you haven't started yet. Create them when content arrives.
