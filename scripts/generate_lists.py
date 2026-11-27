#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SkyNet — генератор и сверщик сводных списков базы знаний (шаблоны №10–19).

Использование:
  python3 scripts/generate_lists.py [КОРЕНЬ]          # обновить списки в КОРНЕ базы знаний
  python3 scripts/generate_lists.py --check [КОРЕНЬ]  # CI-сверка списков с карточками (exit 1 при расхождении)

КОРЕНЬ по умолчанию — родитель папки scripts/ (клон базы знаний).
Генерирует/сверяет 14 сводных файлов:
  реальные данные/материалы/_список_материалов.md    + зеркало работа и и/материалы/
  реальные данные/изделия/_список_изделий.md         + зеркало работа и и/изделия/
  реальные данные/изделия/_список_частей.md
  реальные данные/технологии/_список_технологий.md   + зеркало работа и и/технологии/
  реальные данные/стандарты/_список_стандартов.md
  реальные данные/исследовательские_группы/_список_исследовательских_групп.md
  фантастические данные/_список_моделей.md
  фантастические данные/произведения/_список_произведений.md
  фантастические данные/материалы/_список_фантастических_материалов.md
  результаты/модели/_список_реализаций.md
  _сводный_реестр.md (корень)

Правила (шаблоны/шаблон_списка_*.md, шаблоны/шаблон_сводного_реестра.md):
  • список = только навигация (F26): id/название/путь + навигационные колонки;
  • счётчики — в front matter (машиночитаемо; сумма секций = «всего»);
  • все секции классификационного enum присутствуют, включая пустые «(0)»;
  • сортировка — по алфавиту id (произведения — по номеру work_NNN);
  • генератор обновляет списки в том же коммите, что и карточки зоны.
Поле «генератор» в каждом списке указывается честно; списки с генератором
«вручную» в --check сверяются только по вхождению id карточек зоны.
"""
from __future__ import annotations

import datetime as _dt
import pathlib
import re
import sys

import yaml

GENERATOR = "scripts/generate_lists.py"
TODAY = _dt.date.today().isoformat()

KLASSY_MATERIALOV = ["металл", "сплав", "керамика", "полупроводник", "полимер",
                     "композит", "радиоизотоп", "прочее"]
PODSISTEMY = ["вычислительная", "энергетическая", "каркас", "броня", "маскировка",
              "встроенное_оружие", "сенсоры", "приводная_система", "система_связи",
              "навигация", "система_охлаждения", "система_питания",
              "система_передвижения", "прочее"]
KATEGORII_TEHNOLOGII = ["обработка", "сборка", "испытание", "модификация", "прочее"]
TIPY_MODELEI = ["стационарный", "гуманоидный", "воздушный", "наземный_гусеничный",
                "наземный_колёсный", "водный_надводный", "водный_подводный"]
KATEGORII_STANDARTOV = ["промышленный_стандарт", "прочее"]
KATEGORII_PROIZVEDENII = ["фильм", "сериал", "игра", "книга", "комикс", "HTML-концепция"]
TIPY_REALIZACII = [("реальная реализация", "реальная"),
                   ("фантастическая реализация", "фантастическая"),
                   ("доработанная ии реализация", "доработанная_ии")]


# ─────────────────────────── базовые утилиты ───────────────────────────

def read_frontmatter(path: pathlib.Path):
    """YAML front matter (блок между 1-й и 2-й строкой «---»); None при отсутствии/ошибке."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            try:
                return yaml.safe_load("\n".join(lines[1:i])) or {}
            except yaml.YAMLError:
                return None
    return None


def h1_title(path: pathlib.Path) -> str:
    """Первый заголовок «# …» файла (название карточки)."""
    try:
        m = re.search(r"^# (.+)$", path.read_text(encoding="utf-8"), flags=re.M)
    except OSError:
        m = None
    return m.group(1).strip() if m else ""


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def to_int(s) -> int:
    try:
        return int(str(s).strip())
    except (TypeError, ValueError):
        return 0


def norm(s) -> str:
    return str(s).strip().lower().replace(" ", "_")


def cell(v) -> str:
    """Значение ячейки Markdown-таблицы (экранирование «|», иначе ломается строка)."""
    return str(v).replace("|", "\\|")


# ─────────────────────────── обход базы знаний ───────────────────────────

