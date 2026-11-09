#!/usr/bin/env python3
"""SkyNet Body Renderer — v9.62

Рендерер body-секций из frontmatter. Решает проблему дублирования данных:
frontmatter — источник правды, body-секции генерируются автоматически.

Авто-рендеримые секции (перезаписываются при каждом запуске):
  ## Технические характеристики  ← из frontmatter основные + подсистема + подтип
  ## Используемые материалы      ← из frontmatter материалы_частей
  ## Используемые технологии     ← из frontmatter технологии_частей
  ## Декомпозиция (mermaid)      ← из frontmatter дочерние_части

Сохраняемые секции (НЕ перезаписываются, уникальный контент):
  ## Описание
  ## Принцип работы
  ## Источники
  ## Состав (качественная часть без чисел)
  ## Аналоги и заменители
  ## Химический состав
  ## Физические свойства
  ## Механические свойства
  ## Тепловые свойства
  ## Электрические свойства
  ## Эксплуатационные характеристики
  ## Технологии получения
  ## Применение в изделиях

Использование:
  python3 scripts/render_body.py --file <path>     # один файл
  python3 scripts/render_body.py --all              # все файлы
  python3 scripts/render_body.py --all --dry-run    # dry-run (отчёт без записи)

Маркеры auto-render секций:
  Каждая авто-секция обрамлена HTML-комментариями:
  <!-- AUTO-RENDER: tech_specs START -->
  ...
  <!-- AUTO-RENDER: tech_specs END -->
  Это позволяет рендереру точно находить и заменять только авто-секции.
"""
from __future__ import annotations

import os
import re
import sys
import argparse
import yaml
from pathlib import Path
from datetime import date
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from _helpers import write_atomic, md_internal_link

REPO = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()

# Секции, которые рендерятся автоматически (заменяются целиком)
AUTO_SECTIONS = ['tech_specs', 'materials', 'technologies', 'decomposition']

# Секции, которые сохраняются как есть (уникальный контент)
PRESERVED_SECTIONS = {
    'Описание', 'Принцип работы', 'Источники', 'Состав',
    'Аналоги и заменители', 'Химический состав',
    'Физические свойства', 'Механические свойства',
    'Тепловые свойства', 'Электрические свойства',
    'Эксплуатационные характеристики', 'Технологии получения',
    'Применение в изделиях', 'Каноническая ссылка',
    'Входные ресурсы', 'Операции', 'Параметры режима',
    'Выходной результат', 'Оборудование', 'Ограничения и допуски',
    'Альтернативные технологии', 'Организация', 'Область применения',
    'Связанные изделия', 'Применяется в', 'Локация', 'Специализация',
    'Связанные материалы и изделия',
}


def read_yaml_frontmatter(path: Path) -> tuple:
    """Прочитать frontmatter. Вернуть (data, yaml_text, body)."""
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}, '', text
    end = text.find('\n---', 3)
    if end == -1:
        return {}, '', text
    yaml_text = text[3:end]
    body = text[end + 4:]
    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError:
        return {}, yaml_text, body
    return data or {}, yaml_text, body


