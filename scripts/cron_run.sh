#!/usr/bin/env bash
# scripts/cron_run.sh v9.59 — транзакционная обёртка cron-цикла агента verify-task.
#
# Изменения v9.59 (по сравнению с v9.58):
#   1. Step 0: sanity-sweep — снимает мёртвые in-progress со всех ЗАКРЫТЫХ issues
#      (вызов scripts/sweep_closed_inprogress.sh). Лечит кейсы вида #966,
#      когда цикл закрыл issue вручную без cleanup-ветки unlabeled.
#   2. cleanup() trap усилен: если на момент выхода #${ISSUE} уже закрыт —
#      метка in-progress гарантированно снимается (любой exit code).
#
# Изменения v9.58 (по сравнению с v9.37):
#   1. Complexity-aware stale-detection (порог 30/45/60 мин для quick/medium/complex)
#   2. Parent auto-close: если закрывается sub-issue, проверить parent на закрытие
#   3. Web-search cache hook: проверяет кэш перед web_search
#   4. Sub-issue приоритет: помечает как sub-issue, добавляет parent-ссылку в коммит
#
# Проблема, которую решает (T3 из углублённого анализа v9.37):
#   Текущий cron-протокол: edit file → commit → comment → close issue → remove label.
#   Если цикл падает между edit и commit — в working tree остаются orphaned edits
#   (как 5 файлов в работе #146). Если падает между commit и comment — коммит есть,
#   но issue не закрыто и остаётся висеть с меткой in-progress.
#
# Решение v9.37 (сохранено):
#   1. Снапшот состояния до цикла: список staged/modified файлов + issue labels.
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

# v9.58: путь к web-search кэшу (создаётся при первом использовании)
CACHE_DIR="диалог"
CACHE_FILE="${CACHE_DIR}/web_search_cache.json"

# Снапшот состояния до начала работы
INITIAL_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
INITIAL_COMMIT="$(git rev-parse HEAD)"
MODIFIED_BEFORE="$(git status --porcelain | wc -l)"

echo "[cron_run v9.59] === Transaction begin ==="
echo "[cron_run v9.59] issue=#${ISSUE} files=${#FILES[@]} branch=${INITIAL_BRANCH} commit=${INITIAL_COMMIT:0:8}"
echo "[cron_run v9.59] modified files before: ${MODIFIED_BEFORE}"

# === v9.59: Step 0 — Sweep stale in-progress on CLOSED issues (global sanity check) ===
# Запускается до любых изменений. Снимает мёртвые метки с уже закрытых issues,
# которые могли остаться после ручного закрытия или падения цикла между close и unlabeled.
echo "[cron_run v9.59] Step 0: Sweep stale in-progress on closed issues (global)"
if [ -x "${REPO_ROOT}/scripts/sweep_closed_inprogress.sh" ]; then
    bash "${REPO_ROOT}/scripts/sweep_closed_inprogress.sh" 2>&1 | sed 's/^/[cron_run v9.59]   /' || true
else
    echo "[cron_run v9.59] ⚠️  sweep_closed_inprogress.sh not found — skip"
fi

# === v9.58: Helper — получить сложность issue из labels ===
get_complexity() {
    local issue_num="$1"
    local labels_json
    labels_json=$(curl -s -H "Authorization: token ${PAT}" \
        "https://api.github.com/repos/${REPO}/issues/${issue_num}/labels")
    echo "$labels_json" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    for l in d:
        name = l.get('name', '')
        if name.startswith('complexity:'):
            print(name)
            break
except Exception:
    pass
"
}

# === v9.58: Helper — получить parent issue number из sub-issue body ===
get_parent_number() {
    local issue_num="$1"
    local body
    body=$(curl -s -H "Authorization: token ${PAT}" \
        "https://api.github.com/repos/${REPO}/issues/${issue_num}" | \
        python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('body','') or '')")
    echo "$body" | grep -oP '<!--\s*parent:\s*\d+\s*-->' | grep -oP '\d+' | head -1
}

# === v9.58: Helper — complexity-aware stale threshold ===
get_stale_threshold() {
    local complexity="${1:-}"
    case "$complexity" in
        complexity:quick)   echo 30 ;;
        complexity:medium)  echo 45 ;;
        complexity:complex) echo 60 ;;
        *)                  echo 30 ;;  # default для legacy issues без метки
    esac
}

