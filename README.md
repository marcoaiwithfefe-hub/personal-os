# personal-os

A starter vault that turns [Obsidian](https://obsidian.md) plus **any agent CLI** (Claude Code, Codex, Gemini CLI, Grok Builder, opencode with GLM/Qwen/DeepSeek/Kimi…) into a personal operating system. Your agent reads your vault's state at the start of every session, routes new information to the file where it belongs, and writes session logs back when something worth remembering happens. Nothing is stored in a database or a proprietary app; it's all markdown files you can read, search, and edit yourself.

## What's inside

- **A routing kernel** (`CLAUDE.md`): the rules your agent follows every session, i.e. where information lives, how to write it, when to save it.
- **A memory protocol**: identity and preferences in one place, daily logs in another, domain knowledge routed by topic, no catch-all notes.
- **Agent-run setup** (`SETUP.md`): paste it into your CLI, say "set me up", answer a short interview.
- **Three UI directions** (`design.md`): pick a look once; anything your agent builds you later obeys it.
- **One worked example with live data** (`examples/trading/`): a full domain built out end to end, so you can see the pattern applied to something real before you build your own.

Claude Code users get two optional extras in `.claude/skills/` (`harvest`, `optimize`).

This is a template, not a finished product. You fork it, then spend a week actually living in it before it starts to feel like yours.

## Quickstart

1. Install any agent CLI (see `docs/06-bring-your-own-model.md`).
2. Paste `SETUP.md` (or this repo's URL) into it and say **"set me up"**.
3. Answer the questions.
4. It ends with Obsidian open on your vault and a restart test.

If you'd rather skip the command line entirely, see [`QUICKSTART.md`](QUICKSTART.md) for a no-code walkthrough.

Technical readers who want to understand the mechanics before committing: start with `docs/01-04` for how the routing kernel and memory protocol actually work, then read `examples/trading/` for a complete worked domain.

Related reading: Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the same pattern articulated independently; our `docs/05-ingesting-sources.md` adapts its ingest workflow.

## 廣東話版

<!-- CANTO-DRAFT: needs native pass -->

呢個係一個 starter vault，用 [Obsidian](https://obsidian.md) 加**任何一個 AI agent CLI**（Claude Code、Codex、Gemini CLI、Grok Builder、opencode 配 GLM/Qwen/DeepSeek/Kimi 都得），將你嘅筆記本變成一個「個人操作系統」。你個 agent 每次都會先睇吓 vault 入面而家嘅狀態，再將新資訊擺返去啱嘅檔案度，同埋寫返個 session log 落去。所有嘢都係 markdown 檔案，唔使靠邊個 app 或者資料庫，你自己隨時打開睇到、搵到、改到。

呢個係一個 template，唔係一件完成品。你 fork 咗之後，要真係用一個星期先會開始覺得係自己嘅嘢。

**4 步開始：**

1. 裝一個 AI agent CLI（睇吓 `docs/06-bring-your-own-model.md`）。
2. 將 `SETUP.md` 個內容（或者呢個 repo 嘅 link）貼落去，打 **"set me up"**。
3. 照答佢問嘅問題就得。
4. 佢會幫你開埋 Obsidian，仲會叫你做個重啟測試。

如果你想完全唔使打指令，睇吓 [`QUICKSTART.md`](QUICKSTART.md)，有一個唔使識 code 嘅版本。

<!-- /CANTO-DRAFT -->
