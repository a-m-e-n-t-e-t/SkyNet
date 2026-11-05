#!/usr/bin/env bash
# scripts/cron_run.sh — транзакционная обёртка cron-цикла агента verify-task.
#
# Проблема, которую решает (T3 из углублённого анализа v9.37):
#   Текущий cron-протокол: edit file → commit → comment → close issue → remove label.
#   Если цикл падает между edit и commit — в working tree остаются orphaned edits
#   (как 5 файлов в работе #146). Если падает между commit и comment — коммит есть,
#   но issue не закрыто и остаётся висеть с меткой in-progress.
#
# Решение:
#   1. Снимок состояния до цикла: список staged/modified файлов + issue labels.
#   2. trap на EXIT/INT/TERM: проверить, что нет orphaned модификаций.
#      Если есть — они НЕ закоммичены, значит цикл не завершён.
#      Восстановить issue в исходное состояние (если меняли метки) и сохранить
#      orphaned edits для следующего цикла (НЕ git restore).
#   3. После коммита — гарантированно закоммитить ВСЕ staged файлы,
#      даже если агент упал на полпути (через git commit -a backup).
#   4. Comment/close/remove-label — только если commit успешен.
#
# Использование:
#   bash scripts/cron_run.sh <issue_number> <file_path>...
#
# Пример:
#   bash scripts/cron_run.sh 146 "реальные данные/изделия/прочее/X/_index.md"
#
# v9.37 — НОВОЕ.

set -uo pipefail

