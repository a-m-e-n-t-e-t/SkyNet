#!/usr/bin/env python3
"""SkyNet Web Verify CLI — v9.38 (A2: замена one-shot на рабочий инструмент)

CLI-раннер веб-верификации для cron-агента verify-task. Заменяет одноимённый
one-shot v9.31 (заархивирован: _archive_oneoff/web_verify_one_shot_v9.31.py),
который содержал захардкоженные данные от 2026-11-03 и не вызывался ни одним
workflow — агент делал правки файлов вручную (sed/python inline), без единого
пути исполнения и без анти-фабрикация-гардов.

Подкоманды:
  check  — проверить файл по критериям F22/F23/F25 (cron-протокол, шаг 5:
           «issue устарел?»). Exit 0 = все критерии выполнены (issue можно
           закрыть как устаревший), exit 1 = файл ещё требует работы.

  apply  — применить результаты РЕАЛЬНОГО web_search к файлу (шаг 6).
           Транзакционная запись (write_atomic), preview-режим --dry-run,
           анти-фабрикация-гард: отказывается писать generic-материалы,
           дефолтные габариты и не-URL источники.

Критерии (единый источник правды — validate_decomposition.py):
  F22: источник=web_search → источник_url заполнен конкретным http(s) URL
  F23a: материал не в GENERIC_MATERIALS
  F23b: описание не начинается с шаблонной фразы
  F23c: габариты не дефолтные 100×100×50
  F25*: габариты не старый mounting-шаблон 100×50×20 (сигнатура issue #146)

Примеры:
  python3 scripts/web_verify.py check --file "реальные данные/изделия/прочее/x/_index.md"
  python3 scripts/web_verify.py apply --file "реальные данные/.../_index.md" \
      --url https://pmc.ncbi.nlm.nih.gov/articles/PMC11643587 \
      --material uv-absorbing_pmma --dims 60,25,6 --mass 0.018 \
      --standards "ASTM D638" \
      --desc "Рамка преднатяга плёнки DES: ..." \
      --principle "Равномерный периметральный зажим ..." \
      --source-note "Gratz-Kelly et al., Materials 17(23):5993 (2024)"
"""

from __future__ import annotations
import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import read_yaml_frontmatter, GENERIC_MATERIALS, TEMPLATE_DESCRIPTIONS, SKYNET_REPO
import yaml as _yaml
from _helpers import write_atomic, TransactionBatch

# Старый mounting-шаблон (массовые дубликаты F25, issue #146): 100×50×20
TEMPLATE_DIMS = {(100, 100, 50), (100, 50, 20)}


# ============================================================================
# Проверка критериев
# ============================================================================

def verify_file(fpath: Path) -> tuple[bool, list[str]]:
    """Проверить файл по критериям F22/F23/F25*. Возвращает (all_ok, problems)."""
    problems: list[str] = []
    data, _yaml_text, body = read_yaml_frontmatter(fpath)
    if not data:
        return False, [f"{fpath}: YAML frontmatter не распознан"]

    file_id = data.get('id', fpath.name)

    # F22: источник_url
    source = str(data.get('источник', '')).strip()
    url = str(data.get('источник_url') or '').strip()
    if source == 'web_search':
        if not url or url in ('null', 'None'):
            problems.append(f"F22: источник=web_search, но источник_url пуст")
        elif not url.startswith(('http://', 'https://')):
            problems.append(f"F22: источник_url не http(s) URL: '{url[:60]}'")

    # F23a: материал не generic
    materials = data.get('материалы_частей', [])
    if isinstance(materials, list):
        for m in materials:
            if isinstance(m, dict):
                mat = str(m.get('материал', '')).strip().lower()
                if mat in GENERIC_MATERIALS:
                    problems.append(f"F23a: материал='{mat}' — шаблонная заглушка")

    # F23b: описание не шаблонное
    m = re.search(r"^## Описание\s*\n\s*\n(.+?)(?:\n##|\Z)", body or '', re.MULTILINE | re.DOTALL)
    if m:
        desc = m.group(1).strip()
        for tmpl in TEMPLATE_DESCRIPTIONS:
            if desc.startswith(tmpl):
                problems.append(f"F23b: описание начинается с шаблона '{tmpl[:30]}...'")
                break

    # F23c/F25*: габариты не дефолтные
    basic = data.get('основные', {})
    if isinstance(basic, dict):
        dims = basic.get('габариты_mm')
        if isinstance(dims, dict):
            triple = (dims.get('l'), dims.get('w'), dims.get('h'))
            if triple in TEMPLATE_DIMS:
                problems.append(f"F23c: габариты {triple[0]}×{triple[1]}×{triple[2]} — шаблонный fallback")

    return (len(problems) == 0), problems


