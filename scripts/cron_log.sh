#!/usr/bin/env bash
# scripts/cron_log.sh v9.59
#
# Append-only логгер для cron-цикла SkyNet.
# Каждый шаг cron-агента логируется в диалог/cron_log.md с timestamp.
# В конце цикла лог коммитится отдельным commit'ом (через log_commit).
#
# Использование (через source):
#   source scripts/cron_log.sh
#   log_step "Cron-цикл запущен"
#   log_step "PAT восстановлен: user=a-m-e-n-t-e-t"
#   ...
#   log_step "Cycle complete"
#   log_commit   # коммитит лог отдельным commit'ом (если есть изменения)
#
# Формат лог-файла:
#   ## YYYY-MM-DD HH:MM:SS UTC (cycle #N, run_id=...)
#   - HH:MM:SS | message
#   - HH:MM:SS | message
#   ...

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
LOG_FILE="${REPO_ROOT}/диалог/cron_log.md"

# Получить run_id (уникальный для каждого цикла)
LOG_RUN_ID="${LOG_RUN_ID:-$(date -u +%s)-$$}"
LOG_START_TIME="${LOG_START_TIME:-$(date -u '+%Y-%m-%d %H:%M:%S UTC')}"
LOG_STEP_COUNT="${LOG_STEP_COUNT:-0}"

# Инициализация: убедиться, что папка есть, файл существует
_log_init() {
    mkdir -p "$(dirname "$LOG_FILE")"
    if [ ! -f "$LOG_FILE" ]; then
        cat > "$LOG_FILE" << 'EOF'
# Cron-лог SkyNet v9.62

Append-only лог запусков cron-агента. Каждая запись — один шаг цикла.
Файл обновляется через `source scripts/cron_log.sh && log_step "..."`.

EOF
    fi
}

# Логировать шаг: log_step "сообщение"
log_step() {
    _log_init
    LOG_STEP_COUNT=$((LOG_STEP_COUNT + 1))
    # Если это первый шаг — добавляем заголовок цикла
    if [ "$LOG_STEP_COUNT" = "1" ]; then
        echo "" >> "$LOG_FILE"
        echo "## ${LOG_START_TIME} (cycle run_id=${LOG_RUN_ID})" >> "$LOG_FILE"
    fi
    local ts
    ts=$(date -u '+%H:%M:%S')
    echo "- ${ts} | $1" >> "$LOG_FILE"
    # Дублировать в stderr для отладки в реальном времени
    echo "[cron_log] $1" >&2
}

# Логировать ошибку: log_error "сообщение" [exit_code]
log_error() {
    log_step "❌ ERROR: $1"
    if [ -n "${2:-}" ]; then
        log_step "   exit_code=$2"
    fi
}

# Финализировать и закоммитить лог отдельным commit'ом
# Использовать в конце каждого цикла, даже если других коммитов не было
log_commit() {
    _log_init
    if [ ! -f "$LOG_FILE" ]; then
        return 0
    fi
    # Проверить, есть ли незакоммиченные изменения в лог-файле
    if git diff --quiet "$LOG_FILE" 2>/dev/null && ! git ls-files --others --exclude-standard | grep -q "^${LOG_FILE#$REPO_ROOT/}"; then
        echo "[cron_log] no changes to commit" >&2
        return 0
    fi
    cd "$REPO_ROOT"
    git add "$LOG_FILE" 2>/dev/null
    # Commit с пустым author-change marker, чтобы отличить от verify-коммитов
    local msg="chore(log): cron-cycle run_id=${LOG_RUN_ID} (steps=${LOG_STEP_COUNT})"
    if git commit -m "$msg" 2>&1 | tail -3; then
        echo "[cron_log] ✓ лог закоммичен: $msg" >&2
        # Push (ignore errors — push может быть недоступен в read-only sandbox)
        git push origin main 2>&1 | tail -2 || true
    else
        echo "[cron_log] ⚠️  commit не удался — возможно, нет прав или конфликт" >&2
    fi
}

# Самодиагностика: запустить scripts/cron_log.sh напрямую для теста
if [ "${BASH_SOURCE[0]:-}" = "${0:-}" ]; then
    # Прямой запуск — не через source
    echo "=== Self-test scripts/cron_log.sh ==="
    source "$0"
    log_step "Self-test: логгер работает"
    log_step "LOG_FILE=$LOG_FILE"
    log_step "LOG_RUN_ID=$LOG_RUN_ID"
    log_step "Лог-файл существует: $([ -f "$LOG_FILE" ] && echo yes || echo no)"
    echo ""
    echo "Последние 10 строк лог-файла:"
    tail -10 "$LOG_FILE" 2>/dev/null || echo "  (файл не создан)"
fi
