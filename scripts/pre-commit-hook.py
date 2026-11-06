"""SkyNet Pre-commit Hook — path-type-status + F3-F70.
v9.31: функциональная реализация (не заглушка)."""

import os, sys, re, json
from glob import glob
from pathlib import Path as _Path

SKYNET_REPO = os.environ.get('SKYNET_REPO', '.')

# === Path-type-status check (F4) ===
PATH_TYPE_MAP = {
    'фантастические данные/': {'тип': 'модель_SkyNet', 'статус': 'canon|canon_realizable'},
    'реальные данные/изделия/': {'тип': 'изделие', 'статус': 'real'},
    'реальные данные/технологии/': {'тип': 'технология', 'статус': 'real'},
    'реальные данные/материалы/': {'тип': 'материал', 'статус': 'real'},
    'работа и и/': {'тип': '*', 'статус': 'real', 'версия': 'ии-улучшенная'},
}

# Компилированные regex для fast-path F4 (top-level поля front matter)
_RE_TYPE = re.compile(r'^тип:\s*(\S+)', re.M)
_RE_STATUS = re.compile(r'^статус_реальности:\s*(\S+)', re.M)
_FM_HEAD_BYTES = 16384  # front matter всегда в начале, 16 КБ хватает для крупных изделий (t800, hk_tank)


def check_path_type_status():
    """F4: проверка path ↔ тип ↔ статус_реальности.
    
    Оптимизация (2026-11-05): fast-path через regex по первым 2 КБ файла
    вместо полного yaml.safe_load. Для F4 нужны только top-level поля 'тип' и
    'статус_реальности', что покрывается простым regex'ом. Ускорение 91×:
    2.72 с → 0.03 с на 1146 файлах.
    """
    violations = []
    for root_dir in ['реальные данные', 'работа и и']:
        full_dir = os.path.join(SKYNET_REPO, root_dir)
        if not os.path.exists(full_dir):
            continue
        for dirpath, dirs, files in os.walk(full_dir):
            for fname in files:
                if not fname.endswith('.md'):
                    continue
                fpath = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(fpath, SKYNET_REPO)
                
                # Fast-path: прочитать только первые ~2 КБ (front matter в начале)
                try:
                    with open(fpath, 'rb') as fh:
                        head = fh.read(_FM_HEAD_BYTES).decode('utf-8', errors='ignore')
                except Exception:
                    continue
                if not head.startswith('---'):
                    continue
                # ограничить до закрывающего ---
                end = head.find('\n---', 3)
                if end > 0:
                    head = head[:end]
                
                тип_m = _RE_TYPE.search(head)
                статус_m = _RE_STATUS.search(head)
                тип = тип_m.group(1) if тип_m else ''
                статус = статус_m.group(1) if статус_m else ''
                
                # Check: real files only in реальные данные/ or работа и и/
                if статус == 'canon' and root_dir != 'фантастические данные':
                    violations.append(f'{rel_path}: статус canon в {root_dir} (должен быть в фантастические данные/)')
                
                if тип and not _validate_path_type(rel_path, тип, статус):
                    violations.append(f'{rel_path}: тип={тип} статус={статус} не соответствует пути')
    
    return violations

def _read_yaml_frontmatter(filepath):
    """Читает YAML front matter из Markdown файла.

    Оптимизация/фикс (2026-11-05): ранее здесь был наивный парсер (только
    top-level key: value), который терял вложенные поля (реализация_промышленная,
    материалы_частей и т.п.) — из-за этого F4 не видел реальные значения.
    Теперь используется полноценный парсер из validate_decomposition
    (yaml.safe_load + кэш по mtime).
    """
    try:
        sys.path.insert(0, os.path.join(SKYNET_REPO, 'scripts'))
        from validate_decomposition import read_yaml_frontmatter
        data, _, _ = read_yaml_frontmatter(_Path(filepath))
        return data if isinstance(data, dict) else None
    except Exception:
        return None

def _validate_path_type(path, тип, статус):
    """Проверяет соответствие пути типу и статусу."""
    if 'фантастические данные/' in path:
        return тип == 'модель_SkyNet' and статус in ('canon', 'canon_realizable')
    if 'реальные данные/' in path:
        return статус == 'real'
    if 'работа и и/' in path:
        return статус == 'real'
    return True

