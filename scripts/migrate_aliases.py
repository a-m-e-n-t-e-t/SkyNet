#!/usr/bin/env python3
"""SkyNet — мигратор канонических ID и псевдонимов (F31/F32 infrastructure).

Для каждого материала/технологии проставляет два новых top-level поля в YAML
front matter:

  канонический_id: <self.id>      # сам себе канонический по умолчанию
  псевдонимы: []                   # пустой список = явное отсутствие

Для известных дублей (DUPLICATE_PAIRS ниже) проставляет в каноническом файле
псевдоним на дубликат, а в дубле — канонический_id на канонический.

Идемпотентный: при повторном запуске не дублирует поля, не перезаписывает
непустые значения (только добавляет недостающие).

Запуск:
  python3 scripts/migrate_aliases.py [--dry-run]

После запуска: git add реальные\\ данные/материалы/ && git commit
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import yaml

REPO = Path('/home/z/my-project/SkyNet')
MAT_DIR = REPO / 'реальные данные' / 'материалы'
TECH_DIR = REPO / 'реальные данные' / 'технологии'

# Подтверждённые дубликаты. Формат:
#   (canonical_id, alias_id, note)
# Канонический = оставляем как основной файл. Алиас = помечается как
# перенаправление (для последующего merge в migrate_dedup_materials.py).
DUPLICATE_PAIRS = [
    # #661 создал ni-ysz.md поверх существующего ni_ysz_cermet.md.
    # ni-ysz.md — новее (commit bd6c9ae, 2026-11-06), имеет upgraded F27/F28
    # структуру (перколяционный кермет, 4 варианта, 12 источников).
    # ni_ysz_cermet.md — старше (2026-11-05), variant=multi_phase (generic).
    # Делаем ni-ysz каноническим, ni_ysz_cermet — алиасом (merge в Point 4).
    ('material_ni-ysz', 'material_ni_ysz_cermet',
     'Ni-YSZ кермет анода SOFC; ni-ysz.md — обновлён в #661'),

    # material_karbon.md vs material_uglevolokno.md — ПОВТОРНАЯ ПРОВЕРКА
    # (первичный разбор считал пару ложноположительной — это ошибка):
    #   karbon.md:      'Углерод >93 % (PAN-волокно, Toray T300)', ρ=1760,
    #                   k=10.5, E=230, вариант=fiber_reinforced, URL=T300 datasheet
    #   uglevolokno.md: 'углерод >90–95% (PAN-волокно), жгут 12K', ρ=1760,
    #                   k=10.5, E=230, вариант=fiber, URL=T300 datasheet (ТОТ ЖЕ)
    # Один материал (углеволокно Toray T300), идентичные свойства.
    # Ссылки в изделиях: karbon.md — 3 части (tpv, al-air cathode, mikroreaktor),
    # uglevolokno.md — 1 часть (superkondensatory electrode) → канонический
    # karbon (меньше перезаписей ссылок).
    ('material_karbon', 'material_uglevolokno',
     'углеволокно PAN Toray T300; karbon.md — 3 ссылки в изделиях vs 1'),

    # material_pvdf-trfe-ctfe.md vs material_p_vdf-trfe-ctfe.md — ПОВТОРНАЯ
    # ПРОВЕРКА (первичный разбор перепутал пару с p_vdf-trfe-cfe (#663) —
    # это ТРЕТИЙ отдельный файл, терполимер VDF/TrFE/CFE, chloroFLUOROethylene).
    # Здесь же оба файла — заглушки ОДНОГО полимера P(VDF-TrFE-CTFE)
    # (CTFE = chloroTRIfluoroethylene): состав 'PVDF-TrFE-CTFE' vs 'P' (обрезан),
    # оба ρ=null/k=null/вариант=single_phase/класс=металл (мусор CSV-экстракции).
    # Ссылок в изделиях: 0/0. Канонический p_vdf-trfe-ctfe — консистентно
    # с соседним именем p_vdf-trfe-cfe.md.
    ('material_p_vdf-trfe-ctfe', 'material_pvdf-trfe-ctfe',
     'терполимер P(VDF-TrFE-CTFE); оба — заглушки; консистентно с p_vdf-trfe-cfe'),

    # #751 (v2): material_mednyi_provod РЕКЛАССИФИЦИРОВАН в изделие
    # (реальные данные/изделия/система_питания/mednyi_provod/_index.md).
    # Причина: Cu-ETP C11000 как материал-вещество уже описан в
    # material_copper (состав, ρ, E, проводимость), а медный провод — это
    # форма выпуска (проволока, temper'ы, ASTM B1/B2/B3), то есть ИЗДЕЛИЕ
    # уровня 1. Старая запись о паре-кандидате на слияние — изъята вместе
    # с f32_fp_exclude в check_F32 (после реклассификации F32 их больше
    # не сравнивает — они в разных категориях).

    # material_pbo2.md vs material_spongy_lead.md: PbO₂ (диоксид свинца,
    # керамика) и пористый свинец (металл) — принципиально разные материалы.
    # Совпадение source_url — ошибка заполнения spongy_lead (нужно исправить
    # отдельно). Ложноположительный.
]


def read_fm_and_split(path: Path) -> tuple[dict | None, str, str, str]:
    """Вернуть (yaml_data, yaml_text, body, full_text).

    Использует ту же эвристику что validate_decomposition._read_yaml_frontmatter:
    YAML = всё от opening `---` до первого markdown-заголовка `# ...` (или до
    конца файла, если заголовка нет). Это устойчиво к файлам с одним `---`
    (без closing) и к YAML с inline `:` в комментариях.
    """
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return None, '', '', text

    rest = text[3:].lstrip('\n')
    body_match = re.search(r'^(#+\s+\S)', rest, re.MULTILINE)
    if body_match:
        yaml_section = rest[:body_match.start()].rstrip()
        body = rest[body_match.start():]
        closing = re.search(r'\n---\s*$', yaml_section, re.MULTILINE)
        if closing:
            yaml_text = yaml_section[:closing.start()].rstrip()
        else:
            yaml_text = yaml_section
    else:
        yaml_text = rest.rstrip()
        closing = re.search(r'\n---\s*$', yaml_text, re.MULTILINE)
        if closing:
            yaml_text = yaml_text[:closing.start()].rstrip()
        body = ''

    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError:
        return None, yaml_text, body, text
    return data, yaml_text, body, text


def insert_after_id(yaml_text: str, key: str, value_repr: str) -> str:
    """Вставить `key: value_repr` сразу после строки `id: ...`.
    Если key уже есть — не трогаем (идемпотентность).
    """
    pattern_existing = rf'(?m)^{re.escape(key)}:\s*\S'
    if re.search(pattern_existing, yaml_text):
        return yaml_text
    # Найти `id: ...` строку
    m = re.search(r'(?m)^id:\s*\S[^\n]*$', yaml_text)
    if not m:
        # нет id — вставить в начало
        return f'{key}: {value_repr}\n' + yaml_text
    insert_pos = m.end()
    # найти конец строки (перенос)
    nl = yaml_text.find('\n', insert_pos)
    if nl == -1:
        nl = len(yaml_text)
    return yaml_text[:nl + 1] + f'{key}: {value_repr}\n' + yaml_text[nl + 1:]


def set_top_scalar(yaml_text: str, key: str, value_repr: str) -> str:
    """Установить top-level scalar (заменить если есть, иначе вставить после id).
    """
    pattern = rf'(?m)^{re.escape(key)}:\s*[^\n]*$'
    if re.search(pattern, yaml_text):
        return re.sub(pattern, f'{key}: {value_repr}', yaml_text, count=1)
    return insert_after_id(yaml_text, key, value_repr)


def yaml_quote(s: str) -> str:
    """Безопасное YAML-представление строки. Используем single-quote для kириллицы."""
    if re.match(r'^[A-Za-z0-9_\-]+$', s):
        return s
    return "'" + s.replace("'", "''") + "'"


def yaml_list_repr(items: list[str]) -> str:
    """YAML inline list: [a, b, c] с quoted strings."""
    if not items:
        return '[]'
    parts = [yaml_quote(i) for i in items]
    return '[' + ', '.join(parts) + ']'


def process_file(path: Path, canonical_for: dict[str, str],
                 aliases_for: dict[str, list[str]],
                 dry_run: bool) -> tuple[bool, str]:
    """Обработать один файл. Возвращает (changed, summary)."""
    data, yaml_text, body, orig = read_fm_and_split(path)
    if not data or not isinstance(data, dict):
        return False, f'  SKIP {path.name}: YAML не распознан'

    rid = str(data.get('id', '')).strip()
    if not rid:
        return False, f'  SKIP {path.name}: нет id'

    new_yaml = yaml_text
    changes = []

    # Если этот файл — алиас (canonical_for[rid] указывает на другой canonical)
    if rid in canonical_for:
        canonical = canonical_for[rid]
        # канонический_id = canonical (НЕ self)
        existing = str(data.get('канонический_id', '')).strip()
        if existing != canonical:
            new_yaml = set_top_scalar(new_yaml, 'канонический_id',
                                      yaml_quote(canonical))
            changes.append(f'канонический_id={canonical}')
        # псевдонимы должны быть [] (алиас не имеет своих алиасов)
        existing_aliases = data.get('псевдонимы')
        if not isinstance(existing_aliases, list) or existing_aliases:
            new_yaml = set_top_scalar(new_yaml, 'псевдонимы', '[]')
            changes.append('псевдонимы=[]')
    else:
        # Это канонический файл (или автономный)
        # канонический_id = self.id (если не установлен или отличается)
        existing_canon = str(data.get('канонический_id', '')).strip()
        if existing_canon != rid:
            new_yaml = set_top_scalar(new_yaml, 'канонический_id',
                                      yaml_quote(rid))
            changes.append(f'канонический_id={rid}')

        # псевдонимы = aliases_for.get(rid, []) (если ещё не заданы вручную)
        expected_aliases = aliases_for.get(rid, [])
        existing_aliases = data.get('псевдонимы')
        if isinstance(existing_aliases, list) and existing_aliases:
            # Уже есть непустой список — не трогаем (уважаем ручные правки),
            # но проверим что все ожидаемые алиасы там есть
            missing = [a for a in expected_aliases if a not in existing_aliases]
            if missing:
                new_aliases = existing_aliases + missing
                new_yaml = set_top_scalar(new_yaml, 'псевдонимы',
                                          yaml_list_repr(new_aliases))
                changes.append(f'псевдонимы+={missing}')
        else:
            # Установить (пустой или ожидаемые алиасы)
            if expected_aliases:
                new_yaml = set_top_scalar(new_yaml, 'псевдонимы',
                                          yaml_list_repr(expected_aliases))
                changes.append(f'псевдонимы={expected_aliases}')
            else:
                # пустой список
                if not isinstance(existing_aliases, list):
                    new_yaml = set_top_scalar(new_yaml, 'псевдонимы', '[]')
                    changes.append('псевдонимы=[]')

    if new_yaml == yaml_text:
        return False, f'  OK   {path.name} (no changes)'

    new_text = '---\n' + new_yaml.rstrip('\n') + '\n---\n' + body
    if not dry_run:
        path.write_text(new_text, encoding='utf-8')

    sign = '✓' if not dry_run else '?'
    return True, f'  {sign} {path.name}: {", ".join(changes)}'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--dry-run', action='store_true',
                    help='Показать изменения без записи')
    ap.add_argument('--only', choices=['materials', 'technologies'],
                    help='Обработать только одну категорию')
    args = ap.parse_args()

    # Построить maps из DUPLICATE_PAIRS
    canonical_for: dict[str, str] = {}   # alias_id → canonical_id
    aliases_for: dict[str, list[str]] = {}  # canonical_id → [alias_id, ...]
    for canon, alias, _note in DUPLICATE_PAIRS:
        canonical_for[alias] = canon
        aliases_for.setdefault(canon, []).append(alias)

    print('=== migrate_aliases.py ===')
    print(f'Подтверждённых пар дублей: {len(DUPLICATE_PAIRS)}')
    for canon, alias, note in DUPLICATE_PAIRS:
        print(f'  • {alias} → canonical: {canon}')
        print(f'      ({note})')
    print()

    targets = []
    if not args.only or args.only == 'materials':
        targets.extend(sorted(MAT_DIR.glob('*.md')))
    if not args.only or args.only == 'technologies':
        targets.extend(sorted(TECH_DIR.glob('*.md')))

    changed = 0
    skipped = 0
    for f in targets:
        if f.name.startswith('_'):
            continue
        ok, msg = process_file(f, canonical_for, aliases_for, args.dry_run)
        print(msg)
        if ok:
            changed += 1
        else:
            skipped += 1

    print()
    print(f'Итого: {changed} изменено, {skipped} пропущено')
    if args.dry_run:
        print('(dry-run — ничего не записано)')


if __name__ == '__main__':
    main()
