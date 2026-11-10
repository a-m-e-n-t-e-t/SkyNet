#!/usr/bin/env bash
# scripts/cron_pick.sh v9.59
#
# Wrapper для cron-агента: поднимает PAT (5 уровней recovery) и выводит
# список открытых verify-task issues для PICK'а.
#
# Использование:
#   bash scripts/cron_pick.sh
#
# Вывод:
#   Line 1: PICK_ISSUE=<issue_number>
#   Line 2: PICK_TITLE=<title>
#   Line 3: PICK_LABELS=<comma-separated labels>
#   ...
#   Или: PICK_NONE=all_issues_in_progress_or_no_open
#
# Exit codes:
#   0 — PAT готов, найден кандидат для PICK
#   1 — PAT готов, но нет открытых issue (всё in-progress или очередь пуста)
#   3 — PAT recovery провален

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "[cron_pick v9.59] === Step 1: PAT recovery ==="
# shellcheck disable=SC1091
if ! source "${REPO_ROOT}/scripts/pat_recovery.sh"; then
    echo "[cron_pick v9.59] ✗ pat_recovery.sh not found — exit" >&2
    exit 3
fi
if ! pat_recover; then
    echo "[cron_pick v9.59] ✗ PAT recovery failed — exit" >&2
    exit 3
fi
echo "[cron_pick v9.59] ✓ PAT ready"

# Шаг 0: Sweep dead in-progress на closed issues (cleanup)
echo "[cron_pick v9.59] === Step 0: Sweep dead in-progress on closed issues ==="
if [ -x "${REPO_ROOT}/scripts/sweep_closed_inprogress.sh" ]; then
    bash "${REPO_ROOT}/scripts/sweep_closed_inprogress.sh" 2>&1 | sed 's/^/[cron_pick v9.59]   /' || true
fi

REPO="a-m-e-n-t-e-t/SkyNet"

echo "[cron_pick v9.59] === Step 2: Find oldest open verify-task issue ==="

# Анти-параллель: проверить, есть ли сейчас активные in-progress на ОТКРЫТЫХ issues
# (если есть свежие <30/45/60 мин — выходим, другая сессия работает)
OPEN_INPROGRESS_JSON=$(curl -sSL -H "Authorization: token $PAT" \
    "https://api.github.com/repos/${REPO}/issues?state=open&labels=in-progress&per_page=50")
ACTIVE_COUNT=$(echo "$OPEN_INPROGRESS_JSON" | python3 -c "
import sys, json
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
d = json.load(sys.stdin)
if not isinstance(d, list):
    print(0)
    sys.exit(0)
active = 0
for it in d:
    # Если обновлялось <30 мин назад — другая сессия активно работает
    upd = datetime.fromisoformat(it['updated_at'].replace('Z','+00:00'))
    age_min = (now - upd).total_seconds() / 60
    if age_min < 30:
        active += 1
print(active)
")
if [ "${ACTIVE_COUNT:-0}" -gt 0 ]; then
    echo "[cron_pick v9.59] ⚠️  $ACTIVE_COUNT active in-progress issues (<30 min) — exit (parallel session running)"
    echo "PICK_NONE=parallel_session_active"
    exit 1
fi

# Загрузить все открытые verify-task issues (paginated)
ALL_ISSUES_JSON=$(python3 -c "
import json, urllib.request, sys
PAT = open('/tmp/.pat_tmp').read().strip()
REPO = 'a-m-e-n-t-e-t/SkyNet'
all_issues = []
page = 1
while page <= 10:  # не более 1000 issues
    url = f'https://api.github.com/repos/{REPO}/issues?state=open&labels=verify-task&per_page=100&page={page}'
    req = urllib.request.Request(url, headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github+json'})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.loads(r.read().decode('utf-8'))
            if not isinstance(data, list) or not data:
                break
            all_issues.extend(data)
            if len(data) < 100:
                break
    except Exception as e:
        print(f'API error: {e}', file=sys.stderr)
        break
    page += 1
print(json.dumps(all_issues))
")

# Найти кандидата: исключить in-progress, parent issues, выбрать самый старый
PICK_LINE=$(echo "$ALL_ISSUES_JSON" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if not isinstance(data, list) or not data:
    print('PICK_NONE=no_open_issues')
    sys.exit(0)

# Отфильтровать
candidates = []
for it in data:
    labels = [l['name'] for l in it.get('labels',[])]
    if 'in-progress' in labels:
        continue
    if 'parent' in labels:
        continue  # parent issues не берём напрямую
    candidates.append(it)

if not candidates:
    print('PICK_NONE=all_open_are_in_progress')
    sys.exit(0)

# Приоритет: sub-issue → quick → medium → complex → без метки
# Внутри каждой группы — самый старый по created_at
def priority_key(it):
    labels = [l['name'] for l in it.get('labels',[])]
    if 'sub-issue' in labels: prio = 0
    elif 'complexity:quick' in labels: prio = 1
    elif 'complexity:medium' in labels: prio = 2
    elif 'complexity:complex' in labels: prio = 3
    else: prio = 4
    return (prio, it.get('created_at', '9999'))

candidates.sort(key=priority_key)
oldest = candidates[0]
labels = [l['name'] for l in oldest.get('labels',[])]
print(f'PICK_ISSUE={oldest[\"number\"]}')
print(f'PICK_TITLE={(oldest.get(\"title\") or \"\")[:120]}')
print(f'PICK_LABELS={\",\".join(labels)}')
print(f'PICK_CREATED={oldest.get(\"created_at\")}')
print(f'PICK_URL={oldest.get(\"html_url\")}')
")

echo "[cron_pick v9.59] === Result ==="
echo "$PICK_LINE"

# Извлечь номер для exit code
case "$PICK_LINE" in
    PICK_ISSUE=*)
        exit 0
        ;;
    PICK_NONE=*)
        exit 1
        ;;
    *)
        echo "[cron_pick v9.59] ⚠️  unexpected output" >&2
        exit 1
        ;;
esac
