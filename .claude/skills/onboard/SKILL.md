---
name: onboard
description: Use when the user types /onboard, when Context/me.md still has %%fill this in%% placeholders, or when they ask to set up this vault for the first time.
---

The setup wizard. This is likely someone's first time in this vault, so start by telling them in a sentence or two what's about to happen: a short interview, then Claude fills in their profile and starter folders from the answers.

## 1. Interview

Ask ONE question at a time. Wait for the answer before asking the next. Never batch these into a form.

1. "What's your name, and what do you do day to day?"
2. "What are 2 or 3 areas of your life you want this OS to help you manage?" (a hobby, a business, health, something you're learning, anything)
3. "What's a near-term goal or two you're working toward right now?"
4. "How do you like information presented back to you? Short and direct, detailed, bulleted, something else?"

If the user skips or declines a question, move on. Never invent an answer on their behalf.

## 2. Fill Context/me.md

Open `Context/me.md`. For each section the interview actually answered, replace its `%%fill this in — /onboard does it for you%%` comment and blank fields with the real answer:

- `## Identity`: fill Name and Role from Q1. Leave `- Location:` blank, it wasn't asked, don't guess it.
- `## Goals`: fill `- Near-term:` from Q3. Leave `- Long-term:` blank, it wasn't asked.
- `## Domains I care about`: fill from Q2.
- `## Communication preferences`: fill from Q4.
- `## Working Style` was not covered by this interview. Leave its `%%fill this in — /onboard does it for you%%` comment intact, untouched.

Delete the whole "## Example (delete me)" section, plus the `---` separator above it, once the sections above are filled.

Update frontmatter: `status: template` becomes `status: active`, and the `template` tag is replaced with tags reflecting the domains from Q2.

## 3. Create domain folders

For each domain named in Q2, write one starter note inside `Knowledge/{domain}/`, e.g. `Knowledge/{domain}/overview.md`, with standard frontmatter (`type`, `status: active`, 2+ `tags`) summarizing what the user said about that domain. Writing a real note, not an empty folder, is what satisfies `Knowledge/CLAUDE.md`'s rule against pre-creating empty domain folders.

## 4. Routing table

Root `CLAUDE.md`'s existing row, "Domain knowledge (any subject you track) → `Knowledge/{domain}/`", already covers an ordinary domain. Don't add a new row for a domain that fits there. Only append one if a domain clearly needs its own top-level folder structure beyond a single `Knowledge/{domain}/` subfolder, check with the user before adding it, don't assume.

## 5. First Daily note

Write `Daily/YYYY-MM-DD.md` (today) recording the setup, using the `Focus` / `Progress` / `Open loops` structure from `Daily/CLAUDE.md`. Frontmatter: `type: daily-note`, `date`, `status: active`, `tags: [onboarding, setup]`. Progress lists what got filled and which domain folders got created, wikilinking each. Open loops lists any section left blank (Working Style, Location, Long-term goals) as a reminder to fill in later.

## 6. Close

Tell the user the daily loop: open a session, talk normally, Claude routes and files things as they happen. Corrections they give become permanent rules without them needing to ask for that.
