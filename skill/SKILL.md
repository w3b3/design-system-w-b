---
name: design-system
description: Load the w-b.dev design system tokens, typography, components, and animation patterns before building any web page, hotsite, or HTML demo. Use proactively whenever building frontend for w-b.dev subdomains, or when the user says "use the design system", "follow the design system", "match the style", or references design.w-b.dev.
---

# w-b.dev Design System

Live reference: https://design.w-b.dev

Apply these tokens and patterns to every page built for any w-b.dev subdomain (or any page the user wants to match this aesthetic).

## Color Tokens

```css
:root {
  --bg: #0e0e0e;           /* Page background — near-black */
  --bg2: #141414;          /* Card/component background — slightly lighter */
  --fg: #f3f1ec;           /* Primary text — warm paper, never pure white */
  --dim: rgba(243,241,236,0.35);    /* Body text, labels, secondary */
  --dimmer: rgba(243,241,236,0.15); /* Meta labels, timestamps, borders */
  --hair: rgba(243,241,236,0.08);   /* Subtle borders, dividers */
  --accent: #d4a853;                /* Highlights, alerts, active states — amber */
  --accent-dim: rgba(212,168,83,0.3); /* Accent borders, hover states */
  --mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
  --helv: Helvetica, "Helvetica Neue", Arial, sans-serif;
}
```

### Core rule: hierarchy through opacity, not hue
Never introduce additional colors. Use the opacity ladder (fg → dim → dimmer → hair) to create depth. The only non-grayscale color is `--accent`.

## Typography

Two typefaces only. No exceptions.

| Role | Face | Weight | Size | Tracking | Use |
|------|------|--------|------|----------|-----|
| H1 / Display | Helvetica | 700 | clamp(42px, 6vw, 72px) | -0.04em | Page titles |
| H2 / Section | Helvetica | 700 | clamp(24px, 3.5vw, 40px) | -0.03em | Section headings |
| H3 / Sub | Helvetica | 700 | clamp(18px, 2.5vw, 28px) | -0.02em | Subsections |
| Body | Helvetica | 400 | clamp(16px, 1.6vw, 19px) | normal | Narrative text, color: --dim, max-width: 680px, line-height: 1.65 |
| Label | JetBrains Mono | 400 | 11px | 0.18em | Section labels, uppercase, color: --dim |
| Data / Mono | JetBrains Mono | 400 | 12-13px | 0.02em | Values, descriptions, metadata, color: --dim |
| Meta | JetBrains Mono | 400 | 10px | 0.16em | Tertiary labels, uppercase, color: --dimmer |

Rules:
- Negative tracking for display (tighter = larger)
- Positive tracking for labels (wider = smaller)
- All display sizes use clamp() — no breakpoints for type
- Body text max-width: 680px always
- `<strong>` in body text promotes to --fg color

## External Dependencies

Only one: Google Fonts for JetBrains Mono.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&display=swap" rel="stylesheet">
```

No frameworks. No React. No Tailwind. Vanilla HTML + CSS + JS only.

## Page Structure

Every page follows this skeleton:

1. **Hero section** — title, subtitle, optional visual. `opacity:1; transform:none` (no reveal animation — immediately visible).
2. **Content sections** — each has: `.label` ("01 // Name"), `.divider`, `h2`, `.body` text, then a component.
3. **Outro section** — summary statement + author attribution link.

Section CSS: `min-height: 100vh; padding: 120px 60px` (desktop), `80px 24px` (mobile).

Two container widths:
- `.section-narrow` — max-width: 900px (text-heavy)
- `.section-wide` — max-width: 1400px (grids, comparisons)

## Components Available

| Component | Class | Use |
|-----------|-------|-----|
| Flow Chain | `.flow-chain` > `.flow-step` | Vertical step sequences, border-left guide |
| Card | `.card` / `.card.accent-card` | Content containers, accent border variant |
| Topology Box | `.topo-box` > `.topo-items` > `.topo-item` | Labeled containers with tag pills, `.hot` accent |
| Stacked Layers | `.layers` > `.layer` / `.layer.hot` | Hierarchical depth visualization |
| Maturity Bar | `.mat-level` / `.mat-level.current` | Numbered progress levels |
| Pipeline Nodes | `.node` / `.node.filled` / `.node.accent` | Circle nodes with arrows between |
| Detection Cards | `.det-card` in `.det-grid` | Grid of specification cards |
| Split Panels | `.split` > `.split-panel.old` + `.split-panel.new` | Side-by-side comparison |

## Animation

All animation is scroll-driven via IntersectionObserver. No animation libraries.

```js
const o = new IntersectionObserver(e => e.forEach(x => {
  if (x.isIntersecting) x.target.classList.add('visible');
}), { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('.section').forEach(s => o.observe(s));
```

Patterns:
- **Section reveal**: `opacity: 0 → 1`, `translateY(30px) → 0` over 0.7s
- **Child stagger**: each nth-child adds 0.1–0.15s transition-delay
- **Breathe**: `opacity 0.3 → 1` over 2s infinite (ambient pulse on idle elements)
- **Draw-in (SVG)**: `stroke-dashoffset 1000 → 0` over 1.2s
- **Scale-in**: `scale(0.5) → scale(1)` over 0.6s (circle nodes appearing)

## Author Attribution

Every page ends with:

```html
<a href="https://linkedin.com/in/brasileiro" target="_blank" rel="noopener"
   style="font-family:var(--mono);font-size:12px;letter-spacing:0.12em;
          color:var(--dim);text-decoration:none;border-bottom:1px solid var(--dimmer);
          padding-bottom:2px">Daniel Brasileiro</a>
```

## Anti-patterns

- No pure white (#fff) — use --fg (#f3f1ec)
- No pure black text — this is a dark theme, text is always light
- No additional colors beyond the --accent amber
- No CSS frameworks or utility classes
- No React/Vue/Svelte — vanilla only
- No external JS dependencies
- No rounded corners on cards (square/sharp edges only)
- No gradients
- No shadows except the Stage canvas shadow in animated pieces
- No emoji in the design (the pages are technical, typographic)