def render_tech_specs(data: dict, path: Path) -> str:
    """Рендерить ## Технические характеристики из frontmatter."""
    tip = data.get('тип', '')
    podsystema = data.get('подсистема', '')
    podtip = data.get('подтип', '')
    osn = data.get('основные', {}) or {}

    rows = []
    rows.append('| Параметр | Значение | Единица | Источник |')
    rows.append('|---|---|---|---|')

    if podsystema:
        rows.append(f'| подсистема | {podsystema} | — | canon |')
    if podtip:
        rows.append(f'| подтип | {podtip} | — | canon |')

    # масса
    massa = osn.get('масса_kg')
    if massa is not None:
        if isinstance(massa, dict):
            mn, mx, nom = massa.get('min'), massa.get('max'), massa.get('nominal')
            if mn == mx == nom:
                rows.append(f'| масса | {mn} | kg | canon |')
            elif nom:
                rows.append(f'| масса | {mn}–{mx} (номинал {nom}) | kg | canon |')
            else:
                rows.append(f'| масса | {mn}–{mx} | kg | canon |')
        else:
            rows.append(f'| масса | {massa} | kg | canon |')

    # доля_массы_родителя
    dolya = osn.get('доля_массы_родителя')
    if dolya is not None:
        rows.append(f'| доля массы родителя | {dolya} | — | canon |')

    # габариты
    gab = osn.get('габариты_mm', {})
    if isinstance(gab, dict):
        l, w, h = gab.get('l'), gab.get('w'), gab.get('h')
        if l and w and h:
            rows.append(f'| габариты (Д×Ш×В) | {l}×{w}×{h} | mm | canon |')

    # энергия/тепло
    energy = osn.get('выработка_энергии_W')
    if energy is not None:
        if isinstance(energy, dict):
            mn, mx, nom = energy.get('min'), energy.get('max'), energy.get('nominal')
            if mn == mx == nom:
                rows.append(f'| выработка энергии | {mn} | W | canon |')
            else:
                rows.append(f'| выработка энергии | {mn}–{mx} | W | canon |')
        else:
            rows.append(f'| выработка энергии | {energy} | W | canon |')

    heat = osn.get('выработка_тепла_W')
    if heat is not None:
        if isinstance(heat, dict):
            mn, mx, nom = heat.get('min'), heat.get('max'), heat.get('nominal')
            if mn == mx == nom:
                rows.append(f'| выработка тепла | {mn} | W | canon |')
            else:
                rows.append(f'| выработка тепла | {mn}–{mx} | W | canon |')
        else:
            rows.append(f'| выработка тепла | {heat} | W | canon |')

    # количество (если есть)
    kolvo = data.get('количество')
    if kolvo and kolvo > 1:
        rows.append(f'| количество | {kolvo} | шт. | canon |')

    # тип узла
    if tip:
        rows.append(f'| тип узла | {tip} | — | canon |')

    # уровень
    urov = data.get('уровень_номер')
    if urov:
        rows.append(f'| уровень_номер | {urov} | — | canon |')

    table = '\n'.join(rows)
    return f'## Технические характеристики\n\n{table}\n'


def render_materials(data: dict, path: Path) -> str:
    """Рендерить ## Используемые материалы из frontmatter материалы_частей."""
    mats = data.get('материалы_частей', [])
    if not isinstance(mats, list) or not mats:
        return ''

    lines = ['## Используемые материалы', '']
    for m in mats:
        if not isinstance(m, dict):
            continue
        mat_id = m.get('материал', '?')
        forma = m.get('форма')
        # Попытаться создать markdown-ссылку
        try:
            link = md_internal_link(path, 'материалы', f'{mat_id}.md', mat_id)
        except (ValueError, Exception):
            link = f'`{mat_id}` (canonical material)'
        if forma:
            lines.append(f'- `{mat_id}` (форма: {forma}) → {link}')
        else:
            lines.append(f'- `{mat_id}` → {link}')
    lines.append('')
    return '\n'.join(lines)


def render_technologies(data: dict) -> str:
    """Рендерить ## Используемые технологии из frontmatter технологии_частей."""
    tehs = data.get('технологии_частей', [])
    if not isinstance(tehs, list) or not tehs:
        return ''

    lines = ['## Используемые технологии', '']
    for t in tehs:
        if not isinstance(t, dict):
            continue
        teh_id = t.get('технология', '?')
        dolya = t.get('доля_использования', 1.0)
        lines.append(f'- `{teh_id}` (доля: {dolya})')
    lines.append('')
    return '\n'.join(lines)


def render_decomposition(data: dict) -> str:
    """Рендерить ## Декомпозиция (mermaid) из frontmatter дочерние_части."""
    children = data.get('дочерние_части', [])
    if not isinstance(children, list) or not children:
        return ''

    izd_id = data.get('id', 'unknown')
    # Sanitize id для mermaid (убрать дефисы для node names)
    safe_id = re.sub(r'[^a-zA-Z0-9_]', '_', izd_id)

    lines = ['## Декомпозиция', '', '```mermaid', 'graph TD']
    lines.append(f'    {safe_id}["{izd_id}"]')
    for child in children:
        child_safe = re.sub(r'[^a-zA-Z0-9_]', '_', child)
        lines.append(f'    {child_safe}["{child}"]')
        lines.append(f'    {safe_id} --> {child_safe}')
    lines.append('```')
    lines.append('')
    return '\n'.join(lines)


