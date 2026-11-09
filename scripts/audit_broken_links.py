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


def _strip_code_fences(body: str) -> str:
    """Replace fenced code blocks (``` ... ``` or ~~~ ... ~~~) with blank lines.

    Markdown spec: links inside code-fences are not real links (rendered as
    literal text), so audit must skip them. Without this, doc files that
    contain example links (SkyNet_PROMPT_v9.31.md, требования_к_ии/_examples.md)
    produce false-positive broken-link reports.
    """
    import re
    # Match fenced code blocks: starting ``` (or ~~~) on own line, ending with
    # matching fence. Replaces the whole block (preserving newlines) with
    # empty lines of the same length, to keep line numbers stable.
    pattern = re.compile(
        r'(?ms)^[ \t]*(?P<fence>```|~~~)(?P<info>[^\n]*)\n.*?^[ \t]*(?P=fence)[ \t]*$'
    )
    def _blank(m: re.Match) -> str:
        text = m.group(0)
        # Preserve newlines so line numbers in audit output stay accurate
        return '\n'.join(['' if line.strip() else '' for line in text.split('\n')])
    return pattern.sub(_blank, body)


def _strip_inline_code(body: str) -> str:
    """Replace inline code spans (`...`) with a placeholder.

    Markdown spec: `[text](path)` inside backticks is rendered literally,
    not as a link. Audit must not report such occurrences.

    Replaces the entire `` `...` `` span (including backticks) with the inner
    text wrapped so the link regex won't match it: we replace `[`,`]`,`(`,`)`
    inside the span with their fullwidth Unicode equivalents. This preserves
    readability of the doc while breaking the LINK_RE pattern.
    """
    import re
    # Match `...` not spanning newlines, with no backtick inside
    def _neutralise(m: re.Match) -> str:
        inner = m.group(1)
        # Replace markdown-link syntax chars inside the code span with
        # fullwidth Unicode equivalents — they will no longer match LINK_RE.
        # Using fullwidth forms keeps the doc readable when inspected.
        return inner.replace('[', '［').replace(']', '］').replace('(', '（').replace(')', '）')
    return re.sub(r'`([^`\n]+)`', _neutralise, body)


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
        # v9.59: skip markdown links inside code-fences and inline-code
        # (these are syntax examples in doc files, not real links)
        body = _strip_code_fences(body)
        body = _strip_inline_code(body)
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
