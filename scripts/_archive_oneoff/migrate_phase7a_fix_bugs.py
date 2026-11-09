#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 7a: Исправить баги миграции Phase 3b.

1. Слипшийся 'тип: изделиеуровень_иерархии: верхний' — добавить перенос строки.
   В transform_frontmatter regex был r'^(тип:\s*изделие\s*)$' — но \s* съедал
   последующие переносы. Нужно явное \n после 'изделие'.

2. F12a: несуществующие id — это Т-серия, у которых часть_t600_резиновая_кожа и т.д.
   были перемещены в работа и и/изделия/каркас/t600/ и работа и и/изделия/каркас/hktank/.
   Но в реальные данные/изделия/ вычислительная/ SkyNet-T600/_index.md есть ссылка
   на эти часть_*. Обновить ссылки на путь из работа и и/.

3. F21: SkyNet-T1000 подсистема 'вычислительная' — canon ожидает ≥1. Это связно с тем,
   что mimetic_polyalloy теперь в изделия/компоненты/ (подсистема: компоненты), а не
   в вычислительная/. Нужно обновить модель canon или подсистему SkyNet-T1000.
"""
import re
import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
TODAY = date.today().isoformat()


def fix_typo_typ_ierarhii():
    """Исправить 'тип: изделиеуровень_иерархии' → 'тип: изделие\nуровень_иерархии'."""
    print("=== Фаза 7a.1: Исправление typo 'тип: изделиеуровень_иерархии' ===\n")
    pattern = re.compile(r'^тип:\s*изделиеуровень_иерархии:\s*верхний', re.MULTILINE)
    fixed = 0
    for f in (REPO / 'реальные данные' / 'изделия' / 'компоненты').rglob('_index.md'):
        text = f.read_text(encoding='utf-8')
        if pattern.search(text):
            new_text = pattern.sub('тип: изделие\nуровень_иерархии: верхний', text)
            if new_text != text:
                write_atomic(f, new_text)
                fixed += 1
                print(f"  OK: {f.relative_to(REPO)}")
    # Также проверить работа и и/изделия/компоненты если есть
    ii_dir = REPO / 'работа и и' / 'изделия' / 'компоненты'
    if ii_dir.exists():
        for f in ii_dir.rglob('_index.md'):
            text = f.read_text(encoding='utf-8')
            if pattern.search(text):
                new_text = pattern.sub('тип: изделие\nуровень_иерархии: верхний', text)
                if new_text != text:
                    write_atomic(f, new_text)
                    fixed += 1
                    print(f"  OK: {f.relative_to(REPO)}")
    print(f"\nИсправлено файлов: {fixed}")


def fix_t600_hktank_refs():
    """Обновить ссылки в моделях Т-серии на часть_* которые были перемещены."""
    print("\n=== Фаза 7a.2: Исправление ссылок T600/HKTank ===\n")
    # Найти izdelie_SkyNet-T600/_index.md
    t600_files = list((REPO / 'реальные данные' / 'изделия').rglob('SkyNet-T600/_index.md'))
    hktank_files = list((REPO / 'реальные данные' / 'изделия').rglob('SkyNet-HKTank/_index.md'))

    for files, model_name in [(t600_files, 'T600'), (hktank_files, 'HKTank')]:
        for f in files:
            text = f.read_text(encoding='utf-8')
            # Проверить дочерние_части
            print(f"  {f.relative_to(REPO)} — дочерние_части в YAML:")
            # Найти все id после 'дочерние_части:'
            m = re.search(r'^дочерние_части:\s*\n((?:\s+-\s+\S+\n)*)', text, re.MULTILINE)
            if m:
                children_block = m.group(1)
                children = re.findall(r'-\s+(\S+)', children_block)
                print(f"    {children}")
                # Проверить какие из них не существуют
                for child_id in children:
                    # Найти файл через rglob
                    found = list((REPO / 'реальные данные' / 'изделия').rglob(f'{child_id}/_index.md'))
                    found += list((REPO / 'работа и и' / 'изделия').rglob(f'{child_id}/_index.md'))
                    found += list((REPO / 'реальные данные' / 'изделия').rglob(f'{child_id}__ии/_index.md'))
                    if found:
                        print(f"    ✓ {child_id} — найден в {found[0].parent.relative_to(REPO)}")
                    else:
                        print(f"    ✗ {child_id} — НЕ найден")


def main():
    fix_typo_typ_ierarhii()
    fix_t600_hktank_refs()


if __name__ == '__main__':
    main()
