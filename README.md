# SkyNet Knowledge Engine — Package v9.31

> **Версия промпта:** 9.31 (2026-11-03)
> **Базируется на:** v9.30 + оптимизация + GitHub Free/Private compliance

## Обновление v9.39.3 (2026-11-05) — cron-агент: гибридное stale-detection

> Заменил Job 504688 (30-мин порог) на Job **504891** с гибридным правилом анти-параллельной блокировки:

| Правило | Старое (504688) | Новое (504891) |
|---|---|---|
| Stale-порог | 30 мин жёстко | 30 мин **ИЛИ** (10 мин + нет активности) |
| Холостые циклы при зависании | ~6 циклов (~30 мин потеряно) | ~2 цикла (~10 мин потеряно) |
| Риск прерывания активного batch | — | нет (требуется отсутствие коммитов/комментариев) |
| Покрытие batch | — | до ~10 файлов (~9 мин работы) |

**Логика stale** (пункт 1 протокола): если возраст метки `in-progress` > 30 МИН → снять. Иначе если > 10 МИН **И** нет событий `commented`/`closed` в timeline **И** нет коммитов в `git log --since=<timestamp>` → снять (деградировавший инстанс). Иначе — цикл активен, не вмешиваться.

> Payload cron-job — единственный источник правды протокола (PROMPT v9.31 не дублирует). Batch-по-изделию сохранён: `scripts/web_verify.py apply-batch` (YAML spec → 1 web_search на родителя → batch-коммит).

### Почему НЕ расширен фазой F13

F13 (покрытие подсистем, 0.80, 4 нарушения) требует **канонических структурных решений** — создания новых изделий-подсистем (`система_передвижения`, `система_питания` для 4 гуманоидных моделей T700/T900/T950/TRIP), а не web_search + file-edit. Слияние с verify-task:

| Аргумент против | Обоснование |
|---|---|
| Природа задачи | web_search (verify-task) ≠ каноническая декомпозиция (F13) |
| Длина цикла | F13-проход добавил бы 10–20 мин → риск пересечения 10-мин stale-порога |
| Контекст | F13 требует архитектурного решения пользователя (какие именно изделия добавить), не автоматизируется |
| Anti-parallel lock | Смешение двух типов задач в одном lock увеличивает время ожидания |

**Решение:** F13 выводится в отдельный backlog (issue-трекер) и решается разовым архитектурным патчем, не cron-агентом. Cron Job 504891 фокусируется на verify-task (F22/F23/F25).

## Обновление v9.36 (2026-11-05) — аудит и оптимизация CI/скриптов

> Историческая таблица ниже описывает состояние v9.31 и больше не отражает реальность. Текущее:

| Workflow | Статус |
|---|---|
| verify_decomposition | активен: единый модуль `scripts/_dedup_keys.js` (фикс ложного auto-close F26), пагинация issues, schedule каждые 3 ч |
| telemetry-update | активен: M37_THRESHOLD 35 мин (было 5 → ~48 ложных issues/сутки), дедуп + авто-закрытие stale-telemetry, pull --rebase, concurrency, cron :07/:37 |
| issue-triage | активен: санитизация LLM-вывода (prompt-injection → RCE закрыт), фильтр меток, concurrency, `github.repository` |
| pre-commit-checks | активен: path-фильтры push-триггера |
| sync-alice-concepts | активен: исправлен каталог `требования_к_ии` (была теневая директория с пробелами), `[skip ci]` |
| branch-protection-setup | dispatch-only: ежедневный 403-no-op прогон удалён, фантомные проверки build/deploy убраны |
| batch-process, phase0-init, _download-pat, release-creator | **удалены** (мёртвые/no-op; первые три скачивали публичный PAT) |
| sync-check | активен (F47); известное ограничение: в CI-окружении проверка тавтологична |

⚠️ **SECURITY:** в трёх удалённых воркфлоу был захардкожен публичный Yandex Disk-файл с GitHub PAT. Токен рекомендуется **отозвать/ротировать** и при необходимости перенести в repo secrets.

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
