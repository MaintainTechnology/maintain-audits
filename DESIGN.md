# Design

The **single source of truth** for Maintain Audits visuals. Anything built for the
brand — social graphics, documents, reports, web, future product UI — references
this file. Machine-readable tokens: [`design-system/tokens.css`](design-system/tokens.css) ·
[`design-system/tokens.json`](design-system/tokens.json). Living, rendered reference:
[`design-system/index.html`](design-system/index.html).

Every value below was extracted empirically — from the live site's own CSS
variables (`maintainaudits.com.au`) and from every asset in [`audits/`](audits) —
not invented. Where sources disagree, the drift is called out under **Consistency notes**.

---

## Theme & atmosphere

Maintain Audits is a **dark-first brand**: a deep teal-black surface (**Forge Blue**)
carrying a bright **Assurance Green**, lit by a subtle green radial glow and a faint
1px green grid. The feeling is an **instrument panel / control room** — precise,
lit, under control. Light surfaces (Cloud / white) are the document register:
reports and letterhead. Green is earned emphasis, never wallpaper.

Register: **brand-first, hybrid** (a client portal / product UI is anticipated and
should inherit these tokens). See [`PRODUCT.md`](PRODUCT.md) for strategy, users,
and principles.

---

## Color

Brand names are the brand's own (from the live site). **Build against the semantic
roles**, not the raw brand values.

### Core brand
| Token | Hex | Role |
|---|---|---|
| `--ma-forge-blue` | `#07272D` | Primary dark surface — the signature background |
| `--ma-black` | `#101820` | Near-black base (deepest surface) |
| `--ma-black-2` / `--ma-black-3` | `#0C1319` / `#1A2330` | Darker / raised dark panels |
| `--ma-blue-deep` | `#051F24` | Deepest teal (gradient floor) |
| `--ma-assurance-green` | `#3DDC84` | **Primary brand green** — CTAs, emphasis, accents |
| `--ma-signal-green` | `#06F285` | Logo-mark neon / highest-energy accent (use sparingly) |
| `--ma-green-mid` | `#348F41` | Solid-fill green for panels (report usage) |
| `--ma-green-deep` / `--ma-green-dark` | `#157A40` / `#0C4A26` | Green on light, deep green fills |
| `--ma-blue-light` | `#66A1AB` | Muted teal secondary accent |
| `--ma-cloud` | `#F5F5F1` | Off-white paper — the document surface |
| `--ma-white` | `#FFFFFF` | Pure white surface |

### Ink & tints
| Token | Hex | Role |
|---|---|---|
| `--ma-ink` | `#1F2D2B` | Body text on light (primary) |
| `--ma-slate` | `#64748B` | Muted / secondary text on light |
| `--ma-green-tint-1` / `-2` | `#E5F8EE` / `#CCEFD3` | Pale green chips, highlights |
| `--ma-surface-mint-1` / `-2` | `#F0FBF5` / `#EAF7F0` | Tinted light surfaces / callouts |
| on-dark text | `#FFFFFF`, `70%`, `55%` | Full / muted / faint text on dark |

### Audit severity (from report status colors — a first-class brand system)
Because the product *is* audit findings, severity is a core palette. Never encode
severity by color alone — always pair with a label (accessibility).

| Level | fg | bg |
|---|---|---|
| Pass | `#0C4A26` | `#E5F8EE` |
| Low | `#1E40AF` | `#DBEAFE` *(bg inferred)* |
| Medium | `#854D0E` | `#FEF9C3` |
| High | `#9A3412` | `#FFEDD5` |
| Critical | `#991B1B` | `#FEE2E2` |

### Contrast rules (WCAG 2.2 AA — see PRODUCT.md)
- Body text ≥ 4.5:1; large/bold ≥ 3:1. `--ma-ink` on white ≈ 13:1 ✓; white on `--ma-forge-blue` ≈ 13:1 ✓.
- **Assurance Green is a fill, not a text color on dark** — `#3DDC84` text on Forge Blue is only ~7:1 for large only; for green *body* text use `--ma-green-deep` on light. On green fills, text is `--ma-forge-blue` (dark), never white.

---

## Typography

| Role | Family | Weights | Setting |
|---|---|---|---|
| Display / headings | **Albert Sans** | 700 / 800 | tracking `-0.02em`, leading `1.05`, `text-wrap: balance` |
| Body / UI | **Inter** | 400 / 500 / 600 | leading `1.6`, measure 65–75ch |
| Social graphics (alt) | **Vela Sans** | 400 / 600 / 700 | display face seen across social content |