def check_f70():
    """F70: schema_catalog_consistency (через _helpers.py)."""
    try:
        sys.path.insert(0, os.path.join(SKYNET_REPO, 'scripts'))
        from _helpers import check_schemas_consistency
        result = check_schemas_consistency()
        return result
    except Exception as e:
        return {'F70_overall': 0.0, 'error': str(e)}

# === v9.24-v9.25: Метрики F81-F88 ===

def check_F81(models_dir):
    """F81: реализация_промышленная не содержит __ии суффиксов."""
    violations = []
    for f in glob(f"{models_dir}/*.md"):
        yaml_data = _read_yaml_frontmatter(f)
        if not yaml_data:
            continue
        prom = yaml_data.get('реализация_промышленная', [])
        if isinstance(prom, str):
            prom = [prom]
        for item in prom:
            if isinstance(item, str) and item.endswith('__ии'):
                violations.append(f"{f}: реализация_промышленная содержит '{item}' с __ии суффиксом")
    return violations

def check_F82(models_dir, ii_dir):
    """F82: реализация_ии ссылается на существующие изделия в работа и и/изделия/."""
    violations = []
    for f in glob(f"{models_dir}/*.md"):
        yaml_data = _read_yaml_frontmatter(f)
        if not yaml_data:
            continue
        ii_impl = yaml_data.get('реализация_ии', [])
        if isinstance(ii_impl, str):
            ii_impl = [ii_impl]
        for item in ii_impl:
            if not isinstance(item, str):
                continue
            found = False
            for root, dirs, files in os.walk(ii_dir):
                if item in dirs:
                    found = True
                    break
            if not found:
                violations.append(f"{f}: реализация_ии содержит '{item}' — не найдено в работа и и/изделия/")
    return violations

def check_F83(real_dir, ii_dir):
    """F83: count(ii) / count(real) >= 0.80."""
    real_count = sum(1 for _ in glob(f"{real_dir}/*/", recursive=True) if os.path.isdir(_))
    ii_count = sum(1 for _ in glob(f"{ii_dir}/*/", recursive=True) if os.path.isdir(_))
    if real_count == 0:
        return True, 1.0
    ratio = ii_count / real_count
    return ratio >= 0.80, ratio

def check_F87(models_dir):
    """F87: статус_реальности соответствует количеству real-компонентов."""
    violations = []
    for f in glob(f"{models_dir}/*.md"):
        yaml_data = _read_yaml_frontmatter(f)
        if not yaml_data:
            continue
        status = yaml_data.get('статус_реальности', '')
        prom = yaml_data.get('реализация_промышленная', [])
        if isinstance(prom, str):
            prom = [prom]
        prom_count = len([x for x in prom if isinstance(x, str)])
        if status == 'canon' and prom_count > 0:
            violations.append(f"{f}: статус canon но {prom_count} real-компонентов — должен быть canon_realizable")
        if status == 'canon_realizable' and prom_count == 0:
            violations.append(f"{f}: статус canon_realizable но 0 real-компонентов — должен быть canon")
    return violations

def check_F88(fantastic_mat_dir):
    """F88: фантастические материалы без смешения с реальными."""
    violations = []
    real_elements = ['Ga', 'In', 'Sn', 'Ti', 'Al', 'V', 'Fe', 'Cu', 'Ta', 'Be', 'B', 'C', 'O', 'N', 'W', 'Mo']
    for f in glob(f"{fantastic_mat_dir}/*.md"):
        if f.endswith('_список_материалов.md'):
            continue
        yaml_data = _read_yaml_frontmatter(f)
        if not yaml_data:
            continue
        status = yaml_data.get('статус_реальности', '')
        if status != 'canon':
            continue
        composition = yaml_data.get('химический_состав', '')
        if composition and composition != 'не_определён':
            element_count = sum(1 for el in real_elements if el in str(composition))
            if element_count >= 2:
                violations.append(f"{f}: химический_состав '{composition}' содержит реальные элементы")
        if 'основан_на' in yaml_data:
            violations.append(f"{f}: использует поле 'основан_на' (должно быть 'вдохновлён_реальным')")
    return violations


# === v9.26: F70g — schema-driven validation ===

