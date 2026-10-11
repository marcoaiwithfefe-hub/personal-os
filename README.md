# personal-os

A starter vault that turns [Obsidian](https://obsidian.md) plus **any agent CLI** (Claude Code, Codex, Gemini CLI, Grok Builder, opencode with GLM/Qwen/DeepSeek/Kimi…) into a personal operating system. Your agent reads your vault's state at the start of every session, routes new information to the file where it belongs, and writes session logs back when something worth remembering happens. Nothing is stored in a database or a proprietary app; it's all markdown files you can read, search, and edit yourself.

## What's inside

- **A routing kernel** (`CLAUDE.md`): the rules your agent follows every session, i.e. where information lives, how to write it, when to save it.
- **A memory protocol**: identity and preferences in one place, daily logs in another, domain knowledge routed by topic, no catch-all notes.
- **A to-do list and per-project rules**: tasks land in `Context/todo.md`, tagged by project; a correction becomes a rule in the file of the project it is about, so one project's rules never leak into another.
- **Agent-run setup** (`SETUP.md`): paste it into your CLI, say "set me up", answer a short interview.
- **Three UI directions** (`design.md`): pick a look once; anything your agent builds you later obeys it.
- **One worked example with live data** (`examples/trading/`): a full domain built out end to end, so you can see the pattern applied to something real before you build your own.
- **Two self-maintenance skills** (`.claude/skills/`): `/harvest` learns new rules from your own usage; `/optimize` audits vault hygiene. See below.

This is a template, not a finished product. You fork it, then spend a week actually living in it before it starts to feel like yours.

## The two skills

The vault ships with two commands your agent already knows, in `.claude/skills/`:

- **`/harvest`** scans your last two weeks of daily notes for repeated actions and repeated corrections, then proposes new rules or skills based on how you actually work. Nothing is adopted without your yes. This is the part that makes the vault improve itself: you live in it, it learns your patterns, you approve what sticks.
- **`/optimize`** audits the vault for hygiene — dead wikilinks, orphan notes, misrouted files, missing frontmatter, stale notes — and proposes fixes. Read-only until you approve.

Run `/harvest` after a week or two of real use; run `/optimize` whenever the vault starts to feel messy.

## Quickstart — your part

You don't need to know how to code. The agent runs the setup; you answer its questions. What you need: a computer (Mac, Windows, or Linux), about 30 minutes, and an account for whichever AI CLI you pick (Obsidian is free; the CLIs cost money).

1. Install an agent CLI. [Claude Code](https://claude.com/claude-code) is the default recommendation; for Codex, Gemini CLI, Grok Builder, or opencode with any endpoint, see `docs/06-bring-your-own-model.md`.
2. Open the CLI (anywhere — it will fetch this repo itself).
3. Paste the full contents of [`SETUP.md`](SETUP.md), or just this repo's URL, and say **"set me up"**.
4. Answer the short interview: your name, what you do, the 2–3 areas of your life this should manage, how you like information presented, which language your notes should be in, and a look for anything it builds you later.
5. It finishes with Obsidian open on your new vault.
6. The restart test — this is the moment it becomes real: close the CLI completely, reopen it in the vault folder, and tell it one new fact ("I bought a grinder today"). If it files the fact and tells you the path, your OS is running.

**FAQ.** Where does my data live? On your own machine, as plain markdown files — no database, no lock-in. What if I break something? The files are just text; delete the folder and start over from this repo.

Technical readers who want to understand the mechanics before committing: start with `docs/01-04` for how the routing kernel and memory protocol actually work, then read `examples/trading/` for a complete worked domain.

Related reading: Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the same pattern articulated independently; our `docs/05-ingesting-sources.md` adapts its ingest workflow.
