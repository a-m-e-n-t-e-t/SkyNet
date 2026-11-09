#!/usr/bin/env bash
# scripts/decompose_via_issue.sh v9.60.1
#
# Интеграция recursive_decompose.py с cron-агентом.
# Используется когда F34-issue указывает на сборку, требующую структурной
# декомпозиции (создания sub-parts).
#
# Алгоритм:
#   1. Читает issue body через GitHub API
#   2. Извлекает file_id (часть_X или izdelie_X) из заголовка "[F34] Verify: <id>"
#   3. Запускает recursive_decompose.py --izdelie <id> --issue <N>
#   4. Передаёт paths созданных файлов в cron_run.sh
#
# Использование:
#   bash scripts/decompose_via_issue.sh <issue_number>
#
# Пример:
#   bash scripts/decompose_via_issue.sh 2869

set -uo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <issue_number>" >&2
    exit 2
fi

ISSUE="$1"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

[ -f /tmp/.pat_tmp ] || { echo "ERROR: /tmp/.pat_tmp not found" >&2; exit 3; }
PAT="$(cat /tmp/.pat_tmp)"
REPO="a-m-e-n-t-e-t/SkyNet"

echo "[decompose_via_issue] issue=#${ISSUE}"

# === Шаг 1: Читаем тело issue, ищем file_id ===
ISSUE_DATA=$(curl -s -H "Authorization: token ${PAT}" \
    -H "Accept: application/vnd.github.v3+json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}")

# Извлечь title: "[F34] Verify: <file_id>"
TITLE=$(echo "${ISSUE_DATA}" | python3 -c "
import json, sys, re
data = json.load(sys.stdin)
title = data.get('title', '')
print(title)
")

echo "[decompose_via_issue] title: ${TITLE}"

# Извлечь file_id из title
FILE_ID=$(echo "${TITLE}" | python3 -c "
import re, sys
title = sys.stdin.read().strip()
m = re.match(r'\[F34\]\s*Verify:\s*(\S+)', title)
if m:
    print(m.group(1))
")

if [ -z "${FILE_ID}" ]; then
    echo "ERROR: не удалось извлечь file_id из title: ${TITLE}" >&2
    exit 4
fi

echo "[decompose_via_issue] file_id: ${FILE_ID}"

# === Шаг 2: Найти путь к изделию по file_id ===
# Если file_id начинается с 'izdelie_' — это top-level изделие
# Если 'часть_' — это часть, нужно найти её родителя (top-level izdelie)
IZDELIE_ID="${FILE_ID}"
if [[ "${FILE_ID}" == часть_* ]]; then
    # Найти родителя top-level для этой части
    PARENT=$(grep -rE "^родитель:" "реальные данные/изделия/" --include="_index.md" 2>/dev/null | \
             grep -B1 "${FILE_ID}" | grep "родитель:" | head -1 | awk '{print $2}')
    if [ -z "${PARENT}" ]; then
        # Альтернативный поиск: через find + yaml frontmatter
        for f in $(find "реальные данные/изделия/" -name "_index.md"); do
            ID=$(grep -m1 "^id:" "$f" | awk '{print $2}')
            if [ "${ID}" = "${FILE_ID}" ]; then
                PARENT=$(grep -m1 "^родитель:" "$f" | awk '{print $2}')
                break
            fi
        done
    fi
    if [ -n "${PARENT}" ]; then
        # Подняться до top-level (родитель=null или уровень_номер=1)
        while [ -n "${PARENT}" ] && [ "${PARENT}" != "null" ]; do
            TOP="${PARENT}"
            # Найти файл родителя, проверить его уровень
            PARENT_FILE=$(grep -rl "^id: ${TOP}$" "реальные данные/изделия/" --include="_index.md" 2>/dev/null | head -1)
            if [ -z "${PARENT_FILE}" ]; then break; fi
            LVL=$(grep -m1 "^уровень_номер:" "${PARENT_FILE}" | awk '{print $2}')
            if [ "${LVL}" = "1" ]; then
                IZDELIE_ID="${TOP}"
                break
            fi
            PARENT=$(grep -m1 "^родитель:" "${PARENT_FILE}" | awk '{print $2}')
        done
    fi
fi

echo "[decompose_via_issue] izdelie_id (top-level): ${IZDELIE_ID}"

# === Шаг 3: Запустить recursive_decompose.py (сухой прогон для получения списка файлов) ===
DRY_RUN_OUTPUT=$(python3 scripts/recursive_decompose.py --dry-run --izdelie "${IZDELIE_ID}" --issue "${ISSUE}" 2>&1)

echo "[decompose_via_issue] dry-run output:"
echo "${DRY_RUN_OUTPUT}"
echo ""

# Проверить action
ACTION=$(echo "${DRY_RUN_OUTPUT}" | grep "action:" | head -1 | awk '{print $2}')
if [ "${ACTION}" = "STOP_UNKNOWN" ]; then
    echo "[decompose_via_issue] STOP_UNKNOWN — подтип не в реестре."
    echo "  Cron-агент должен вручную: пометить 'неделимый' или добавить подтип в реестр."
    exit 5
fi

if [ "${ACTION}" != "RECURSE" ]; then
    echo "[decompose_via_issue] action=${ACTION} — декомпозиция не нужна/невозможна."
    exit 6
fi

# === Шаг 4: Применить декомпозицию ===
echo "[decompose_via_issue] Применяю декомпозицию..."
python3 scripts/recursive_decompose.py --izdelie "${IZDELIE_ID}" --issue "${ISSUE}" 2>&1

# === Шаг 5: Найти изменённые/созданные файлы ===
CHANGED_FILES=$(git status --short "реальные данные/изделия/" "работа и и/изделия/" 2>&1 | awk '{print $2}')

if [ -z "${CHANGED_FILES}" ]; then
    echo "[decompose_via_issue] Нет изменений — файлы уже корректны."
    exit 0
fi

echo "[decompose_via_issue] Изменённые файлы:"
echo "${CHANGED_FILES}"
echo ""

# === Шаг 6: Передать в cron_run.sh ===
echo "[decompose_via_issue] Запуск cron_run.sh для коммита..."
# shellcheck disable=SC2086
bash scripts/cron_run.sh "${ISSUE}" ${CHANGED_FILES}