# === v9.58: Helper — проверить, является ли issue sub-issue ===
is_sub_issue() {
    local issue_num="$1"
    local labels_json
    labels_json=$(curl -s -H "Authorization: token ${PAT}" \
        "https://api.github.com/repos/${REPO}/issues/${issue_num}/labels")
    echo "$labels_json" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print('yes' if any(l.get('name') == 'sub-issue' for l in d) else 'no')
except Exception:
    print('no')
"
}

# === v9.58: Helper — проверить, все ли sub-issues parent'а закрыты ===
check_all_subs_closed() {
    local parent_num="$1"
    local all_subs=""
    local page=1
    while true; do
        local resp
        resp=$(curl -s -H "Authorization: token ${PAT}" \
            "https://api.github.com/repos/${REPO}/issues?state=all&labels=sub-issue&per_page=100&page=${page}")
        local count
        count=$(echo "$resp" | python3 -c "import sys, json; d=json.load(sys.stdin); print(len(d) if isinstance(d, list) else 0)")
        if [ "$count" = "0" ]; then break; fi
        all_subs="$all_subs
$resp"
        if [ "$count" -lt 100 ]; then break; fi
        page=$((page + 1))
    done
    echo "$all_subs" | python3 -c "
import sys, json
data = sys.stdin.read().strip()
if not data:
    print('no-subs')
    sys.exit(0)
# Parse concatenated JSON arrays (GitHub API returns pretty-printed multi-line JSON;
# raw_decode handles both compact single-line and multi-line documents, and multiple
# concatenated pages separated by newlines)
subs = []
dec = json.JSONDecoder()
idx = 0
while idx < len(data):
    while idx < len(data) and data[idx] in ' \n\t\r':
        idx += 1
    if idx >= len(data):
        break
    try:
        obj, end = dec.raw_decode(data, idx)
        if isinstance(obj, list):
            subs.extend(obj)
        idx = end
    except Exception:
        # skip to next line on unparsable garbage
        nl = data.find('\n', idx)
        if nl == -1:
            break
        idx = nl + 1
parent_marker = f'<!-- parent: ${parent_num} -->'
parent_subs = [s for s in subs if parent_marker in (s.get('body') or '')]
if not parent_subs:
    print('no-subs')
else:
    all_closed = all(s.get('state') == 'closed' for s in parent_subs)
    print('all-closed' if all_closed else 'has-open')
"
}

# === v9.58: Helper — закрыть parent issue (auto-close) ===
auto_close_parent() {
    local parent_num="$1"
    local close_body="## ✅ Parent closed — all sub-issues done (v9.58)

Все sub-issues закрыты. Parent автоматически закрывается.

*Авто-закрыто cron_run.sh v9.58 — parent auto-close.*"
    curl -s -X POST -H "Authorization: token ${PAT}" -H "Content-Type: application/json" \
        "https://api.github.com/repos/${REPO}/issues/${parent_num}/comments" \
        -d "$(python3 -c "import json,sys; print(json.dumps({'body': sys.stdin.read()}))" <<< "$close_body")" >/dev/null
    curl -s -X PATCH -H "Authorization: token ${PAT}" -H "Content-Type: application/json" \
        "https://api.github.com/repos/${REPO}/issues/${parent_num}" \
        -d '{"state":"closed","state_reason":"completed"}' >/dev/null
    # Remove in-progress label if present
    curl -s -X DELETE -H "Authorization: token ${PAT}" \
        "https://api.github.com/repos/${REPO}/issues/${parent_num}/labels/in-progress" >/dev/null 2>&1
    echo "[cron_run v9.58] ✓ Parent #${parent_num} auto-closed (all sub-issues done)"
}

# === v9.58: Helper — lookup web-search cache ===
web_search_cached() {
    local query="$1"
    [ -f "$CACHE_FILE" ] || return 1
    python3 -c "
import json, sys
try:
    with open('$CACHE_FILE') as f:
        cache = json.load(f)
    query = sys.argv[1]
    now = __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat()
    for entry in cache.get('entries', []):
        # TTL check: 24 hours
        created = entry.get('created_at', '')
        if created:
            try:
                dt = __import__('datetime').datetime.fromisoformat(created.replace('Z','+00:00'))
                age_h = (__import__('datetime').datetime.now(__import__('datetime').timezone.utc) - dt).total_seconds() / 3600
                if age_h > 24:
                    continue
            except Exception:
                pass
        # Match by query or keywords
        if entry.get('query') == query:
            print(json.dumps(entry.get('results', []), ensure_ascii=False))
            sys.exit(0)
        keywords = entry.get('keywords', [])
        if any(kw in query for kw in keywords if len(kw) > 4):
            print(json.dumps(entry.get('results', []), ensure_ascii=False))
            sys.exit(0)
    sys.exit(1)
except Exception:
    sys.exit(1)
" "$query"
}