# ============================================================================
# Точечные правки YAML front matter (без переформатирования всего блока)
# ============================================================================

def _replace_top_scalar(yaml_text: str, key: str, value_repr: str) -> str:
    """Заменить значение top-level скалярного поля (или добавить перед '---' / концом YAML)."""
    pattern = rf'(?m)^{re.escape(key)}:[^\n]*$'
    if re.search(pattern, yaml_text):
        return re.sub(pattern, f"{key}: {value_repr}", yaml_text, count=1)
    # Ключ отсутствует — вставить после последнего top-level поля перед закрывающим '---'
    # (или в конец блока, если '---' нет)
    lines = yaml_text.rstrip('\n').split('\n')
    # Найти позицию вставки: после последней строки без отступа
    insert_idx = len(lines)
    for i in range(len(lines) - 1, -1, -1):
        if lines[i] and not lines[i].startswith((' ', '\t', '-')) and ':' in lines[i]:
            insert_idx = i + 1
            break
    lines.insert(insert_idx, f"{key}: {value_repr}")
    return '\n'.join(lines) + ('\n' if yaml_text.endswith('\n') else '')


def _block_span(yaml_text: str, key: str) -> tuple[int, int] | None:
    """Границы блока `key:` (до следующего top-level ключа)."""
    m = re.search(rf'(?m)^{re.escape(key)}:[ \t]*$', yaml_text)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r'(?m)^\S', yaml_text[start:])
    end = start + nxt.start() if nxt else len(yaml_text)
    return (m.start(), end)


def set_standards(yaml_text: str, standards: list[str]) -> str:
    span = _block_span(yaml_text, 'стандарты')
    if span is None:
        return yaml_text
    lines = ['стандарты:'] + [f'  - {s}' for s in standards]
    return yaml_text[:span[0]] + '\n'.join(lines) + '\n' + yaml_text[span[1]:]


def set_materials(yaml_text: str, material_id: str) -> str:
    """Заменить материал во всех записях материалы_частей."""
    span = _block_span(yaml_text, 'материалы_частей')
    if span is None:
        return yaml_text
    block = yaml_text[span[0]:span[1]]
    new_block, n = re.subn(r'(?m)^(\s+материал:\s+)\S.*$', rf'\g<1>{material_id}', block)
    return yaml_text[:span[0]] + new_block + yaml_text[span[1]:]


def set_basic_fields(yaml_text: str, mass_kg: float | None = None,
                     share: float | None = None,
                     dims: tuple[float, float, float] | None = None) -> str:
    """Обновить основные.масса_kg / доля_массы_родителя / габариты_mm."""
    span = _block_span(yaml_text, 'основные')
    if span is None:
        return yaml_text
    block = yaml_text[span[0]:span[1]]
    if mass_kg is not None:
        block = re.sub(r'(?m)^(\s+масса_kg:\s+).*$',
                       rf'\g<1>{mass_kg:g}', block, count=1)
    if share is not None:
        block = re.sub(r'(?m)^(\s+доля_массы_родителя:\s+).*$',
                       rf'\g<1>{share:g}', block, count=1)
    if dims is not None:
        block = re.sub(
            r'(?m)^(\s+габариты_mm:\s*\n\s+l:\s+).*\n(\s+w:\s+).*\n(\s+h:\s+).*$',
            rf'\g<1>{dims[0]:g}\n\g<2>{dims[1]:g}\n\g<3>{dims[2]:g}',
            block, count=1)
    return yaml_text[:span[0]] + block + yaml_text[span[1]:]