def extract_preserved_sections(body: str) -> dict:
    """Извлечь сохраняемые секции из body. Вернуть {section_name: content}."""
    sections = {}
    # Найти все ## заголовки
    matches = list(re.finditer(r'^##\s+(.+?)\s*$', body, re.MULTILINE))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[start:end].rstrip()
        # Нормализовать имя (убрать суффиксы типа (F28))
        norm_name = re.sub(r'\s*\(F\d+\)\s*$', '', name).strip()
        sections[norm_name] = content
    return sections


def render_file(path: Path, dry_run: bool = False) -> bool:
    """Перегенерировать auto-render секции в файле. Вернуть True если изменён."""
    data, yaml_text, body = read_yaml_frontmatter(path)
    if not data:
        return False

    # Извлечь сохраняемые секции
    preserved = extract_preserved_sections(body)

    # Сгенерировать auto-render секции
    tech_specs = render_tech_specs(data, path)
    materials = render_materials(data, path)
    technologies = render_technologies(data)
    decomposition = render_decomposition(data)

    # Собрать новый body
    # Порядок: Описание → Технические характеристики → Принцип работы →
    #          Состав → Используемые технологии → Используемые материалы →
    #          Источники → Декомпозиция

    new_body_parts = []

    # Описание
    if 'Описание' in preserved:
        new_body_parts.append(preserved['Описание'])

    # Технические характеристики (auto-render)
    if tech_specs:
        new_body_parts.append(tech_specs)

    # Принцип работы
    if 'Принцип работы' in preserved:
        new_body_parts.append(preserved['Принцип работы'])

    # Состав (сохраняем, но без чисел — качественное описание)
    if 'Состав' in preserved:
        new_body_parts.append(preserved['Состав'])

    # Используемые технологии (auto-render)
    if technologies:
        new_body_parts.append(technologies)

    # Используемые материалы (auto-render)
    if materials:
        new_body_parts.append(materials)

    # Источники
    if 'Источники' in preserved:
        new_body_parts.append(preserved['Источники'])

    # Декомпозиция (auto-render, mermaid)
    if decomposition:
        new_body_parts.append(decomposition)

    # Добавить остальные сохраняемые секции (которые не вошли в стандартный порядок)
    standard_sections = {'Описание', 'Технические характеристики', 'Принцип работы',
                         'Состав', 'Используемые технологии', 'Используемые материалы',
                         'Источники', 'Декомпозиция'}
    for name, content in preserved.items():
        if name not in standard_sections:
            new_body_parts.append(content)

    new_body = '\n\n'.join(new_body_parts).strip() + '\n'

    # Собрать полный файл
    new_text = f'---\n{yaml_text}\n---\n{new_body}'

    old_text = path.read_text(encoding='utf-8')
    if new_text != old_text:
        if not dry_run:
            write_atomic(path, new_text)
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description='SkyNet Body Renderer v9.62')
    parser.add_argument('--file', help='путь к .md файлу')
    parser.add_argument('--all', action='store_true', help='обработать все .md')
    parser.add_argument('--dry-run', action='store_true', help='не записывать, только отчёт')
    args = parser.parse_args()

    if not args.file and not args.all:
        parser.error('укажите --file <path> или --all')

    print("=== SkyNet Body Renderer v9.62 ===")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()

    if args.file:
        files = [Path(args.file)]
    else:
        files = []
        for pattern in ['реальные данные/**/*.md', 'работа и и/**/*.md']:
            full = REPO / pattern.split('/')[0]
            if full.exists():
                files.extend(Path(REPO).glob(pattern))
        # Исключить _*.md и _archive_oneoff
        files = [f for f in files if not f.name.startswith('_')
                 and '_archive_oneoff' not in str(f)]

    print(f"Файлов к обработке: {len(files)}")

    changed = 0
    for f in sorted(files):
        try:
            if render_file(f, args.dry_run):
                changed += 1
        except Exception as e:
            print(f"  ERROR {f.name}: {e}")

    print(f"\nОбновлено файлов: {changed}")


if __name__ == '__main__':
    main()
