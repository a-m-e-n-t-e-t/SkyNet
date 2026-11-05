#!/usr/bin/env python3
"""Patch §19 in v9.20: replace ${SKYNET_REPO} with f-string + add env var import."""
import re
from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.20.md")
text = SRC.read_text(encoding="utf-8")

# 1. Заменить все вхождения "${SKYNET_REPO}/..." внутри §19 блока
# Используем точную регулярку: def check_current_state ... return { ... }
pattern = re.compile(
    r'(def check_current_state\(\) -> dict:\n    """Проверка фактического состояния перед запуском pipeline."""\n)(    return \{[\s\S]*?\n    \})',
    re.MULTILINE
)
m = pattern.search(text)
if not m:
    print("✗ Блок §19 не найден")
    exit(1)

header, body = m.group(1), m.group(2)
print(f"Найден блок §19, длина body = {len(body)}")

# Вставить import os + SKYNET_REPO = os.environ.get(...) перед return
new_header = header + '''    import os
    SKYNET_REPO = os.environ.get("SKYNET_REPO", "/home/z/my-project/SkyNet")  # v9.20: env var (sandbox default)
'''

# Заменить все "${SKYNET_REPO}/..." на f"{SKYNET_REPO}/..."
new_body = body.replace('"${SKYNET_REPO}/', 'f"{SKYNET_REPO}/')

# Также для случаев is_repo_empty("${SKYNET_REPO}") — без trailing slash
new_body = new_body.replace('"${SKYNET_REPO}"', 'f"{SKYNET_REPO}"')

# Собрать обратно
new_block = new_header + new_body

# Проверить компилируемость
try:
    compile(new_block, '<§19>', 'exec')
    print("✓ Обновлённый §19 компилируется")
except SyntaxError as e:
    print(f"✗ SyntaxError: {e}")
    print(new_block)
    exit(1)

# Применить
text_new = text.replace(m.group(0), new_block)

# Финальная проверка
m2 = pattern.search(text_new)
if m2:
    final_code = m2.group(1) + m2.group(2)
    try:
        compile(final_code, '<§19-final>', 'exec')
        print("✓ Финальный §19 компилируется")
    except SyntaxError as e:
        print(f"✗ Финальный §19 не компилируется: {e}")
        exit(1)

SRC.write_text(text_new, encoding="utf-8")
print(f"\n✓ Патч §19 применён")

# Показать ключевые проверки
for needle, desc in [
    ('SKYNET_REPO = os.environ.get("SKYNET_REPO"', "env var definition"),
    ('os.path.exists(f"{SKYNET_REPO}/.git")', "f-string path .git"),
    ('is_repo_empty(f"{SKYNET_REPO}")', "is_repo_empty f-string"),
    ('read_yaml_safe(f"{SKYNET_REPO}/требования', "read_yaml_safe f-string"),
    ('len(glob.glob(f"{SKYNET_REPO}/scripts/*.py"))', "glob f-string"),
]:
    ok = "✓" if needle in text_new else "✗"
    print(f"  {ok} {desc}")