# ============================================================================
# Точечные правки тела (markdown)
# ============================================================================

def set_body_description(body: str, desc: str) -> str:
    """Заменить первый абзац секции '## Описание'."""
    pattern = r'(?m)^(## Описание\s*\n\s*\n)(.+?)(\n##|\Z)'
    def repl(m):
        return m.group(1) + desc.strip() + ('\n' + m.group(3) if m.group(3) == '\n##' else m.group(3))
    new, n = re.subn(pattern, repl, body, count=1, flags=re.DOTALL)
    return new if n else body


def set_body_principle(body: str, principle: str) -> str:
    pattern = r'(?m)^(## Принцип работы\s*\n\s*\n)(.+?)(\n##|\Z)'
    def repl(m):
        return m.group(1) + principle.strip() + ('\n' + m.group(3) if m.group(3) == '\n##' else m.group(3))
    new, n = re.subn(pattern, repl, body, count=1, flags=re.DOTALL)
    return new if n else body


def set_body_param_rows(body: str, mass_kg: float | None, share: float | None,
                        dims: tuple[float, float, float] | None,
                        material_id: str | None, source_note: str) -> str:
    """Обновить строки таблицы '## Технические характеристики'."""
    if mass_kg is not None:
        body = re.sub(r'(?m)^\| масса \| [^|]+\| kg \| [^|]+\|$',
                      f'| масса | {mass_kg:g} | kg | {source_note} |', body, count=1)
    if share is not None:
        body = re.sub(r'(?m)^\| доля массы родителя \| [^|]+\| — \| [^|]+\|$',
                      f'| доля массы родителя | {share:g} | — | оценка |', body, count=1)
    if dims is not None:
        body = re.sub(r'(?m)^\| габариты \(Д×Ш×В\) \| [^|]+\| mm \| [^|]+\|$',
                      f'| габариты (Д×Ш×В) | {dims[0]:g}×{dims[1]:g}×{dims[2]:g} | mm | {source_note} |', body, count=1)
    if material_id is not None:
        body = re.sub(r'(?m)^\| материал \| [^|]+\| — \| [^|]+\|$',
                      f'| материал | {material_id} | — | {material_id}.md |', body, count=1)
    return body


def set_body_materials_link(body: str, material_id: str) -> str:
    pattern = r'(?m)^- `[^`]+` → \[`[^`]+`\]\(([^)]+)\)$'
    rel_dir = '../' * 4  # реальные данные/изделия/<кат>/<изделие>/часть_*/ → реальные данные/материалы/
    new, n = re.subn(pattern, f'- `{material_id}` → [`{material_id}.md`]({rel_dir}материалы/{material_id}.md)', body, count=1)
    return new if n else body


def set_body_sources(body: str, url: str, source_note: str) -> str:
    """Заменить строку 'Канон: ...' в '## Источники' на конкретную ссылку."""
    today = date.today().isoformat()
    new_line = f'- {source_note}: {url} (проверено {today})'
    # Заменить строку, начинающуюся с '- Канон:'
    new, n = re.subn(r'(?m)^- Канон:.*$', new_line, body, count=1)
    if n:
        return new
    # Или строку со старым URL
    if url not in body:
        new, n = re.subn(r'(?m)^- https?://\S+$', new_line, body, count=1)
        if n:
            return new
    # Или вставить после заголовка '## Источники\n\n'
    return re.sub(r'(?m)^(## Источники\s*\n\s*\n)', rf'\1{new_line}\n', body, count=1)


# ============================================================================
# apply
# ============================================================================

