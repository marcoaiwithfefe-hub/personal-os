# design.md — taste insurance

At setup, the user picked a direction: 1 (Neobrutalist), 2 (Editorial serif), or 3 (Swiss minimal). Whenever the agent builds UI later — dashboards, generated pages, any HTML surface — it obeys three things together: the picked direction's tokens and layout rules below, the shared dashboard contract (section 6), and the anti-slop constraints (section 5). If the agent doesn't know which direction was picked, ask before building; don't default silently.

## Direction 1 — Neobrutalist

Bold, loud, high-contrast. Flat color blocks with hard edges, not soft cards.

**Palette tokens:**
```css
--bg: #F5F1E8;
--ink: #111111;
--accent: #FF4D00;
--panel: #FFFFFF;
--border: #111111;
```

**Type:** Latin headings in Archivo Black, Latin body in Inter. CJK text in Noto Sans TC.

**Layout rules:**
- Borders: 3–4px solid, always `var(--border)`.
- Shadows: hard offset only, `4px 4px 0 #111` — no blur, no spread.
- Border-radius: zero, everywhere.
- Color: flat blocks, no gradients.
- Labels: chunky, uppercase, letter-spaced.

**Sample snippet:**
```html
<style>
  .hero { background: var(--panel); border: 4px solid var(--border);
    box-shadow: 4px 4px 0 #111; padding: 24px; margin-bottom: 16px; }
  .hero h1 { font-family: "Archivo Black", sans-serif; font-size: 2rem;
    text-transform: uppercase; margin: 0; color: var(--ink); }
  .stat-card { background: var(--accent); border: 3px solid var(--border);
    box-shadow: 4px 4px 0 #111; padding: 16px; display: inline-block; }
  .stat-card .label { font-family: Inter, sans-serif; font-size: 0.75rem;
    text-transform: uppercase; letter-spacing: 0.08em; color: #FFFFFF; }
  .stat-card .value { font-family: "Archivo Black", sans-serif; font-size: 2.5rem;
    color: #FFFFFF; }
</style>
<div class="hero"><h1>Today's Focus</h1></div>
<div class="stat-card"><div class="label">Open Loops</div><div class="value">4</div></div>
```

## Direction 2 — Editorial serif

Calm, print-like. Reads like a well-set page, not an app.

**Palette tokens:**
```css
--bg: #FAF7F2;
--ink: #1A1815;
--accent: #8B2500;
--rule: #D8D2C6;
```

**Type:** Latin headings and body both in Newsreader. CJK text in Noto Serif TC.

**Layout rules:**
- Single column, max width 68ch.
- Dividers are hairline rules (`border-top: 1px solid var(--rule)`), never boxes or cards.
- Whitespace is generous; let sections breathe rather than compressing.
- Section labels are small-caps, not bold or uppercase.
- No shadows anywhere.

**Sample snippet:**
```html
<style>
  body { background: var(--bg); color: var(--ink); font-family: Newsreader, serif;
    max-width: 68ch; margin: 0 auto; padding: 32px; }
  .masthead { border-bottom: 1px solid var(--rule); padding-bottom: 12px;
    margin-bottom: 24px; display: flex; justify-content: space-between; }
  .masthead .date { font-variant: small-caps; letter-spacing: 0.04em; color: var(--accent); }
  .stat-list { list-style: none; padding: 0; margin: 0; }
  .stat-list li { border-top: 1px solid var(--rule); padding: 10px 0;
    display: flex; justify-content: space-between; }
  .stat-list .label { font-variant: small-caps; color: var(--ink); }
  .stat-list .value { color: var(--accent); }
</style>
<div class="masthead"><h1>Daily Brief</h1><span class="date">12 July 2026</span></div>
<ul class="stat-list"><li><span class="label">Open Loops</span><span class="value">4</span></li></ul>
```

## Direction 3 — Swiss minimal

Clean grid, no decoration. Hierarchy comes from size and position, not ornament.

**Palette tokens:**
```css
--bg: #FFFFFF;
--ink: #0A0A0A;
--accent: #0033CC;
--grid: #EDEDED;
```

**Type:** Latin in Inter with tight tracking. CJK text in Noto Sans TC.

**Layout rules:**
- Strict 12-column grid; every block snaps to it.
- Everything left-aligned, no centered text or elements.
- `var(--accent)` appears at most twice per view — spend it deliberately.
- No decoration: no icons, no borders-as-ornament, no background tints.
- Hierarchy is size only (font-size and weight steps), not color or boxes.

**Sample snippet:**
```html
<style>
  .grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 8px;
    background: var(--bg); color: var(--ink); font-family: Inter, sans-serif;
    letter-spacing: -0.01em; padding: 24px; }
  .header { grid-column: 1 / 13; border-bottom: 1px solid var(--grid);
    padding-bottom: 8px; margin-bottom: 8px; }
  .header h1 { font-size: 1.25rem; font-weight: 600; margin: 0; }
  table { grid-column: 1 / 9; border-collapse: collapse; width: 100%; }
  th, td { text-align: left; padding: 6px 0; border-bottom: 1px solid var(--grid);
    font-size: 0.875rem; font-weight: 400; }
  th { color: var(--accent); font-weight: 600; }
</style>
<div class="grid">
  <div class="header"><h1>Projects</h1></div>
  <table><tr><th>Name</th><th>Status</th></tr><tr><td>Macro Sync</td><td>Active</td></tr></table>
</div>
```

## Anti-slop constraints

Apply to all three directions, no exceptions:

1. No indigo/violet gradients.
2. No gradient-clipped headline text.
3. No glassmorphism or backdrop-blur panels.
4. No glowing status dots.
5. No pastel rounded-square icon tiles.
6. No emoji used as UI icons.
7. No "tasteful terminal" look (mono font + near-black background + neon accent + grid lines + glow, stacked together).
8. No decorative highlight bars.
9. No oversized drop shadows (Direction 1's flat offset shadow is the one exception — it's structural, not atmospheric).
10. No badge/pill spam.
11. No AI-drawn SVG mascots or illustrations.

## Shared dashboard contract

Every dashboard the agent builds, regardless of direction, has:

- **Panels:** today's `Daily/` focus + open loops, active projects list, memory count + 3 latest memories.
- **Data sources:** latest `Daily/` note, `Projects/` folder names, `memory/MEMORY.md`.
- **Privacy:** local file only. Never deploy, never upload, never expose over a network.
- **Delivery:** one static, self-contained HTML file the agent generates. No server, no framework, no build step. Regenerate on request by re-running the same generation step against current vault state.

## Build prompt template

Copy-paste this to have the agent build the dashboard:

```
Read design.md. Build my dashboard as a single static HTML file per the shared dashboard contract, in direction N. Data from my actual vault files. Regenerate it when I ask.
```

Replace `N` with 1, 2, or 3.
