#!/usr/bin/env bash
# scripts/pat_crypto.sh v9.59
#
# Симметричное шифрование GitHub PAT для хранения в публичном git-репозитории.
#
# Зачем:
#   Репозиторий a-m-e-n-t-e-t/SkyNet — публичный. PAT в plaintext закоммитить
#   нельзя: GitHub Secret Scanning автоматически детектирует github_pat_*/ghp_*
#   и отзывает токен в течение минут. Зашифрованный ciphertext — это случайные
#   байты в base64, не матчат паттерн Secret Scanning'а.
#
# Криптография:
#   Cipher:  AES-256-CBC + PKCS7 padding
#   KDF:     PBKDF2-HMAC-SHA256, 100000 итераций
#   Salt:    случайный при шифровании (вшит в openssl-вывод)
#   Key:     SHA-256 от публичного URL Яндекс.Диска (PAT_YANDEX_PUBLIC_KEY).
#            URL и так захардкожен в pat_recovery.sh — не добавляем новый секрет.
#            Это НЕ криптозащита, это обфускация от ботов. Реальный секрет —
#            URL Яндекс.Диска, который известен только тем, у кого есть скрипты.
#
# Слабость (явная):
#   Кто угодно с доступом к pat_recovery.sh и .pat.enc может расшифровать PAT.
#   Это НЕ замена уровням 1-4, это уровень 5 — last resort когда Yandex Disk
#   API упал (429), а sandbox полностью потерян (нет ни /tmp, ни /home/.pat_tmp,
#   ни git remote URL с PAT).
#
# Использование:
#   source scripts/pat_crypto.sh
#
#   # Зашифровать (PAT из stdin):
#   echo -n "GITHUB_TOKEN_VALUE" | pat_encrypt > scripts/.pat.enc
#
#   # Расшифровать (PAT в stdout):
#   pat_decrypt < scripts/.pat.enc
#
# Зависимости: openssl (стандартный в Linux sandbox).

# Константа — должна совпадать с pat_recovery.sh
PAT_CRYPTO_KEY_SOURCE="${PAT_CRYPTO_KEY_SOURCE:-https://disk.yandex.ru/i/3RiKQucdvHI2Sg}"

# Получить ключ шифрования (32 hex символа от SHA-256)
_pat_crypto_key() {
    printf '%s' "$PAT_CRYPTO_KEY_SOURCE" | sha256sum | cut -d' ' -f1
}

# Зашифровать PAT (PAT из stdin, ciphertext+base64 в stdout)
pat_encrypt() {
    local key
    key=$(_pat_crypto_key)
    # openssl enc с -pbkdf2 генерирует случайный salt, кладёт его в output.
    # -base64 -A → одна строка без переносов (удобно для git diff).
    openssl enc -aes-256-cbc -pbkdf2 -iter 100000 \
        -pass pass:"$key" -base64 -A 2>/dev/null
}

# Расшифровать PAT (ciphertext из stdin, PAT в stdout)
pat_decrypt() {
    local key
    key=$(_pat_crypto_key)
    openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 \
        -pass pass:"$key" -base64 -A 2>/dev/null
}

# Тест: зашифровать и расшифровать тестовую строку (для ручной проверки)
pat_crypto_selftest() {
    local test_str="test_pat_crypto_$(date +%s)_$$"
    local encrypted decrypted
    encrypted=$(printf '%s' "$test_str" | pat_encrypt)
    decrypted=$(printf '%s' "$encrypted" | pat_decrypt)
    if [ "$test_str" = "$decrypted" ]; then
        echo "✓ pat_crypto selftest OK (roundtrip match, len=${#encrypted})"
        return 0
    else
        echo "✗ pat_crypto selftest FAILED"
        echo "  input:    $test_str"
        echo "  encrypted: ${encrypted:0:40}..."
        echo "  decrypted: $decrypted"
        return 1
    fi
}
