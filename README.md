# w-b.dev Design System

<img width="1097" height="495" alt="image" src="https://github.com/user-attachments/assets/ae9b5498-3d1e-42ac-a43d-e5bffdea0992" />

A dark monochrome design system for publishing single-page technical hotsites. Two typefaces. One accent color. Scroll-driven animations. Zero frameworks.

**Live reference:** [design.w-b.dev](https://design.w-b.dev)

---

## What's in this repo

```
design-system-w-b/
  starter/
    index.html          ← Copy this to start a new page. All tokens, all components, scroll observer included.
  reference/
    index.html          ← The design.w-b.dev reference page (live demo of every token and component).
  skill/
    SKILL.md            ← Claude Code skill definition. Install it and Claude builds pages on-system.
  tokens.css            ← Standalone CSS custom properties — import into any project.
  README.md             ← You are here.
```

## Quick start

### Option A: Copy the starter template

```bash
cp starter/index.html ~/my-new-page/index.html
# Edit the content, keep the tokens and components
```

The starter includes every component (flow chains, cards, topology boxes, layers, maturity bars, pipeline nodes, split panels, timeline/roadmap) and the scroll observer. Delete what you don't need.

### Option B: Import just the tokens

```html
<link rel="stylesheet" href="tokens.css">
```

Or copy the `:root` block into your own `<style>`.

### Option C: Use with Claude Code

```bash
# Install the skill (one-time)
cp -r skill/ ~/.claude/skills/design-system/

# Then in any Claude Code session:
# /design-system
# or just ask Claude to "build a page following the design system"
```

## Design tokens

### Colors

| Token | Value | Use |
|-------|-------|-----|
| `--bg` | `#0e0e0e` | Page background |
| `--bg2` | `#141414` | Card/component background |
| `--fg` | `#f3f1ec` | Primary text — warm paper, never `#fff` |
| `--dim` | `fg @ 0.35` | Body text, labels, secondary content |
| `--dimmer` | `fg @ 0.15` | Meta labels, timestamps, subtle borders |
| `--hair` | `fg @ 0.08` | Card edges, dividers |
| `--accent` | `#d4a853` | Highlights, alerts, active states |
| `--accent-dim` | `accent @ 0.3` | Accent borders, hover states |

**Core rule:** hierarchy through opacity, not hue. Never introduce additional colors.

### Typography

| Role | Face | Weight | Size | Tracking |
|------|------|--------|------|----------|
| Display / H1 | Helvetica | 700 | clamp(42px, 6vw, 72px) | -0.04em |
| Section / H2 | Helvetica | 700 | clamp(24px, 3.5vw, 40px) | -0.03em |
| Sub / H3 | Helvetica | 700 | clamp(18px, 2.5vw, 28px) | -0.02em |
| Body | Helvetica | 400 | clamp(16px, 1.6vw, 19px) | normal |
| Label | JetBrains Mono | 400 | 11px | 0.18em |
| Data | JetBrains Mono | 400 | 12-13px | 0.02em |
| Meta | JetBrains Mono | 400 | 10px | 0.16em |

Two typefaces. No exceptions. Tighter tracking = larger type. Wider tracking = smaller type.

### Spacing

| Context | Value |
|---------|-------|
| Section padding | 120px 60px (desktop), 80px 24px (mobile) |
| Narrow container | max-width: 900px |
| Wide container | max-width: 1400px |
| Component gap | 50-60px |
| Card padding | 24-28px |
| Grid gap | 24px |

## Components

All components follow the same reveal pattern: hidden by default (`opacity:0; transform:translateY(30px)`), revealed when their section enters the viewport via IntersectionObserver.

| Component | Class | Description |
|-----------|-------|-------------|
| Flow Chain | `.flow-chain` > `.flow-step` | Vertical step sequence, border-left guide, `.highlight` accent |
| Card Grid | `.card-grid` > `.card` | Content cards, `.accent-card` variant |
| Topology Box | `.topo-box` > `.topo-items` > `.topo-item` | Floating label, tag pills, `.hot` accent |
| Stacked Layers | `.layers` > `.layer` | Hierarchical depth, `.hot` for emphasis |
| Maturity Bar | `.maturity` > `.mat-level` | Numbered progress levels, `.current` for active |
| Pipeline Nodes | `.node-row` > `.node` | Circle nodes, `.filled` / `.accent` variants |
| Split Panels | `.split` > `.split-panel` | Side-by-side comparison, `.old` / `.new` |
| Roadmap | `.roadmap` > `.phase` | Timeline with dot markers |

## Animation

One pattern: scroll-driven reveals via IntersectionObserver. No animation libraries.

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
document.querySelectorAll('.section').forEach(s => observer.observe(s));
```

Child elements stagger via `transition-delay: nth-child * 0.1s`.

## Page structure

Every page follows this skeleton:

1. **Hero** — title, subtitle, visual. No reveal animation (immediately visible).
2. **Numbered sections** — `.label` ("01 // Name"), `.divider`, `h2`, `.body`, then components.
3. **Outro** — summary statement + author attribution.

## Anti-patterns

- No pure white (`#fff`) — use `--fg` (`#f3f1ec`)
- No additional colors beyond `--accent`
- No CSS frameworks, no Tailwind, no Bootstrap
- No React/Vue/Svelte — vanilla HTML + CSS + JS
- No external JS dependencies
- No rounded corners on cards — square edges only
- No gradients, no shadows (except animated canvas pieces)
- No emoji in the design

## Sites using this system

| URL | Type |
|-----|------|
| [pipeline-deep-dive.w-b.dev](https://pipeline-deep-dive.w-b.dev) | Interactive longform (reference implementation) |
| [xdr-animated.w-b.dev](https://xdr-animated.w-b.dev) | 45s React animation |
| [design.w-b.dev](https://design.w-b.dev) | This design system |

## Author

[Daniel Brasileiro](https://linkedin.com/in/brasileiro)
