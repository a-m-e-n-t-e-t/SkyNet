#!/usr/bin/env python3
"""SkyNet — слияние дублей-материалов (F31/F32 remediation, v9.44).

Сливает файл-алиас в канонический файл:

  1. Проверяет, что алиас объявлен: alias.канонический_id == canonical.id,
     а canonical.псевдонимы содержит alias.id (иначе — отказ с подсказкой
     запустить scripts/migrate_aliases.py).
  2. Переносит в канонический файл:
     - непустые скаляры основных/дополнительных, которых нет (null) у канона
       → копируются БЕЗ перезаписи существующих значений канона;
     - записи стандартов, отсутствующие у канона → добавляются;
     - поле истчников из тела «## Источники» алиаса → при отсутствии
       аналогичных строк добавляются в конец секции канона;
     - вариант_структуры/сравнение_структур НЕ переносятся (структурные
       решения канона приоритетны; при конфликте — ручное слияние).
  3. Пополняет canonical.псевдонимы id алиаса (идемпотентно).
  4. Перезаписывает ВСЕ ссылки на alias_id по репозиторию (реальные данные/,
     graphs/, mermaid) → canonical_id: markdown-ссылки [x.md](...),
     плоские упоминания id, имена файлов alias.md → canonical.md.
  5. Удаляет файл-алиас (git rm).
  6. Печатает отчёт; --dry-run показывает план без изменений.

Запуск:
  python3 scripts/migrate_dedup_materials.py \
      --alias material_uglevolokno --canonical material_karbon [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from validate_decomposition import read_yaml_frontmatter, SKYNET_REPO  # noqa: E402

SCAN_ROOTS = [
    SKYNET_REPO / 'реальные данные',
]
# graphs/ НЕ сканируем: graph1_data.json и mermaid — генерируемые артефакты
# (generate_graphs.py --all запускается pre-commit'ом и перечитает файлы
# после удаления алиаса; строковая замена создала бы дубли узлов).
SCAN_EXTS = {'.md', '.json'}
# Каталоги, которые не сканируем (архивы правим только вручную)
SKIP_DIRS = {'архив', '_archive_oneoff', '.git', '__pycache__'}


def read_full(path: Path) -> tuple[dict | None, str, str]:
    """(data, yaml_text, body) через общий reader валидатора."""
    data, _, _ = read_yaml_frontmatter(path)
    text = path.read_text(encoding='utf-8')
    return data, text, text


def is_null(v) -> bool:
    return v is None or (isinstance(v, str) and v.strip() in ('', 'null', 'None'))


def merge_yaml_fields(canon_data: dict, alias_data: dict) -> list[str]:
    """Перенести в canon непустые значения основных/дополнительных, где null.
    Возвращает список описаний переносов (мутирует canon_data)."""
    moved = []
    for section in ('основные', 'дополнительные'):
        c = canon_data.get(section) or {}
        a = alias_data.get(section) or {}
        if not isinstance(c, dict) or not isinstance(a, dict):
            continue
        for key, val in a.items():
            if is_null(val):
                continue
            if key not in c or is_null(c.get(key)):
                c[key] = val
                moved.append(f'{section}.{key} = {str(val)[:60]!r}')
        canon_data[section] = c
    return moved


def merge_standards(canon_data: dict, alias_data: dict) -> list[str]:
    cs = canon_data.get('стандарты') or []
    as_ = alias_data.get('стандарты') or []
    if not isinstance(cs, list):
        cs = []
    added = []
    for s in as_:
        s = str(s).strip()
        if s and s not in {str(x).strip() for x in cs}:
            cs.append(s)
            added.append(s)
    if added:
        canon_data['стандарты'] = cs
    return added


def merge_body_sources(canon_yaml: str, alias_body: str) -> tuple[str, list[str]]:
    """Добавить строки источников из тела алиаса (## Источники) в YAML-комментарий
    канона не можем — возвращаем список строк для append в конец файла.
    Фактически источники алиаса дописываются в конец тела канона секцией
    «## Источники (слиты из <alias_id>)»."""
    m = re.search(r'(?ms)^## Источники\s*$\n(.*?)(?=^## |\Z)', alias_body)
    if not m:
        return canon_yaml, []
    lines = [l for l in m.group(1).strip().splitlines() if l.strip()]
    return canon_yaml, lines


def dump_yaml_value(v) -> str:
    return yaml.safe_dump(v, allow_unicode=True, default_flow_style=False,
                          sort_keys=False).rstrip('\n')


def dump_flow(v) -> str:
    """Компактное flow-представление для скаляров/списков в одну строку."""
    if isinstance(v, list):
        if not v:
            return '[]'
        return '[' + ', '.join(yaml_quote(str(x)) for x in v) + ']'
    if isinstance(v, str):
        return yaml_quote(v)
    return yaml.safe_dump(v, allow_unicode=True, default_flow_style=True,
                          sort_keys=False).strip()


def rewrite_yaml_scalar(yaml_text: str, key: str, value) -> str:
    """Заменить значение top-level ключа на flow-представление (одна строка)."""
    pattern = rf'(?m)^{re.escape(key)}:[^\n]*$'
    return re.sub(pattern, f'{key}: {dump_flow(value)}', yaml_text, count=1)


def set_nested_scalar(yaml_text: str, section: str, key: str, value) -> str:
    """Заменить `  key: ...` внутри блока section: (2-й уровень отступа)."""
    m = re.search(rf'(?ms)^{re.escape(section)}:[ \t]*\n(.*?)(?=^\S|\Z)',
                  yaml_text)
    if not m:
        return yaml_text
    block = m.group(1)
    new_block, n = re.subn(
        rf'(?m)^(\s+){re.escape(key)}:[^\n]*$',
        lambda mm: f"{mm.group(1)}{key}: {dump_flow(value)}",
        block, count=1)
    if n == 0:
        # ключа нет в блоке — добавить в конец блока (с отступом 2)
        new_block = block.rstrip('\n') + f'\n  {key}: {dump_flow(value)}\n'
    return yaml_text[:m.start(1)] + new_block + yaml_text[m.end(1):]


def yaml_quote(s: str) -> str:
    """Безопасное YAML-представление строки (module-level для dump_flow)."""
    if re.match(r'^[A-Za-z0-9_\-]+$', s):
        return s
    return "'" + s.replace("'", "''") + "'"


def rewrite_references(alias_id: str, canonical_id: str,
                       alias_stem: str, canonical_stem: str,
                       skip_files: set[Path] | None = None) -> list[str]:
    """Перезаписать ссылки alias → canonical по SCAN_ROOTS. Возвращает файлы.

    skip_files: пути, которые НЕ трогать (включая canonical_path — у него
    свои правила обновления псевдонимов/body).
    """
    skip_files = skip_files or set()
    changed = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for f in root.rglob('*'):
            if f.suffix not in SCAN_EXTS or not f.is_file():
                continue
            if any(part in SKIP_DIRS for part in f.parts):
                continue
            if f in skip_files:
                continue
            try:
                text = f.read_text(encoding='utf-8')
            except (UnicodeDecodeError, OSError):
                continue
            new = text
            # markdown-ссылки на файл алиаса
            new = new.replace(f'({alias_stem}.md)', f'({canonical_stem}.md)')
            new = new.replace(f'[{alias_stem}]', f'[{canonical_stem}]')
            # плоский полный id
            new = re.sub(rf'(?<![\w-]){re.escape(alias_id)}(?![\w-])',
                         canonical_id, new)
            # голый стем (без префикса material_) — значения материал: X,
            # таблицы | материал | X |, элементы списков
            new = re.sub(rf'(?<![\w-]){re.escape(alias_stem)}(?![\w-])',
                         canonical_stem, new)
            # имя файла алиаса (относительные ссылки)
            new = new.replace(f'{alias_stem}.md', f'{canonical_stem}.md')
            if new != text:
                f.write_text(new, encoding='utf-8')
                changed.append(str(f.relative_to(SKYNET_REPO)))
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--alias', required=True, help='id файла-алиаса (удаляется)')
    ap.add_argument('--canonical', required=True, help='id канонического файла')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    alias_stem = args.alias.replace('material_', '', 1)
    canonical_stem = args.canonical.replace('material_', '', 1)
    alias_path = SKYNET_REPO / 'реальные данные' / 'материалы' / f'{alias_stem}.md'
    canon_path = SKYNET_REPO / 'реальные данные' / 'материалы' / f'{canonical_stem}.md'

    if not alias_path.exists():
        print(f'ERROR: алиас-файл не найден: {alias_path}')
        return 2
    if not canon_path.exists():
        print(f'ERROR: канонический файл не найден: {canon_path}')
        return 2

    alias_data, alias_text = read_yaml_frontmatter(alias_path)[0], alias_path.read_text(encoding='utf-8')
    canon_data, _, _ = read_yaml_frontmatter(canon_path)
    if not alias_data or not canon_data:
        print('ERROR: YAML front matter не читается')
        return 2

    if str(alias_data.get('id')).strip() != args.alias:
        print(f"ERROR: id алиас-файла = {alias_data.get('id')!r}, ожидался {args.alias!r}")
        return 2
    if str(canon_data.get('id')).strip() != args.canonical:
        print(f"ERROR: id канона = {canon_data.get('id')!r}, ожидался {args.canonical!r}")
        return 2

    # --- Шаг 1: проверка объявления алиас-связи ---
    a_canon = str(alias_data.get('канонический_id') or '').strip()
    c_aliases = [str(x).strip() for x in (canon_data.get('псевдонимы') or [])]
    print(f'=== Слияние {args.alias} → {args.canonical} ===')
    print(f'  alias.канонический_id = {a_canon!r}')
    print(f'  canon.псевдонимы      = {c_aliases}')
    if a_canon != args.canonical:
        print(f'ГАРД: алиас не объявлен (канонический_id={a_canon!r} != {args.canonical!r}).')
        print('  → сначала python3 scripts/migrate_aliases.py (добавить пару в DUPLICATE_PAIRS)')
        return 3
    if args.alias not in c_aliases:
        print(f'ГАРД: канон не перечисляет алиас в псевдонимах {c_aliases}.')
        print('  → сначала python3 scripts/migrate_aliases.py')
        return 3

    # --- Шаг 2: перенос полей ---
    moved = merge_yaml_fields(canon_data, alias_data)
    std_added = merge_standards(canon_data, alias_data)
    _, src_lines = merge_body_sources('', alias_text)
    print(f'  перенос полей: {len(moved)}; стандартов +{len(std_added)}; '
          f'строк источников +{len(src_lines)}')
    for m in moved:
        print(f'    • {m}')
    for s in std_added:
        print(f'    + стандарт: {s}')

    # --- Шаг 3: псевдонимы канона (идемпотентно — алиас уже там по гарду) ---

    # --- Шаг 4: сборка нового текста канона ---
    # ВАЖНО: canon_data мутировал merge_yaml_fields/merge_standards — все
    # переносы ДОЛЖНЫ попасть в текст. Применяем их как точечные правки
    # yaml_text (а не дамп всего dict — сохранияем исходное форматирование).
    canon_text = canon_path.read_text(encoding='utf-8')
    m = re.match(r'^(---\n)(.*?)(\n---\n?)(.*)$', canon_text, re.DOTALL)
    if not m:
        print('ERROR: канонический файл без closing ---')
        return 2
    new_canon_yaml = m.group(2)

    # Стандарты: перезаписать список целиком (порядок сохранён)
    if std_added:
        new_canon_yaml = rewrite_yaml_scalar(new_canon_yaml, 'стандарты',
                                             canon_data.get('стандарты') or [])
    # Перенесённые скаляры: основные/дополнительные (вложенные блоки)
    for desc in moved:
        section, _, rest = desc.partition('.')
        key, _, _ = rest.partition(' =')
        val = (canon_data.get(section) or {}).get(key)
        new_canon_yaml = set_nested_scalar(new_canon_yaml, section, key, val)
    new_canon_yaml = rewrite_yaml_scalar(new_canon_yaml, 'канонический_id', args.canonical)
    new_canon_yaml = rewrite_yaml_scalar(new_canon_yaml, 'псевдонимы', c_aliases)
    # дата_обновления
    new_canon_yaml = re.sub(r'(?m)^дата_обновления:[^\n]*$',
                            'дата_обновления: 2026-11-06', new_canon_yaml, count=1)
    new_canon_text = m.group(1) + new_canon_yaml + m.group(3) + m.group(4)

    # Источники алиаса → в конец тела канона
    if src_lines:
        block = ('\n## Источники (слиты из ' + args.alias + ')\n\n'
                 + '\n'.join(src_lines) + '\n')
        new_canon_text = new_canon_text.rstrip('\n') + '\n' + block

    # --- Шаг 5: перезапись ссылок по репо (ПОСЛЕ dry-run проверки!) ---
    if args.dry_run:
        print('DRY-RUN: ничего не записано')
        return 0

    refs = rewrite_references(args.alias, args.canonical, alias_stem,
                              canonical_stem, skip_files={canon_path})
    print(f'  перезаписано ссылок в {len(refs)} файлах:')
    for r in refs[:15]:
        print(f'    → {r}')
    if len(refs) > 15:
        print(f'    … и ещё {len(refs) - 15}')

    canon_path.write_text(new_canon_text, encoding='utf-8')
    alias_path.unlink()
    print(f'✓ канон обновлён: {canon_path.name}')
    print(f'✓ алиас удалён: {alias_path.name}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
