# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`maintain-audits` is a **content and document asset repository** — not a software project — for **Maintain Audits** (maintainaudits.com.au), an independent franchise assurance / audit business. There is no application code, build system, or test suite. The `.gitignore` is the stock GitHub Node template and does **not** imply a Node project (there is no `package.json`).

Everything of value lives under `audits/`. Work here means organizing, naming, inspecting, and adding PDF/DOCX marketing and report assets — treat requests accordingly rather than looking for code to build or test.

Remote: `github.com:MaintainTechnology/maintain-audits`.

## Structure & naming conventions

```
audits/
├── social-content/   # Social posts & carousels (PDF). Numbered by posting order: "0N — Title.pdf"
├── brand-assets/     # Reusable brand collateral: letterhead template, branded backgrounds
├── team-photos/      # Headshots, named by person (no number)
└── sample-reports/   # Client-facing sample audit reports
    ├── docs/         # .docx sources
    └── pdf/          # exported .pdf — same base name as its .docx pair
```

House naming style (match it for any new file):
- Separator is a spaced **em dash** ` — ` (U+2014), never a hyphen.
- Sample reports: `Sample Report N — <Audit Type> (Branded).ext`, kept as a matching `.docx`/`.pdf` pair with an identical base name.
- Ordered social content carries a zero-padded lead number: `0N — <Title>.pdf`.
- Drop redundant brand prefixes — no `Maintain Audits — ` inside filenames; the repo already scopes that.

Keep `sample-reports/docs/` and `sample-reports/pdf/` in sync: every report should exist as both a `.docx` source and an exported `.pdf`.

## Inspecting assets (there is no build/lint/test)

Available tooling for identifying or categorizing a file before moving/renaming it:
- `pdftotext "file.pdf" -` — dump the text layer. Empty output means an image-only PDF (a photo or a branded background, not a text document).
- Python `pymupdf` (`import fitz`) — page count, page dimensions, image extraction, thumbnail rendering. Page size is a strong format hint: `810×810` = square social post, `1440×810` = 16:9 background/slide.
- For image-only PDFs, render a thumbnail (`page.get_pixmap()`) to see what it is.

## Brand facts (verified from the letterhead and social assets — use for captions, alt text, letterhead edits)

- Entity: **The Pep Collective Pty Limited t/a Maintain Audits**, ABN **70 646 284 586**.
- Contact: accounts@maintain.com.au · PO Box 447, Coorparoo, QLD 4151 · maintainaudits.com.au
- Positioning: independent franchise assurance; headline promise is a **48-hour turnaround from engagement to report**.
- Visual identity: green logo mark on a dark background; a reusable dark branded background lives in `brand-assets/`.

## Design system (use this for ANY visual work)

`DESIGN.md` (repo root) is the **single source of truth** for brand visuals — color, type, logo, icons, spacing, motion, usage rules. Implementation lives in `design-system/`: `tokens.css` / `tokens.json` (build against the semantic roles), `assets/` (logo + 14 icons as SVG), and `index.html` (a living style guide). Values were extracted from `maintainaudits.com.au` and the `audits/` files, so they are authoritative — don't invent colors or fonts. Canonical fonts: **Albert Sans** (display) + **Inter** (body). Brand core: Forge Blue `#07272D`, Assurance Green `#3DDC84`, Black `#101820`, Cloud `#F5F5F1`. See `DESIGN.md` → *Consistency notes* for known drift (reports still use Calibri; two greens exist).
