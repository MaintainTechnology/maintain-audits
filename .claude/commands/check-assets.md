---
description: Check the audits/ tree against the house naming & organization conventions.
allowed-tools: Bash(python:*)
---

Run the asset-convention linter and report to the user:

`python .claude/hooks/check-audit-naming.py`

- If it prints issues, summarize them and offer to fix each (rename to em-dash style, move a loose file into a category folder, export a missing PDF, add a missing order number).
- If it prints nothing, confirm the `audits/` tree is fully to convention.
