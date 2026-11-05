#!/usr/bin/env python3
"""Restore 4 accidentally-deleted part files in parent's дочерние_части and материалы_частей.

These files were deleted in commit d35e893 due to a bug in migrate_dedup_quantity.py
(incorrectly identified as duplicates despite different subtypes).

Files affected:
  - часть_reversivnye_pelte_ceramic_bottom (parent: izdelie_reversivnye_pelte)
  - часть_superkondensatory_electrode_neg (parent: izdelie_superkondensatory)
  - часть_svintsovo-kislotnye_akb_grid_neg (parent: izdelie_svintsovo-kislotnye_akb)
  - часть_termomoduli_pelte_ceramic_bottom (parent: izdelie_termomoduli_pelte)
"""

import sys, os, re
sys.path.insert(0, 'scripts')
from validate_decomposition import read_yaml_frontmatter, SKYNET_REPO
from pathlib import Path

TODAY = "2026-11-05"
IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"

# (parent_id, missing_part_id, material, share_in_parent)
MISSING = [
    ('izdelie_reversivnye_pelte', 'часть_reversivnye_pelte_ceramic_bottom', 'alumina', 0.19),
    ('izdelie_superkondensatory', 'часть_superkondensatory_electrode_neg', 'activated_carbon', 0.15),
    ('izdelie_svintsovo-kislotnye_akb', 'часть_svintsovo-kislotnye_akb_grid_neg', 'pbca_alloy', 0.05),
    ('izdelie_termomoduli_pelte', 'часть_termomoduli_pelte_ceramic_bottom', 'alumina', 0.2),
]


def find_parent_path(parent_id: str) -> Path | None:
    short = parent_id[len('izdelie_'):]
    for sub in IZDELIYA_DIR.iterdir():
        if not sub.is_dir():
            continue
        for cand in [short, short.lower()]:
            parent_dir = sub / cand
            idx = parent_dir / "_index.md"
            if idx.exists():
                text = idx.read_text(encoding='utf-8')
                if f"id: {parent_id}" in text:
                    return idx
    return None


def fix_parent(parent_path: Path, missing_id: str, material: str, share: float):
    data, yaml_text, body = read_yaml_frontmatter(parent_path)
    if not data:
        return False
    new_yaml = yaml_text

    # 1. Add to дочерние_части (find sibling pattern)
    # Find "  - часть_<sibling>" in дочерние_части block and add missing_id after last sibling
    # Strategy: find last "  - часть_*" in дочерние_части block, add missing_id after it
    children_pattern = re.compile(
        r"^(дочерние_части:\s*\n(?:  - [^\n]+\n)*)",
        re.MULTILINE,
    )
    m = children_pattern.search(new_yaml)
    if m:
        block = m.group(1)
        if missing_id not in block:
            # Add missing_id at end of block
            new_block = block.rstrip('\n') + f"\n  - {missing_id}\n"
            new_yaml = new_yaml[:m.start()] + new_block + new_yaml[m.end():]

    # 2. Add to материалы_частей
    mats_pattern = re.compile(
        r"^(материалы_частей:\s*\n(?:(?:  - часть: [^\n]+\n(?:    [^\n]+\n)*?)+))",
        re.MULTILINE,
    )
    m2 = mats_pattern.search(new_yaml)
    if m2:
        block = m2.group(1)
        if missing_id not in block:
            # Append a new entry at end of block
            new_entry = f"  - часть: {missing_id}\n    материал: {material}\n    доля_массы: {share:.4f}\n"
            new_block = block.rstrip('\n') + '\n' + new_entry
            new_yaml = new_yaml[:m2.start()] + new_block + new_yaml[m2.end():]
    else:
        # No материалы_частей block — skip (shouldn't happen)
        pass

    # 3. Update дата_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )

    new_text = "---\n" + new_yaml + "\n---\n" + body
    if not new_text.endswith("\n"):
        new_text += "\n"
    parent_path.write_text(new_text, encoding="utf-8")
    return True


def main():
    print("=== Restoring 4 missing part files ===")
    for parent_id, missing_id, material, share in MISSING:
        parent_path = find_parent_path(parent_id)
        if not parent_path:
            print(f"  ! parent not found: {parent_id}")
            continue
        ok = fix_parent(parent_path, missing_id, material, share)
        print(f"  {'✓' if ok else '✗'} {parent_id} ← {missing_id} (материал={material}, доля={share})")


if __name__ == "__main__":
    main()
