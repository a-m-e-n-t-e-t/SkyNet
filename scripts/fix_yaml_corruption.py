#!/usr/bin/env python3
"""SkyNet — ремонт YAML-коррупции в front matter (следствие b97e283/ff154da-эпохи).

Три типа повреждений:
  1. Прилипший markdown-заголовок: `дата_обновления: 2026-11-03# Технология: X`
     (старый H1 склеен со значением при добавлении полей; заголовок — дубль
     `## Описание`, отрезается).
  2. Строка `...` (YAML document end marker) внутри block mapping — karbon.md.
  3. Незакавыченный plain scalar с `: ` внутри — химический_состав mo_hf.
  4. Битое значение `псевдонимы: aterial_XXX]` (потерян `[m` от
     `[material_XXX]`) — ni-ysz.md, p_vdf-trfe-ctfe.md (yaml-валидно, но
     семантически это должен быть список).

Идемпотентный. После каждой правки проверяет yaml.safe_load.
Запуск: python3 /home/z/my-project/scripts/fix_yaml_corruption.py [--dry-run]
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from migrate_aliases import read_fm_and_split  # noqa: E402

REPO = Path('/home/z/my-project/SkyNet')
DIRS = [REPO / 'реальные данные' / 'материалы',
        REPO / 'реальные данные' / 'технологии']


def quote_scalar(v: str) -> str:
    """Закавычить значение в одинарные кавычки (YAML single-quote escape)."""
    return "'" + v.replace("'", "''") + "'"


def fix_text(text: str, path: Path) -> tuple[str, list[str]]:
    """Вернуть (исправленный_текст, список_применённых_фиксов)."""
    fixes: list[str] = []
    # --- работы только над front matter (до первого markdown-заголовка) ---
    if not text.startswith('---'):
        return text, fixes
    rest = text[3:].lstrip('\n')
    m_head = re.search(r'^(#+\s+\S)', rest, re.MULTILINE)
    fm_end = m_head.start() if m_head else len(rest)
    fm, tail = rest[:fm_end], rest[fm_end:]

    # 1. Прилипший заголовок: key: value# H1 → key: value
    def unglue(mo: re.Match) -> str:
        fixes.append(f'отрезан прилипший заголовок: {mo.group(2)[:40]!r}')
        return mo.group(1)
    fm2 = re.sub(r'^([\wа-яё_]+\s*: [^\n#]*\d{4}-\d{2}-\d{2})#\s*(.+)$',
                 unglue, fm, flags=re.MULTILINE)

    # 2. Строка '...' внутри front matter
    n_dots = len(re.findall(r'^\.\.\.\s*$', fm2, flags=re.MULTILINE))
    if n_dots:
        fm2 = re.sub(r'^\.\.\.\s*\n', '', fm2, flags=re.MULTILINE)
        fixes.append(f'удалены YAML document-end маркеры "...": {n_dots}')

    # 3. Незакавыченный top-level скаляр с ': ' внутри
    def requote(mo: re.Match) -> str:
        key, val = mo.group(1), mo.group(2).rstrip()
        fixes.append(f'закавычен {key} (было двоеточие в plain scalar)')
        return f'{key}: {quote_scalar(val)}'
    fm3 = re.sub(
        r'^([\wа-яё_]+): ([^\'"\[{\n|#]+?: [^\n]*)$',
        requote, fm2, flags=re.MULTILINE)

    # 4. Битое значение псевдонимов: aterial_XXX] → [material_XXX]
    def realias(mo: re.Match) -> str:
        fixes.append(f'восстановлен список псевдонимов: [material_{mo.group(1)}]')
        return f'псевдонимы: [material_{mo.group(1)}]'
    fm4 = re.sub(r'^псевдонимы: aterial_([^]\n]*)\]\s*$',
                 realias, fm3, flags=re.MULTILINE)

    if not fixes:
        return text, fixes
    return '---\n' + fm4 + tail, fixes


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    changed = 0
    still_broken = []
    for d in DIRS:
        for p in sorted(d.glob('*.md')):
            if p.name.startswith('_'):
                continue
            text = p.read_text(encoding='utf-8')
            new_text, fixes = fix_text(text, p)
            if not fixes:
                continue
            # верификация после правки
            ok = False
            try:
                ok = yaml.safe_load(new_text.split('---\n')[1].split('\n---')[0]) is not None or True
            except yaml.YAMLError:
                ok = False
            # полная проверка — через read_fm_and_split на виртуальном файле
            tmp = REPO / '.tmp_fm_check.md'
            tmp.write_text(new_text, encoding='utf-8')
            data2, _, _, _ = read_fm_and_split(tmp)
            tmp.unlink()
            status = 'OK' if data2 is not None else 'STILL-BROKEN'
            print(f'{p.name}: {"; ".join(fixes)} -> {status}')
            if data2 is None:
                still_broken.append(p)
                continue
            if not args.dry_run:
                p.write_text(new_text, encoding='utf-8')
            changed += 1

    print()
    print(f'Итого: {changed} файлов изменено'
          + (' (dry-run — ничего не записано)' if args.dry_run else ''))
    if still_broken:
        print('ОСТАЛИСЬ БИТЫЕ:')
        for p in still_broken:
            print('  ', p)
        sys.exit(1)


if __name__ == '__main__':
    main()
