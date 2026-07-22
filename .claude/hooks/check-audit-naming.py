#!/usr/bin/env python3
"""Advisory linter for the audits/ asset tree.

Enforces the house naming/organization convention documented in CLAUDE.md and
.claude/skills/asset-conventions. Shared by the PostToolUse hook (silent when the
tree is clean) and the /check-assets command.

Requires: python 3. Never blocks — always exits 0.
ponytail: full-tree rescan on every Write/Edit; fine while audits/ is small (dozens
of files). If it ever grows large, scope the hook to only re-check changed paths.
"""
import os, re, sys

ASSET_EXT = (".pdf", ".docx", ".doc")


def repo_root():
    # this script lives at <root>/.claude/hooks/check-audit-naming.py
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def check(root):
    audits = os.path.join(root, "audits")
    problems = []
    if not os.path.isdir(audits):
        return problems

    # 1. no loose assets sitting directly in audits/ (must be in a category folder)
    for name in sorted(os.listdir(audits)):
        if os.path.isfile(os.path.join(audits, name)) and name.lower().endswith(ASSET_EXT):
            problems.append(f"loose asset in audits/ root (move into a category folder): {name}")

    # 2 & 4. per-file naming checks
    for dirpath, _dirs, files in os.walk(audits):
        rel = os.path.relpath(dirpath, audits).replace("\\", "/")
        for f in sorted(files):
            if not f.lower().endswith(ASSET_EXT):
                continue
            if " - " in f:  # spaced hyphen used as a separator; house style is a spaced em dash
                problems.append(f"use the em-dash separator, not ' - ': {rel}/{f}")
            if rel == "social-content" and not re.match(r"^\d{2} — ", f):
                problems.append(f"social-content file should start with a 2-digit order number ('01 ...'): {f}")

    # 3. sample-reports: every docx source needs a matching pdf export and vice versa
    sr = os.path.join(audits, "sample-reports")
    docs, pdf = os.path.join(sr, "docs"), os.path.join(sr, "pdf")
    if os.path.isdir(docs) and os.path.isdir(pdf):
        d = {os.path.splitext(x)[0] for x in os.listdir(docs) if x.lower().endswith((".docx", ".doc"))}
        p = {os.path.splitext(x)[0] for x in os.listdir(pdf) if x.lower().endswith(".pdf")}
        for miss in sorted(d - p):
            problems.append(f"sample report missing PDF export: {miss}")
        for miss in sorted(p - d):
            problems.append(f"sample report PDF has no DOCX source: {miss}")

    return problems


def selftest():
    import tempfile, shutil
    t = tempfile.mkdtemp()
    try:
        a = os.path.join(t, "audits")
        os.makedirs(os.path.join(a, "social-content"))
        os.makedirs(os.path.join(a, "sample-reports", "docs"))
        os.makedirs(os.path.join(a, "sample-reports", "pdf"))
        open(os.path.join(a, "loose.pdf"), "w").close()
        open(os.path.join(a, "social-content", "bad - name.pdf"), "w").close()
        open(os.path.join(a, "sample-reports", "docs", "R1.docx"), "w").close()
        joined = " | ".join(check(t))
        assert "loose asset" in joined, joined
        assert "em-dash separator" in joined, joined
        assert "2-digit order number" in joined, joined
        assert "missing PDF export" in joined, joined
        print("selftest OK")
    finally:
        shutil.rmtree(t, ignore_errors=True)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if "--selftest" in sys.argv:
        selftest()
        return
    try:
        problems = check(repo_root())
    except Exception:
        return  # advisory only — never disrupt the session
    if problems:
        print("audits/ convention issues (see .claude/skills/asset-conventions):")
        for p in problems:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
