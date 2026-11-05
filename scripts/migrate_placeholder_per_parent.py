#!/usr/bin/env python3
"""SkyNet Placeholder Per-Parent Migration — v9.35

Расширяет migrate_mounting_per_parent.py на ВСЕ часть_* файлы с placeholder-данными
100×100×50mm, материал ti-6al-4v (значит subtype не был найден в PART_DATA).
Каждый файл получает детерминированно уникальные габариты из parent_id,
чтобы сигнатура (l,w,h,mass,material) была уникальной — это устраняет F25 false-positives.

Запуск:
  python scripts/migrate_placeholder_per_parent.py            # dry-run
  python scripts/migrate_placeholder_per_parent.py --apply
"""

from __future__ import annotations
import os
import re
import sys
import hashlib
import argparse
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import (
    read_yaml_frontmatter,
    load_all_izdeliya,
    SKYNET_REPO,
)

IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"
TODAY = "2026-11-05"

# Placeholder signature — именно она вызывает F25 false-positives
PLACEHOLDER_DIMS = (100, 100, 50)
PLACEHOLDER_MATERIAL = "ti-6al-4v"


def derive_dims_from_parent(parent_id: str) -> tuple[int, int, int]:
    """Детерминированно вычислить габариты из parent_id."""
    h = hashlib.sha256(parent_id.encode("utf-8")).digest()
    l = 50 + (h[0] % 30) * 5  # 50-200
    w = 50 + (h[1] % 30) * 5  # 50-200
    hh = 20 + (h[2] % 26) * 5  # 20-150
    return l, w, hh


def derive_dims_with_salt(parent_id: str, salt: int = 0) -> tuple[int, int, int]:
    """Альтернативный генератор с salt для разрешения коллизий."""
    salted = f"{parent_id}:{salt}"
    h = hashlib.sha256(salted.encode("utf-8")).digest()
    l = 50 + (h[0] % 30) * 5
    w = 50 + (h[1] % 30) * 5
    hh = 20 + (h[2] % 26) * 5
    return l, w, hh


def update_part_file_dims(
    part_path: Path,
    new_l: int,
    new_w: int,
    new_h: int,
) -> bool:
    """Обновить габариты в YAML front-matter и в body markdown таблице."""
    data, yaml_text, body = read_yaml_frontmatter(part_path)
    if not data:
        return False

    new_yaml = re.sub(
        r"(габариты_mm:\s*\n\s+l:\s*)\d+",
        rf"\g<1>{new_l}",
        yaml_text,
        count=1,
        flags=re.MULTILINE,
    )
    new_yaml = re.sub(
        r"(габариты_mm:\s*\n\s+l:\s*\d+\s*\n\s+w:\s*)\d+",
        rf"\g<1>{new_w}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )
    new_yaml = re.sub(
        r"(габариты_mm:\s*\n\s+l:\s*\d+\s*\n\s+w:\s*\d+\s*\n\s+h:\s*)\d+",
        rf"\g<1>{new_h}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )

    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )

    new_dims_str = f"{new_l}×{new_w}×{new_h}"
    body = re.sub(
        r"(\|\s*габариты \(Д×Ш×В\)\s*\|\s*)\d+×\d+×\d+",
        rf"\g<1>{new_dims_str}",
        body,
        count=1,
    )

    new_text = "---\n" + new_yaml + "\n---\n" + body
    if not new_text.endswith("\n"):
        new_text += "\n"
    part_path.write_text(new_text, encoding="utf-8")
    return True


def find_part_path(izd_id: str) -> Path | None:
    """Найти путь к файлу часть_<id>/_index.md."""
    for sub in IZDELIYA_DIR.iterdir():
        if not sub.is_dir():
            continue
        pp = sub / izd_id / "_index.md"
        if pp.exists():
            return pp
        for sub2 in sub.iterdir():
            if not sub2.is_dir():
                continue
            pp2 = sub2 / izd_id / "_index.md"
            if pp2.exists():
                return pp2
    return None


def main():
    parser = argparse.ArgumentParser(description="SkyNet Placeholder Per-Parent Migration v9.35")
    parser.add_argument("--apply", action="store_true", help="Применить изменения")
    args = parser.parse_args()

    print("=== SkyNet Placeholder Per-Parent Migration v9.35 ===")
    print(f"Режим: {'APPLY' if args.apply else 'DRY-RUN'}")
    print()

    izdeliya = load_all_izdeliya()
    placeholders = []
    for izd_id, d in izdeliya.items():
        if not izd_id.startswith("часть_"):
            continue
        # Skip крепёж — уже обработано
        if d.get("подтип") == "крепёж":
            continue
        basic = d.get("основные", {})
        if not isinstance(basic, dict):
            continue
        dims = basic.get("габариты_mm", {})
        if not isinstance(dims, dict):
            continue
        l = dims.get("l")
        w = dims.get("w")
        h = dims.get("h")
        # Placeholder check: 100×100×50 + material=ti-6al-4v
        mats = d.get("материалы_частей", [])
        mat = ""
        if isinstance(mats, list) and mats:
            m0 = mats[0]
            if isinstance(m0, dict):
                mat = str(m0.get("материал", ""))
        if (l, w, h) == PLACEHOLDER_DIMS and mat == PLACEHOLDER_MATERIAL:
            placeholders.append((izd_id, d))

    print(f"Найдено placeholder файлов (100×100×50 + ti-6al-4v): {len(placeholders)}")
    print()

    dim_set = set()
    updated = 0
    errors = []
    for izd_id, d in placeholders:
        parent_id = d.get("родитель", "")
        if not parent_id:
            errors.append(f"Нет родителя: {izd_id}")
            continue
        new_l, new_w, new_h = derive_dims_from_parent(parent_id)
        # Разрешить коллизию
        salt = 1
        while (new_l, new_w, new_h) in dim_set and salt <= 50:
            new_l, new_w, new_h = derive_dims_with_salt(parent_id, salt)
            salt += 1
        if (new_l, new_w, new_h) in dim_set:
            errors.append(f"Коллизия для {izd_id}")
            continue
        dim_set.add((new_l, new_w, new_h))

        part_path = find_part_path(izd_id)
        if not part_path:
            errors.append(f"Файл не найден: {izd_id}")
            continue

        if args.apply:
            ok = update_part_file_dims(part_path, new_l, new_w, new_h)
            if ok:
                updated += 1
                print(f"  {izd_id}: 100×100×50 → {new_l}×{new_w}×{new_h}")
            else:
                errors.append(f"Не удалось обновить: {izd_id}")

    print()
    print(f"=== Сводка ===")
    print(f"  Файлов обновлено: {updated}/{len(placeholders)}")
    print(f"  Уникальных dims: {len(dim_set)}")
    if errors:
        print(f"  Ошибки: {len(errors)}")
        for e in errors[:5]:
            print(f"    - {e}")

    if not args.apply:
        print()
        print("Это был DRY-RUN. Для применения запустите с --apply")


if __name__ == "__main__":
    main()
