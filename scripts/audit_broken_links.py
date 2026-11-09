#!/usr/bin/env python3
"""
Audit broken internal markdown links across the SkyNet repo.

For each .md file we look at markdown links of the form
    [text](path)
where path is a relative path (starts with ../ or ./ or a plain directory
name), and verify that the target file actually exists on disk.

External (http(s)://, mailto:, tel:) and intra-page (#anchor) links are skipped.
"""
from __future__ import annotations

import os
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path("/home/z/my-project/SkyNet")

# Markdown link pattern. Captures (label, target).
LINK_RE = re.compile(r"\[(?P<label>[^\]]*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://", "#", "data:")


def is_internal_link(target: str) -> bool:
    if not target:
        return False
    if target.startswith(SKIP_PREFIXES):
        return False
    # Skip raw html anchors or weird stuff
    if target.startswith("<"):
        return False
    return True


def audit() -> int:
    broken = []
    checked = 0
    for path in ROOT.rglob("*.md"):
        rel_path = path.relative_to(ROOT)
        # Skip dialog/telemetry files
        if str(rel_path).startswith("диалог/"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARN: cannot read {path}: {e}", file=sys.stderr)
            continue
        # Strip frontmatter (between first --- ... --- at file start)
        body = text
        if text.startswith("---"):
            end = text.find("\n---", 3)
            if end != -1:
                body = text[end + 4:]
        for m in LINK_RE.finditer(body):
            target = m.group("target")
            if not is_internal_link(target):
                continue
            checked += 1
            # URL-decode the target (markdown supports %20 etc.)
            decoded = urllib.parse.unquote(target)
            # Resolve relative to the file's directory
            target_path = (path.parent / decoded).resolve()
            if not target_path.exists():
                broken.append((rel_path, path.parent, target, target_path))

    print(f"\nChecked {checked} internal links; {len(broken)} broken.\n")
    if broken:
        # Group by file for readability
        print("=" * 80)
        print("BROKEN INTERNAL LINKS:")
        print("=" * 80)
        cur = None
        for rel_path, src_dir, target, target_path in broken:
            if rel_path != cur:
                print(f"\n[{rel_path}]")
                cur = rel_path
            print(f"  line-link: '{target}'")
            try:
                disp = target_path.relative_to(ROOT)
            except ValueError:
                disp = target_path
            print(f"    resolves to: {disp}  (missing)")
    return len(broken)


if __name__ == "__main__":
    sys.exit(1 if audit() else 0)
