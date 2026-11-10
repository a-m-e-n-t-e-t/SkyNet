#!/usr/bin/env bash
# scripts/pat_recovery.sh v9.59
#
# Восстановление GitHub PAT для cron-агента SkyNet.
# Используется cron_run.sh и sweep_closed_inprogress.sh в pre-flight.
#
# Стратегия (5 уровней, по убыванию предпочтительности):
#   1. /tmp/.pat_tmp                     — быстрый путь, но исчезает при sandbox-recycle
#   2. /home/z/my-project/.pat_tmp         — персистентное, переживает recycle
#   3. git remote get-url origin          — URL репозитория содержит x-access-token:...
#   4. Yandex Disk публичная ссылка       — Token.docx на disk.yandex.ru/i/3RiKQucdvHI2Sg
#                                          (не требует OAuth, публичный доступ через
#                                          cloud-api.yandex.net/v1/disk/public/resources)
#   5. scripts/.pat.enc в git репозитории — зашифрованный PAT (AES-256-CBC + PBKDF2,
#                                          ключ из SHA-256 URL Яндекс.Диска). Last resort
#                                          когда Yandex Disk API упал (429).
#
# Использование:
#   source scripts/pat_recovery.sh
#   # после source: $PAT установлен, /tmp/.pat_tmp и /home/z/my-project/.pat_tmp синхронны
#
# Возвращает 0 при успехе, 3 при неудаче. Выводит диагностику в stderr.

# Константы
PAT_REPO_ROOT="${PAT_REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
PAT_HOME_STORAGE="${PAT_HOME_STORAGE:-/home/z/my-project/.pat_tmp}"
PAT_TMP_STORAGE="${PAT_TMP_STORAGE:-/tmp/.pat_tmp}"
PAT_YANDEX_PUBLIC_KEY="${PAT_YANDEX_PUBLIC_KEY:-https://disk.yandex.ru/i/3RiKQucdvHI2Sg}"
PAT_YANDEX_API="${PAT_YANDEX_API:-https://cloud-api.yandex.net/v1/disk/public/resources}"
PAT_ENC_FILE="${PAT_ENC_FILE:-${PAT_REPO_ROOT}/scripts/.pat.enc}"

# Вспомогательная: валидация PAT через GitHub API /user
_pat_validate() {
    local token="$1"
    [ -z "$token" ] && return 1
    local resp
    resp=$(curl -sS -m 10 -H "Authorization: token $token" "https://api.github.com/user" 2>/dev/null)
    echo "$resp" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    sys.exit(0 if d.get('login') else 1)
except Exception:
    sys.exit(1)
"
}

# Уровень 4: Yandex Disk public link → Token.docx → extract PAT
_pat_from_yandex_disk() {
    # Запрос метаданных публичного ресурса (follow redirects — Yandex API иногда редиректит)
    local meta_url="${PAT_YANDEX_API}?public_key=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$PAT_YANDEX_PUBLIC_KEY")"
    local meta_json
    meta_json=$(curl -sSL -m 15 -A "SkyNet-cron/1.0" "$meta_url" 2>/dev/null)
    [ -z "$meta_json" ] && return 1

    # Извлечь прямой URL скачивания (поле "file")
    local download_url
    download_url=$(echo "$meta_json" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get('file',''))
except Exception:
    sys.exit(1)
")
    [ -z "$download_url" ] && return 1

    # Скачать .docx (timeout 30s, max size 1MB для безопасности, follow redirects)
    local tmp_docx="/tmp/.pat_token.docx.$$"
    curl -sSL -m 30 -A "SkyNet-cron/1.0" "$download_url" -o "$tmp_docx" 2>/dev/null
    [ ! -s "$tmp_docx" ] && { rm -f "$tmp_docx"; return 1; }

    # Извлечь PAT из .docx (word/document.xml → <w:t> текст → regex github_pat_...|ghp_...)
    local token
    token=$(unzip -p "$tmp_docx" word/document.xml 2>/dev/null | python3 -c "
import sys, re
xml = sys.stdin.read()
texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml)
full = ''.join(texts)
m = re.search(r'(github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+)', full)
if m:
    print(m.group(1))
else:
    m2 = re.search(r'Token:\s*(\S+)', full)
    if m2: print(m2.group(1))
" 2>/dev/null)
    rm -f "$tmp_docx"
    [ -z "$token" ] && return 1

    echo "$token"
    return 0
}

# Уровень 5: Зашифрованный PAT в git репозитории (scripts/.pat.enc)
# Last resort: Yandex Disk API упал (429), но raw-файл .pat.enc доступен локально
# из git clone. Шифр AES-256-CBC + PBKDF2 (100000 итераций), ключ = SHA-256(URL Яндекс.Диска).
_pat_from_encrypted() {
    [ ! -f "$PAT_ENC_FILE" ] && return 1
    [ ! -f "${PAT_REPO_ROOT}/scripts/pat_crypto.sh" ] && return 1

    # Source pat_crypto.sh для функции pat_decrypt
    # shellcheck disable=SC1091
    source "${PAT_REPO_ROOT}/scripts/pat_crypto.sh"

    local token
    token=$(pat_decrypt < "$PAT_ENC_FILE" 2>/dev/null)
    [ -z "$token" ] && return 1
    echo "$token"
    return 0
}

