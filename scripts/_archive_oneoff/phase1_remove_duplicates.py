#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.62 Фаза 1: Убрать точные дубликаты из frontmatter.

Удаляет:
1. канонический_id == id (self-canonical) — 272 файла, default=self
2. псевдонимы: [] (пустые) — 326 файлов, default=[]
3. наследуемые: {} (пустые) — 971 файл, default={}
4. дополнительные: {} (пустые) — 286 файлов, default={}
5. свойства_таблица (full duplicate) — 13 файлов
6. применяется_в_изделиях_счёт (auto-computed) — 274 файла
7. gallinstan.md — дублирующая ## Описание
8. ## Источники (F28) → ## Источники (19 файлов)
9. иссл.группы — дублирующая ## Изделия и материалы (10 файлов)

НЕ удаляет (источник правды):
- дата_создания, дата_обновления (историческая инфа)
- источник_разбора: канон (самостоятельная семантика)
- канонический_id где != id (alias-файлы, 74 файла)
- псевдонимы с реальными значениями (20 файлов)
- наследуемые с реальными данными (102 файла)
"""
import re
import sys
import os
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
TODAY = date.today().isoformat()

stats = {
    'canonical_self': 0,
    'aliases_empty': 0,
    'inherited_empty': 0,
    'additional_empty': 0,
    'properties_table': 0,
    'usage_count': 0,
    'gallinstan_dup': 0,
    'f28_suffix': 0,
    'isg_dup_section': 0,
}


def remove_self_canonical(text: str, file_id: str) -> tuple:
    """Убрать 'канонический_id: <id>' если == id."""
    cid_match = re.search(r'^канонический_id:\s*(\S+)\s*$', text, re.MULTILINE)
    if not cid_match:
        return text, False
    cid = cid_match.group(1).strip()
    # Нормализовать: material_X vs X
    own_id_match = re.search(r'^id:\s*(\S+)\s*$', text, re.MULTILINE)
    if not own_id_match:
        return text, False
    own_id = own_id_match.group(1).strip()
    if cid == own_id:
        # Убрать строку
        new_text = re.sub(r'^канонический_id:\s*\S+\s*\n', '', text, count=1, flags=re.MULTILINE)
        stats['canonical_self'] += 1
        return new_text, True
    return text, False


def remove_empty_aliases(text: str) -> tuple:
    """Убрать 'псевдонимы: []' (пустые)."""
    if re.search(r'^псевдонимы:\s*\[\]\s*$', text, re.MULTILINE):
        new_text = re.sub(r'^псевдонимы:\s*\[\]\s*\n', '', text, count=1, flags=re.MULTILINE)
        stats['aliases_empty'] += 1
        return new_text, True
    return text, False


def remove_empty_inherited(text: str) -> tuple:
    """Убрать 'наследуемые: {}' (пустые)."""
    if re.search(r'^наследуемые:\s*\{\}\s*$', text, re.MULTILINE):
        new_text = re.sub(r'^наследуемые:\s*\{\}\s*\n', '', text, count=1, flags=re.MULTILINE)
        stats['inherited_empty'] += 1
        return new_text, True
    return text, False


def remove_empty_additional(text: str) -> tuple:
    """Убрать 'дополнительные: {}' (пустые)."""
    if re.search(r'^дополнительные:\s*\{\}\s*$', text, re.MULTILINE):
        new_text = re.sub(r'^дополнительные:\s*\{\}\s*\n', '', text, count=1, flags=re.MULTILINE)
        stats['additional_empty'] += 1
        return new_text, True
    return text, False


def remove_properties_table(text: str) -> tuple:
    """Убрать блок 'свойства_таблица:' (дубликат основные+дополнительные)."""
    # Найти начало блока
    m = re.search(r'^свойства_таблица:\s*\n((?:  .+\n)*)', text, re.MULTILINE)
    if not m:
        return text, False
    # Удалить весь блок
    block = m.group(0)
    new_text = text.replace(block, '', 1)
    stats['properties_table'] += 1
    return new_text, True


def remove_usage_count(text: str) -> tuple:
    """Убрать 'применяется_в_изделиях_счёт: <N>' (auto-computed)."""
    if re.search(r'^применяется_в_изделиях_счёт:\s*\d+\s*$', text, re.MULTILINE):
        new_text = re.sub(r'^применяется_в_изделиях_счёт:\s*\d+\s*\n', '', text, count=1, flags=re.MULTILINE)
        stats['usage_count'] += 1
        return new_text, True
    return text, False


def fix_f28_suffix(text: str) -> tuple:
    """Заменить '## Источники (F28)' → '## Источники'."""
    if '## Источники (F28)' in text:
        new_text = text.replace('## Источники (F28)', '## Источники')
        stats['f28_suffix'] += 1
        return new_text, True
    return text, False


def fix_gallinstan_dup(text: str, filepath: Path) -> tuple:
    """Удалить дублирующую ## Описание в gallinstan.md."""
    if 'gallinstan' not in filepath.name:
        return text, False
    # Найти все вхождения ## Описание
    matches = list(re.finditer(r'^##\s+Описание\s*$', text, re.MULTILINE))
    if len(matches) < 2:
        return text, False
    # Удалить второе вхождение и следующий за ним параграф
    second = matches[1]
    # Найти следующий ## заголовок или конец файла
    next_h2 = re.search(r'^##\s+', text[second.end():], re.MULTILINE)
    if next_h2:
        end_pos = second.end() + next_h2.start()
    else:
        end_pos = len(text)
    # Удалить от второго ## Описание до следующего ##
    new_text = text[:second.start()] + text[end_pos:]
    stats['gallinstan_dup'] += 1
    return new_text, True