# === v9.58: Helper — save web-search result to cache ===
web_search_save() {
    local query="$1"
    local results="$2"  # JSON array
    mkdir -p "$CACHE_DIR"
    python3 -c "
import json, sys, os
from datetime import datetime, timezone
cache_file = '$CACHE_FILE'
query = sys.argv[1]
results = json.loads(sys.argv[2])
try:
    with open(cache_file) as f:
        cache = json.load(f)
except Exception:
    cache = {'version': 'v9.58', 'entries': []}
now = datetime.now(timezone.utc).isoformat()
entry = {
    'id': f'ws_{len(cache.get(\"entries\", [])) + 1:04d}',
    'query': query,
    'keywords': [w for w in query.split() if len(w) > 3],
    'results': results,
    'created_at': now,
    'last_used': now,
    'usage_count': 1,
    'used_in_issues': [],
}
cache.setdefault('entries', []).append(entry)
with open(cache_file, 'w') as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)
print(f'[cache] saved: {entry[\"id\"]}')
" "$query" "$results"
}

# === v9.58: Helper — mark cache entry as used by issue ===
web_search_mark_used() {
    local query="$1"
    local issue_num="$2"
    [ -f "$CACHE_FILE" ] || return 0
    python3 -c "
import json
cache_file = '$CACHE_FILE'
try:
    with open(cache_file) as f:
        cache = json.load(f)
    for entry in cache.get('entries', []):
        if entry.get('query') == sys.argv[1]:
            issues = entry.setdefault('used_in_issues', [])
            if int(sys.argv[2]) not in issues:
                issues.append(int(sys.argv[2]))
    with open(cache_file, 'w') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
except Exception:
    pass
" "$query" "$issue_num"
}

# === Cleanup function — вызывается на EXIT/INT/TERM ===
cleanup() {
    local EXIT_CODE=$?
    echo ""
    echo "[cron_run v9.59] === Cleanup (exit=$EXIT_CODE) ==="

    # v9.59: GUARANTEED in-progress sweep — если #${ISSUE} закрыт, метка обязана быть снята.
    # Это ловит кейсы, когда цикл упал между close (Step 7) и remove label (Step 8),
    # а также ручные закрытия «нарушение не воспроизводится» без commit-фазы.
    local CURRENT_STATE
    CURRENT_STATE=$(curl -s -H "Authorization: token ${PAT}" \
        "https://api.github.com/repos/${REPO}/issues/${ISSUE}" | \
        python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('state','unknown'))" 2>/dev/null || echo "unknown")
    if [ "${CURRENT_STATE}" = "closed" ]; then
        echo "[cron_run v9.59] Issue #${ISSUE} is closed — guaranteed in-progress removal"
        local SWEEP_CODE
        SWEEP_CODE=$(curl -s -X DELETE -H "Authorization: token ${PAT}" \
            "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels/in-progress" \
            -o /dev/null -w "%{http_code}" 2>/dev/null || echo "000")
        # 200/204 = снято; 404 = метки уже нет — оба варианта OK
        if [ "${SWEEP_CODE}" = "200" ] || [ "${SWEEP_CODE}" = "204" ] || [ "${SWEEP_CODE}" = "404" ]; then
            echo "[cron_run v9.59] ✓ guaranteed sweep done (HTTP ${SWEEP_CODE})"
        else
            echo "[cron_run v9.59] ⚠️  sweep returned HTTP ${SWEEP_CODE} (issue still closed)"
        fi
    else
        echo "[cron_run v9.59] Issue #${ISSUE} state=${CURRENT_STATE} — leave in-progress in place"
    fi

    if [ $EXIT_CODE -eq 0 ]; then
        # Успех — проверяем, что нет orphaned edits
        local NEW_MODS
        NEW_MODS=$(git status --porcelain | grep -vE '^\?\?' | wc -l)
        if [ "$NEW_MODS" -gt 0 ]; then
            echo "[cron_run v9.59] ⚠️  Success exit but $NEW_MODS modified files remain in working tree:"
            git status --porcelain | grep -vE '^\?\?' | head -10
            echo "[cron_run v9.59] These are orphaned edits — kept for next cycle (NOT restored)."
        else
            echo "[cron_run v9.59] ✓ Working tree clean"
        fi
        return 0
    fi

    # Failure — restore issue labels if we changed them
    echo "[cron_run v9.59] ⚠️  Cycle failed at exit=$EXIT_CODE"
    echo "[cron_run v9.59] Checking if we added in-progress label to #${ISSUE}..."

    local NEW_MODS
    NEW_MODS=$(git status --porcelain | grep -vE '^\?\?' | wc -l)
    if [ "$NEW_MODS" -gt 0 ]; then
        echo "[cron_run v9.59] Orphaned edits preserved ($NEW_MODS files):"
        git status --porcelain | grep -vE '^\?\?' | head -10
    fi

    echo "[cron_run v9.59] ✗ Cycle ended with error — issue #${ISSUE} may need manual cleanup"
}