def _validate_inputs(url: str, material: str, dims_str: str | None) -> tuple[list[str], tuple | None]:
    """Анти-фабрикация-гарды. Возвращает (errors, dims_tuple_or_None)."""
    errors = []
    if not url.startswith(('http://', 'https://')):
        errors.append(f"url должен быть http(s) URL, получено: '{url[:60]}'")
    if material.strip().lower() in GENERIC_MATERIALS:
        errors.append(f"material '{material}' — generic-заглушка, отклонено")
    dims = None
    if dims_str:
        try:
            dims = tuple(float(x) for x in dims_str.split(','))
            if len(dims) != 3 or any(d <= 0 for d in dims):
                errors.append(f"dims должен быть 'L,W,H' из 3 положительных чисел, получено: '{dims_str}'")
                dims = None
            elif dims in TEMPLATE_DIMS:
                errors.append(f"dims {dims} — шаблонный fallback, отклонено")
                dims = None
        except ValueError:
            errors.append(f"dims не парсится как числа: '{dims_str}'")
    return errors, dims


def _build_new_text(fpath: Path, url: str, material_id: str, dims: tuple | None,
                    mass_kg: float | None, share: float | None,
                    standards: list[str] | None, desc: str | None,
                    principle: str | None, source_note: str) -> tuple[str, str, dict]:
    """Читает файл, возвращает (new_text, orig_text, orig_data).
    Не пишет на диск — вызывающий код решает write_atomic / batch."""
    data, yaml_text, body = read_yaml_frontmatter(fpath)
    if not data:
        raise ValueError(f"YAML frontmatter не распознан в {fpath}")
    orig_text = fpath.read_text(encoding='utf-8')
    today = date.today().isoformat()

    new_yaml = yaml_text
    new_yaml = _replace_top_scalar(new_yaml, 'дата_обновления', today)
    new_yaml = _replace_top_scalar(new_yaml, 'источник', 'web_search')
    new_yaml = _replace_top_scalar(new_yaml, 'источник_url', url)
    new_yaml = _replace_top_scalar(new_yaml, 'источник_дата', today)
    if standards:
        new_yaml = set_standards(new_yaml, standards)
    new_yaml = set_materials(new_yaml, material_id)
    new_yaml = set_basic_fields(new_yaml, mass_kg=mass_kg, share=share, dims=dims)

    new_body = body
    if desc:
        new_body = set_body_description(new_body, desc)
    if principle:
        new_body = set_body_principle(new_body, principle)
    new_body = set_body_param_rows(new_body, mass_kg, share, dims, material_id, source_note)
    new_body = set_body_materials_link(new_body, material_id)
    new_body = set_body_sources(new_body, url, source_note)

    new_text = '---\n' + new_yaml.rstrip('\n') + '\n---\n' + new_body
    return new_text, orig_text, data


# ============================================================================
# apply
# ============================================================================

def cmd_apply(args) -> int:
    fpath = Path(args.file)
    if not fpath.is_absolute():
        fpath = SKYNET_REPO / fpath
    if not fpath.exists():
        print(f"ERROR: файл не найден: {fpath}", file=sys.stderr)
        return 2

    errors, dims = _validate_inputs(args.url, args.material, args.dims)
    if errors:
        for e in errors:
            print(f"GUARD: {e}", file=sys.stderr)
        return 3

    mass_kg = args.mass
    share = args.share
    material_id = args.material.strip()
    standards = [s.strip() for s in args.standards.split(';')] if args.standards else None
    source_note = (args.source_note or 'web_search').strip()

    try:
        new_text, orig_text, data = _build_new_text(
            fpath, args.url, material_id, dims, mass_kg, share,
            standards, args.desc, args.principle, source_note)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    if args.dry_run:
        print("=== DRY RUN (ничего не записано) ===")
    else:
        write_atomic(fpath, new_text)
        print(f"=== Записано (atomic): {fpath} ===")

    changed = []
    for label, old, new in [
        ('источник_url', str(data.get('источник_url', '')), args.url),
        ('масса_kg', str(data.get('основные', {}).get('масса_kg', '')), f'{mass_kg:g}' if mass_kg is not None else None),
        ('габариты_mm', str(data.get('основные', {}).get('габариты_mm', '')), f'{dims[0]:g}×{dims[1]:g}×{dims[2]:g}' if dims else None),
        ('материал', '; '.join(str(m.get('материал', '')) for m in data.get('материалы_частей', []) if isinstance(m, dict)), material_id),
    ]:
        if new is not None and str(old) != str(new):
            changed.append(f"  {label}: {old[:40]!r} → {new[:60]!r}")
    print('\n'.join(changed) if changed else '  (front matter без изменений)')
    print(f"  байт: {len(orig_text)} → {len(new_text)}")
    return 0