def collect_cards(root: pathlib.Path) -> dict:
    cards = {k: [] for k in ("материал", "изделие", "часть", "технология", "стандарт",
                             "группа", "модель", "произведение", "реализация",
                             "фант_материал",
                             "ии_материал", "ии_технология", "ии_изделие")}

    def add(kind, path, domain):
        fm = read_frontmatter(path)
        if not isinstance(fm, dict):
            return
        cards[kind].append({"path": path, "fm": fm, "domain": domain,
                            "id": str(fm.get("id") or ""), "title": h1_title(path)})

    rd = root / "реальные данные"
    for zone, kind in (("материалы", "материал"), ("технологии", "технология"),
                       ("стандарты", "стандарт"),
                       ("исследовательские_группы", "группа")):
        zone_dir = rd / zone
        if zone_dir.is_dir():
            for p in sorted(zone_dir.glob("*.md")):
                if not p.name.startswith("_"):
                    add(kind, p, "реальные данные")

    izd = rd / "изделия"
    if izd.is_dir():
        for p in sorted(izd.rglob("*.md")):
            if p.name.startswith("_") and p.name != "_index.md":
                continue
            fm = read_frontmatter(p)
            if not isinstance(fm, dict):
                continue
            rid = str(fm.get("id") or "")
            # часть — по любому признаку (§12.6): id-префикс, родитель, уровень 2–4
            # или плоский файл <часть>.md; изделие верхнего уровня — _index.md без родителя
            is_part = (rid.startswith("часть_") or bool(fm.get("родитель"))
                       or to_int(fm.get("уровень_номер")) > 1 or p.name != "_index.md")
            cards["часть" if is_part else "изделие"].append(
                {"path": p, "fm": fm, "domain": "реальные данные",
                 "id": rid, "title": h1_title(p)})

    fd = root / "фантастические данные"
    for zone, kind in (("модели", "модель"), ("произведения", "произведение")):
        zone_dir = fd / zone
        if zone_dir.is_dir():
            for p in sorted(zone_dir.glob("*.md")):
                if not p.name.startswith("_"):
                    add(kind, p, "фантастические данные")
    fmat = fd / "материалы"
    if fmat.is_dir():
        for p in sorted(fmat.glob("*.md")):
            if not p.name.startswith("_"):
                add("фант_материал", p, "фантастические данные")

    wii = root / "работа и и"
    for zone, kind in (("материалы", "ии_материал"), ("технологии", "ии_технология")):
        zone_dir = wii / zone
        if zone_dir.is_dir():
            for p in sorted(zone_dir.glob("*.md")):
                if not p.name.startswith("_"):
                    add(kind, p, "работа и и")
    if (wii / "изделия").is_dir():
        # обёртки и части — папки с _index.md (+ плоские файлы часть_*.md);
        # сгенерированные списки (_список_*.md) карточками НЕ считаются
        for p in sorted((wii / "изделия").rglob("*.md")):
            if p.name.startswith("_") and p.name != "_index.md":
                continue
            fm = read_frontmatter(p)
            if not isinstance(fm, dict):
                continue
            rid = str(fm.get("id") or "")
            cards["ии_изделие"].append(
                {"path": p, "fm": fm, "domain": "работа и и",
                 "id": rid, "title": h1_title(p)})

    res = root / "результаты" / "модели"
    if res.is_dir():
        for p in sorted(res.rglob("_index.md")):
            # результаты/модели/<модель>/<тип> реализация/<имя>/_index.md — глубина 4
            if len(p.relative_to(res).parts) == 4:
                add("реализация", p, "результаты")
    return cards


def model_index(cards: dict, root: pathlib.Path) -> dict:
    """Индекс моделей: file_stem → {id, тип, категория, канон, N_произведений}.

    Источник 1 — карточки моделей (фантастические данные/модели/*.md).
    Источник 2 (карточек нет) — таблица существующего _список_моделей.md;
    старый формат v0 с колонкой «класс» читается по правилу миграции v3
    (класс → тип_модели).
    """
    idx: dict = {}
    for rec in cards["модель"]:
        fm = rec["fm"]
        idx[rec["path"].stem] = {
            "id": rec["id"] or f"SkyNet-{rec['path'].stem}",
            "тип": fm.get("тип_модели"),
            "категория": fm.get("категория"),
            "канон": fm.get("канон_источник", ""),
            "N_произведений": len(as_list(fm.get("произведения"))),
        }
    if not idx:
        p = root / "фантастические данные" / "_список_моделей.md"
        if p.is_file():
            text = p.read_text(encoding="utf-8")
            # тип модели из секций нового формата (## <тип> (N)) — таблица тип не несёт
            section_tip: dict[str, str] = {}
            cur_tip = None
            for ln in text.splitlines():
                m_sec = re.match(r"^## (\S+) \(\d+\)$", ln.strip())
                if m_sec:
                    cur_tip = m_sec.group(1)
                    continue
                if not ln.startswith("|"):
                    continue
                cells = [c.strip().replace("\\|", "|")
                         for c in ln.strip().strip("|").split("|")]
                if len(cells) < 6 or not cells[0].strip("`").startswith("SkyNet-"):
                    continue
                mid, fname = cells[0].strip("`"), cells[1].strip("`")
                stem = fname[:-3] if fname.endswith(".md") else fname
                if len(cells) >= 7:  # v0: id|файл|класс|тип_модели|канон|N|статус
                    tip_v0, klass_v0 = cells[3], cells[2]
                    kategor = None
                    if tip_v0 not in TIPY_MODELEI and klass_v0 in TIPY_MODELEI:
                        # миграция v0→v3: колонки переставлены — «жидкий_металл» и пр.
                        # это значения КАТЕГОРИИ, не тип_модели (§11.0)
                        tip_v0, kategor = klass_v0, tip_v0
                    idx[stem] = {"id": mid, "тип": tip_v0, "категория": kategor,
                                 "канон": cells[4], "N_произведений": to_int(cells[5])}
                else:               # новый: id|файл|категория|канон|N|обёртка_ии
                    idx[stem] = {"id": mid, "тип": section_tip.get(stem),
                                 "категория": cells[2],
                                 "канон": cells[3], "N_произведений": to_int(cells[4])}
                if cur_tip:
                    section_tip[stem] = cur_tip
                    idx[stem]["тип"] = cur_tip
    return idx


