#!/usr/bin/env python3
"""
SkyNet Model Completeness Checker — v9.24 (v9.31.1: актуализировано)
Self-аудит полноты подсистем для каждой модели (F86).

Урок из v9.17: AI не делал эту проверку сам — пользователь должен был попросить
«проверь содержат ли подсистемы каждой модели все необходимые изделия».
После этого нашлось 3 пробела: маскировка, навигация, система_связи.

Этот скрипт запускается ПОСЛЕ каждого batch автоматически (§9.5 авто-отчёт).
Не требует пользовательской команды.

Метрика: F86 — доля_моделей_с_100%_покрытием_подсистем = 1.0 БЛОКИРОВКА
"""

import os
import sys
import re
import json
from pathlib import Path

SKYNET_REPO = os.environ.get('SKYNET_REPO', '.')


def parse_yaml_frontmatter(filepath):
    """Читает YAML front matter из Markdown файла. Возвращает dict."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            return {}
        end = content.find('\n---', 3)
        if end < 0:
            return {}
        yaml_text = content[3:end]
        # Simple YAML parsing
        data = {}
        current_key = None
        current_list = None
        for line in yaml_text.split('\n'):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            # Inline list: key: ['a', 'b', 'c']
            if ':' in line and not line.startswith(' '):
                if current_list is not None:
                    current_list = None
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                if val.startswith('[') and val.endswith(']'):
                    # Inline list
                    items = re.findall(r"'([^']+)'|\"([^\"]+)\"|(\w+)", val[1:-1])
                    items = [a or b or c for a, b, c in items if (a or b or c)]
                    data[key] = items
                elif val:
                    data[key] = val
                else:
                    current_key = key
                    current_list = []
                    data[key] = current_list
            elif line.startswith('  - ') and current_list is not None:
                item = line.strip()[2:].strip()
                # Remove comments
                if '#' in item:
                    item = item[:item.index('#')].strip()
                if item:
                    current_list.append(item)
        return data
    except Exception as e:
        print(f"  ⚠️ Cannot parse {filepath}: {e}", file=sys.stderr)
        return {}


def get_all_models():
    """Возвращает список всех моделей из фантастические данные/."""
    models_dir = os.path.join(SKYNET_REPO, 'фантастические данные')
    if not os.path.exists(models_dir):
        return []
    models = []
    for f in sorted(os.listdir(models_dir)):
        if f.endswith('.md') and not f.startswith('_'):
            models.append(os.path.join(models_dir, f))
    return models


def extract_subsystems_from_implementation(impl_list):
    """Извлекает подсистемы из списка изделий (по пути или имени)."""
    subsystems = set()
    for item in impl_list:
        if not isinstance(item, str):
            continue
        # Remove __ии suffix
        clean = item.replace('__ии', '').replace('__пром', '')
        # Try to find in реальные данные/изделия/<подсистема>/<item>/
        for sub in ['каркас', 'энергетическая', 'броня', 'вычислительная', 'сенсоры',
                     'встроенное_оружие', 'приводная_система', 'система_охлаждения',
                     'система_питания', 'система_передвижения', 'система_связи',
                     'навигация', 'маскировка', 'прочее']:
            item_path = os.path.join(SKYNET_REPO, 'реальные данные', 'изделия', sub, clean)
            if os.path.exists(item_path):
                subsystems.add(sub)
                break
            # Also check работа и и/
            item_path_ii = os.path.join(SKYNET_REPO, 'работа и и', 'изделия', sub, item)
            if os.path.exists(item_path_ii):
                subsystems.add(sub)
                break
    return subsystems


def check_model_completeness(model_path):
    """Проверяет полноту подсистем для одной модели. Возвращает dict с результатами."""
    yaml_data = parse_yaml_frontmatter(model_path)
    model_name = yaml_data.get('id', os.path.basename(model_path).replace('.md', ''))
    
    expected = yaml_data.get('expected_subsystems', [])
    if isinstance(expected, str):
        expected = [expected]
    
    prom_impl = yaml_data.get('реализация_промышленная', [])
    if isinstance(prom_impl, str):
        prom_impl = [prom_impl]
    
    ii_impl = yaml_data.get('реализация_ии', [])
    if isinstance(ii_impl, str):
        ii_impl = [ii_impl]
    
    # Extract subsystems from implementations
    prom_subs = extract_subsystems_from_implementation(prom_impl)
    ii_subs = extract_subsystems_from_implementation(ii_impl)
    covered = prom_subs | ii_subs
    
    # Find missing
    missing_prom = set(expected) - prom_subs
    missing_ii = set(expected) - ii_subs
    missing_both = set(expected) - covered
    
    # Check подтип_модели for exemptions (v9.24)
    podtip = yaml_data.get('подтип_модели', 'стандартный')
    exempt = set()
    if podtip == 'жидкий_металл':
        # T-1000, T-X — exempt from каркас, броня, приводная_система, система_передвижения
        exempt = {'каркас', 'броня', 'приводная_система', 'система_передвижения'}
    
    missing_both -= exempt
    
    is_complete = len(missing_both) == 0
    
    return {
        'model': model_name,
        'expected_count': len(expected),
        'covered_count': len(covered & set(expected)),
        'missing_prom': sorted(missing_prom - exempt),
        'missing_ii': sorted(missing_ii - exempt),
        'missing_both': sorted(missing_both),
        'exempt': sorted(exempt),
        'подтип_модели': podtip,
        'is_complete': is_complete,
        'F86_pass': is_complete,
    }


def check_all_models():
    """Проверяет все модели. Возвращает сводку + метрику F86."""
    models = get_all_models()
    if not models:
        return {
            'total_models': 0,
            'complete_models': 0,
            'F86': 1.0,  # vacuously true
            'details': [],
        }
    
    details = []
    complete = 0
    for model_path in models:
        result = check_model_completeness(model_path)
        details.append(result)
        if result['is_complete']:
            complete += 1
    
    f86 = complete / len(models) if models else 1.0
    
    return {
        'total_models': len(models),
        'complete_models': complete,
        'F86': round(f86, 4),
        'F86_threshold': 1.0,
        'F86_pass': f86 >= 1.0,
        'details': details,
    }


def main():
    """Главная функция — проверяет все модели и выводит отчёт."""
    print("=" * 70)
    print("SkyNet Model Completeness Checker v9.24 (F86)")
    print("=" * 70)
    
    result = check_all_models()
    
    print(f"\nМоделей проверено: {result['total_models']}")
    print(f"Полных (100% покрытие): {result['complete_models']}")
    print(f"F86 = {result['F86']} (порог: {result['F86_threshold']})")
    print(f"Статус: {'✅ PASS' if result['F86_pass'] else '❌ FAIL (БЛОКИРОВКА)'}")
    
    if not result['F86_pass']:
        print("\n=== НЕПОЛНЫЕ МОДЕЛИ ===")
        for d in result['details']:
            if not d['is_complete']:
                print(f"\n  ❌ {d['model']}:")
                print(f"     Ожидалось: {d['expected_count']} подсистем")
                print(f"     Покрыто: {d['covered_count']}")
                if d['missing_both']:
                    print(f"     Отсутствует (пром+ии): {', '.join(d['missing_both'])}")
                if d['missing_prom']:
                    print(f"     Отсутствует (только пром): {', '.join(d['missing_prom'])}")
                if d['missing_ii']:
                    print(f"     Отсутствует (только ии): {', '.join(d['missing_ii'])}")
                if d['exempt']:
                    print(f"     Exempt (подтип={d['подтип_модели']}): {', '.join(d['exempt'])}")
    
    # Save JSON
    output_path = os.path.join(SKYNET_REPO, 'результаты', '_model_completeness.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nРезультат сохранён: {output_path}")
    
    # Exit code
    sys.exit(0 if result['F86_pass'] else 1)


if __name__ == '__main__':
    main()
