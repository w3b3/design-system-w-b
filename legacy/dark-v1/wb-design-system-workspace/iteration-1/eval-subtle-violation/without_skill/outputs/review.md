# Design System Review — Pipeline Overview Snippet

## Violations Found and Fixed

### 1. Light theme background (`background:#fff`)
**Original:** `background:#fff`
**Fixed:** `background:var(--bg)` (`#0e0e0e`)
**Rule:** The w-b.dev design system is dark-only. `#fff` (pure white) is explicitly forbidden as a background. The page background must always be `--bg`.

### 2. Pure-white foreground text (`color:#fff` implied by light theme)
**Original:** `color:#333` on the outer div; `color:#1a1a1a` on the h1
**Fixed:** `color:var(--fg)` (`#f3f1ec`)
**Rule:** Text is never dark-on-light. The foreground color is `--fg`, a warm paper tone, never pure white or any dark shade. `#1a1a1a` and `#333` are dark colors that belong to a light theme — both violate the dark monochrome base.

### 3. Wrong font family (`font-family:Arial`)
**Original:** `font-family:Arial`
**Fixed:** `font-family:var(--helv)` (`Helvetica, "Helvetica Neue", Arial, sans-serif`)
**Rule:** Only two typefaces are permitted — `--helv` and `--mono`. Specifying `Arial` directly bypasses the Helvetica-first stack and skips the CSS variable entirely. The design system requires `var(--helv)`.

### 4. Hard-coded h1 size (`font-size:48px`)
**Original:** `font-size:48px` (fixed pixel value)
**Fixed:** `font-size:clamp(42px,6vw,72px)`
**Rule:** All display sizes must use `clamp()` for fluid responsiveness. No breakpoints for type, no fixed pixel values on headings. H1 spec: `clamp(42px, 6vw, 72px)`.

### 5. Hard-coded h1 color (`color:#1a1a1a`)
**Original:** `color:#1a1a1a`
**Fixed:** `color:var(--fg)`
**Rule:** Headlines use `--fg`. `#1a1a1a` is a near-black dark color appropriate for a light theme — entirely wrong on the dark background. This would render as dark text on a dark background, making it invisible.

### 6. Wrong body text color (`color:#666`)
**Original:** `color:#666`
**Fixed:** `color:var(--dim)` (`rgba(243,241,236,0.35)`)
**Rule:** Secondary/body text must use `--dim`, which is the foreground color at 35% opacity. `#666` is a mid-grey designed for light themes and has no relation to the opacity-ladder hierarchy. The design system mandates hierarchy through opacity, not hue variation.

### 7. Hard-coded body font size (`font-size:16px`)
**Original:** `font-size:16px`
**Fixed:** `font-size:clamp(16px,1.6vw,19px)`
**Rule:** Body text uses `clamp(16px, 1.6vw, 19px)` for fluid sizing. A fixed `16px` violates the "clamp everything" typography rule.

### 8. Missing body text constraints (line-height, max-width)
**Original:** No `line-height` or `max-width` on the paragraph
**Fixed:** Added `line-height:1.65` and `max-width:680px`
**Rule:** Body text spec requires `line-height: 1.65` and `max-width: 680px` always. Both are mandatory for readable long-form text in the design system.

### 9. Card background is wrong (`background:#f0f0f0`)
**Original:** `background:#f0f0f0` (light grey)
**Fixed:** `background:var(--bg2)` (`#141414`)
**Rule:** Card/component backgrounds must use `--bg2`. A light grey background is a direct anti-pattern — this is a dark theme with only two background tones (`--bg` and `--bg2`).

### 10. Card border-radius (`border-radius:12px`)
**Original:** `border-radius:12px`
**Fixed:** Removed entirely (no border-radius)
**Rule:** "No rounded corners on cards (square/sharp edges only)" is an explicit anti-pattern in the design system. Cards use sharp square edges.

### 11. Card box-shadow (`box-shadow:0 2px 8px rgba(0,0,0,0.1)`)
**Original:** `box-shadow:0 2px 8px rgba(0,0,0,0.1)`
**Fixed:** Removed entirely
**Rule:** "No shadows except the Stage canvas shadow in animated pieces" is an explicit anti-pattern. General-purpose drop shadows are forbidden.

### 12. Card padding value (`padding:20px`)
**Original:** `padding:20px`
**Fixed:** `padding:24px`
**Rule:** Card padding spec is 24–28px. While 20px is close, the design system specifies 24px as the standard card interior padding.

### 13. Card lacks a border
**Original:** No border on the card div
**Fixed:** Added `border:1px solid var(--hair)`
**Rule:** Cards use `border: 1px solid var(--hair)`. Without a border, the card is undefined against the dark background. The `--hair` border (fg at 8% opacity) provides the subtle edge that defines the card shape.

### 14. Accent color used as a raw keyword (`color:blue`)
**Original:** `color:blue`
**Fixed:** `color:var(--accent)` (amber `#d4a853`)
**Rule:** "The only non-grayscale color is `--accent`." Raw `blue` introduces a forbidden color that is completely outside the palette. Active/highlighted states must use `--accent` (the amber).

### 15. Active label uses no typographic treatment
**Original:** `<span style="color:blue">Active</span>` — plain inline text with no font specification
**Fixed:** Applied mono label treatment: `font-family:var(--mono);font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--accent)`
**Rule:** Status labels (Active, Processing, etc.) are label-role text: JetBrains Mono, 11px, 0.18em tracking, uppercase. The "Processing" text following it is data/mono role and uses `var(--dim)`.

### 16. Missing JetBrains Mono font import
**Original:** No `<link>` to Google Fonts
**Fixed:** Added the required Google Fonts preconnect and stylesheet link
**Rule:** JetBrains Mono is the sole external dependency and must be loaded. Without it, mono typography falls back to system fonts and the label/data roles lose their intended appearance.

---

## Summary

The original snippet was written entirely in light-theme conventions (white background, dark text, greys, Arial, blue, rounded cards with shadows) — almost every property violated a w-b.dev design rule. The fixed version replaces all hard-coded values with CSS custom properties from the token set, enforces the dark monochrome palette, applies fluid typography with `clamp()`, removes forbidden decorations (radius, shadow), and assigns correct typographic roles (Helvetica for headings/body, JetBrains Mono for labels/status).
