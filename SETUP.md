# SETUP — read this whole file, then run it

You, the AI agent reading this, are setting up a Personal OS for the user: an Obsidian vault they talk to daily, where you route information into markdown files and it compounds. The user may not know how to code. You do every step; they only answer questions and click installer buttons.

Canonical repo: `https://github.com/marcoaiwithfefe/personal-os`
(If the user pasted only this file, that URL is your fetch target. Normalize any GitHub form they give you — `/blob/`, `/raw/`, `.git` — back to that repo root.)

Run the phases in order. Announce each phase in one short line. Ask ONE question at a time.

## Phase 0 — Detect

Determine, without asking the user unless a check fails:
- Which CLI you are (Claude Code / Codex CLI / Gemini CLI / opencode / Grok Builder / other).
- Whether `git` exists (`git --version`).
- OS (macOS / Windows / Linux).

Then tell the user honestly what approvals to expect: most CLIs ask permission for shell commands and file writes, so they'll approve a handful of prompts (or enable their CLI's auto-accept mode if they're comfortable). This is normal, not an error.

## Phase 1 — Fetch

Skip this phase entirely if you're already inside the repo (a folder containing this SETUP.md alongside CLAUDE.md).

- With git: `git clone https://github.com/marcoaiwithfefe/personal-os` into a location the user confirms (default: their home or Desktop), then work inside it.
- No git, macOS/Linux: `curl -L https://github.com/marcoaiwithfefe/personal-os/archive/refs/heads/main.tar.gz | tar xz`, rename the extracted folder `personal-os`.
- No git, Windows: walk the user through the browser route — open the repo page, green **Code** button → **Download ZIP** → right-click the ZIP → **Extract All**. Beware the nested-folder trap: after extraction, confirm the working folder is the one that DIRECTLY contains `CLAUDE.md` (not a folder containing another `personal-os` folder).

End of phase check: `CLAUDE.md`, `SETUP.md`, `Daily/`, `Context/`, `memory/` all present in the working folder. State the absolute path to the user; this is their vault path, they'll need it twice more.

## Phase 2 — Interview

One question at a time. If they skip one, move on; never invent answers.

1. "What's your name, and what do you do day to day?"
2. "What are 2 or 3 areas of your life you want this OS to help you manage?" (hobby, business, health, learning, anything)
3. "What's a near-term goal or two you're working toward right now?"
4. "How do you like information presented back to you? Short and direct, detailed, bulleted, something else?"
5. "Which language should I write your notes in — English, 廣東話, or 普通話? If Chinese: 繁體 or 簡體?"
6. "Pick a look for anything I build you later (dashboards, pages). Open `design.md` if you want details: 1 = Neobrutalist (bold, loud), 2 = Editorial serif (calm, print-like), 3 = Swiss minimal (clean grid). Just say 1, 2, or 3."
7. "This vault ships with a worked trading example (`examples/trading/`) so you can see the pattern. Keep it for reference, or delete it?"

## Phase 3 — Wire rule files

`CLAUDE.md` is the master; never edit it in this phase.

- If you are Codex CLI, opencode, Grok Builder, or any CLI whose native rule file is `AGENTS.md`: write `AGENTS.md` as a FULL copy of `CLAUDE.md`'s content, prefixed with this exact header line:
  `<!-- Generated from CLAUDE.md — edit CLAUDE.md, then ask your agent to re-sync. -->`
  A one-line pointer is NOT enough; your future sessions will only load this file.
- If you are Gemini CLI: write `GEMINI.md` containing exactly:
  `@./CLAUDE.md`
- If you are Claude Code: nothing to generate, `CLAUDE.md` is already native.
- If you are something else: find your CLI's project-rules file convention and apply the full-copy treatment.

## Phase 4 — Personalize

1. Fill `Context/me.md` from answers 1–5 (the file's comments say what goes where). Delete the whole "Example (delete me)" section. Set `status: active`, replace the `template` tag with domain tags. Record the language policy and design pick (e.g. `Design direction: 2 — editorial serif`) under Communication preferences.
2. Seed each domain from answer 2: one real starter note `Knowledge/{domain}/overview.md` with frontmatter (`type: note`, `status: active`, 2+ tags) summarizing what they told you. Never an empty folder.
3. Reset memory: delete `memory/_example_feedback.md` AND its line in `memory/MEMORY.md` (the Alex recipe example). The index must contain only the user's own memories from here on.
4. If answer 7 was delete: remove `examples/trading/`, then patch every reference to it in `README.md` and `docs/` so no dead link remains.
5. Write today's first `Daily/` note per `Daily/CLAUDE.md` (Focus / Progress / Open loops), logging the setup. Open loops = any interview question they skipped.

## Phase 5 — Verify (run it yourself, report results)

- `CLAUDE.md` and your generated rule file(s) exist and are non-empty; the generated copy contains the routing table (grep for `Knowledge Routing`).
- Link check, scoped: in `Context/me.md`, today's `Daily/` note, `memory/MEMORY.md`, and any file you patched — every `[[wikilink]]` target exists. Shipped teaching examples (`Daily/2025-01-01-example.md`) are exempt.
- Memory round trip: create one real memory from the interview (e.g. their presentation preference) as `memory/` file + index line, close your mental context, then re-read ONLY `memory/MEMORY.md` and prove you can recover the fact from the index line.
- Daily note conforms to `Daily/CLAUDE.md` structure.

Report each check pass/fail. Fix fails before moving on.

## Phase 6 — Demo

Ask the user to tell you one true thing that happened this week. Route it live: file it in the right place per the routing table, then tell them the file path and why it went there. This is the OS working.

## Phase 7 — Obsidian

Have the user install Obsidian (free, [obsidian.md](https://obsidian.md)), then: Open folder as vault → pick the vault path from Phase 1. Success check they can see: the left sidebar shows `Daily`, `Context`, `Knowledge`, and today's note is in `Daily/`.

## Phase 8 — Restart probe (the real test)

Tell the user: close this CLI completely, reopen it in the vault folder, and tell the new session one new fact (anything). The new session — without this SETUP.md in context — must route it to the right file and say where it put it. That proves the rule file actually loads. If the new session behaves like a generic chatbot instead, the rule-file wiring failed: re-open SETUP.md and re-run Phase 3.

That's it. Daily loop from here: open a session, talk normally, the agent files everything. Corrections you give become permanent memories without asking.
