---
name: harvest
description: Use when the user types /harvest, or asks to scan recent days for repeated patterns worth turning into a rule or a skill.
---

Scan the last ~2 weeks of `Daily/` notes for repeated actions, repeated corrections, or workflows done 3 or more times. Read-only until step 3, nothing gets adopted without the user saying yes.

## 1. Scan

Read every `Daily/YYYY-MM-DD.md` dated within the last 14 days. Grep across them rather than reading each file whole. Look for:

- The same manual step showing up in `Progress` across 3+ days.
- The same correction given more than once, i.e. the user telling Claude the same thing twice because it didn't stick the first time.
- A multi-step workflow (fetch this, cross-reference that, update this note) run the same way 3+ times.

## 2. Propose, don't adopt

For each pattern found, propose exactly one of:

- **A new rule** for root `CLAUDE.md`'s Rules section, if it's a standing behavior Claude should always follow. One line, plus a one-line justification citing where it happened 3+ times.
- **A new skill**, if it's a multi-step process worth capturing as `.claude/skills/{name}/SKILL.md`. One line describing what it would do, plus a one-line justification.

If nothing repeated 3+ times, say so and stop. Don't force a proposal.

## 3. Write the proposal note

Create `Projects/os-maintenance/` if it doesn't exist yet. Write `Projects/os-maintenance/harvest-YYYY-MM-DD.md` (today) with frontmatter `type: harvest`, `date`, `status: active`, `tags: [os-maintenance, harvest]`. One entry per pattern: what was observed, where (wikilink the `Daily/` notes it came from), the proposal, and the justification.

## 4. Ask

Tell the user what you found and ask which proposals, if any, they want adopted. Don't edit `CLAUDE.md` or create a skill file until they say yes to that specific item.
