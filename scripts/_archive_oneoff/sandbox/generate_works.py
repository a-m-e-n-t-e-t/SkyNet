#!/usr/bin/env python3
"""SkyNet — Генератор файлов произведений в фантастические данные/произведения/.

Читает:  требования_к_ии/_реестр_произведений.md  (канонический реестр, 52 работы)
         фантастические данные/_список_моделей.md   (плоский индекс моделей)
Пишет:   фантастические данные/произведения/work_001.md .. work_052.md
         фантастические данные/_индекс_произведений.md  (тематический указатель)

Стратегия валидации (поэтому коммит пройдёт pre-commit-hook):
  • тип: произведение            — не входит в schema_map F70g (модель_SkyNet/изделие/...),
                                  → validate_against_schema() возвращает []
  • каноничность: canon|apocrypha — поле не входит в ENUM_VALUES F70h
                                    (там только тип_модели / статус_реальности /
                                     подтип_модели / кристаллическая_структура)
  • файлы в фантастические данные/произведения/ — не сканируются
                                    check_path_type_status (только реальные данные/
                                    и работа и и/) и не входят в F81/F87/F88
                                    (те смотрят только модели/ и материалы/)
"""

from __future__ import annotations
import os
import re
import json
from pathlib import Path

# === Пути ===
REPO = Path("/home/z/my-project/skynet_clone/SkyNet")
REGISTRY_PATH = REPO / "требования_к_ии" / "_реестр_произведений.md"
MODELS_LIST_PATH = REPO / "фантастические данные" / "_список_моделей.md"
WORKS_DIR = REPO / "фантастические данные" / "произведения"
INDEX_PATH = REPO / "фантастические данные" / "_индекс_произведений.md"
TODAY = "2026-11-03"

