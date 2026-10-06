---
name: design-system
description: Load the w-b.dev design system, "Blueprint", whose flagship theme is tatame0 (white paper, one accent color, Tatame Red by default, black ink, hard corners, solid offset shadows, Big Shoulders Display + Space Mono + Archivo, 44px mat grid) before building any web page, landing page, app screen, kiosk UI, email, SwiftUI view or HTML demo. Use proactively for w-b.dev subdomains, hotsites, tatame0 (marketing/, web/, ios/, kiosk) and any project using Blueprint, and whenever the user says "use the design system", "follow the design system", "match the style", "make it look like tatame0", "blueprint style", or references design.w-b.dev.
---

# w-b.dev design system: "Blueprint"

Blueprint is the w-b.dev design system (v2, Oct 2026). It was extracted from tatame0, which stays its flagship theme. The canonical source is the repo below. **Read the files when you need exact values**, because they change and this skill only summarises them:

| File (`~/dev/repos/design-system-w-b/`) | What it is |
|------|------------|
| `tokens.css` | Core CSS custom properties (`--t-*`), accent via 4 `--t-accent-*` vars |
| `themes/tatame0.css` | Tatame Red plus the IBJJF belt palette. Also `alertecole.css` (slate blue) and `neutral.css` (ink) |
| `index.html` | The live style guide at https://design.w-b.dev, with working CSS for every component |
| `starter/index.html` | Copy-and-edit page template (ticker, nav, hero, steps, cards, form, footer) |
| `tailwind.css` | Tailwind v4 `@theme` map (`bg-paper`, `text-ink`, `bg-accent`, `font-display`, `shadow-offset`…) |
| `theme.json` | Machine-readable export for tooling and iOS |
| `legacy/dark-v1/` | The old dark w-b.dev system (archived; use only if asked for it) |

Hosted files work for any page: `https://design.w-b.dev/tokens.css` and `https://design.w-b.dev/themes/tatame0.css`. The tatame0 product's own copy lives in `~/dev/repos/tatame0/design-system/`, and its README has the full spec, including the SwiftUI guide.

## The idea

The page should feel like an engineer's drawing of a gym mat: tactile, precise and high-contrast. It is also readable under bright gym lighting, which is why the system is light only and so stark.

1. **White paper dominates.** Use white surfaces with a faint 44px mat grid behind the page.
2. **One accent.** In the tatame0 theme it is Tatame Red `#e5121f` (other projects swap the 4 `--t-accent-*` vars). It is for CTAs, live status, line-art and construction marks. Never use it for page backgrounds or body text.
3. **Black ink carries text and structure.** Use `#0a0a0a` for type, 2.5px borders and outlines.
4. **Corners are hard.** The radius is 0. Exceptions are 6px for inner nested elements, 7px for the logo "0", and 15px for badge caps.
5. **Shadows are solid offsets and never blurred.** Depth comes from hard cast shadows: `6px 6px 0` red or ink.
6. **It is light only.** Use `color-scheme: only light`, with no dark mode. On iOS, use `.preferredColorScheme(.light)`.
7. **Belts are first-class.** The IBJJF kids and adult belt palette (`--t-belt-*`) and stripes are shown clearly wherever progression appears.

## Core tokens (summary)

```css
--t-accent:#e5121f; --t-accent-deep:#a60a14; --t-accent-tint:#fdeaea; --t-accent-grid:#f0e4e4;  /* tatame0 theme */
--t-red / --t-red-deep / --t-red-tint / --t-grid = aliases of the accent vars (tatame0 code keeps working)
--t-paper:#ffffff; --t-ink:#0a0a0a; --t-muted:#6b6b6b;
--t-on-ink:#ffffff; --t-on-ink-dim:#b9b9b9;   /* amber #b7791f = pending/warning only */
--t-line:2.5px; --t-border:2.5px solid var(--t-ink); --t-divider:2.5px dashed var(--t-red);
--t-shadow:6px 6px 0 var(--t-red); --t-shadow-ink:6px 6px 0 var(--t-ink);
--t-shadow-hover:9px 9px 0 var(--t-ink); --t-shadow-sm:4px 4px 0 var(--t-ink); --t-shadow-active:2px 2px 0 var(--t-ink);
--t-maxw:1180px; --t-gutter:24px; --t-section-y:74px; --t-grid-size:44px;
spacing: 6 / 12 / 22 / 30 / 48px
```

Page background:

