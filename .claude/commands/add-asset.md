---
description: Inspect a new/dropped-in asset, categorize it, rename to house style, and file it under audits/.
argument-hint: <path-to-file> [intended category]
allowed-tools: Bash(pdftotext:*), Bash(python:*), Read, Glob
---

File a new asset into the `audits/` tree, following `.claude/skills/asset-conventions`.

Target: $ARGUMENTS

1. **Identify** it — `pdftotext "<file>" -` and/or a pymupdf page-size check. Empty text = image-only (photo → `team-photos/`; branded background → `brand-assets/`).
2. **Categorize**: social-content / brand-assets / team-photos / sample-reports.
3. **Rename** to house style — spaced em dash ` — `; social content gets the next `NN — ` order number (check existing files to pick it); strip any `Maintain Audits — ` prefix.
4. **Move** it into the category folder. Never overwrite an existing destination. For a sample report, ensure both a `.docx` source and a `.pdf` export exist with the same base name.
5. **Verify**: `python .claude/hooks/check-audit-naming.py` and report the result.

If the category is genuinely ambiguous, ask before moving.