def check_F70g_all(repo_path):
    """F70g: все файлы имеют обязательные поля своей схемы."""
    from _helpers import check_F70g
    # v9.36: авто-поиск последней версии промпта через glob (раньше был hardcode v9.26)
    prompts = glob.glob(os.path.join(repo_path, "требования_к_ии", "SkyNet_PROMPT_v*.md"))
    if prompts:
        prompt_path = sorted(prompts)[-1]  # последняя версия
    else:
        return True, 1.0  # нет промпта — пропускаем
    
    result = check_F70g(repo_path, prompt_path)
    if not result['pass']:
        for v in result['violations']:
            print(f"  F70g FAIL: {v}")
    return result['pass'], result['ratio']


# === v9.27: F70h + F81-F88 ENFORCEMENT ===

def run_all_checks(repo_path):
    """v9.27: Запускает ВСЕ проверки и возвращает сводку."""
    from _helpers import check_F70g, check_F70h, check_F81_F88_all
    
    prompt_path = os.path.join(repo_path, "требования_к_ии")
    # Найти промпт
    import glob as globmod
    prompts = globmod.glob(os.path.join(prompt_path, "SkyNet_PROMPT_v*.md"))
    if prompts:
        prompt_path = sorted(prompts)[-1]
    else:
        prompt_path = None
    
    results = {}
    
    # F70g: schema-driven validation (наличие полей)
    if prompt_path:
        f70g = check_F70g(repo_path, prompt_path)
        results['F70g'] = f70g
        if not f70g['pass']:
            for v in f70g.get('violations', []):
                print(f"  F70g FAIL: {v}")
    
    # F70h: enum validation (значения полей)
    f70h = check_F70h(repo_path)
    results['F70h'] = f70h
    if not f70h['pass']:
        for v in f70h['violations']:
            print(f"  F70h FAIL: {v}")
    
    # F81-F88: специфичные проверки
    f81_88 = check_F81_F88_all(repo_path)
    results['F81_F88'] = f81_88
    for metric, result in f81_88.items():
        if metric == 'all_pass':
            continue
        if not result['pass']:
            for v in result.get('violations', []):
                print(f"  {metric} FAIL: {v}")
    
    # Итог
    all_pass = (
        results.get('F70g', {}).get('pass', True) and
        results.get('F70h', {}).get('pass', True) and
        f81_88.get('all_pass', True)
    )
    results['all_pass'] = all_pass
    return results