def fix_isg_duplicate_section(text: str, filepath: Path) -> tuple:
    """Удалить дублирующую ## Изделия и материалы в иссл.группах."""
    if 'исследовательские_группы' not in str(filepath):
        return text, False
    if '## Изделия и материалы' not in text:
        return text, False
    # Удалить секцию целиком (от ## Изделия и материалы до следующего ##)
    new_text = re.sub(
        r'^##\s+Изделия\s+и\s+материалы\s*\n.*?(?=^##\s|\Z)',
        '',
        text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )
    if new_text != text:
        stats['isg_dup_section'] += 1
        return new_text, True
    return text, False


def process_file(filepath: Path) -> bool:
    """Обработать один файл. Вернуть True если были изменения."""
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception:
        return False
    original = text

    # Извлечь id для проверки self-canonical
    id_match = re.search(r'^id:\s*(\S+)\s*$', text, re.MULTILINE)
    file_id = id_match.group(1) if id_match else ''

    text, _ = remove_self_canonical(text, file_id)
    text, _ = remove_empty_aliases(text)
    text, _ = remove_empty_inherited(text)
    text, _ = remove_empty_additional(text)
    text, _ = remove_properties_table(text)
    text, _ = remove_usage_count(text)
    text, _ = fix_f28_suffix(text)
    text, _ = fix_gallinstan_dup(text, filepath)
    text, _ = fix_isg_duplicate_section(text, filepath)

    if text != original:
        write_atomic(filepath, text)
        return True
    return False


def main():
    print("=== v9.62 Фаза 1: Удаление точных дубликатов frontmatter ===\n")

    # Найти все .md файлы
    all_files = []
    for pattern in ['реальные данные/**/*.md', 'работа и и/**/*.md', 'фантастические данные/**/*.md']:
        all_files.extend(REPO.glob(pattern))
    # Исключить _*.md (индексные)
    all_files = [f for f in all_files if not f.name.startswith('_')]

    print(f"Файлов к обработке: {len(all_files)}")
    print()

    changed = 0
    for f in sorted(all_files):
        if process_file(f):
            changed += 1

    print(f"Изменено файлов: {changed}")
    print(f"\nСтатистика по типам:")
    for k, v in stats.items():
        if v > 0:
            print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