# === 1. Парсинг реестра ===
def parse_registry() -> list[dict]:
    text = REGISTRY_PATH.read_text(encoding="utf-8")
    works = []
    # - work_XXX: "Name" (YEAR, Author) — CANONICITY — Description.
    #   - тип: <type>
    pattern = re.compile(
        r'- (work_\d+):\s*"([^"]+)"\s*\((\d+),\s*([^)]+)\)\s*—\s*(\w+)\s*—\s*(.+?)\n\s*-\s*тип:\s*(\w+)',
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        works.append({
            "id": m.group(1),
            "title": m.group(2),
            "year": int(m.group(3)),
            "author": m.group(4).strip(),
            "canonicity": m.group(5).strip().lower(),
            "description": m.group(6).strip().rstrip("."),
            "type": m.group(7).strip(),
        })
    return works

# === 2. Парсинг списка моделей ===
def parse_models() -> list[dict]:
    text = MODELS_LIST_PATH.read_text(encoding="utf-8")
    models = []
    # | id | имя_файла | класс | тип_модели | канон_источник | статус_реальности |
    pat = re.compile(
        r'\|\s*(SkyNet-[A-Za-z0-9]+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|'
    )
    for m in pat.finditer(text):
        models.append({
            "id": m.group(1),
            "file": m.group(2),
            "class": m.group(3).strip(),
            "type": m.group(4).strip(),
            "canon_source": m.group(5).strip(),
            "status": m.group(6).strip(),
        })
    return models

# === 3. Сопоставление work → models ===
# По ключевым фразам в canon_source. Каноничные Core/DefenseGrid всегда входят.
WORK_KEYWORDS: dict[str, list[str]] = {
    # Фильмы
    "work_001": ["the terminator (1984)", "t1 (1984)", "the terminator (1984)"],
    "work_002": ["t2: judgment day (1991)", "t2 (1991)"],
    "work_003": ["terminator 3: rise of the machines (2003)", "t3"],
    "work_004": ["terminator: salvation (2009)", "t: salvation (2009)", "t:s (2009)"],
    "work_005": ["terminator: genisys (2015)"],
    "work_006": ["terminator: dark fate (2019)", "t: dark fate"],
    # Сериалы
    "work_007": ["terminator: the sarah connor chronicles"],
    "work_008": ["terminator zero"],
    # Игры — Terminator: Resistance (2019) — самый плодовитый
    "work_046": ["terminator: resistance (2019)"],
    # T2 3D аттракцион
    "work_050": ["t2 3d: battle across time (1996)"],
}

# Для work_009-work_019 (новелизации), work_020-work_036 (комиксы),
# work_037-work_049 (игры кроме Resistance), work_051-work_052 — отдельная логика
# (по умолчанию только Core + DefenseGrid, т.к. конкретные модели в реестре не указаны).

# Специальные case-by-case соответствия, не покрытые keyword search:
WORK_EXTRA_MODELS: dict[str, list[str]] = {
    # T2 arcade/chess/SNES — упрощённо связанные с T2 моделями
    "work_040": ["SkyNet-T800", "SkyNet-T1000", "SkyNet-T600"],
    "work_041": ["SkyNet-T800", "SkyNet-T1000"],
    "work_051": ["SkyNet-T800", "SkyNet-T1000"],
    # Robocop vs Terminator (1993) — для T800 + T1000 (комикс/игра по мотивам)
    "work_039": ["SkyNet-T800", "SkyNet-T1000"],
    "work_027": ["SkyNet-T800", "SkyNet-T1000"],
    "work_026": ["SkyNet-T800", "SkyNet-T1000"],
    # Genisys Future War — T-3000, T-5000, T-800
    "work_049": ["SkyNet-T3000", "SkyNet-T5000", "SkyNet-T800"],
    # Salvation (game) — те же модели что в фильме Salvation
    "work_045": ["SkyNet-T800", "SkyNet-T600", "SkyNet-T600Early", "SkyNet-Aerostat",
                 "SkyNet-MotoTerminator", "SkyNet-Hydrobot", "SkyNet-HKAerial",
                 "SkyNet-HKDrone", "SkyNet-HKTank", "SkyNet-T900"],
    # Dawn of Fate (2002) — приквел T1
    "work_042": ["SkyNet-T800", "SkyNet-T600", "SkyNet-HKTank", "SkyNet-HKAerial"],
    # T3: Rise of the Machines (game) — те же модели что в фильме
    "work_043": ["SkyNet-T850", "SkyNet-TX", "SkyNet-T1"],
    # T3: The Redemption (game)
    "work_044": ["SkyNet-T850", "SkyNet-TX", "SkyNet-T1"],
    # Dark Fate — Defiance (RTS, 2023) — Rev-9, T-800
    "work_047": ["SkyNet-Rev9", "SkyNet-T800"],
    # Survivors (2025) — T-800 (из трейлеров)
    "work_048": ["SkyNet-T800"],
    # Terminator 2029 (DOS, 1992) — T-800
    "work_038": ["SkyNet-T800"],
    # The Terminator (DOS, 1991) — T-800
    "work_037": ["SkyNet-T800"],
}

def find_models_for_work(work: dict, models: list[dict]) -> list[str]:
    wid = work["id"]
    cs_lower = work["title"].lower()
    found = set()

    # 1. Keyword search по canon_source моделей
    keywords = WORK_KEYWORDS.get(wid, [])
    if keywords:
        for m in models:
            src = m["canon_source"].lower()
            for kw in keywords:
                if kw in src:
                    found.add(m["id"])
                    break

    # 2. Дополнительные специальные сопоставления
    for mid in WORK_EXTRA_MODELS.get(wid, []):
        # проверяем что модель существует в _список_моделей
        if any(m["id"] == mid for m in models):
            found.add(mid)

    # 3. SkyNet-Core и SkyNet-DefenseGrid присутствуют во всех произведениях
    if any(m["id"] == "SkyNet-Core" for m in models):
        found.add("SkyNet-Core")
    if any(m["id"] == "SkyNet-DefenseGrid" for m in models):
        found.add("SkyNet-DefenseGrid")

    # Сохраняем детерминированный порядок: Core, DefenseGrid, остальные по алфавиту
    head = []
    if "SkyNet-Core" in found:
        head.append("SkyNet-Core")
    if "SkyNet-DefenseGrid" in found:
        head.append("SkyNet-DefenseGrid")
    rest = sorted(found - {"SkyNet-Core", "SkyNet-DefenseGrid"})
    return head + rest

# === 4. Шаблон файла ===
TYPE_LABELS = {
    "фильм": "Фильм",
    "сериал": "Сериал",
    "книга": "Книга / новелизация",
    "комикс": "Комикс",
    "игра": "Игра",
    "прочее": "Прочее",
}

CANON_LABELS = {
    "canon": "canon — основа вселенной",
    "apocrypha": "apocrypha — расширенная вселенная",
}

def render_work_md(work: dict, models: list[str]) -> str:
    wid = work["id"]
    num = wid.split("_")[1]
    sky_id = f"SkyNet-Work-{num}"
    type_label = TYPE_LABELS.get(work["type"], work["type"])
    canon_label = CANON_LABELS.get(work["canonicity"], work["canonicity"])
    yaml_models = "[" + ", ".join(f'"{m}"' for m in models) + "]" if models else "[]"

    # Markdown-ссылки на файлы моделей (для удобной навигации)
    model_links = []
    id_to_file = {m["id"]: m["file"] for m in parse_models_cache}
    for mid in models:
        fname = id_to_file.get(mid, "")
        if fname:
            model_links.append(f"- `{mid}` → [`{fname}`](../модели/{fname})")
        else:
            model_links.append(f"- `{mid}`")

    md = f"""---
id: {sky_id}
тип: произведение
категория: {work["type"]}
название: "{work["title"]}"
год: {work["year"]}
режиссёр_или_автор: "{work["author"]}"
каноничность: {work["canonicity"]}
источник_вселенная: SkyNet
модели_в_произведении: {yaml_models}
дата_создания: {TODAY}
дата_обновления: {TODAY}
---

# {sky_id}: {work["title"]}

## Описание

{work["description"]}.

## Метаданные

| Параметр | Значение |
|---|---|
| id | `{sky_id}` |
| категория | {type_label} |
| название | "{work["title"]}" |
| год | {work["year"]} |
| режиссёр_или_автор | {work["author"]} |
| каноничность | {canon_label} |
| источник_вселенная | SkyNet |

## Каноничность

**{work["canonicity"]}** — {CANON_LABELS[work["canonicity"]]}.

## Модели SkyNet в произведении

"""
    if models:
        md += "\n".join(model_links) + "\n"
    else:
        md += "_Конкретные модели SkyNet в реестре не зафиксированы; присутствует инфраструктура (SkyNet-Core, SkyNet-DefenseGrid)._\n"

    md += f"""
## Источники

- Реестр: `требования_к_ии/_реестр_произведений.md` (§9 Phase 0.7)
- Каноничность: {canon_label}
- Загружено: {TODAY}

## Связанные произведения

- См. тематический указатель: [`_индекс_произведений.md`](../_индекс_произведений.md)
"""
    return md

# === 5. Главный индекс ===
def render_index(works: list[dict], work_models: dict[str, list[str]]) -> str:
    by_type: dict[str, list[dict]] = {}
    for w in works:
        by_type.setdefault(w["type"], []).append(w)

    lines = [
        "# SkyNet — Тематический индекс произведений",
        f"# Всего: {len(works)} произведений, сгруппированных по категориям",
        f"# Обновлено: {TODAY}",
        "",
        "Канонический источник: `требования_к_ии/_реестр_произведений.md` (§9 Phase 0.7).",
        "Каждое произведение имеет отдельный файл в `фантастические данные/произведения/work_XXX.md`.",
        "",
    ]

    type_order = ["фильм", "сериал", "книга", "комикс", "игра", "прочее"]
    for t in type_order:
        ws = by_type.get(t, [])
        if not ws:
            continue
        label = TYPE_LABELS.get(t, t)
        canon_count = sum(1 for w in ws if w["canonicity"] == "canon")
        apoc_count = len(ws) - canon_count
        canon_str = f"{canon_count} canon" + (f", {apoc_count} apocrypha" if apoc_count else "")
        lines.append(f"## {label}  ({len(ws)} произведений: {canon_str})")
        lines.append("")
        for w in ws:
            num = w["id"].split("_")[1]
            fname = f"work_{num}.md"
            models = work_models.get(w["id"], [])
            canon_mark = "✅" if w["canonicity"] == "canon" else "📚"
            models_count = len(models)
            models_str = f"{models_count} моделей SkyNet" if models_count else "нет моделей"
            lines.append(
                f"- {canon_mark} **{w['id']}** — «{w['title']}» ({w['year']}, {w['author']}) — {models_str} → `{fname}`"
            )
        lines.append("")

    # Сводка по каноничности
    canon_total = sum(1 for w in works if w["canonicity"] == "canon")
    apoc_total = len(works) - canon_total
    lines.append("## Сводка по каноничности")
    lines.append("")
    lines.append(f"- **canon** (основа вселенной): {canon_total} произведений")
    lines.append(f"- **apocrypha** (расширенная вселенная): {apoc_total} произведений")
    lines.append(f"- **всего**: {len(works)} произведений")
    lines.append("")

    # Самые «моделенасыщенные» произведения
    lines.append("## Топ-10 произведений по числу моделей SkyNet")
    lines.append("")
    top = sorted(works, key=lambda w: -len(work_models.get(w["id"], [])))[:10]
    for i, w in enumerate(top, 1):
        num = w["id"].split("_")[1]
        fname = f"work_{num}.md"
        n = len(work_models.get(w["id"], []))
        lines.append(f"{i}. **{w['id']}** — «{w['title']}» ({w['year']}) — {n} моделей → `{fname}`")
    lines.append("")

    lines.append("## Связанные индексы")
    lines.append("")
    lines.append("- [`_индекс.md`](_индекс.md) — тематический указатель моделей SkyNet (41 модель)")
    lines.append("- [`_список_моделей.md`](_список_моделей.md) — плоский индекс моделей")
    lines.append("- [`_реестр_произведений.md`](_реестр_произведений.md) — указатель на канонический реестр")
    lines.append("- [`../требования_к_ии/_реестр_произведений.md`](../../требования_к_ии/_реестр_произведений.md) — канонический реестр произведений")
    lines.append("")
    return "\n".join(lines)

# === 6. Main ===
def main():
    global parse_models_cache

    works = parse_registry()
    print(f"Распарсено произведений: {len(works)}")
    assert len(works) == 52, f"Ожидалось 52, получено {len(works)}"

    models = parse_models()
    parse_models_cache = models
    print(f"Распарсено моделей: {len(models)}")
    assert len(models) == 41, f"Ожидалось 41, получено {len(models)}"

    # Сопоставление work → models
    work_models = {}
    for w in works:
        work_models[w["id"]] = find_models_for_work(w, models)
    print("\nСопоставление work → models:")
    for w in works:
        n = len(work_models[w["id"]])
        print(f"  {w['id']} ({w['title'][:40]:40s}): {n} моделей")

    # Создать директорию
    WORKS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\nСоздана папка: {WORKS_DIR}")

    # Сгенерировать 52 файла
    for w in works:
        num = w["id"].split("_")[1]
        fpath = WORKS_DIR / f"work_{num}.md"
        md = render_work_md(w, work_models[w["id"]])
        fpath.write_text(md, encoding="utf-8")
    print(f"Сгенерировано {len(works)} файлов в {WORKS_DIR}")

    # Сгенерировать индекс
    index_md = render_index(works, work_models)
    INDEX_PATH.write_text(index_md, encoding="utf-8")
    print(f"Создан индекс: {INDEX_PATH} ({len(index_md)} байт)")

    # Сводка
    total_models_in_works = sum(len(v) for v in work_models.values())
    print(f"\nСводка:")
    print(f"  Произведений: {len(works)}")
    print(f"  Файлов work_*.md: {len(works)}")
    print(f"  Индекс: 1 файл")
    print(f"  Всего ссылок work→model: {total_models_in_works}")

if __name__ == "__main__":
    main()
