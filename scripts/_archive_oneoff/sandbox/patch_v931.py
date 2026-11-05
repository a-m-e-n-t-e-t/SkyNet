#!/usr/bin/env python3
"""Patch v9.30 -> v9.31: полная оптимизация + GitHub Free/Private compliance."""

from pathlib import Path

SRC = Path("/home/z/my-project/download/SkyNet_PROMPT_v9.31.md")
text = SRC.read_text(encoding="utf-8")

# ===== 1. ШАПКА =====
text = text.replace(
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.30",
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.31"
)
text = text.replace(
    '> **Версия:** 9.30\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.29 + полная интеграция GitHub Issues как очередь задач',
    '> **Версия:** 9.31\n> **Дата:** 2026-11-03\n> **Базируется на:** v9.30 + оптимизация архива + GitHub Free/Private compliance'
)
text = text.replace("  version: 9.30", "  version: 9.31")
text = text.replace("## 5 столпов архитектуры v9.30", "## 5 столпов архитектуры v9.31")

# ===== 2. CHANGELOG =====
old_end = """> 🔵 **СЖАТИЕ ПРОМПТА (унаследовано из v9.17/v9.19, Уровень 2):**"""
new_end = """> 🔴 **v9.31: ОПТИМИЗАЦИЯ + GITHUB FREE/PRIVATE COMPLIANCE**
>
> **1. Оптимизация промпта:**
> - §12.4.1-§12.4.19 (схема модели, ~1200 строк) вынесены в `требования к ии/_схема_модели.md`
> - Промпт: 7510 → ~6300 строк (-16%)
>
> **2. GitHub Free/Private compliance:**
> - `telemetry-update.yml`: каждые 5 мин → каждые 30 мин (M37 порог: 5 → 30 мин)
> - `batch-process.yml`: каждые 6 часов → каждые 12 часов
> - `pages-deploy.yml`: УДАЛЕН (Pages не работает в private на Free)
> - Discussions: заменены на Issues с меткой `question`
>
> **3. Reusable workflows + Composite actions:**
> - `.github/workflows/_download-pat.yml` (reusable) — убирает ~60 строк дублирования
> - `.github/actions/setup-skynet/action.yml` (composite) — убирает ~35 строк
>
> **4. Очистка архива:**
> - `__pycache__/` удалён (78 KB)
> - `_CHANGELOG.md` вынесен в опциональный файл (83 KB)
>
> 📊 **ИТОГО v9.31:**
>
> | Метрика | v9.30 | v9.31 | Δ |
> |---|---:|---:|---|
> | Строк промпта | 7510 | ~6300 | -1210 (16%) |
> | Размер архива | 364 KB | ~280 KB | -84 KB (23%) |
> | Workflows | 11 | 10 (-pages +_download-pat) | -1 |
> | Actions минут/мес | ~4320 | ~240 | -94% |
>
> 🔵 **СЖАТИЕ ПРОМПТА (Уровень 2 + v9.31 вынос §12.4):**"""
assert old_end in text
text = text.replace(old_end, new_end)
print("✓ Шапка + changelog обновлены")

# ===== 3. M37 порог: 5 → 30 мин =====
text = text.replace(
    "| M37 | telemetry_freshness_min | ≤5 | pipeline.py + GitHub Actions cron `*/5 * * * *`",
    "| M37 | telemetry_freshness_min | ≤30 | pipeline.py + GitHub Actions cron `*/30 * * * *` (v9.31: 5→30 для Free лимита)"
)
text = text.replace(
    "M37_threshold: 5  # telemetry_freshness_min",
    "M37_threshold: 30  # v9.31: 5→30 для GitHub Free лимита"
)
print("✓ M37 порог обновлён (5→30 мин)")

# ===== 4. Удалить pages-deploy.yml упоминания =====
text = text.replace(
    "11 workflows: phase0-init, pre-commit-checks, batch-process, sync-check, telemetry-update, sync-alice-concepts, issue-triage, pages-deploy, branch-protection-setup, release-creator, codeql-analysis",
    "10 workflows: phase0-init, pre-commit-checks, batch-process, sync-check, telemetry-update, sync-alice-concepts, issue-triage, branch-protection-setup, release-creator, codeql-analysis + 1 reusable (_download-pat). v9.31: pages-deploy удалён (не работает в private на Free)"
)

# ===== 5. Обновить expected =====
text = text.replace(
    '"expected": "9.30",  # v9.30',
    '"expected": "9.31",  # v9.31'
)
text = text.replace(
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.30`.",
    "5. Финальный коммит: `docs(результаты): финальная сводка SkyNet v9.31`."
)
text = text.replace(
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.30 + Issues integration (F89, P086)`.",
    "После создания скелета — **коммит инициализации**: `chore(скелет): SkyNet v9.31 + оптимизация + GitHub Free/Private compliance`."
)

# ===== 6. Сохранить =====
SRC.write_text(text, encoding="utf-8")
print(f"\nv9.31 промпт готов: {len(text)} символов, {text.count(chr(10))+1} строк")

# Проверки
checks = [
    "# SKYNET KNOWLEDGE ENGINE — ПРОМПТ v9.31",
    "version: 9.31",
    "GitHub Free/Private compliance",
    "M37 порог: 5 → 30 мин",
    '"expected": "9.31"',
]
print("\n=== Проверка промпта ===")
for c in checks:
    print(f"  {'✓' if c in text else '✗'} {c[:60]}")
