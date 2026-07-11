# Vault as OS

## The core idea

Three pieces, three jobs:

- **The vault** (this folder of markdown files) is state. Who you are, what you're working on, what happened, what you've learned. Not a cache of it, the actual record.
- **Your agent** (Claude Code, Codex, Gemini CLI, or whichever CLI you're running) is the runtime. It's what reads the state, does whatever work you asked for, and writes the state back.
- **`CLAUDE.md`** is the kernel. It's the file your agent loads automatically at the start of every session in this folder, and it tells the runtime where every kind of information lives and what rules to follow while it works. See `docs/02-routing-kernel.md` for how that file is actually structured.

None of this is a new invention, it's the same read-eval-write loop every stateful program runs, just with markdown as the storage layer and an LLM as the interpreter.

## What a session looks like

1. **Read state.** First response of a session: read the latest `Daily/` note and `Context/me.md`, silently, no "let me check your files" preamble.
2. **Do the work.** Answer the question, write the code, research the thing, whatever was asked.
3. **Route new information.** Anything worth keeping goes to its canonical file, per the table in `CLAUDE.md`. Not a chat reply that evaporates, a file that persists.
4. **Write the session log.** If the session produced real work (not casual chat), append a log to `Daily/YYYY-MM-DD.md` so the next session has a paper trail.

Next session repeats the loop, starting from whatever state the last one left behind.

## Why files beat a chat history

A chat history is a transcript: it's linear, it's tied to one interface, and finding anything in it later means scrolling or re-asking. A vault is structured state:

- **Inspectable.** Every fact lives in a named file you can open, `grep`, diff, or edit yourself, without going through a chat interface at all.
- **Portable.** It's markdown. It doesn't depend on this specific tool, this specific model, or this specific vendor staying around. Point any editor, any future assistant, at the same folder and the state is still there, fully readable.
- **Compounds.** A chat history resets your context every time you close the window. A vault doesn't, today's session log, this week's routed research, last month's decision are all still sitting in their files, ready to be read again. The system gets more useful the longer you run it, because there's more real state behind it, not because the model got smarter.

## This is not magic

The discipline is doing the work. Routing has to actually happen, i.e. new information has to land in the right file, not get left in a chat reply nobody saves. `CLAUDE.md` is what makes that automatic instead of something you have to remember to ask for every time, but it only works if the rules in it stay accurate and get followed. A vault that never gets routed into is just a folder of stale files, same as a chat history nobody re-reads.

The payoff for keeping it running is compounding, not a single big unlock. One week of use gets you a few routed notes and a couple of daily logs. Read after a few months and your agent opens a session already knowing your goals, your open loops, and the reasoning behind decisions you made a while back, because that's all just sitting in files it reads first.