Both Albert Sans and Inter are on Google Fonts. Scale (fluid) lives in the tokens
(`--text-display` → `--text-overline`). Pair is deliberate: Albert Sans (geometric,
heavy, tight) for impact vs. Inter (neutral, legible) for reading — a weight/register
contrast, not two lookalike sans.

---

## Logo

Assets: [`design-system/assets/logo/`](design-system/assets/logo). The logo is the
**Maintain Audits wordmark**: the text renders in `currentColor` (white on dark,
Forge Blue on light).

- **On dark surfaces:** [`wordmark-on-dark.svg`](design-system/assets/logo/wordmark-on-dark.svg) (text white).
- **On light surfaces:** [`wordmark-on-light.svg`](design-system/assets/logo/wordmark-on-light.svg) (text Forge Blue).
- **Clear space:** ≥ the cap height on all sides. **Min width:** ≥ 120px.
- **Don't:** stretch, add effects, or place the white wordmark on light or busy photography without a dark scrim.

Native source lockups also live in [`audits/brand-assets/`](audits/brand-assets) (letterhead, dark-theme background).

---

## Iconography

A 14-icon brand set (line style, 24×24, `stroke: currentColor`, width 2, round caps),
extracted to [`design-system/assets/icons/`](design-system/assets/icons) and bundled
in [`assets/sprite.svg`](design-system/assets/sprite.svg):

`i-check` · `i-clipboard` · `i-search` · `i-shield` · `i-chart` · `i-network` ·
`i-speed` · `i-star` · `i-cpu` · `i-mail` · `i-phone` · `i-pin` · `i-arrow-right` · `i-menu`

Use via sprite: `<svg class="icon"><use href="assets/sprite.svg#i-shield"/></svg>`
with `.icon{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}`.
Do not mix in a second icon library; extend this set in the same style.

---

## Spacing, radius, elevation

- **Spacing:** 4px base scale `--space-1`…`--space-10` (4→128px). Vary rhythm; don't use one uniform gap.
- **Radius:** `--radius-sm` 6 · `--radius-md` 10 (default control) · `--radius-lg` 16 · `--radius-xl` 24 · `--radius-pill`. Sharp (0) for data/report tables.
- **Elevation:** `--shadow-sm/md/lg` for light surfaces; `--glow-green` (`0 0 40px rgba(61,220,132,.25)`) for the signature green halo on dark.

## Signature backgrounds

The brand texture, provided as utilities in `tokens.css`:
- **`.ma-grid-bg`** — Forge Blue + a 1px green grid (`rgba(61,220,132,0.05)`, 40px cells).
- **`.ma-glow`** — a soft green radial glow (top-right by default).
Layer glow over grid for the hero look seen on the site and the dark-theme background.

## Motion

Durations `--dur-fast/base/slow` (120/200/320ms), easing `--ease-out`
(`cubic-bezier(.22,1,.36,1)` — no bounce). Every animation has a
`prefers-reduced-motion` fallback (already enforced globally in `tokens.css`).

---

## Components (baseline)

Rendered examples in [`design-system/index.html`](design-system/index.html):
- **Primary button** — Assurance Green fill, Forge-Blue text, `--radius-md`, weight 600.
- **Secondary / ghost** — hairline border (`--color-line`), text-only on dark.
- **Severity pill** — `bg`/`fg` from the severity tokens + label + icon.
- **Finding card** — light surface, severity pill, title (Albert Sans), body (Inter).
- **Stat block** — big Albert Sans numeral (e.g. "48hr"), Inter caption — the brand's key proof point.

---

## Consistency notes (real drift to reconcile)

1. **Fonts across channels differ.** Web = Albert Sans + Inter · Social = Vela Sans + Albert Sans · Sample reports = Calibri/Carlito (office default). **Canonical = Albert Sans + Inter.** New report templates should migrate off Calibri.
2. **Two greens exist.** `#3DDC84` (Assurance Green, primary) vs `#06F285` (Signal Green, the logo neon). Keep Signal Green for the mark and rare high-energy accents only.
3. **Severity "Low" bg** (`#DBEAFE`) is inferred — only its foreground blue appeared in reports. Confirm against a real report template before shipping status chips.

## Source asset index

- Brand & templates → [`audits/brand-assets/`](audits/brand-assets)
- Social content (Vela Sans register) → [`audits/social-content/`](audits/social-content)
- Branded reports (Calibri register) → [`audits/sample-reports/`](audits/sample-reports)
- Team photography (green-gradient headshots) → [`audits/team-photos/`](audits/team-photos)
- Extracted logo/icons → [`design-system/assets/`](design-system/assets)
