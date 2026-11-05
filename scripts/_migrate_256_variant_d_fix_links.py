#!/usr/bin/env python3
"""SkyNet — фикс ссылок варианта D.

Bug: в _migrate_256_variant_d.py для каждой части использовался old_dir обёртки,
а не её собственный src_dir. Из-за этого target_abs уходил выше repo root,
.exists() возвращал False, и ссылки оставались старыми (6 ../'s вместо 5).

Фикс: для каждого файла вычисляем его src_dir как (wrapper_src_dir / rel_to_wrapper_root).parent.
"""
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

MAPPING = [
    ("фантастические данные/модели/t600/реализация/t600",                "каркас",         "t600"),
    ("фантастические данные/модели/t800/реализация/t800",                "каркас",         "t800"),
    ("фантастические данные/модели/t850/реализация/t850",                "каркас",         "t850"),
    ("фантастические данные/модели/t_x/реализация/tx",                   "каркас",         "tx"),
    ("фантастические данные/модели/cameron_phillips/реализация/cameron", "каркас",         "cameron"),
    ("фантастические данные/модели/rev9/реализация/rev9",                "каркас",         "rev9"),
    ("фантастические данные/модели/marcus_wright/реализация/marcuswright","каркас",         "marcuswright"),
    ("фантастические данные/модели/hk_tank/реализация/hktank",            "каркас",         "hktank"),
    ("фантастические данные/модели/hk_aerial/реализация/hkaerial",       "каркас",         "hkaerial"),
    ("фантастические данные/модели/t1000/реализация/t1000",              "вычислительная", "t1000"),
    ("фантастические данные/модели/t1001/реализация/t1001",              "вычислительная", "t1001"),
]

LINK_RE = re.compile(r"\((\.\./[^)\s]*(?:%20[^)\s]*)*)\)")


def rewrite_links(new_file: Path, old_dir: Path) -> int:
    text = new_file.read_text(encoding="utf-8")
    count = 0

    def _sub(m: re.Match) -> str:
        nonlocal count
        old_rel = m.group(1)
        target_abs = (old_dir / old_rel.replace("%20", " ")).resolve()
        if not target_abs.exists():
            return m.group(0)
        new_rel = os.path.relpath(target_abs, new_file.parent.resolve())
        new_link = new_rel.replace(" ", "%20")
        if new_link != old_rel:
            count += 1
        return f"({new_link})"

    new_text = LINK_RE.sub(_sub, text)
    if count:
        new_file.write_text(new_text, encoding="utf-8")
    return count


def main() -> int:
    work_root = REPO / "работа и и" / "изделия"
    total = 0
    for src_rel, subsystem, wrapper_name in MAPPING:
        src_dir = REPO / src_rel  # путь (больше не существует в ФС, но Path позволяет строить)
        dest_dir = work_root / subsystem / wrapper_name
        if not dest_dir.is_dir():
            print(f"ERROR: нет назначения {dest_dir}")
            return 1
        n = 0
        for new_file in dest_dir.rglob("*.md"):
            rel_to_wrapper_root = new_file.relative_to(dest_dir)
            old_dir = (src_dir / rel_to_wrapper_root).parent
            n += rewrite_links(new_file, old_dir)
        if n:
            print(f"  ✓ {wrapper_name}: пересчитано {n} ссылок")
            total += n
    print(f"Всего пересчитано: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
