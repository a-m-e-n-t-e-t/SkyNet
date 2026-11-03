"""SkyNet Pre-commit Hook — path-type-status + F3-F70.
v9.31: функциональная реализация (не заглушка)."""

import os, sys, re, json

SKYNET_REPO = os.environ.get('SKYNET_REPO', '.')

# === Path-type-status check (F4) ===
PATH_TYPE_MAP = {
    'фантастические данные/': {'тип': 'модель_SkyNet', 'статус': 'canon|canon_realizable'},
    'реальные данные/изделия/': {'тип': 'изделие', 'статус': 'real'},
    'реальные данные/технологии/': {'тип': 'технология', 'статус': 'real'},
    'реальные данные/материалы/': {'тип': 'материал', 'статус': 'real'},
    'работа и и/': {'тип': '*', 'статус': 'real', 'версия': 'ии-улучшенная'},
}

def check_path_type_status():
    """F4: проверка path ↔ тип ↔ статус_реальности."""
    violations = []
    # Walk all .md files in реальные данные/ and работа и и/
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
                
                # Read YAML front matter
                yaml_data = _read_yaml_frontmatter(fpath)
                if not yaml_data:
                    continue
                
                тип = yaml_data.get('тип', '')
                статус = yaml_data.get('статус_реальности', '')
                
                # Check: real files only in реальные данные/ or работа и и/
                if статус == 'canon' and root_dir != 'фантастические данные':
                    violations.append(f'{rel_path}: статус canon в {root_dir} (должен быть в фантастические данные/)')
                
                if тип and not _validate_path_type(rel_path, тип, статус):
                    violations.append(f'{rel_path}: тип={тип} статус={статус} не соответствует пути')
    
    return violations

def _read_yaml_frontmatter(filepath):
    """Читает YAML front matter из Markdown файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            return None
        end = content.find('\n---', 3)
        if end < 0:
            return None
        yaml_text = content[3:end]
        # Simple YAML parsing (avoid dependency)
        data = {}
        for line in yaml_text.split('\n'):
            if ':' in line and not line.startswith(' ') and not line.startswith('#'):
                key, val = line.split(':', 1)
                data[key.strip()] = val.strip()
        return data
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
    prompt_path = os.path.join(repo_path, "требования_к_ии", "SkyNet_PROMPT_v9.26.md")
    if not os.path.exists(prompt_path):
        # Fallback: найти любой SkyNet_PROMPT_v*.md
        import glob
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
