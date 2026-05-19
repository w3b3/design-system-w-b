# Design System Review — Pipeline Overview Snippet

## Violations Found and Fixed

### 1. Background color — `background:#fff`
**Violation:** White background. The design system uses a near-black dark monochrome scheme.  
**Fix:** Changed to `background:var(--bg)` (`#0e0e0e`).

### 2. Body text color — `color:#333`
**Violation:** Hardcoded dark gray. All text must use token colors only.  
**Fix:** Changed to `color:var(--fg)` (`#f3f1ec`, warm paper) on the wrapper.

### 3. Font family — `font-family:Arial`
**Violation:** Arial is not a permitted typeface. Only Helvetica and JetBrains Mono are allowed.  
**Fix:** Changed to `font-family:var(--helv)` (Helvetica stack). Also added the required JetBrains Mono Google Fonts import and full token/reset `<head>`.

### 4. H1 font size — `font-size:48px`
**Violation:** Hardcoded pixel size. All H1/H2/H3 headings must use `clamp()` for fluid responsive sizing.  
**Fix:** Changed to `font-size:clamp(42px,6vw,72px)` per the H1 spec.

### 5. H1 color — `color:#1a1a1a`
**Violation:** Hardcoded near-black color. On a dark background this is invisible; primary text must use `--fg`.  
**Fix:** Changed to `color:var(--fg)`.

### 6. Paragraph color — `color:#666`
**Violation:** Hardcoded medium gray. Body/secondary text must use the `--dim` token.  
**Fix:** Changed to `color:var(--dim)` (`rgba(243,241,236,0.35)`).

### 7. Paragraph font size — `font-size:16px`
**Violation:** Hardcoded body font size. Body text must use `clamp()` for responsive scaling.  
**Fix:** Changed to `font-size:clamp(16px,1.6vw,19px)` and added `line-height:1.65;max-width:680px` per body text spec.

### 8. Panel background — `background:#f0f0f0`
**Violation:** Light gray panel background. All card/panel backgrounds must use `--bg2`.  
**Fix:** Changed to `background:var(--bg2)` (`#141414`).

### 9. Panel border-radius — `border-radius:12px`
**Violation:** Rounded corners are an explicit anti-pattern. All cards and panels must have sharp square edges.  
**Fix:** Removed `border-radius` entirely.

### 10. Panel box-shadow — `box-shadow:0 2px 8px rgba(0,0,0,0.1)`
**Violation:** Box shadows are an explicit anti-pattern (except in animated SVG canvas pieces).  
**Fix:** Removed `box-shadow`. Added `border:1px solid var(--hair)` instead to give the panel definition.

### 11. Span color — `color:blue`
**Violation:** `blue` is outside the token palette entirely. `--accent` (amber `#d4a853`) is the only non-grayscale color and should be used for active/highlight states.  
**Fix:** Changed to `color:var(--accent)`. Applied `font-family:var(--mono)` and `font-size:12px;letter-spacing:0.02em` since this is a data/label context. The " — Processing" text was also wrapped and given `color:var(--dim)` with mono styling.

---

## Summary

| # | Element | Violation | Fix |
|---|---------|-----------|-----|
| 1 | Wrapper div | `background:#fff` | `var(--bg)` |
| 2 | Wrapper div | `color:#333` | `var(--fg)` |
| 3 | Wrapper div | `font-family:Arial` | `var(--helv)` + JetBrains Mono import added |
| 4 | `<h1>` | `font-size:48px` (hardcoded) | `clamp(42px,6vw,72px)` |
| 5 | `<h1>` | `color:#1a1a1a` | `var(--fg)` |
| 6 | `<p>` | `color:#666` | `var(--dim)` |
| 7 | `<p>` | `font-size:16px` (hardcoded) | `clamp(16px,1.6vw,19px)` |
| 8 | Panel div | `background:#f0f0f0` | `var(--bg2)` |
| 9 | Panel div | `border-radius:12px` | Removed (sharp edges only) |
| 10 | Panel div | `box-shadow:...` | Removed; replaced with `border:1px solid var(--hair)` |
| 11 | `<span>` | `color:blue` | `var(--accent)` with mono label styling |
