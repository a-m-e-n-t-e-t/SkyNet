#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.62 Фаза 4: Убрать alias-физику из компонентов.

73 alias-файла в изделия/компоненты/ содержат `основные:` блок с физическими
свойствами (плотность, E, Tпл, k, cp, CTE) — дублирующими canonical-материал.

Заменяем `основные:` на `canonical_inherits: <canonical_id>` — указатель, что
физика наследуется из canonical. При рендеринге render_body.py будет
разрешать canonical_inherits и подставлять физику из canonical-файла.

Также убираем дублирующие поля:
- химический_состав (дублирует canonical)
- кристаллическая_структура (дублирует canonical)
- класс (дублирует canonical)
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
COMP_DIR = REPO / 'реальные данные' / 'изделия' / 'компоненты'


def remove_alias_physics(filepath: Path) -> bool:
    """Убрать дублирующие canonical-данные из alias-файла компонента."""
    text = filepath.read_text(encoding='utf-8')
    original = text

    # Найти канонический_id
    cid_match = re.search(r'^канонический_id:\s*(\S+)\s*$', text, re.MULTILINE)
    if not cid_match:
        return False
    canonical_id = cid_match.group(1).strip()

    # Если canonical_id == id (self-canonical, уже убран в Фазе 1) — skip
    id_match = re.search(r'^id:\s*(\S+)\s*$', text, re.MULTILINE)
    if not id_match:
        return False
    own_id = id_match.group(1).strip()
    if canonical_id == own_id:
        return False  # это canonical, не alias

    # Заменить блок основные: на canonical_inherits:
    # Найти блок 'основные:' (от 'основные:' до следующего top-level поля)
    m = re.search(r'^(основные:)\s*\n((?:  .+\n)*)', text, re.MULTILINE)
    if m:
        # Заменить на canonical_inherits
        text = text[:m.start()] + f'canonical_inherits: {canonical_id}\n' + text[m.end():]

    # Убрать дублирующие canonical-поля (химический_состав, кристаллическая_структура, класс)
    # Только если есть канонический_id (alias-файл)
    # химический_состав — убрать целиком (однострочное значение)
    text = re.sub(r'^химический_состав:\s*\'.*?\'\s*\n', '', text, count=1, flags=re.MULTILINE | re.DOTALL)
    # кристаллическая_структура
    text = re.sub(r'^кристаллическая_структура:\s*\'.*?\'\s*\n', '', text, count=1, flags=re.MULTILINE | re.DOTALL)

    if text != original:
        write_atomic(filepath, text)
        return True
    return False


def main():
    print("=== v9.62 Фаза 4: Убрать alias-физику из компонентов ===\n")

    if not COMP_DIR.exists():
        print("ERROR: директория компоненты/ не найдена")
        return

    changed = 0
    total = 0
    for f in COMP_DIR.rglob('_index.md'):
        total += 1
        if remove_alias_physics(f):
            changed += 1
            print(f"  OK: {f.relative_to(REPO)}")

    print(f"\nОбработано: {total}, изменено: {changed}")


if __name__ == '__main__':
    main()