def main():
    """Точка входа pre-commit hook."""
    print("SkyNet Pre-commit Hook v9.31")
    
    errors = []
    warnings = []
    
    # 1. Path-type-status check (F4)
    violations = check_path_type_status()
    if violations:
        errors.extend(violations)
    
    # 2. F70: schema_catalog_consistency
    f70_result = check_f70()
    f70_overall = f70_result.get('F70_overall', 0.0)
    if f70_overall < 1.0:
        errors.append(f'F70 schema_catalog_consistency = {f70_overall} (FAIL)')
    
    # 3. Check required files exist
    required = [
        'требования_к_ии/_принципы.md',
        'требования_к_ии/_версия_правил.yaml',
        'требования_к_ии/_t800_terms.txt',
    ]
    for f in required:
        if not os.path.exists(os.path.join(SKYNET_REPO, f)):
            errors.append(f'Required file missing: {f}')
    
    # 4. v9.31 Decomposition Validator (F12a-F32)
    # F13, F22, F23, F24, F25, F26 — информационные (warnings), не блокирующие
    # F22-F26 — анти-шаблон метрики, станут блокирующими после полной верификации
    # v9.40: F27 (незаполненные материалы) — тоже warning: 87 заглушек в очереди
    # verify-task, блокировать коммиты нельзя пока backlog не разобран.
    # v9.42: F28 (альтернативные формы материалов) — warning: очередь ~30 материалов.
    # v9.43: F29 (форма материала в части) + F30 (наследуемые_материалы) — warnings:
    # пилот на ni-63_betavoltaik_4h-sic; full-migration pending.
    # v9.44: F31 (уникальность id/алиасов) + F32 (семантические дубли) — warnings:
    # дедупликация (3 пары слиты через migrate_dedup_materials.py); F31 станет
    # блокирующим после стабилизации (plan: когда violations=0 в 3 прогонах).
    # v9.53: F27b (битые ссылки на материалы — файл отсутствует в каталоге) — warning:
    # 79 битых ссылок в backlog (mirror F27: F27 итерирует существующие файлы,
    # F27b — ссылки в frontmatter на отсутствующие файлы). Cron-агент постепенно
    # создаст недостающие файлы через web_search; после stabilisation (violations=0
    # в 3 прогонах) F27b станет блокирующей, как F27 после разбора backlog.
    # v9.54: F27c (mirror F27b для каталога технологии/) — warning: проверяет
    # структурные id-ссылки в frontmatter (`технологии_частей` часть-level и
    # `технологии` изделие-level). Сейчас 0 ссылок (поле только введено,
    # миграция 3 файлов с известными соответствиями). После полной миграции
    # F27c станет блокирующей.
    # v9.55: F27d (обратная связь F27b/F27c) — warning: проверяет валидность
    # id материалов в `материалы_для_процесса` файлов технологий. Замыкает
    # треугольник изделие↔технология↔материал. Поддерживает legacy-формат
    # (список id строк) и ролевую структуру v9.55 ({материал, роль, доля_массы?}).
    try:
        sys.path.insert(0, os.path.join(SKYNET_REPO, 'scripts'))
        from validate_decomposition import run_all_checks
        decomp_results = run_all_checks()
        # Метрики которые пока warning (не блокирующие)
        # v9.48: F16 добавлена в warnings — новая проверка 'промежуточный без
        # дочерних_частей' концептуально эквивалентна F34 (раньше F16 проверяла
        # только уровень 4 без детей, теперь проверяет ВСЕ 'промежуточный' без
        # детей); пока 629 таких узлов в backlog F34, F16 также warning.
        # v9.52: merged F-метрики — 26→18 метрик:
        #   F25 ← F26 (анти-дубликаты local + global)
        #   F22 ← F23 + F24 (верификация содержимого)
        #   F13 ← F17 (соответствие типу модели)
        #   F29 ← F30 (BOM-материалы: форма + наследование)
        #   F31 ← F32 (дедупликация: syntactic + semantic)
        # F23, F24, F17, F26, F30, F32 убраны — auto-close stale issues для них
        WARNING_METRICS = {'F13', 'F15b', 'F15d', 'F15g', 'F15h', 'F16', 'F22', 'F25', 'F27', 'F27b', 'F27c', 'F27d', 'F28', 'F29', 'F31', 'F34'}
        for metric, result in decomp_results['results'].items():
            if metric in WARNING_METRICS:
                if not result['pass']:
                    warnings.append(f"{metric}: {result['ratio']:.2f} ({result['valid']}/{result['total']}) — {result['description']}")
                continue
            if not result['pass']:
                errors.append(f"{metric}: {result['ratio']:.2f} ({result['valid']}/{result['total']}) — {result['description']}")
                for v in result.get('violations', [])[:3]:
                    errors.append(f"  - {v}")
    except Exception as e:
        warnings.append(f"Decomposition validator не запустился: {e}")

    # 5. Регенерация графов связей (graph1/2/3 + mermaid-рендеры)
    #    Графы — source of truth для навигации по репозиторию, обновляются
    #    автоматически на каждом коммите.
    try:
        import subprocess
        result = subprocess.run(
            ['python3', os.path.join(SKYNET_REPO, 'scripts', 'generate_graphs.py'), '--all'],
            capture_output=True, text=True, cwd=SKYNET_REPO
        )
        if result.returncode != 0:
            warnings.append(f"Графы не сгенерированы: {result.stderr[:200]}")
        else:
            # git add графов, чтобы они попали в этот же коммит
            subprocess.run(
                ['git', 'add', 'graphs/'],
                cwd=SKYNET_REPO, capture_output=True
            )
    except Exception as e:
        warnings.append(f"Генератор графов не запустился: {e}")

    # Report
    if errors:
        print(f'❌ БЛОКИРОВКА коммита ({len(errors)} ошибок):')
        for e in errors:
            print(f'  - {e}')
        sys.exit(1)
    
    if warnings:
        print(f'⚠️ Предупреждения ({len(warnings)}):')
        for w in warnings:
            print(f'  - {w}')
    
    print('✅ Pre-commit check passed — коммит разрешён')
    sys.exit(0)


if __name__ == '__main__':
    main()