# Главная функция: восстановить PAT в /tmp/.pat_tmp
pat_recover() {
    # Уровень 1: /tmp/.pat_tmp существует
    if [ -f "$PAT_TMP_STORAGE" ]; then
        PAT="$(cat "$PAT_TMP_STORAGE")"
        if _pat_validate "$PAT"; then
            # Уровень 1 OK — синхронизируем персистентную копию на всякий случай
            [ -f "$PAT_HOME_STORAGE" ] || { cp "$PAT_TMP_STORAGE" "$PAT_HOME_STORAGE" 2>/dev/null && chmod 600 "$PAT_HOME_STORAGE"; } || true
            return 0
        fi
    fi

    echo "[pat_recovery v9.59] /tmp/.pat_tmp missing or invalid — trying recovery:" >&2

    # Уровень 2: /home/z/my-project/.pat_tmp (персистентное)
    if [ -f "$PAT_HOME_STORAGE" ]; then
        PAT="$(cat "$PAT_HOME_STORAGE")"
        if _pat_validate "$PAT"; then
            cp "$PAT_HOME_STORAGE" "$PAT_TMP_STORAGE"
            chmod 600 "$PAT_TMP_STORAGE"
            echo "[pat_recovery v9.59] ✓ recovered from /home/z/my-project/.pat_tmp (persistent storage)" >&2
            return 0
        fi
        echo "[pat_recovery v9.59]   home storage present but PAT invalid — escalating" >&2
    fi

    # Уровень 3: git remote get-url origin
    cd "$PAT_REPO_ROOT" 2>/dev/null || true
    local remote_url
    remote_url=$(git remote get-url origin 2>/dev/null || echo "")
    case "$remote_url" in
        https://x-access-token:*@*)
            PAT=$(echo "$remote_url" | sed -nE 's#https://x-access-token:([^@]+)@.*#\1#p')
            if _pat_validate "$PAT"; then
                echo "$PAT" > "$PAT_TMP_STORAGE"; chmod 600 "$PAT_TMP_STORAGE"
                cp "$PAT_TMP_STORAGE" "$PAT_HOME_STORAGE" 2>/dev/null && chmod 600 "$PAT_HOME_STORAGE"
                echo "[pat_recovery v9.59] ✓ recovered from git remote URL + saved to persistent storage" >&2
                return 0
            fi
            echo "[pat_recovery v9.59]   git remote URL has token but it's invalid — escalating" >&2
            ;;
    esac

    # Уровень 4: Yandex Disk public link
    echo "[pat_recovery v9.59]   trying Yandex Disk public link..." >&2
    local yandex_token
    yandex_token=$(_pat_from_yandex_disk)
    if [ -n "$yandex_token" ] && _pat_validate "$yandex_token"; then
        PAT="$yandex_token"
        echo "$PAT" > "$PAT_TMP_STORAGE"; chmod 600 "$PAT_TMP_STORAGE"
        cp "$PAT_TMP_STORAGE" "$PAT_HOME_STORAGE" 2>/dev/null && chmod 600 "$PAT_HOME_STORAGE"
        echo "[pat_recovery v9.59] ✓ recovered from Yandex Disk public link + saved to persistent storage" >&2
        return 0
    fi
    echo "[pat_recovery v9.59]   Yandex Disk download/validation failed" >&2

    # Уровень 5: Зашифрованный PAT в git репозитории
    echo "[pat_recovery v9.59]   trying encrypted PAT from scripts/.pat.enc..." >&2
    local enc_token
    enc_token=$(_pat_from_encrypted)
    if [ -n "$enc_token" ] && _pat_validate "$enc_token"; then
        PAT="$enc_token"
        echo "$PAT" > "$PAT_TMP_STORAGE"; chmod 600 "$PAT_TMP_STORAGE"
        cp "$PAT_TMP_STORAGE" "$PAT_HOME_STORAGE" 2>/dev/null && chmod 600 "$PAT_HOME_STORAGE"
        echo "[pat_recovery v9.59] ✓ recovered from encrypted .pat.enc + saved to persistent storage" >&2
        return 0
    fi
    echo "[pat_recovery v9.59]   encrypted .pat.enc decryption/validation failed" >&2

    # Все уровни провалены
    echo "ERROR: PAT recovery failed at all 5 levels" >&2
    echo "       1. /tmp/.pat_tmp                       — missing/invalid" >&2
    echo "       2. /home/z/my-project/.pat_tmp         — missing/invalid" >&2
    echo "       3. git remote get-url origin           — no token or invalid" >&2
    echo "       4. Yandex Disk public link             — failed" >&2
    echo "       5. scripts/.pat.enc (encrypted)        — missing/invalid" >&2
    echo "       Manual PAT injection required." >&2
    return 3
}
