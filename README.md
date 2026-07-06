# personal-os

A starter vault that turns [Obsidian](https://obsidian.md) plus [Claude Code](https://claude.com/claude-code) into a personal operating system. Claude reads your vault's state at the start of every session, routes new information to the file where it belongs, and writes session logs back when something worth remembering happens. Nothing is stored in a database or a proprietary app; it's all markdown files you can read, search, and edit yourself.

## What's inside

- **A routing kernel** (`CLAUDE.md`): the rules Claude follows every session, i.e. where information lives, how to write it, when to save it.
- **A memory protocol**: identity and preferences in one place, daily logs in another, domain knowledge routed by topic, no catch-all notes.
- **Starter skills**: small, composable instructions Claude can call on for recurring tasks.
- **One worked example with live data** (`examples/trading/`): a full domain built out end to end, so you can see the pattern applied to something real before you build your own.

This is a template, not a finished product. You fork it, then spend a week actually living in it before it starts to feel like yours.

## Quickstart

1. Install [Obsidian](https://obsidian.md) (free).
2. Install [Claude Code](https://claude.com/claude-code).
3. Clone this repo, or click "Use this template" on GitHub, then open the folder in Obsidian as a vault.
4. Run `claude` inside the folder and type `/onboard`.
5. Live in it daily. Tell Claude what happened, what you learned, what changed. It files everything.

If you'd rather skip the command line entirely, see [`QUICKSTART.md`](QUICKSTART.md) for a no-code walkthrough.

Technical readers who want to understand the mechanics before committing: start with `docs/01-04` for how the routing kernel and memory protocol actually work, then read `examples/trading/` for a complete worked domain.

## 廣東話版

<!-- CANTO-DRAFT: needs native pass -->

呢個係一個 starter vault，用 [Obsidian](https://obsidian.md) 加 [Claude Code](https://claude.com/claude-code)，將你嘅筆記本變成一個「個人操作系統」。每次同 Claude 傾偈，佢會先睇吓 vault 入面而家嘅狀態，再將新資訊擺返去啱嘅檔案度，同埋寫返個 session log 落去。所有嘢都係 markdown 檔案，唔使靠邊個 app 或者資料庫，你自己隨時打開睇到、搵到、改到。

呢個係一個 template，唔係一件完成品。你 fork 咗之後，要真係用一個星期先會開始覺得係自己嘅嘢。

**5 步開始：**

1. 裝 [Obsidian](https://obsidian.md)（免費）。
2. 裝 [Claude Code](https://claude.com/claude-code)。
3. Clone 呢個 repo，或者喺 GitHub 度撳 "Use this template"，然後喺 Obsidian 度打開個 folder 做 vault。
4. 喺個 folder 入面行 `claude`，打 `/onboard`。
5. 每日用。發生咗咩、學到咩、變咗咩，同 Claude 講，佢會幫你歸檔。

如果你想完全唔使打指令，睇吓 [`QUICKSTART.md`](QUICKSTART.md)，有一個唔使識 code 嘅版本。

<!-- /CANTO-DRAFT -->