# ─────────────────────────── конструкторы списков ───────────────────────────

def fm_block(oxvat: str, domen: str, schetchiki: dict,
             tip: str = "список", versiya: str = "1.0") -> str:
    lines = ["---", "метаданные:", f"  версия_схемы: {versiya}",
             f"  тип_файла: {tip}", f"  генератор: {GENERATOR}",
             f"  охват: {oxvat}", f"  домен: {domen}", f"  обновлено: {TODAY}",
             "  счётчики:"]
    for k, v in schetchiki.items():
        lines.append(f"    {k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def checklist() -> str:
    return ("## Чек-лист (перед коммитом)\n\n"
            f"- [x] Список сгенерирован `{GENERATOR}`: счётчики = числу записей секций; сумма секций = `всего`.\n"
            "- [x] Каждая карточка зоны присутствует в списке; каждая запись ведёт к существующему файлу.\n"
            f"- [x] `обновлено` = {TODAY}; `генератор` = `{GENERATOR}` (честно).\n")


def page(title: str, blockquote: str, sections) -> str:
    return f"# {title}\n\n> {blockquote}\n\n" + "\n\n".join(sections) + "\n\n" + checklist()


def bullet_sections(recs, enum_values, field, rel_of=lambda r: r["path"].name):
    """Секции «- id — Название → путь» по enum; возвращает (тело, счётчики)."""
    schet = {"всего": len(recs)}
    sections = []
    for value in enum_values:
        rows = sorted((r for r in recs if str(r["fm"].get(field)) == value),
                      key=lambda r: r["id"])
        schet[value] = len(rows)
        body = ("\n".join(f"- `{r['id']}` — {r['title'] or r['id']} → `{rel_of(r)}`"
                          for r in rows) if rows else "- — нет —")
        sections.append(f"## {value} ({len(rows)})\n\n{body}")
    return sections, schet


def build_materials(recs):
    sections, schet = bullet_sections(recs, KLASSY_MATERIALOV, "класс")
    front = fm_block("реальные данные/материалы/", "реальные данные", schet)
    quote = ("**Единый источник данных.** Свойства, варианты структуры и цены — в карточках "
             "материалов (`material_<имя>.md`); GitHub отрендерит front matter таблицей. "
             "Список — только навигация: id, название, путь (F26).")
    return front, page("SkyNet — Список материалов", quote, sections)


def build_materials_mirror(recs):
    sections, _ = bullet_sections(recs, KLASSY_MATERIALOV, "класс")
    schet = {"всего": len(recs)}
    for value in KLASSY_MATERIALOV:
        schet[value] = sum(1 for r in recs if str(r["fm"].get("класс")) == value)
    front = fm_block("работа и и/материалы/", "работа и и", schet)
    quote = ("**Единый источник данных.** Свойства — в карточках-предках (`<оригинал>.md`, "
             "реальные данные/); обёртки — только дельты §12.7. Список — только навигация: "
             "id, название, путь (F26).")
    return front, page("SkyNet — Список материалов (зеркало: работа и и)", quote, sections)


def build_technologies(recs):
    sections, schet = bullet_sections(recs, KATEGORII_TEHNOLOGII, "категория")
    front = fm_block("реальные данные/технологии/", "реальные данные", schet)
    quote = ("**Единый источник данных.** Параметры режима, оборудование и материалы — "
             "в карточках технологий (`tekhnologia_<имя>.md`); GitHub отрендерит front matter "
             "таблицей. Список — только навигация: id, название, путь (F26).")
    return front, page("SkyNet — Список технологий", quote, sections)


def build_technologies_mirror(recs):
    sections, _ = bullet_sections(recs, KATEGORII_TEHNOLOGII, "категория")
    schet = {"всего": len(recs)}
    for value in KATEGORII_TEHNOLOGII:
        schet[value] = sum(1 for r in recs if str(r["fm"].get("категория")) == value)
    front = fm_block("работа и и/технологии/", "работа и и", schet)
    quote = ("**Единый источник данных.** Свойства — в карточках-предках (`<оригинал>.md`, "
             "реальные данные/); обёртки — только дельты §12.7. Список — только навигация: "
             "id, название, путь (F26).")
    return front, page("SkyNet — Список технологий (зеркало: работа и и)", quote, sections)


def build_products(recs, zone_dir, mirror=False):
    def rel(r):
        return str(r["path"].relative_to(zone_dir))
    sections, schet = bullet_sections(recs, PODSISTEMY, "подсистема", rel_of=rel)
    if mirror:
        for value in PODSISTEMY:
            schet[value] = sum(1 for r in recs if str(r["fm"].get("подсистема")) == value)
        front = fm_block("работа и и/изделия/", "работа и и", schet)
        quote = ("**Единый источник данных.** Свойства — в карточках-предках (реальные данные/); "
                 "обёртки и части — только дельты §12.7. Список — только навигация (F26).")
        title = "SkyNet — Список изделий (зеркало: работа и и)"
    else:
        front = fm_block("реальные данные/изделия/", "реальные данные", schet)
        quote = ("**Единый источник данных.** Классификация, B-BOM и масса — в карточках изделий "
                 "(`_index.md`); GitHub отрендерит front matter таблицей. Список — только "
                 "навигация: id, название, путь (F26).")
        title = "SkyNet — Список изделий (плоский индекс)"
    return front, page(title, quote, sections)


def build_parts(cards, zone_dir):
    """Ведомость частей (уровни 2–4): ## <подсистема> → ### <изделие> → части."""
    by_id = {r["id"]: r for r in
             cards["часть"] + cards["изделие"] + cards["ии_изделие"] if r["id"]}

    def host_of(part):
        seen, cur = set(), part
        while True:
            parent = str(cur["fm"].get("родитель") or "")
            if parent not in by_id or parent in seen:
                return None
            seen.add(parent)
            cur = by_id[parent]
            if cur["fm"].get("тип") == "изделие" or cur["path"].name == "_index.md":
                return cur

    parts = sorted(cards["часть"], key=lambda r: r["id"])
    groups: dict[str, dict] = {}
    for part in parts:
        host = host_of(part)
        key = host["id"] if host else "—_без_родителя"
        groups.setdefault(key, {"host": host, "parts": []})["parts"].append(part)

    def pod_of(host):
        return str((host["fm"].get("подсистема") if host else None) or "прочее")

    schet = {"всего_частей": len(parts),
             "изделий_с_декомпозицией": len(groups),
             "уровней": {2: 0, 3: 0, 4: 0}}
    sections = []
    for pod in PODSISTEMY:
        host_ids = [h for h, g in groups.items() if pod_of(g["host"]) == pod]
        if not host_ids:
            continue
        pod_sections = [f"## {pod} ({len(host_ids)} изделий)"]
        for hid in sorted(host_ids):
            pod_sections.append(f"### {hid} (уровень 1)")
            for part in groups[hid]["parts"]:
                lvl = to_int(part["fm"].get("уровень_номер") or 2)
                lvl = lvl if lvl in (2, 3, 4) else 2
                schet["уровней"][lvl] += 1
                rel = str(part["path"].relative_to(zone_dir))
                pod_sections.append(f"- `{part['id']}` (уровень {lvl}) — "
                                     f"{part['title'] or part['id']} → `{rel}`")
        sections.append("\n\n".join(pod_sections))
    if not sections:
        sections = ["## прочее (0 изделий)\n\n- — нет —"]
    front = fm_block("реальные данные/изделия/", "реальные данные", schet)
    quote = ("**Единый источник данных.** B-BOM — в карточках изделий: `дочерние_части`, "
             "`материалы_частей` (с `оптимальная_структура`, F62), `наследуемые_материалы`, "
             "`технологии_частей`. Ведомость — только навигация: где лежит каждая часть и её "
             "уровень (F26).")
    return front, page("SkyNet — Ведомость частей изделий", quote, sections)


def build_standards(cards):
    """Список стандартов: 2 секции категории; N_ссылок — обратные ссылки поля «стандарты»."""
    ref_counts: dict[str, int] = {}
    unmatched: list[str] = []
    known = {norm(r["id"]): r for r in cards["стандарт"]}
    known.update({norm(r["path"].stem): r for r in cards["стандарт"]})
    for kind in ("материал", "изделие", "часть", "технология",
                 "ии_материал", "ии_изделие", "ии_технология"):
        for rec in cards[kind]:
            for ref in as_list(rec["fm"].get("стандарты")):
                key = norm(ref)
                if key in known:
                    ref_counts[key] = ref_counts.get(key, 0) + 1
                else:
                    unmatched.append(f"{rec['id']}: «{ref}»")

    def refs_of(r):
        return ref_counts.get(norm(r["id"]), 0) + ref_counts.get(norm(r["path"].stem), 0)

    schet = {"всего": len(cards["стандарт"])}
    sections = []
    for value in KATEGORII_STANDARTOV:
        rows = sorted((r for r in cards["стандарт"]
                       if str(r["fm"].get("категория")) == value),
                      key=lambda r: r["id"])
        schet[value] = len(rows)
        if rows:
            body = ["| id | имя_файла | обозначение | организация | N_ссылок |",
                    "|---|---|---|---|---:|"]
            for r in rows:
                body.append(f"| {r['id']} | `{r['path'].name}` | "
                            f"{cell(r['fm'].get('обозначение') or '—')} | "
                            f"{cell(r['fm'].get('организация') or '—')} | {refs_of(r)} |")
        else:
            body = ["- — нет —"]
        sections.append(f"## {value} ({len(rows)})\n\n" + "\n".join(body))
    schet["с_ссылками"] = sum(1 for r in cards["стандарт"] if refs_of(r))
    front = fm_block("реальные данные/стандарты/", "реальные данные", schet)
    quote = ("**Единый источник данных.** Организация, область применения и требования — "
             "в карточках стандартов (`standart_<имя>.md`). Список — только навигация: id, "
             "файл, организация, счётчик ссылок (F26).")
    return front, page("SkyNet — Список стандартов", quote, sections), sorted(set(unmatched))


def build_groups(cards):
    """Группы: единая секция (в §10.2 нет enum); N_материалов — по полю F7."""
    mat_by_group: dict[str, int] = {}
    for rec in cards["материал"]:
        g = str(rec["fm"].get("исследовательская_группа") or "")
        if g:
            mat_by_group[g] = mat_by_group.get(g, 0) + 1
    izd_by_group: dict[str, int] = {}
    for rec in cards["изделие"]:
        g = str(rec["fm"].get("исследовательская_группа") or "")
        if g:
            izd_by_group[g] = izd_by_group.get(g, 0) + 1
    rows = sorted(cards["группа"], key=lambda r: r["id"])
    body = ["| id | имя_файла | локация | N_материалов | N_изделий |",
            "|---|---|---|---:|---:|"]
    for r in rows:
        body.append(f"| {r['id']} | `{r['path'].name}` | "
                    f"{str(r['fm'].get('локация') or '—')} | "
                    f"{mat_by_group.get(r['id'], 0)} | {izd_by_group.get(r['id'], 0)} |")
    if not rows:
        body = ["- — нет —"]
    schet = {"всего": len(rows),
             "групп_с_материалами": sum(1 for r in rows if mat_by_group.get(r["id"])),
             "групп_без_материалов": sum(1 for r in rows if not mat_by_group.get(r["id"]))}
    front = fm_block("реальные данные/исследовательские_группы/",
                     "реальные данные", schet)
    quote = ("**Единый источник данных.** Название, локация и специализация — в карточках "
             "групп (`group_<имя>.md`). Список — только навигация: id, файл, локация, "
             "счётчики связей (F26).")
    return front, page("SkyNet — Список исследовательских групп", quote,
                       [f"## группы ({len(rows)})\n\n" + "\n".join(body)])


def build_fant_materials(cards):
    """Фантастические материалы (§12.3a): единая секция; вдохновлён_реальным, N_произведений."""
    work_counts: dict[str, int] = {}
    for rec in cards["произведение"]:
        for mid in as_list(rec["fm"].get("материалы_в_произведении")):   # v11.0 — кросс-связи
            work_counts[str(mid)] = work_counts.get(str(mid), 0) + 1
    rows = sorted(cards["фант_материал"], key=lambda r: r["id"])
    body = ["| id | имя_файла | вдохновлён_реальным | N_произведений |", "|---|---|---|---:|"]
    for r in rows:
        body.append(f"| {r['id']} | `{r['path'].name}` | "
                    f"{cell(r['fm'].get('вдохновлён_реальным') or '—')} | "
                    f"{work_counts.get(r['id'], 0)} |")
    if not rows:
        body = ["- — нет —"]
    schet = {"всего": len(rows),
             "с_реальным_аналогом": sum(1 for r in rows if r["fm"].get("вдохновлён_реальным"))}
    front = fm_block("фантастические данные/материалы/", "фантастические данные", schet)
    quote = ("**Единый источник данных.** Канон-факты, фантастические свойства и реальный "
             "аналог-вдохновение — в карточках (`material_<имя>.md`, §12.3a). Список — только "
             "навигация (F26).")
    return front, page("SkyNet — Список фантастических материалов (канон)", quote,
                       [f"## фантастические материалы ({len(rows)})\n\n" + "\n".join(body)])


def build_works(cards):
    """Произведения: 6 секций категорий §9; сортировка по номеру work_NNN."""
    def work_num(r):
        m = re.search(r"(\d+)", r["id"])
        return (to_int(m.group(1)) if m else 0, r["id"])
    schet = {"всего": len(cards["произведение"]), "канон": 0}
    sections = []
    for value in KATEGORII_PROIZVEDENII:
        rows = sorted((r for r in cards["произведение"]
                       if str(r["fm"].get("категория")) == value), key=work_num)
        schet[value] = len(rows)
        if rows:
            body = ["| id | имя_файла | каноничность | N_моделей |", "|---|---|---|---:|"]
            for r in rows:
                if str(r["fm"].get("каноничность")) == "canon":
                    schet["канон"] += 1
                body.append(f"| {r['id']} | `{r['path'].name}` | "
                            f"{str(r['fm'].get('каноничность') or '—')} | "
                            f"{len(as_list(r['fm'].get('модели_в_произведении')))} |")
        else:
            body = ["- — нет —"]
        sections.append(f"## {value} ({len(rows)})\n\n" + "\n".join(body))
    front = fm_block("фантастические данные/произведения/",
                     "фантастические данные", schet)
    quote = ("**Единый источник данных.** Метаданные произведения — в карточках "
             "(`work_NNN.md`). Список — только навигация и классификация канона (F26).")
    return front, page("SkyNet — Список произведений канона", quote, sections)


def build_models(cards, midx):
    """Модели: 7 секций типов §11.0; колонки id|файл|категория|канон|N_произведений|обёртка_ии."""
    wii_ids = {r["id"] for r in cards["ии_изделие"]}
    work_counts: dict[str, int] = {}
    for rec in cards["произведение"]:
        for mid in as_list(rec["fm"].get("модели_в_произведении")):
            work_counts[str(mid)] = work_counts.get(str(mid), 0) + 1
    entries, dropped = [], []
    for stem, info in midx.items():
        rec = next((r for r in cards["модель"] if r["path"].stem == stem), None)
        tip_val = info.get("тип")
        if rec is not None and not tip_val:
            tip_val = rec["fm"].get("тип_модели")
        if str(tip_val) not in TIPY_MODELEI:
            dropped.append(f"{info.get('id') or stem} (тип={tip_val!r} вне §11.0)")
            continue
        entries.append((info.get("id") or f"SkyNet-{stem}", stem, info, tip_val))
    schet = {"всего": 0, "обёрток_ии": 0}
    sections = []
    for tip in TIPY_MODELEI:
        rows = []
        for mid, stem, info, tip_val in entries:
            if str(tip_val) != tip:
                continue
            wrapper = f"izdelie_{mid}" if f"izdelie_{mid}" in wii_ids else "—"
            if wrapper != "—":
                schet["обёрток_ии"] += 1
            n_works = (work_counts.get(mid)
                       or to_int(info.get("N_произведений") or 0))
            rows.append((mid, stem, info, wrapper, n_works))
        rows.sort(key=lambda t: t[0])
        schet[tip] = len(rows)
        schet["всего"] += len(rows)
        if rows:
            body = ["| id | имя_файла | категория | канон_источник | N_произведений | обёртка_ии |",
                    "|---|---|---|---|---:|---|"]
            for mid, stem, info, wrapper, n in rows:
                body.append(f"| {mid} | `{stem}.md` | {cell(info.get('категория') or '—')} | "
                            f"{cell(info.get('канон') or '—')} | {n} | {wrapper} |")
        else:
            body = ["- — нет —"]
        sections.append(f"## {tip} ({len(rows)})\n\n" + "\n".join(body))
    front = fm_block("фантастические данные/ (карточки моделей)",
                     "фантастические данные", schet)
    quote = ("**Единый источник данных.** Спецификации (§12.4) и связи — в карточках моделей; "
             "список — только навигация и классификация модели (F26). Колонка «класс» удалена "
             "(v3 — дубль «тип_модели»); сумма секций = «всего» (вне §11.0 — в диагностике).")
    return front, page("SkyNet — Список моделей (плоский индекс)", quote, sections), dropped


def build_realizations(cards, midx, root):
    """Ведомость реализаций: ## <модель> (N) → ### <тип> реализация → записи."""
    res = root / "результаты" / "модели"
    schet = {"всего": 0, "моделей_с_реализациями": 0,
             "реальная": 0, "фантастическая": 0, "доработанная_ии": 0}
    sections = []
    if res.is_dir():
        for model_dir in sorted(p for p in res.iterdir() if p.is_dir()):
            model_id = midx.get(model_dir.name, {}).get("id") or model_dir.name
            pod_sections = []
            total = 0
            for type_dir, key in TIPY_REALIZACII:
                tdir = model_dir / type_dir
                recs = sorted((r for r in cards["реализация"]
                               if r["path"].parent.parent == tdir), key=lambda r: r["id"])
                schet[key] += len(recs)
                total += len(recs)
                if recs:
                    body = "\n".join(
                        f"- `{r['id']}` — {r['title'] or r['id']} → "
                        f"`{type_dir}/{r['path'].parent.name}/_index.md`" for r in recs)
                else:
                    body = "- — нет —"
                pod_sections.append(f"### {type_dir} ({len(recs)})\n\n{body}")
            schet["всего"] += total
            if total:
                schet["моделей_с_реализациями"] += 1
            sections.append(f"## {model_id} ({total})\n\n" + "\n\n".join(pod_sections))
    if not sections:
        sections = ["## — нет моделей с реализациями (0) —\n\n- — нет —"]
    front = fm_block("результаты/модели/", "результаты", schet)
    quote = ("**Единый источник данных.** Состав, покрытие_функций, масса и цена — в карточках "
             "реализаций (`_index.md`, §12.5). Ведомость — только навигация: где лежит каждая "
             "реализация и её тип (F26).")
    return front, page("SkyNet — Ведомость реализаций моделей", quote, sections)


def zone_latest(recs) -> str:
    latest = ""
    for r in recs:
        d = str(r["fm"].get("дата_обновления") or "")
        if not d and isinstance(r["fm"].get("метаданные"), dict):
            d = str(r["fm"]["метаданные"].get("обновлено") or "")   # v10/v11 — единый блок метаданных
        if d > latest:
            latest = d
    return latest


def build_registry(cards, root, list_paths):
    """Сводный реестр: счётчики доменов × типы + покрытие списками."""
    rows = [
        ("реальные данные", "изделие", cards["изделие"], "реальные данные/изделия/"),
        ("реальные данные", "часть", cards["часть"], "реальные данные/изделия/ (папки часть_*)"),
        ("реальные данные", "материал", cards["материал"], "реальные данные/материалы/"),
        ("реальные данные", "технология", cards["технология"], "реальные данные/технологии/"),
        ("реальные данные", "стандарт", cards["стандарт"], "реальные данные/стандарты/"),
        ("реальные данные", "исследовательская_группа", cards["группа"],
         "реальные данные/исследовательские_группы/"),
        ("фантастические данные", "модель_SkyNet", cards["модель"],
         "фантастические данные/модели/"),
        ("фантастические данные", "материал (фантастический, §12.3a)", cards["фант_материал"],
         "фантастические данные/материалы/"),
        ("фантастические данные", "произведение", cards["произведение"],
         "фантастические данные/произведения/"),
        ("работа и и", "изделие (обёртки и части)", cards["ии_изделие"], "работа и и/изделия/"),
        ("работа и и", "материал", cards["ии_материал"], "работа и и/материалы/"),
        ("работа и и", "технология", cards["ии_технология"], "работа и и/технологии/"),
        ("результаты", "реализация_модели", cards["реализация"],
         "результаты/модели/<модель>/<тип> реализация/"),
    ]
    total = sum(len(r[2]) for r in rows)
    dom_types = ["| Домен | Тип карточки | Карточек | Доля % | Путь |",
                 "|---|---|---:|---:|---|"]
    for dom, tip, recs, path in rows:
        share = (len(recs) / total * 100) if total else 0
        dom_types.append(f"| {dom} | {tip} | {len(recs)} | {share:.1f}% | `{path}` |")
    dom_types.append(f"| **ИТОГО** | | **{total}** | **100.0%** | |")

    cov_rows = ["| Список | Путь | Обновлено | Генератор | Статус |", "|---|---|---|---|---|"]
    for name, rel, zone_recs in list_paths:
        p = root / rel
        if not p.is_file():
            cov_rows.append(f"| {name} | `{rel}` | — | — | отсутствует |")
            continue
        fm = read_frontmatter(p) or {}
        meta = fm.get("метаданные") if isinstance(fm, dict) else None
        meta = meta if isinstance(meta, dict) else {}
        upd = str(meta.get("обновлено") or "—")
        gen = str(meta.get("генератор") or "вручную")
        latest = zone_latest(zone_recs)
        status = "актуален" if (upd != "—" and (not latest or upd >= latest)) else "отстал"
        cov_rows.append(f"| {name} | `{rel}` | {upd} | {gen} | {status} |")
    for name, rel in AUX_LISTS:  # вспомогательные сводные файлы (если существуют)
        p = root / rel
        if not p.is_file():
            continue
        fm = read_frontmatter(p) or {}
        meta = fm.get("метаданные") if isinstance(fm, dict) else None
        meta = meta if isinstance(meta, dict) else {}
        upd = str(meta.get("обновлено") or "—")
        cov_rows.append(f"| {name} | `{rel}` | {upd} | вручную | актуален |")

    n_cov = len(cov_rows) - 2   # строки покрытия без шапки и разделителя
    front = fm_block("весь репозиторий базы знаний", "весь репозиторий",
                     {"всего_карточек": total, "всего_списков": n_cov},
                     tip="реестр", versiya="1.1")
    quote = ("**Единый источник данных.** Свойства карточек — в самих карточках; навигация "
             "внутри зоны — в списках `_список_*.md`. Реестр — верхний уровень: сколько каких "
             "карточек в каждом домене и какие списки их покрывают (F26).")
    body = ["## Домены и типы\n\n" + "\n".join(dom_types),
            "## Покрытие списками\n\n" + "\n".join(cov_rows)]
    return front, page("SkyNet — Сводный реестр базы знаний", quote, body)


# ─────────────────────────── запись и сверка ───────────────────────────

AUX_LISTS = [
    ("Индекс подсистем", "реальные данные/изделия/_индекс_подсистем.md"),
    ("Иерархия изделий", "реальные данные/изделия/_иерархия_изделий.md"),
    ("Реестр произведений (нумерация §9)", "фантастические данные/_реестр_произведений.md"),
    ("Индекс произведений (тематический)", "фантастические данные/_индекс_произведений.md"),
    ("Индекс канона", "фантастические данные/_индекс.md"),
]


def process(name: str, rel: str, built, zone: list, root: pathlib.Path,
            check: bool) -> int:
    """Запись (generate) или сверка (check) одного сводного файла. Возвращает 0/1."""
    front, body = built
    content = front + "\n\n" + body
    target = root / rel
    if check:
        if not target.is_file():
            print(f"  ! {name}: ОТСУТСТВУЕТ ({rel})")
            return 1
        meta = read_frontmatter(target) or {}
        meta = meta.get("метаданные") if isinstance(meta, dict) else None
        gen = str((meta or {}).get("генератор") or "")
        text = target.read_text(encoding="utf-8")
        if gen == GENERATOR:
            if text == content:
                print(f"  = {name}: АКТУАЛЕН ({rel})")
                return 0
            print(f"  ! {name}: ОТЛИЧАЕТСЯ от карточек ({rel}) — обновите генератором")
            return 1
        missing = [r["id"] for r in zone if f"`{r['id']}`" not in text]
        if missing:
            shown = ", ".join(missing[:5])
            print(f"  ! {name} (вручную): нет записей: {shown}"
                  f"{' …' if len(missing) > 5 else ''}")
            return 1
        print(f"  = {name} (вручную): все карточки зоны входят ({rel})")
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"  + {name}: записан ({rel})")
    return 0


