#!/usr/bin/env bash
# scripts/sweep_closed_inprogress.sh v9.59
#
# Sanity-sweep: находит все ЗАКРЫТЫЕ issues с меткой `in-progress` и снимает её.
#
# Проблема, которую решает:
#   cron_run.sh v9.58 имеет линейный сценарий: edit → commit → comment → close → remove label.
#   Если цикл падает между close и remove label (или закрывает issue вручную,
#   как было с #966: «нарушение не воспроизводится, чинить нечего»),
#   в API остаётся closed issue с мёртвой меткой in-progress.
#   Эти мёртвые метки не блокируют PICK (state=open фильтр их не видит),
#   но загрязняют очередь и вводят в заблуждение мониторинг.
#
# Стратегия:
#   GET /issues?state=closed&labels=in-progress → для каждого: DELETE label.
#   Безопасно: issue уже закрыто, метка не несёт смысловой нагрузки.
#
# Использование:
#   bash scripts/sweep_closed_inprogress.sh           # silent, снимает всё найденное
#   bash scripts/sweep_closed_inprogress.sh --dry-run # показать, но не снимать
#   bash scripts/sweep_closed_inprogress.sh --verbose # показывать HTTP-коды

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# v9.59: Auto-recovery PAT (тот же механизм что в cron_run.sh)
if [ ! -f /tmp/.pat_tmp ]; then
    if [ -f /home/z/my-project/.pat_tmp ]; then
        cp /home/z/my-project/.pat_tmp /tmp/.pat_tmp
        chmod 600 /tmp/.pat_tmp
        echo "[sweep v9.59] ✓ PAT recovered from /home/z/my-project/.pat_tmp" >&2
    else
        REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
        case "$REMOTE_URL" in
            https://x-access-token:*@*)
                echo "$REMOTE_URL" | sed -nE 's#https://x-access-token:([^@]+)@.*#\1#p' > /tmp/.pat_tmp
                chmod 600 /tmp/.pat_tmp
                cp /tmp/.pat_tmp /home/z/my-project/.pat_tmp 2>/dev/null || true
                echo "[sweep v9.59] ✓ PAT recovered from git remote URL" >&2
                ;;
            *)
                echo "ERROR: PAT not found" >&2; exit 3
                ;;
        esac
    fi
fi

[ -f /tmp/.pat_tmp ] || { echo "ERROR: /tmp/.pat_tmp not found" >&2; exit 3; }

DRY_RUN=0
VERBOSE=0
for arg in "$@"; do
    case "$arg" in
        --dry-run)  DRY_RUN=1 ;;
        --verbose)   VERBOSE=1 ;;
        *) echo "Unknown arg: $arg" >&2; exit 2 ;;
    esac
done

# GitHub labels query имеет задержку индексации (~2-5 сек). Если первый запрос
# вернул 0, делаем ретрай через 3 сек. Sweep запускается раз в 6 мин, поэтому
# лишние 3 сек ничего не стоят, зато ловим только что появившиеся метки.
echo "[sweep v9.59] === Sweep stale in-progress on closed issues (dry_run=$DRY_RUN) ==="

run_sweep() {
python3 - "$1" <<'PYEOF'
import json, urllib.request, sys, time, os
PAT = open('/tmp/.pat_tmp').read().strip()
REPO = "a-m-e-n-t-e-t/SkyNet"
DRY_RUN = int(os.environ.get('SWEEP_DRY_RUN', '0'))
VERBOSE = int(os.environ.get('SWEEP_VERBOSE', '0'))

def api(method, url):
    req = urllib.request.Request(url, method=method,
        headers={"Authorization": f"token {PAT}", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode('utf-8') or 'null')
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return -1, None

def api_delete(url):
    req = urllib.request.Request(url, method='DELETE',
        headers={"Authorization": f"token {PAT}", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return -1

found = 0
removed = 0
page = 1
while True:
    url = f"https://api.github.com/repos/{REPO}/issues?state=closed&labels=in-progress&per_page=100&page={page}"
    status, data = api('GET', url)
    if status != 200 or not isinstance(data, list) or not data:
        break
    for it in data:
        found += 1
        num = it.get('number')
        title = (it.get('title') or '')[:60]
        closed_at = it.get('closed_at')
        print(f"[sweep v9.59] found: #{num} '{title}' closed={closed_at}")
        if DRY_RUN:
            print(f"[sweep v9.59]   → [DRY-RUN] would DELETE label")
            removed += 1  # count intended removals
            continue
        code = api_delete(f"https://api.github.com/repos/{REPO}/issues/{num}/labels/in-progress")
        if code in (200, 204):
            removed += 1
            print(f"[sweep v9.59]   ✓ removed (HTTP {code})")
        else:
            print(f"[sweep v9.59]   ✗ failed (HTTP {code})")
        time.sleep(0.3)
    if len(data) < 100:
        break
    page += 1
    if page > 5:
        print(f"[sweep v9.59] page limit reached — stop at page {page}")
        break

action = "would remove" if DRY_RUN else "removed"
print(f"[sweep v9.59] === Sweep complete: found={found}, {action}={removed} ===")
# Exit code 0 если ничего не найдено (sweep-ретрай не нужен), иначе 1 (найдено что снимать)
sys.exit(0 if found == 0 else 1)
PYEOF
}

# v9.59: retry-passthrough — если первый sweep нашёл 0, сделать ретрай через 3 сек
# (защита от лага индексации GitHub labels query)
SWEEP_DRY_RUN=$DRY_RUN SWEEP_VERBOSE=$VERBOSE run_sweep "first"
FIRST_EXIT=$?
if [ $FIRST_EXIT -eq 0 ] && [ $DRY_RUN -eq 0 ]; then
    echo "[sweep v9.59] First sweep found nothing — retry in 3s (GitHub labels index lag protection)"
    sleep 3
    SWEEP_DRY_RUN=$DRY_RUN SWEEP_VERBOSE=$VERBOSE run_sweep "retry"
    exit $?
fi
exit $FIRST_EXIT