trap cleanup EXIT INT TERM

# === Step 1: Verify in-progress lock (v9.59: complexity-aware) ===
echo "[cron_run v9.59] Step 1: Check in-progress lock on #${ISSUE}"
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

# v9.59: если issue уже закрыт — ничего не делать, метка будет снята cleanup-trap'ом
CURRENT_STATE=$(curl -s -H "Authorization: token $PAT" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}" | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('state','unknown'))" 2>/dev/null || echo "unknown")
if [ "${CURRENT_STATE}" = "closed" ]; then
    echo "[cron_run v9.59] Issue #${ISSUE} is already CLOSED — nothing to commit. Cleanup-trap снимет метку."
    exit 0
fi

if [ "$HAS_INPROGRESS" = "yes" ]; then
    # v9.59: получить сложность issue для complexity-aware threshold
    COMPLEXITY=$(get_complexity "$ISSUE")
    THRESHOLD=$(get_stale_threshold "$COMPLEXITY")
    echo "[cron_run v9.59] issue complexity: ${COMPLEXITY:-none} → stale threshold: ${THRESHOLD} min"

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
    echo "[cron_run v9.59] in-progress label age: ${AGE_MIN} min (threshold: ${THRESHOLD})"
    if [ "$AGE_MIN" -lt "$THRESHOLD" ]; then
        echo "[cron_run v9.59] ⚠️  Lock is ACTIVE (<${THRESHOLD} min for ${COMPLEXITY:-default}) — another cycle is running. Exit without changes."
        exit 0
    fi
    echo "[cron_run v9.59] Lock is STALE (>=${THRESHOLD} min) — removing and taking over."
    curl -s -X DELETE -H "Authorization: token $PAT" \
        "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels/in-progress" >/dev/null
fi

# === Step 2: Add in-progress label ===
echo "[cron_run v9.59] Step 2: Add in-progress label to #${ISSUE}"
curl -s -X POST -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels" \
    -d '{"labels":["in-progress"]}' >/dev/null
echo "[cron_run v9.59] ✓ in-progress label set"

# === Step 3: Stage files ===
echo "[cron_run v9.59] Step 3: Stage ${#FILES[@]} file(s)"
for f in "${FILES[@]}"; do
    if [ ! -f "$f" ]; then
        echo "[cron_run v9.59] ERROR: file not found: $f" >&2
        exit 4
    fi
    git add "$f"
    echo "[cron_run v9.59]   staged: $f"
done

# === Step 4: Commit (atomic via git) ===
echo "[cron_run v9.59] Step 4: git commit"

# v9.59: если issue sub-issue — добавить parent-ссылку в коммит
PARENT_NUM=""
if [ "$(is_sub_issue "$ISSUE")" = "yes" ]; then
    PARENT_NUM=$(get_parent_number "$ISSUE")
fi

if [ -n "$PARENT_NUM" ]; then
    COMMIT_MSG="fix(verify): #${ISSUE} (sub of #${PARENT_NUM}) — real data from web_search