```css
body{background:var(--t-paper);color:var(--t-ink);font-family:var(--t-font-body);line-height:1.5;
  background-image:linear-gradient(var(--t-grid) 1px,transparent 1px),linear-gradient(90deg,var(--t-grid) 1px,transparent 1px);
  background-size:44px 44px}
```

## Typography

Google Fonts: `Big+Shoulders+Display:wght@700;800;900`, `Space+Mono:wght@400;700`, `Archivo:wght@400;500;600;700;800;900`.

| Role | Face | Style | Size |
|------|------|-------|------|
| Display (h1–h3, buttons, step numbers) | Big Shoulders Display 800/900 | UPPERCASE, leading .92, tracking -.01em | hero `clamp(2.9rem,7.6vw,6rem)`, h2 `clamp(2.1rem,5.5vw,3.8rem)`, h3 1.45rem |
| Mono (kickers, labels, `FIG.01` tags, timers, ticker) | Space Mono 700 | UPPERCASE, tracking .14–.18em | .72rem |
| Body | Archivo 400–700 | sentence case, leading 1.5 | 1rem, lead 1.18rem/500, small .9rem |
| Wordmark | Archivo 900 | lowercase `tatame0`, tracking -.055em; "0" in red at .92em | — |

## Components (copy from `index.html` or `starter/index.html`)

- **Buttons.** Display font, uppercase, 2.5px ink border, radius 0.
  - **Primary:** red fill, white text, `--t-shadow-ink`.
  - **Ghost:** white fill, `--t-shadow` (red).
  - **`.sm`:** padding 11px 16px.
  - **Danger:** red text and border on white.
  - **Hover:** `translate(-2px,-2px)` plus the 9px shadow.
  - **Active:** `translate(3px,3px)` plus the 2px shadow.
  - **Arrow:** a `→` that slides 4px on hover.
- **Cards.**
  - **Paper card:** white, ink border, red offset shadow.
  - **`.ink` card:** black, white text, red shadow, for emphasis, pricing or the footer.
  - **Step card:** a huge red Big Shoulders numeral plus a `STEP 01` mono badge.
- **Inputs.** Mono uppercase label in muted grey. White field, ink border, radius 0, padding 10px 14px. On focus, the border turns red with no outline glow.
- **Kicker.** Red mono label with a 26px red leading dash (`::before`). Put one above every section heading.
- **Section.** Padding is `--t-section-y`. Separate sections with a dashed red divider. A red `+` crosshair (14px) sits top-right.
- **Ticker bar.** Black, white mono text at .74rem, a red bottom border, red `/` and `★` separators, and a marquee that loops every 28s.
- **Blueprint motifs.**
  - Dimension lines: dashed red with mono measurements (`1 TAP = ✓ PRESENT`).
  - `FIG.01 — …` tags.
  - Line-art icons with a 2.5–3.2px stroke and `stroke-linecap="square"`.
- **Belt bar.** A 2.5px ink outline, a black sleeve on the right, and white stripe ticks. The progress bar is red on an ink outline.

## Motion

- **Draw-on:** SVG strokes animate in over 1.6s, `cubic-bezier(.7,0,.3,1)`.
- **Section rise and stagger:** 0.7s, `cubic-bezier(.2,.7,.2,1)`.
- **Hover and press:** 0.12s.
- **Reduced motion:** disable everything under `prefers-reduced-motion: reduce`.

## Per platform

- **Plain HTML:** start from `starter/index.html`, or load the Google Fonts above plus `tokens.css` and one theme.
- **Tailwind v4:** `@import "tailwindcss";` then import `tailwind.css` from this repo (tatame0 `web/` imports its own copy).
- **SwiftUI (`ios/`):** use the `Color.tatame*` extension and the `tatameShadow()` modifier from README §7.3, plus `tatameLightOnly()`.
- **Claude Artifacts:** the artifact runtime expects dark-mode handling. This system is deliberately single-theme, so set `color-scheme: only light` on `:root` and set every color explicitly. Keep content visible on load, and treat reveal animations as enhancement only.
- **Other projects:** the system can be reused by overriding only the 4 red tokens (`--t-red`, `--t-red-deep`, `--t-red-tint`, `--t-grid`). That's how alertecole gets slate blue (`themes/alertecole.css`). The picker on design.w-b.dev derives the 4 values from any color.

## Don't

- Blurred shadows, gradients (the mat grid is the only exception), or pill buttons.
- Dark mode or auto-inversion.
- Red page backgrounds, or red behind body text. Use the inverted ink surface for emphasis instead.
- A second accent color. The only other hues are amber for pending states and the belt palette.
- Lowercase display headings, or a mono face for body prose.
