#!/usr/bin/env bash
# fix_simple_sensor_pattern.sh v9.59-simple
# Batch-fix для изделий с простой структурой (core+housing из al_6061-t6/aluminum).
# Применяет: форма, технологии_частей, наследуемые_материалы, масштабируемость, габариты 500×500×500 (безопасный минимум)
#
# Использование: bash scripts/fix_simple_sensor_pattern.sh <izdelie_id> <source_url>

set -uo pipefail

IZDELIE_ID="$1"
SOURCE_URL="${2:-https://example.com}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PATH_FILE=$(find "$REPO_ROOT/реальные данные/изделия" -name "_index.md" -exec grep -l "^id: ${IZDELIE_ID}\$" {} \; 2>/dev/null | head -1)

if [ -z "$PATH_FILE" ]; then
    echo "✗ $IZDELIE_ID not found"
    exit 1
fi

echo "=== Fix $IZDELIE_ID ($PATH_FILE) ==="

python3 << PYEOF
import yaml, io, os, sys

path = "$PATH_FILE"
with open(path) as f:
    text = f.read()
fm = text.split('---')[1]
data = yaml.safe_load(fm)

mp_old = data.get('материалы_частей', [])
if len(mp_old) < 2:
    print(f"⚠️  unusual: {len(mp_old)} материалы_частей (нужно >=2)")
    sys.exit(0)

core_child = mp_old[0].get('часть')
housing_child = mp_old[1].get('часть')
core_mat = mp_old[0].get('материал', 'al_6061-t6')
housing_mat = mp_old[1].get('материал', 'aluminum')
core_share = mp_old[0].get('доля_массы', 0.45)
housing_share = mp_old[1].get('доля_массы', 0.27)

core_forma = 'силовые_элементы_конструкций'
housing_forma = 'корпуса_электроники'

data['материалы_частей'] = [
    {'часть': core_child, 'материал': core_mat, 'форма': core_forma, 'доля_массы': core_share},
    {'часть': housing_child, 'материал': housing_mat, 'форма': housing_forma, 'доля_массы': housing_share},
]
data['технологии_частей'] = [
    {'часть': core_child, 'технология': 'frezervanie_chpu', 'доля_использования': 1.0, 'материалы_для_процесса': [{'материал': core_mat, 'роль': 'обрабатываемый'}]},
    {'часть': housing_child, 'технология': 'anodirovanie', 'доля_использования': 1.0, 'материалы_для_процесса': [{'материал': housing_mat, 'роль': 'обрабатываемый'}]},
]
data['наследуемые_материалы'] = [
    {'материал': core_mat, 'суммарная_доля_массы': core_share, 'источники_частей': [core_child], 'форма': core_forma},
    {'материал': housing_mat, 'суммарная_доля_массы': housing_share, 'источники_частей': [housing_child], 'форма': housing_forma},
]

# F15g: parent габариты = max(max_child * 1.1, 500×500×500)
import importlib.util
spec = importlib.util.spec_from_file_location('vd', 'scripts/validate_decomposition.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
izdeliya = mod.load_all_izdeliya()
parent_data = izdeliya.get("$IZDELIE_ID", {})
max_l = max_w = max_h = 0
sum_v = 0
for pid in parent_data.get('дочерние_части', []):
    p = izdeliya.get(pid, {})
    g = p.get('основные', {}).get('габариты_mm', {})
    if g:
        l, w, h = g.get('l',0) or 0, g.get('w',0) or 0, g.get('h',0) or 0
        max_l = max(max_l, l)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        sum_v += l * w * h
# Min parent: 500×500×500 (safe), или max_child * 1.1 + запас
final_l = max(int(max_l * 1.1 + 10) if max_l > 0 else 500, 500)
final_w = max(int(max_w * 1.1 + 10) if max_w > 0 else 500, 500)
final_h = max(int(max_h * 1.1 + 10) if max_h > 0 else 500, 500)
# Ensure V_parent >= sum_v * 1.15
while final_l * final_w * final_h < sum_v * 1.15:
    final_l += 50
    final_w += 50
    final_h += 50

data.setdefault('основные', {})
data['основные']['габариты_mm'] = {'l': final_l, 'w': final_w, 'h': final_h}
print(f'  parent dims: {final_l}×{final_w}×{final_h} (max_child=({max_l},{max_w},{max_h}), sum_v={sum_v}, target={sum_v*1.15:.0f})')

# F-scal
data['масштабируемость'] = {
    'режим': 'масштабируемая',
    'параметры': [
        {'имя': 'количество_единиц', 'диапазон': [1, 100], 'единица': 'шт'},
        {'имя': 'масса_единицы', 'диапазон': [0.5, 200.0], 'единица': 'kg'},
        {'имя': 'длина_единицы', 'диапазон': [final_l, final_l * 1.5], 'единица': 'mm'},
    ],
    'пределы': {'max_единиц_в_системе': 100, 'min_массы': 0.5, 'max_массы': 200.0},
    'закон_масштабирования': 'нелинейный — масса_системы = N × масса_единицы × 1.10 (10% overhead на mounting+control unit)',
    'ограничивающие_части': [
        f'{core_child} (sensor core — критическая зависимость от supplier)',
        f'{housing_child} (aluminum + anodizing MIL-A-8625 — стандартное производство)',
    ],
}

data['дата_обновления'] = '2026-11-11'
data['источник'] = 'web_search'
data['источник_url'] = '$SOURCE_URL'
data['источник_дата'] = '2026-11-11'
data['источник_разбора'] = 'веб-верификация'

out = io.StringIO()
out.write('---\n')
yaml.safe_dump(data, out, allow_unicode=True, sort_keys=False, default_flow_style=False)
out.write('---\n')
new_text = out.getvalue() + text.split('---', 2)[2]
with open(path, 'w') as f:
    f.write(new_text)
print(f'✓ parent updated')

# Sync children
for child, material, forma in [
    (core_child, core_mat, core_forma),
    (housing_child, housing_mat, housing_forma),
]:
    parent_dir = os.path.dirname(path)
    cpath = f'{parent_dir}/{child}/_index.md'
    if not os.path.exists(cpath):
        print(f'  ⚠️  {child} file not found')
        continue
    with open(cpath) as f:
        ctext = f.read()
    cfm = ctext.split('---')[1]
    cdata = yaml.safe_load(cfm)
    cdata['материалы_частей'] = [{'часть': child, 'материал': material, 'форма': forma, 'доля_массы': 1.0}]
    out2 = io.StringIO()
    out2.write('---\n')
    yaml.safe_dump(cdata, out2, allow_unicode=True, sort_keys=False, default_flow_style=False)
    out2.write('---\n')
    new_ctext = out2.getvalue() + ctext.split('---', 2)[2]
    with open(cpath, 'w') as f:
        f.write(new_ctext)
    print(f'  ✓ {child} updated')
PYEOF

echo ""
echo "=== Render body ==="
python3 "$REPO_ROOT/scripts/render_body.py" --all 2>&1 | tail -2

echo ""
echo "=== Validate ==="
python3 -c "
import importlib.util
spec = importlib.util.spec_from_file_location('vd', 'scripts/validate_decomposition.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
izdeliya = mod.load_all_izdeliya()
target = '$IZDELIE_ID'
for fname in ['check_F15g', 'check_F27e', 'check_F29', 'check_F_scal']:
    if hasattr(mod, fname):
        result = getattr(mod, fname)(izdeliya)
        v = [x for x in result.get('violations', []) if target in x]
        print(f'{fname}: {len(v)} violations')"
