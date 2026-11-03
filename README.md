# SkyNet Knowledge Engine — Package v9.31

> **Версия промпта:** 9.31 (2026-11-03)
> **Базируется на:** v9.30 + оптимизация + GitHub Free/Private compliance

## Что нового в v9.31

### 1. Оптимизация архива

| Что | Было | Стало | Δ |
|---|---|---|---|
| `__pycache__/` | 78 KB | 0 | -78 KB |
| `_CHANGELOG.md` | в основном пакете | вынесен в `optional/` | -83 KB |
| `pages-deploy.yml` | 11 KB | удалён | -11 KB |
| Дублирование PAT | 3 × ~30 строк | 1 reusable | -60 строк |
| Дублирование install | 6 × ~5 строк | 1 composite | -25 строк |
| **Архив** | **364 KB** | **~280 KB** | **-84 KB (23%)** |

### 2. GitHub Free/Private compliance

| Workflow | v9.30 | v9.31 | Мин/мес |
|---|---|---|---|
| telemetry-update | */5 мин | */30 мин | 4320→24 |
| batch-process | 6ч | 12ч | 120→60 |
| pages-deploy | на push | удалён | 0 |
| **Итого Actions** | ~4320 | **~240** | -94% (в пределах 2000 Free) |

### 3. Reusable + Composite

- `.github/workflows/_download-pat.yml` (reusable) — один код для PAT
- `.github/actions/setup-skynet/action.yml` (composite) — checkout+python+install

### Структура

```
v9.31_pack/
├── SkyNet_PROMPT_v9.31.md          7539 строк
├── README.md
├── .gitignore                      (+ __pycache__/)
├── .github/
│   ├── workflows/                   10 .yml (-pages +_download-pat)
│   ├── actions/setup-skynet/        composite action (НОВОЕ)
│   ├── ISSUE_TEMPLATE/              7 templates
│   ├── CODEOWNERS
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── scripts/                         10 .py (без __pycache__)
├── требования_к_ии/                16 файлов (-_CHANGELOG.md)
├── optional/                        _CHANGELOG_v9.31.md (опциональный)
├── гипотезы/ улучшения/ диалог/ концепции/ архив/
```