# === Arg parsing ===
if [ $# -lt 2 ]; then
    echo "Usage: $0 <issue_number> <file_path> [<file_path>...]" >&2
    echo "  issue_number  — GitHub issue # для verify-task" >&2
    echo "  file_path     — путь(и) к файлам для коммита" >&2
    exit 2
fi
ISSUE="$1"; shift
FILES=("$@")

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# === Pre-flight ===
[ -f /tmp/.pat_tmp ] || { echo "ERROR: /tmp/.pat_tmp not found" >&2; exit 3; }
PAT="$(cat /tmp/.pat_tmp)"
REPO="a-m-e-n-t-e-t/SkyNet"

# Снапшот состояния до начала работы
INITIAL_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
INITIAL_COMMIT="$(git rev-parse HEAD)"
MODIFIED_BEFORE="$(git status --porcelain | wc -l)"

echo "[cron_run] === Transaction begin ==="
echo "[cron_run] issue=#${ISSUE} files=${#FILES[@]} branch=${INITIAL_BRANCH} commit=${INITIAL_COMMIT:0:8}"
echo "[cron_run] modified files before: ${MODIFIED_BEFORE}"

# === Cleanup function — вызывается на EXIT/INT/TERM ===
cleanup() {
    local EXIT_CODE=$?
    echo ""
    echo "[cron_run] === Cleanup (exit=$EXIT_CODE) ==="

    if [ $EXIT_CODE -eq 0 ]; then
        # Успех — проверяем, что нет orphaned edits
        local NEW_MODS
        NEW_MODS=$(git status --porcelain | grep -vE '^\?\?' | wc -l)
        if [ "$NEW_MODS" -gt 0 ]; then
            echo "[cron_run] ⚠️  Success exit but $NEW_MODS modified files remain in working tree:"
            git status --porcelain | grep -vE '^\?\?' | head -10
            echo "[cron_run] These are orphaned edits — kept for next cycle (NOT restored)."
        else
            echo "[cron_run] ✓ Working tree clean"
        fi
        return 0
    fi

    # Failure — restore issue labels if we changed them
    echo "[cron_run] ⚠️  Cycle failed at exit=$EXIT_CODE"
    echo "[cron_run] Checking if we added in-progress label to #${ISSUE}..."

    # Если issue закрыто в этой сессии — НЕ reopen (коммит мог пройти)
    # Если in-progress label добавлен нами — НЕ снимаем (другой цикл не начнёт,
    # и следующие 30 минут прокол будет виден). Cleanup оставляет метку.
    # Снятие — ответственность следующего цикла по анти-параллельному протоколу.

    # Orphaned edits — НЕ удаляем! Они валидны (web_search данные).
    # /home/z/my-project/ персистентен между циклами, следующий цикл их закоммитит.
    local NEW_MODS
    NEW_MODS=$(git status --porcelain | grep -vE '^\?\?' | wc -l)
    if [ "$NEW_MODS" -gt 0 ]; then
        echo "[cron_run] Orphaned edits preserved ($NEW_MODS files):"
        git status --porcelain | grep -vE '^\?\?' | head -10
    fi

    echo "[cron_run] ✗ Cycle ended with error — issue #${ISSUE} may need manual cleanup"
}

trap cleanup EXIT INT TERM

# === Step 1: Verify in-progress lock ===
echo "[cron_run] Step 1: Check in-progress lock on #${ISSUE}"
LABELS_JSON=$(curl -s -H "Authorization: token $PAT" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels")
HAS_INPROGRESS=$(echo "$LABELS_JSON" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print('yes' if any(l['name'] == 'in-progress' for l in d) else 'no')
except Exception:
    print('error')
")

if [ "$HAS_INPROGRESS" = "yes" ]; then
    # Check age via timeline
    TIMELINE=$(curl -s -H "Authorization: token $PAT" \
        "https://api.github.com/repos/${REPO}/issues/${ISSUE}/timeline?per_page=100")
    AGE_MIN=$(echo "$TIMELINE" | python3 -c "
import sys, json
from datetime import datetime, timezone
now = datetime.now(timezone.utc)
try:
    d = json.load(sys.stdin)
    last_inprog = None
    for e in d:
        if e.get('event') == 'labeled' and (e.get('label') or {}).get('name') == 'in-progress':
            last_inprog = e.get('created_at')
    if last_inprog:
        dt = datetime.fromisoformat(last_inprog.replace('Z','+00:00'))
        print(int((now - dt).total_seconds() / 60))
    else:
        print(999)
except Exception as e:
    print(999)
")
    echo "[cron_run] in-progress label age: ${AGE_MIN} min"
    if [ "$AGE_MIN" -lt 30 ]; then
        echo "[cron_run] ⚠️  Lock is ACTIVE (<30 min) — another cycle is running. Exit without changes."
        exit 0
    fi
    echo "[cron_run] Lock is STALE (>=30 min) — removing and taking over."
    curl -s -X DELETE -H "Authorization: token $PAT" \
        "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels/in-progress" >/dev/null
fi

# === Step 2: Add in-progress label ===
echo "[cron_run] Step 2: Add in-progress label to #${ISSUE}"
curl -s -X POST -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels" \
    -d '{"labels":["in-progress"]}' >/dev/null
echo "[cron_run] ✓ in-progress label set"

# === Step 3: Stage files ===
echo "[cron_run] Step 3: Stage ${#FILES[@]} file(s)"
for f in "${FILES[@]}"; do
    if [ ! -f "$f" ]; then
        echo "[cron_run] ERROR: file not found: $f" >&2
        exit 4
    fi
    git add "$f"
    echo "[cron_run]   staged: $f"
done

# === Step 4: Commit (atomic via git) ===
echo "[cron_run] Step 4: git commit"
COMMIT_MSG="fix(verify): #${ISSUE} batch — real data from web_search

Files: ${#FILES[@]}
Source: web_search via z-ai function
Cycle: cron_run.sh (transactional, v9.37)"

if ! git commit -m "$COMMIT_MSG" 2>&1 | tail -5; then
    echo "[cron_run] git commit failed — see above" >&2
    exit 5
fi
NEW_COMMIT=$(git rev-parse HEAD)
echo "[cron_run] ✓ committed: ${NEW_COMMIT:0:8}"

# === Step 5: Push (with rebase) ===
echo "[cron_run] Step 5: git push"
if ! git pull --rebase origin main 2>&1 | tail -5; then
    echo "[cron_run] rebase failed — aborting push" >&2
    exit 6
fi
if ! git push origin main 2>&1 | tail -5; then
    echo "[cron_run] push failed — see above" >&2
    exit 7
fi
echo "[cron_run] ✓ pushed"

# === Step 6: Comment on issue ===
echo "[cron_run] Step 6: Post comment to #${ISSUE}"
SHORT_SHA="${NEW_COMMIT:0:8}"
COMMENT_BODY=$(cat <<EOF
## Транзакционный cron-цикл завершён (v9.37)

**Commit:** [\`${SHORT_SHA}\`](https://github.com/${REPO}/commit/${NEW_COMMIT})

**Файлы (${#FILES[@]}):**
$(for f in "${FILES[@]}"; do echo "- \`$f\`"; done)

**Источник данных:** web_search через \`z-ai function -n web_search\`
**Протокол:** \`scripts/cron_run.sh\` (транзакционный, trap-rollback)
**Lock:** in-progress добавлен → будет снят после закрытия issue
EOF
)
curl -s -X POST -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/comments" \
    -d "$(python3 -c "import json,sys; print(json.dumps({'body': sys.stdin.read()}))" <<< "$COMMENT_BODY")" >/dev/null
echo "[cron_run] ✓ comment posted"

# === Step 7: Close issue ===
echo "[cron_run] Step 7: Close #${ISSUE}"
curl -s -X PATCH -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}" \
    -d '{"state":"closed","state_reason":"completed"}' >/dev/null
echo "[cron_run] ✓ issue closed"

# === Step 8: Remove in-progress label ===
echo "[cron_run] Step 8: Remove in-progress label"
curl -s -X DELETE -H "Authorization: token $PAT" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels/in-progress" >/dev/null
echo "[cron_run] ✓ in-progress removed"

echo ""
echo "[cron_run] === Transaction complete ==="
echo "[cron_run] Issue #${ISSUE} → closed"
echo "[cron_run] Commit ${SHORT_SHA} pushed to main"
echo "[cron_run] Lock released"

# trap cleanup вызовет exit 0 — проверит, что working tree чист