# ============================================================================
# apply-batch — транзакционная batch-правка N файлов одной партией
# ============================================================================

# Структура спецификации (YAML):
#   url: https://example.com/datasheet.pdf
#   source_note: "Vendor Datasheet 2024"
#   files:
#     - file: реальные данные/.../_index.md
#       material: al_6061_t6
#       dims: 120,80,15
#       mass: 0.45
#       share: 0.18
#       standards: "ASTM B209;ISO 6361"
#       desc: "..."
#       principle: "..."
#     - file: ...

def cmd_apply_batch(args) -> int:
    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = SKYNET_REPO / spec_path
    if not spec_path.exists():
        print(f"ERROR: spec-файл не найден: {spec_path}", file=sys.stderr)
        return 2

    try:
        spec = _yaml.safe_load(spec_path.read_text(encoding='utf-8'))
    except _yaml.YAMLError as e:
        print(f"ERROR: spec YAML не парсится: {e}", file=sys.stderr)
        return 2
    if not isinstance(spec, dict) or 'files' not in spec:
        print("ERROR: spec должен быть dict с ключом 'files'", file=sys.stderr)
        return 2

    url = spec.get('url', '').strip()
    source_note = (spec.get('source_note') or 'web_search').strip()
    files_spec = spec['files']
    if not isinstance(files_spec, list) or not files_spec:
        print("ERROR: 'files' должен быть непустым списком", file=sys.stderr)
        return 2

    # --- 1. Валидация всех записей до начала записи (fail-fast) ---
    plans = []  # [(fpath, material_id, dims, mass_kg, share, standards, desc, principle, new_text)]
    errors = []
    for i, fs in enumerate(files_spec):
        if not isinstance(fs, dict):
            errors.append(f"files[{i}]: не dict")
            continue
        fpath = Path(fs['file'])
        if not fpath.is_absolute():
            fpath = SKYNET_REPO / fpath
        if not fpath.exists():
            errors.append(f"files[{i}]: файл не найден: {fpath}")
            continue

        mat = str(fs.get('material', '')).strip()
        dims_str = str(fs.get('dims', '') or '')
        # Per-file URL override: если у записи свой url/source_note — использовать их
        furl = str(fs.get('url') or url).strip()
        fnote = str(fs.get('source_note') or source_note).strip()
        sub_errs, dims = _validate_inputs(furl, mat, dims_str)
        for e in sub_errs:
            errors.append(f"files[{i}] ({fpath.name}): {e}")
        if sub_errs:
            continue

        try:
            new_text, _, _ = _build_new_text(
                fpath, furl, mat, dims,
                fs.get('mass'), fs.get('share'),
                [s.strip() for s in str(fs.get('standards', '')).split(';')] if fs.get('standards') else None,
                fs.get('desc'), fs.get('principle'), fnote)
        except ValueError as e:
            errors.append(f"files[{i}] ({fpath.name}): {e}")
            continue
        plans.append((fpath, mat, dims, fs.get('mass'), fs.get('share'),
                      fs.get('standards'), fs.get('desc'), fs.get('principle'), new_text))

    if errors:
        print(f"ERROR: {len(errors)} проблем(ы) в spec — batch отклонён:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 3
    if not plans:
        print("ERROR: нет валидных файлов в spec", file=sys.stderr)
        return 2

    # --- 2. Транзакционная запись ---
    print(f"=== apply-batch: {len(plans)} файлов, url={url[:60]} ===")
    if args.dry_run:
        print("--- DRY RUN (ничего не записано) ---")
        for fpath, mat, dims, *_rest, new_text in plans:
            print(f"  {fpath.name}: material={mat}, dims={dims}, +{len(new_text)}B")
        return 0

    try:
        with TransactionBatch() as batch:
            for fpath, _mat, _dims, _mass, _share, _std, _desc, _princ, new_text in plans:
                batch.write(fpath, new_text)
    except OSError as e:
        print(f"ERROR: batch write failed: {e}", file=sys.stderr)
        print("All staging cleaned up; targets untouched.", file=sys.stderr)
        return 4

    print(f"--- Записано {len(plans)} файлов (atomic batch) ---")
    for fpath, mat, dims, *_rest in plans:
        dims_str = f"{dims[0]:g}×{dims[1]:g}×{dims[2]:g}" if dims else "—"
        print(f"  ✓ {fpath.name}: material={mat}, dims={dims_str}")
    return 0


# ============================================================================
# check
# ============================================================================

def cmd_check(args) -> int:
    fpath = Path(args.file)
    if not fpath.is_absolute():
        fpath = SKYNET_REPO / fpath
    if not fpath.exists():
        print(f"ERROR: файл не найден: {fpath}", file=sys.stderr)
        return 2
    ok, problems = verify_file(fpath)
    if args.json:
        import json
        print(json.dumps({'file': str(fpath), 'ok': ok, 'problems': problems},
                         ensure_ascii=False, indent=2))
    else:
        status = '✓ PASS — все критерии F22/F23/F25* выполнены' if ok else '✗ FAIL'
        print(f"{fpath.name}: {status}")
        for p in problems:
            print(f"  - {p}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog='web_verify', description=__doc__.split('\n')[1])
    sub = ap.add_subparsers(dest='cmd', required=True)

    ap_check = sub.add_parser('check', help='Проверить файл по критериям F22/F23/F25*')
    ap_check.add_argument('--file', required=True, help='Путь к _index.md (относительный или абсолютный)')
    ap_check.add_argument('--json', action='store_true', help='JSON-вывод (для скриптов)')
    ap_check.set_defaults(func=cmd_check)

    ap_apply = sub.add_parser('apply', help='Применить web_search-данные к файлу')
    ap_apply.add_argument('--file', required=True, help='Путь к _index.md')
    ap_apply.add_argument('--url', required=True, help='URL источника (http/https)')
    ap_apply.add_argument('--material', required=True, help='ID материала (не generic)')
    ap_apply.add_argument('--dims', required=True, help='Габариты L,W,H в мм (не шаблонные)')
    ap_apply.add_argument('--mass', type=float, default=None, help='Масса, кг (опционально)')
    ap_apply.add_argument('--share', type=float, default=None, help='Доля массы родителя (опционально)')
    ap_apply.add_argument('--standards', default=None, help='Стандарты через ";" (опционально)')
    ap_apply.add_argument('--desc', default=None, help='Новое описание (первый абзац ## Описание)')
    ap_apply.add_argument('--principle', default=None, help='Принцип работы (## Принцип работы)')
    ap_apply.add_argument('--source-note', default=None, help='Подпись источника для таблиц/списка')
    ap_apply.add_argument('--dry-run', action='store_true', help='Показать изменения, не писать')
    ap_apply.set_defaults(func=cmd_apply)

    ap_batch = sub.add_parser('apply-batch',
        help='Транзакционно применить данные к N файлам из YAML spec (1 search → N файлов)')
    ap_batch.add_argument('--spec', required=True, help='Путь к YAML spec-файлу')
    ap_batch.add_argument('--dry-run', action='store_true', help='Показать изменения, не писать')
    ap_batch.set_defaults(func=cmd_apply_batch)

    args = ap.parse_args()
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
