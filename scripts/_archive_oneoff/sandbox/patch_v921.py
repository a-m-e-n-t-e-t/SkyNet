#!/usr/bin/env python3
"""Patch v9.20 -> v9.21: mention 14 workflows + 8 config files in header."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.21.md")
text = SRC.read_text(encoding="utf-8")

# Update version in header
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.20",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.21"
)

text = text.replace(
    '> **Версия:** 9.20\n> **Дата:** 2026-11-02\n> **Базируется на:** v9.19 + аудит SkyNet_PROMPT_v9.19_AUDIT_WORKFLOWS.md + 6 workflow-файлов',
    '> **Версия:** 9.21\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.20 (9 багов исправлено) + расширенная GitHub-автоматизация (14 workflows + 8 configs)'
)

text = text.replace(
    '  version: 9.20',
    '  version: 9.21'
)

text = text.replace(
    '## 5 столпов архитектуры v9.20',
    '## 5 столпов архитектуры v9.21'
)

# Replace the v9.20 changelog block with v9.21
old_block_start = '> **Ключевые изменения v9.20 (поверх v9.19):**'
old_block_end = '> Промпт сжат с **8881 до ~5888 строк (-34%)** через вынос в 4 отдельных файла:'

# Find the block and replace
import re
pattern = re.compile(
    r'> \*\*Ключевые изменения v9\.20 \(поверх v9\.19\):\*\*[\s\S]*?> Промпт сжат с \*\*8881 до ~5888 строк \(-34%\)\*\* через вынос в 4 отдельных файла:',
    re.MULTILINE
)
m = pattern.search(text)
if m:
    old_block = m.group(0)
    new_block = '''> **Ключевые изменения v9.21 (поверх v9.20):**
>
> 🟢 **РАСШИРЕННАЯ GITHUB-АВТОМАТИЗАЦИЯ (8 новых файлов):**
>
> Поверх 6 workflows из v9.20 добавлены 5 workflows и 3 config-файла:
>
> **Новые workflows (5):**
> 1. `issue-triage.yml` — авто-парсинг issues с запросами моделей через GitHub Models API → создание файлов + меток
> 2. `pages-deploy.yml` — генерация и публикация статьи на GitHub Pages (`https://a-m-e-n-t-e-t.github.io/SkyNet/`)
> 3. `branch-protection-setup.yml` — настройка Branch Protection на main + ежедневный drift detection
> 4. `release-creator.yml` — авто-релизы на тегах v* с changelog и package assets
> 5. `codeql-analysis.yml` — статический анализ `scripts/*.py` (security-extended + security-and-quality)
>
> **Новые config-файлы (3):**
> 6. `.github/dependabot.yml` — авто-обновление pip + github-actions deps (weekly, grouped)
> 7. `.github/CODEOWNERS` — auto-assign reviewer для каждого раздела репо
> 8. `.github/PULL_REQUEST_TEMPLATE.md` — шаблон PR с чек-листом метрик (F3, F4, F5, F37, F43, F47, F70)
>
> **Шаблоны Issues (3 + config):**
> - `ISSUE_TEMPLATE/model-request.md` — запрос новой модели с триггером для `issue-triage.yml`
> - `ISSUE_TEMPLATE/bug-report.md` — bug report с метриками
> - `ISSUE_TEMPLATE/hypothesis.md` — гипотеза (P039)
> - `ISSUE_TEMPLATE/q-and-a.md` — вопрос
> - `ISSUE_TEMPLATE/config.yml` — отключает blank issues, добавляет contact links
>
> 📊 **ИТОГО GITHUB-АВТОМАТИЗАЦИЯ v9.21:**
>
> | Категория | Кол-во | Файлы |
> |---|---:|---|
> | GitHub Actions workflows | 11 | phase0-init, pre-commit-checks, batch-process, sync-check, telemetry-update, sync-alice-concepts, issue-triage, pages-deploy, branch-protection-setup, release-creator, codeql-analysis |
> | Dependabot config | 1 | dependabot.yml (pip + github-actions + docker) |
> | CODEOWNERS | 1 | 28 path-правил |
> | PR Template | 1 | PULL_REQUEST_TEMPLATE.md с чек-листом метрик |
> | Issue Templates | 4 + config | model-request, bug-report, hypothesis, q-and-a |
> | **Всего** | **18 файлов** | в `.github/` |
>
> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**
>
> Промпт сжат с **8881 до ~5888 строк (-34%)** через вынос в 4 отдельных файла:'''

    text = text.replace(old_block, new_block)
    print("✓ Header changelog updated")
else:
    print("✗ Block not found")

# Update file_system comment
text = text.replace(
    "    file_system: ${WORK_DIR}/  # v9.20: path from environment; sandbox=/home/z/my-project, GitHub Actions runner=/home/runner/work/SkyNet/SkyNet",
    "    file_system: ${WORK_DIR}/  # v9.21: path from environment; sandbox=/home/z/my-project, GitHub Actions runner=/home/runner/work/SkyNet/SkyNet"
)

# Update rules_version expected to 9.21
text = text.replace(
    '"expected": "9.20",  # v9.20',
    '"expected": "9.21",  # v9.21'
)

# Update final commit message
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): инициализация структуры SkyNet v9.20`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): инициализация структуры SkyNet v9.21 + 14 workflows + 8 configs`."
)

text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.20`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.21`."
)

text = text.replace(
    "0.10 Коммит инициализации | ❌ | `chore(скелет): инициализация структуры SkyNet v9.20 + Workflows`",
    "0.10 Коммит инициализации | ❌ | `chore(скелет): инициализация структуры SkyNet v9.21 + 14 workflows + 8 configs`"
)

text = text.replace(
    "0.9 **Создать `.github/workflows/` (6 файлов, v9.20 НОВОЕ)** | ❌ | `phase0-init.yml`, `pre-commit-checks.yml`, `batch-process.yml`, `sync-check.yml`, `telemetry-update.yml`, `sync-alice-concepts.yml` — см. Layer 3 §W (v9.20)",
    "0.9 **Создать `.github/workflows/` (11 файлов) + `.github/` configs (7 файлов, v9.21 РАСШИРЕНО)** | ❌ | **11 workflows:** `phase0-init.yml`, `pre-commit-checks.yml`, `batch-process.yml`, `sync-check.yml`, `telemetry-update.yml`, `sync-alice-concepts.yml`, `issue-triage.yml`, `pages-deploy.yml`, `branch-protection-setup.yml`, `release-creator.yml`, `codeql-analysis.yml` + **7 configs:** `dependabot.yml`, `CODEOWNERS`, `PULL_REQUEST_TEMPLATE.md`, `ISSUE_TEMPLATE/model-request.md`, `ISSUE_TEMPLATE/bug-report.md`, `ISSUE_TEMPLATE/hypothesis.md`, `ISSUE_TEMPLATE/q-and-a.md` — см. Layer 3 §W (v9.21)"
)

SRC.write_text(text, encoding="utf-8")
print(f"✓ v9.21.md сохранён ({len(text)} байт, {text.count(chr(10))+1} строк)")

# Verify
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.21",
    "version: 9.21",
    "5 столпов архитектуры v9.21",
    "11 workflows",
    "issue-triage.yml",
    "pages-deploy.yml",
    "branch-protection-setup.yml",
    "release-creator.yml",
    "codeql-analysis.yml",
    "dependabot.yml",
    "CODEOWNERS",
    "PULL_REQUEST_TEMPLATE.md",
    "ISSUE_TEMPLATE/model-request.md",
    "v9.21: path from environment",
    '"expected": "9.21"',
]
print("\n=== Проверка ===")
for c in checks:
    ok = "✓" if c in text else "✗"
    print(f"  {ok} {c[:60]}")
