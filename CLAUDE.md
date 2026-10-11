# Personal OS

This vault is your operating system. All state, i.e. who you are, what you're working on, what happened today, lives in markdown files. Your AI agent reads that state at the start of every session, routes new information to the file where it belongs, and writes session logs back when something worth remembering happens. The vault doesn't just store your notes; it accumulates a memory that compounds.

> If you are reading this as `AGENTS.md` or another generated copy: `CLAUDE.md` is the master. After the user edits `CLAUDE.md`, re-sync every generated copy when asked (see Rules).

## Session Startup

On first response in a session:
1. Silently read the latest note in `Daily/` for recent context.
2. Silently read `Context/me.md` for identity, preferences, and current focus.
3. Silently read `memory/MEMORY.md`; open an individual memory file only when its index line is relevant.
4. Silently read `Context/todo.md` for open tasks.

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
| Open tasks, each tagged with its project or area | `Context/todo.md` |
| Rules for one project only | `Projects/{name}/CLAUDE.md` |
| Rules for every session | Root `CLAUDE.md` (Rules section) |

As you extend this system into your own domains, add a row here rather than dumping new content into an existing one. See `docs/04-extending-to-a-domain.md` for a worked example.

## Frontmatter

```yaml
---
type: daily-note
date: 2025-01-01
status: active
tags: [example, onboarding]
---
```

Standard fields: `type`, `date`, `status`, `tags`. Always include `status:` and 2 or more specific `tags:`. Exempt: router files (`CLAUDE.md`, `README.md`) and `memory/` files (own schema, see `memory/README.md`).

## Obsidian Syntax

- **Wikilinks** for every entity, i.e. people, projects, domains, other notes: `[[Note Name]]`, `[[Note|Display Text]]`. Weave them into sentences naturally.
- **Callouts** (`> [!note]`, `> [!tip]`, `> [!warning]`) for visual structure. Sparingly, 1 to 3 per document.
- Never use `[markdown](links)` for internal vault notes.

## Rules

1. On first response in a session, read the latest `Daily/` note, `Context/me.md`, and `memory/MEMORY.md`.
2. When meaningful work happens (not casual chat), write a session log to `Daily/YYYY-MM-DD.md` before your final reply, without being asked. Append; never rewrite earlier entries.
3. Route new information to its canonical home per the table above. Never a catch-all note.
4. When the user corrects you, save the correction as a rule without asking, in the narrowest file where it applies: `Projects/{name}/CLAUDE.md` if it is about one project (create it if missing), root `CLAUDE.md` if it applies everywhere. A fact about the user goes to `memory/` instead. Say in one line where you saved it.
5. Auto-save state changes without asking. Then report what was saved and where.
6. Every note should stand alone and compose with others, a Lego block, not a fragment.
7. When a project or piece of work finishes, move it to an archive folder rather than leaving it live.
8. Never create files at vault root. Every note lives inside an existing folder.
9. Before writing into any folder, read that folder's `CLAUDE.md` router first. Some CLIs load nested rule files automatically; most don't, so do it explicitly.
10. Every memory write updates `memory/MEMORY.md` in the same action. A correction replaces the stale memory, never duplicates it. Reading the index alone is not memory; maintaining it is.
11. When an answer is worth keeping (a comparison, an analysis, a synthesis), file it into its canonical home per the routing table instead of letting it die in chat history. `Knowledge/{domain}/` only when it IS domain knowledge; project material goes to `Projects/{name}/`; facts about the user go to `memory/`.
12. When the user says "ingest this" or "process this source" (or drops a source file/URL), follow `docs/05-ingesting-sources.md`: read, extract, integrate into existing pages, update cross-references, log the ingest in today's `Daily/` note.
13. `CLAUDE.md` is the master rule file. `AGENTS.md` and other copies are generated. When the user edits `CLAUDE.md` and asks to re-sync, regenerate every copy in full.
14. When the user asks for something to be done later, or work leaves an open item, add one line to `Context/todo.md`: a status tag (`[TODO]`, `[ACTIVE]` or `[BLOCKED]`), the project or area tag, then the task in plain words. Delete the line when it is done. Update the list before your final reply in any session where tasks changed.
15. If you are not sure which project or area a task, note or rule belongs to, ask one short question instead of guessing. Expect these questions often in the first month. When the answer will recur, save it as a rule (Rule 4).

## Anti-Patterns

Do not:
- Put a `# Title` heading that just repeats the filename.
- Create orphan notes with no link from any existing note.
- Update vault files in response to casual chat that produced no new information.
- Write a catch-all "misc" or "notes" file instead of routing.
- Pre-create empty folders for domains you haven't started yet.
