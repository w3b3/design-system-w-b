# w-b.dev Design System: Blueprint (v2)

A light, bold, wireframe design system for product pages, hotsites and app UIs.

- **Colors:** white paper, one accent, black ink.
- **Shapes:** hard corners, and solid offset shadows that are never blurred.
- **Fonts:** three typefaces.

**Live reference:** [design.w-b.dev](https://design.w-b.dev)

Blueprint came from the [tatame0](https://tatame0.com) marketing site, a gym app whose look borrows from mat grids and engineering drawings. tatame0 stays the **flagship theme**, and other projects reuse the same system by swapping one accent color.

> **v1 is archived.** The original dark, monochrome w-b.dev system (Helvetica plus JetBrains Mono, amber accent) lives in [`legacy/dark-v1/`](legacy/dark-v1/). Pages already built with it keep working, because they inline their own styles.

---

## What's in this repo

```
design-system-w-b/
  index.html          ← The design.w-b.dev style guide: every token and component, plus a live theme/accent picker
  tokens.css          ← Core CSS custom properties (--t-*). Import into any project.
  themes/
    tatame0.css       ← Tatame Red + IBJJF belt palette (flagship, default)
    alertecole.css    ← Slate blue
    neutral.css       ← Ink only, no color
  starter/index.html  ← Copy this to start a new page: ticker, nav, hero, steps, cards, form, footer
  tailwind.css        ← Tailwind v4 @theme map
  theme.json          ← Machine-readable tokens (tooling, iOS)
  skill/SKILL.md      ← Claude Code skill (installed as ~/.claude/skills/design-system/)
  legacy/dark-v1/     ← The archived dark system, its reference page, starter and skill
```

The repo root mirrors the live site, so every file above is also served at `https://design.w-b.dev/<path>`.

## Quick start

### Option A: copy the starter

```bash
cp starter/index.html ~/my-new-page/index.html
```

Fix the two stylesheet links if the page lives elsewhere. Point them at `https://design.w-b.dev/tokens.css` and `https://design.w-b.dev/themes/tatame0.css`.

### Option B: link the tokens

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Space+Mono:wght@400;700&family=Archivo:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="https://design.w-b.dev/tokens.css">
<link rel="stylesheet" href="https://design.w-b.dev/themes/tatame0.css">
```

### Option C: your own accent

Override four variables after `tokens.css`. The picker on design.w-b.dev derives them from any color and copies the CSS for you.

```css
:root {
  --t-accent:      #2563eb;
  --t-accent-deep: #1d4ed8;   /* pressed state, deep shadow */
  --t-accent-tint: #eff6ff;   /* hover fill, <code> background */
  --t-accent-grid: #e8f0fe;   /* background grid lines */
}
```

### Option D: Tailwind v4

```css
@import "tailwindcss";
@import "<path-to>/design-system-w-b/tailwind.css";
@theme { --color-accent: #2563eb; }
```

### Option E: Claude Code

The `design-system` skill is installed at `~/.claude/skills/design-system/`. A copy lives in `skill/` here. Ask Claude to "use the design system" or "match the style".

## Principles

1. **White paper dominates.** Use white surfaces with a faint 44px grid.
2. **One accent.** Use it for CTAs, live status, line-art and construction marks. Never use it for page backgrounds or body text.
3. **Black ink carries text and structure.** Use `#0a0a0a` with 2.5px borders.
4. **Hard corners.** The radius is 0. Exceptions are 6px for inner elements, 7px for the logo "0", and 15px for badge caps.
5. **Solid offset shadows.** Use `6px 6px 0` in the accent or ink. Hover lifts the element by `-2px` and grows the shadow to `9px`. Press sinks it by `3px` and shrinks the shadow to `2px`.
6. **Light only.** Set `color-scheme: only light`. There is no dark mode.

## Tokens (summary)

| Token | Value (tatame0) | Use |
|-------|-----------------|-----|
| `--t-paper` | `#ffffff` | Page and card background |
| `--t-ink` | `#0a0a0a` | Text, borders, structure |
| `--t-accent` | `#e5121f` | The one accent |
| `--t-accent-deep` | `#a60a14` | Pressed state, deep shadow |
| `--t-accent-tint` | `#fdeaea` | Hover fill, code background |
| `--t-accent-grid` | `#f0e4e4` | Background grid |
| `--t-muted` | `#6b6b6b` | Secondary text, labels |
| `--t-amber` | `#b7791f` | Pending or warning only |
| `--t-red*`, `--t-grid` | aliases | Keep tatame0 code working unchanged |

| Role | Face | Style |
|------|------|-------|
| Display | Big Shoulders Display 800/900 | Uppercase, leading .92. Hero `clamp(2.9rem,7.6vw,6rem)` |
| Mono | Space Mono 700 | Uppercase, tracking .14–.18em, .72rem. Kickers, labels, FIG tags |
| Body | Archivo 400–700 | Leading 1.5. Lead 1.18rem/500 |
| Wordmark | Archivo 900 | Lowercase, tracking -.055em |

The full spec, including belt colors, motifs and the SwiftUI guide, is in `tokens.css`, the style guide, and tatame0's `design-system/README.md`.

## Deploy

design.w-b.dev is a static site on rv415 (`~/sites/design.w-b.dev`), behind the rv415 Cloudflare tunnel.

```bash
rsync -av --delete --exclude .git --exclude .claude --exclude 'legacy/dark-v1/wb-design-system-workspace' \
  ./ rv415:~/sites/design.w-b.dev/
```

## Related repos

- **`tatame0/design-system/`:** the tatame0 product's own copy, imported by its web, kiosk and iOS code. Changes to the core system should flow both ways.
- **`ds-blueprint/`:** the first extraction (June 2026), archived on GitHub. This repo has replaced it.

---

Daniel Brasileiro · [linkedin.com/in/brasileiro](https://linkedin.com/in/brasileiro)
