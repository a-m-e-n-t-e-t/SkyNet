#!/usr/bin/env python3
"""
SkyNet — миграция структуры папок.

ДО:  реальные данные/изделия/<подсистема>/часть_<parent>_<suffix>/_index.md
ПОСЛЕ: реальные данные/изделия/<подсистема>/<parent>/часть_<parent>_<suffix>/_index.md

Дочерние части переезжают внутрь папки своего родительского изделия.
Все ссылки `../../материалы/` в _index.md частей исправляются на `../../../../материалы/`
(4 уровня вверх вместо 2), чтобы они правильно указывали на реальные данные/материалы/.

Валидатор `validate_decomposition.py` использует rglob('_index.md') и поле `id:` в
frontmatter, так что переезд безопасен для всех метрик F12a-F25.

Использование:
  python scripts/migrate_parts_into_parents.py --dry-run    # отчёт без записи
  python scripts/migrate_parts_into_parents.py --execute    # реально выполнить git mv
"""
from __future__ import annotations
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
IZDELIYA = REPO / "реальные данные" / "изделия"


def read_yaml_field(text: str, field: str) -> str | None:
    """Прочитать одно строковое поле из YAML frontmatter (безопасно для юникода)."""
    m = re.search(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    fm = re.sub(r"\s+#.*$", "", fm, flags=re.MULTILINE)  # убрать комментарии
    m2 = re.search(rf"^{re.escape(field)}:\s*(.+?)\s*$", fm, re.MULTILINE)
    if not m2:
        return None
    val = m2.group(1).strip().strip('"').strip("'")
    return None if val in ("null", "~", "") else val


def git_mv(src: Path, dst: Path) -> tuple[bool, str]:
    """Выполнить git mv папки/файла."""
    cmd = ["git", "-C", str(REPO), "mv", str(src.relative_to(REPO)), str(dst.relative_to(REPO))]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (r.returncode == 0, r.stderr.strip() or r.stdout.strip())


def fix_links_in_file(path: Path) -> int:
    """Заменить `../../` на `../../../../` в markdown-ссылках на материалы.
    Возвращает число замен.
    """
    text = path.read_text(encoding="utf-8")
    # Заменяем только двухуровневые ссылки на материалы/технологии/etc.
    # (остальные ссылки в тексте оставляем как есть)
    new_text, n = re.subn(
        r"\]\(\.\./\.\./(материалы|технологии|исследовательские_группы|стандарты)/",
        r"](../../../../\1/",
        text,
    )
    if n:
        path.write_text(new_text, encoding="utf-8")
    return n


def build_parent_index() -> dict[str, Path]:
    """Построить карту id → путь к папке для всех изделий верхнего уровня."""
    idx: dict[str, Path] = {}
    for f in IZDELIYA.glob("*/*/_index.md"):
        if "часть_" in f.parent.name:
            continue
        t = f.read_text(encoding="utf-8")
        izd_id = read_yaml_field(t, "id")
        if izd_id:
            idx[izd_id] = f.parent
    return idx


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="только отчёт")
    ap.add_argument("--execute", action="store_true", help="выполнить миграцию")
    args = ap.parse_args()
    if not args.dry_run and not args.execute:
        ap.error("укажите --dry-run или --execute")

    parent_index = build_parent_index()
    print(f"Индекс родительских изделий: {len(parent_index)}")

    # Найти все части на 2-м уровне рядом с родителем
    parts = sorted(IZDELIYA.glob("*" + "/часть_*"))
    parts = [p for p in parts if p.is_dir()]

    print(f"Найдено частей для миграции: {len(parts)}")
    moves = []
    skipped = []
    link_fixes = 0

    for part_dir in parts:
        subsystem = part_dir.parent.name
        idx = part_dir / "_index.md"
        if not idx.exists():
            skipped.append((part_dir, "нет _index.md"))
            continue
        text = idx.read_text(encoding="utf-8")
        parent_id = read_yaml_field(text, "родитель")
        if not parent_id or not parent_id.startswith("izdelie_"):
            skipped.append((part_dir, f"родитель={parent_id!r}"))
            continue
        parent_dir = parent_index.get(parent_id)
        if not parent_dir:
            skipped.append((part_dir, f"нет папки родителя {parent_id}"))
            continue
        if not parent_dir.is_dir():
            skipped.append((part_dir, f"папка родителя не существует {parent_dir}"))
            continue
        # Часть переносится в подсистему своего родителя (даже если подсистемы различались —
        # это исправит рассинхронизацию: часть будет рядом со своим родителем).
        dst = parent_dir / part_dir.name
        if dst.exists():
            skipped.append((part_dir, f"уже существует {dst.relative_to(REPO)}"))
            continue
        moves.append((part_dir, dst, idx))

    print(f"К перемещению: {len(moves)}")
    print(f"Пропущено:    {len(skipped)}")
    if skipped:
        print("Причины пропуска:")
        for p, why in skipped[:10]:
            print(f"  - {p.relative_to(REPO)}: {why}")

    if args.dry_run:
        print("\n[dry-run] примеры перемещений (первые 5):")
        for src, dst, _ in moves[:5]:
            print(f"  {src.relative_to(REPO)}  →  {dst.relative_to(REPO)}")
        return 0

    if not args.execute:
        return 1

    # Выполняем git mv
    ok = 0
    failed = []
    for src, dst, idx in moves:
        success, msg = git_mv(src, dst)
        if success:
            ok += 1
            # починить ссылки в новом месте
            link_fixes += fix_links_in_file(dst / "_index.md")
        else:
            failed.append((src, msg))

    print(f"\nПеремещено успешно: {ok}/{len(moves)}")
    print(f"Исправлено ссылок: {link_fixes}")
    if failed:
        print(f"ОШИБОК: {len(failed)}")
        for src, msg in failed[:5]:
            print(f"  - {src.relative_to(REPO)}: {msg}")
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