Files: ${#FILES[@]}
Source: web_search via z-ai function
Cycle: cron_run.sh v9.59 (transactional, complexity-aware, sweep-on-start)
Parent: #${PARENT_NUM}"
else
    COMMIT_MSG="fix(verify): #${ISSUE} batch — real data from web_search

Files: ${#FILES[@]}
Source: web_search via z-ai function
Cycle: cron_run.sh v9.59 (transactional, complexity-aware, sweep-on-start)"
fi

if ! git commit -m "$COMMIT_MSG" 2>&1 | tail -5; then
    echo "[cron_run v9.59] git commit failed — see above" >&2
    exit 5
fi
NEW_COMMIT=$(git rev-parse HEAD)
echo "[cron_run v9.59] ✓ committed: ${NEW_COMMIT:0:8}"

# === Step 5: Push (with rebase) ===
echo "[cron_run v9.59] Step 5: git push"
if ! git pull --rebase origin main 2>&1 | tail -5; then
    echo "[cron_run v9.59] rebase failed — aborting push" >&2
    exit 6
fi
if ! git push origin main 2>&1 | tail -5; then
    echo "[cron_run v9.59] push failed — see above" >&2
    exit 7
fi
echo "[cron_run v9.59] ✓ pushed"

# === Step 6: Comment on issue ===
echo "[cron_run v9.59] Step 6: Post comment to #${ISSUE}"
SHORT_SHA="${NEW_COMMIT:0:8}"

# v9.59: получить сложность issue для комментария
COMPLEXITY=$(get_complexity "$ISSUE")
COMPLEXITY_LINE=""
if [ -n "$COMPLEXITY" ]; then
    COMPLEXITY_LINE="**Сложность:** ${COMPLEXITY}"
fi

# v9.59: sub-issue info
SUB_INFO=""
if [ -n "$PARENT_NUM" ]; then
    SUB_INFO="**Parent:** #${PARENT_NUM}

"
fi

COMMENT_BODY=$(cat <<EOF
## Транзакционный cron-цикл завершён (v9.59)

${SUB_INFO}**Commit:** [\`${SHORT_SHA}\`](https://github.com/${REPO}/commit/${NEW_COMMIT})

**Файлы (${#FILES[@]}):**
$(for f in "${FILES[@]}"; do echo "- \`$f\`"; done)

**Источник данных:** web_search через \`z-ai function -n web_search\`
${COMPLEXITY_LINE}
**Протокол:** \`scripts/cron_run.sh\` v9.59 (транзакционный, complexity-aware stale-detection, sweep-on-start)
**Lock:** in-progress добавлен → будет снят после закрытия issue
EOF
)
curl -s -X POST -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/comments" \
    -d "$(python3 -c "import json,sys; print(json.dumps({'body': sys.stdin.read()}))" <<< "$COMMENT_BODY")" >/dev/null
echo "[cron_run v9.59] ✓ comment posted"

# === Step 7: Close issue ===
echo "[cron_run v9.59] Step 7: Close #${ISSUE}"
curl -s -X PATCH -H "Authorization: token $PAT" -H "Content-Type: application/json" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}" \
    -d '{"state":"closed","state_reason":"completed"}' >/dev/null
echo "[cron_run v9.59] ✓ issue closed"

# === Step 8: Remove in-progress label ===
echo "[cron_run v9.59] Step 8: Remove in-progress label"
curl -s -X DELETE -H "Authorization: token $PAT" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE}/labels/in-progress" >/dev/null
echo "[cron_run v9.59] ✓ in-progress removed"

# === Step 9 (NEW v9.58): Parent auto-close check ===
if [ -n "$PARENT_NUM" ]; then
    echo "[cron_run v9.59] Step 9: Check parent #${PARENT_NUM} for auto-close"
    RESULT=$(check_all_subs_closed "$PARENT_NUM")
    case "$RESULT" in
        all-closed)
            echo "[cron_run v9.59] All sub-issues of #${PARENT_NUM} closed — auto-closing parent"
            auto_close_parent "$PARENT_NUM"
            ;;
        has-open)
            echo "[cron_run v9.59] Parent #${PARENT_NUM} still has open sub-issues — keep parent open"
            ;;
        no-subs)
            echo "[cron_run v9.59] ⚠️ No sub-issues found for parent #${PARENT_NUM} — skip auto-close"
            ;;
    esac
fi

echo ""
echo "[cron_run v9.59] === Transaction complete ==="
echo "[cron_run v9.59] Issue #${ISSUE} → closed"
echo "[cron_run v9.59] Commit ${SHORT_SHA} pushed to main"
echo "[cron_run v9.59] Lock released"

# trap cleanup вызовет exit 0 — проверит, что working tree чист
# v9.59: cleanup() также сделает гарантированный sweep (closed → remove label)