def main() -> int:
    check = "--check" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--check"]
    root = pathlib.Path(args[0]).resolve() if args else \
        pathlib.Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"ОШИБКА: корень базы знаний не найден: {root}")
        return 2

    cards = collect_cards(root)
    midx = model_index(cards, root)
    rd_izd = root / "реальные данные" / "изделия"
    wii_izd = root / "работа и и" / "изделия"

    std_front, std_page, unmatched_refs = build_standards(cards)
    mod_front, mod_page, mod_dropped = build_models(cards, midx)
    # фаза 1: 12 списков (реестр — фаза 3, после записи, из факта на диске)
    lists = {
        "Список материалов": ("реальные данные/материалы/_список_материалов.md",
                               build_materials(cards["материал"]), cards["материал"]),
        "Зеркало: материалы": ("работа и и/материалы/_список_материалов.md",
                               build_materials_mirror(cards["ии_материал"]),
                               cards["ии_материал"]),
        "Список изделий": ("реальные данные/изделия/_список_изделий.md",
                           build_products(cards["изделие"], rd_izd), cards["изделие"]),
        "Зеркало: изделия": ("работа и и/изделия/_список_изделий.md",
                             build_products(cards["ии_изделие"], wii_izd, mirror=True),
                             cards["ии_изделие"]),
        "Ведомость частей": ("реальные данные/изделия/_список_частей.md",
                             build_parts(cards, rd_izd), cards["часть"]),
        "Список технологий": ("реальные данные/технологии/_список_технологий.md",
                              build_technologies(cards["технология"]), cards["технология"]),
        "Зеркало: технологии": ("работа и и/технологии/_список_технологий.md",
                                build_technologies_mirror(cards["ии_технология"]),
                                cards["ии_технология"]),
        "Список стандартов": ("реальные данные/стандарты/_список_стандартов.md",
                              (std_front, std_page), cards["стандарт"]),
        "Список групп": ("реальные данные/исследовательские_группы/"
                         "_список_исследовательских_групп.md",
                         build_groups(cards), cards["группа"]),
        "Список моделей": ("фантастические данные/_список_моделей.md",
                           (mod_front, mod_page), cards["модель"]),
        "Список произведений": ("фантастические данные/произведения/_список_произведений.md",
                               build_works(cards), cards["произведение"]),
        "Список фантастических материалов": (
            "фантастические данные/материалы/_список_фантастических_материалов.md",
            build_fant_materials(cards), cards["фант_материал"]),
        "Ведомость реализаций": ("результаты/модели/_список_реализаций.md",
                                 build_realizations(cards, midx, root), cards["реализация"]),
    }

    print(f"КОРЕНЬ: {root}")
    print("Карточек: " + ", ".join(f"{k}={len(v)}" for k, v in cards.items() if v))
    print()

    # фаза 2: запись/сверка 12 списков
    problems = 0
    for name, (rel, built, zone) in lists.items():
        problems += process(name, rel, built, zone, root, check)

    # фаза 3: реестр — из фактического состояния списков на диске (после фазы 2)
    registry = build_registry(cards, root,
                              [(n, rel, zone) for n, (rel, _b, zone) in lists.items()])
    problems += process("Сводный реестр", "_сводный_реестр.md", registry, [], root, check)

    if unmatched_refs:
        print("\nДИАГНОСТИКА — ссылки на стандарты без карточек (нормализовать id):")
        for ref in unmatched_refs[:10]:
            print(f"  ? {ref}")
        if len(unmatched_refs) > 10:
            print(f"  … всего {len(unmatched_refs)}")
    if mod_dropped:
        print("\nДИАГНОСТИКА — модели вне канонических типов §11.0 (исправить тип_модели):")
        for d in mod_dropped[:10]:
            print(f"  ? {d}")
        if len(mod_dropped) > 10:
            print(f"  … всего {len(mod_dropped)}")

    print()
    if check:
        print("СВЕРКА:", "ОШИБКИ" if problems else "ВСЁ АКТУАЛЬНО")
        return 1 if problems else 0
    print(f"Готово: {len(lists) + 1} списков обновлено ({TODAY}); "
          "закоммитьте вместе с карточками (§15a.2).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
