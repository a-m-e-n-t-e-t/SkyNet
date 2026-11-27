#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SkyNet — синхронизация зоны материалов со ссылками базы знаний.

Список материалов (`_список_материалов.md`) строится `scripts/generate_lists.py`
из КАРТОЧЕК `реальные данные/материалы/*.md`. Этот скрипт дополняет зону материалов
карточками, на которые ССЫЛАЮТСЯ другие карточки базы, но которых ещё нет (§15a.2):

  • изделия и части (`реальные данные/изделия/**`, `работа и и/изделия/**`):
      - `материалы_частей[].материал`                     — BOM части (F26, F62)
      - `технологии_частей[].материалы_для_процесса[].материал`
      - `наследуемые_материалы[].материал`
      - ссылки вида `material_<имя>` в тексте карточки     — «смотри …»
  • технологии (`реальные данные/технологии/*.md`, `работа и и/технологии/*.md`):
      - `материалы_для_процесса[].материал`, `типичные_материалы_для_процесса[].материал`
      - ссылки вида `material_<имя>` в тексте карточки
  • альтернативы и аналоги материалов (`реальные данные/материалы/*.md`,
    `работа и и/материалы/*.md`):
      - ссылки вида `material_<имя>` в front matter и теле карточки
        (разделы «Аналоги и заменители», альтернативы применения, «см. …»)

Для КАЖДОЙ ссылки без карточки автоматически создаётся пустой шаблон
`реальные данные/материалы/<имя>.md` (`статус: пустой_шаблон`, класс по умолчанию
`прочее`) с обратными ссылками — в каких карточках и в каких полях материал
упомянут. Затем `scripts/generate_lists.py` включает шаблон в список материалов:
список дополняется автоматически, «висячих» ссылок в BOM не остаётся.

В CI конвейер встроен в `.github/workflows/update-lists.yml` (пуш карточек →
синхронизация → генерация списков → коммит). Скрипт идемпотентен: повторный
запрос ничего не меняет.

Использование:
  python3 scripts/sync_materials.py [КОРЕНЬ]          # создать пустые шаблоны
  python3 scripts/sync_materials.py --check [КОРЕНЬ]  # только отчёт, без записи
                                                       # (код выхода 1 — есть пробелы)
"""
from __future__ import annotations

import datetime as _dt
import pathlib
import re
import sys

import yaml

TODAY = _dt.date.today().isoformat()
GENERATOR = "scripts/sync_materials.py"

# id-подобная ссылка: строчные латиница/цифры/._- (§15a.1, конвенция имён)
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{1,78}[a-z0-9]$|^[a-z0-9]$")
# ссылка вида material_<имя> в тексте карточки (front matter + тело)
REF_RE = re.compile(r"material_[a-z0-9][a-z0-9._-]*")

# Подтверждённые синонимы ссылок → канонические карточки (образец: migrate_aliases.py
# старой системы; пары «старая система» помечены). Ссылка-синоним НЕ создаёт
# пустой шаблон, а резолвится в каноническую карточку; если канонической
# карточки тоже нет — шаблон создаётся для канонического имени.
ALIASES = {
    "barium_titanate": "batio3",             # BaTiO₃ — титанат бария
    "bearing_steel_52100": "100cr6",          # 52100 (ASTM A295) = 100Cr6 (DIN/EN)
    "gst_chalcogenide": "gst",                # Ge₂Sb₂Te₅ (GST-225), халькогенид
    "lithium_metal": "lithium",               # металлический литий
    "monocrystalline_si": "si",               # моно-CZ/FZ — структурный вариант si
    "silicon": "si",                          # кремний — обобщающая ссылка
    "silicon_wafer": "si",                    # пластина — форма поставки si
    "silicon_carbide": "monokristallicheskogo_sic",   # SiC — карточка 4H-SiC/политипы
    "nafion_117": "nafion",                   # Nafion 117 — марка/толщина
    "ni63_metal": "ni-63",                    # металлический Ni-63
    "ni_ysz_cermet": "ni-ysz",                # пара migrate_aliases (старая система)
    "pcm": "pcm_rt35",                        # в базе один PCM — RT35
    "pvdf-trfe-ctfe": "p_vdf-trfe-ctfe",      # пара migrate_aliases (старая система)
    "pp_membrane": "polypropylene",           # канонический_id старой карточки
    "stainless_steel_304": "ss_aisi_304",     # нержавеющая AISI 304
    "stainless_steel_316": "ss_316l",         # 316 → карточка 316L
    "uo2_pellets": "uo2",                      # пеллеты — форма поставки UO₂
    "ybco_bulk": "ybco",                      # bulk-керамика — форма
    "uglevolokno": "karbon",                  # пара migrate_aliases (старая система):
    #   углеволокно PAN Toray T300 — канонический пары karbon; обе карточки
    #   отсутствуют в базе → создаётся один шаблон karbon
}

# родительские ключи YAML, под которыми живут списки ссылок на материалы
PARENT_KEYS = {
    "материалы_частей",                 # BOM изделия/части (§12.6)
    "материалы_для_процесса",           # материалы процесса в части и технологии
    "типичные_материалы_процесса",      # вариант написания в старых карточках
    "типичные_материалы_для_процесса",
    "наследуемые_материалы",            # агрегат по частям (§12.6)
    "материалы",                        # обобщённый список
}
# ключи-спутники, подтверждающие, что «материал: …» — ссылка (а не описание)
COMPANION_KEYS = {"часть", "роль", "форма", "доля_массы", "суммарная_доля_массы",
                  "источники_частей", "форма_хранения"}


def read_frontmatter(path: pathlib.Path):
    """YAML front matter (блок между 1-й и 2-й строкой «---»); None при ошибке."""
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


def ref_to_stem(ref) -> str:
    """Ссылка → стем файла: нижний регистр, пробелы → _, без префикса material_."""
    s = str(ref).strip().lower().replace(" ", "_").rstrip("._-")
    return s[len("material_"):] if s.startswith("material_") else s


def resolve_alias(stem: str) -> str:
    """Стем → канонический стем по ALIASES (цепочки ограничены глубиной 3)."""
    for _ in range(3):
        nxt = ALIASES.get(stem)
        if not nxt or nxt == stem:
            return stem
        stem = nxt
    return stem


def is_id_shaped(ref) -> bool:
    return bool(ID_RE.match(ref_to_stem(ref)))


def walk_struct_refs(node, parent_key: str, out: list):
    """Рекурсивный обход front matter: словари с ключом «материал» — ссылки.

    Условие: значение id-подобное И (родительский ключ из PARENT_KEYS
    или в словаре есть ключ-спутник). Свободный текст («Ti-6Al-4V (Grade 5)»)
    отсекается проверкой формы id.
    """
    if isinstance(node, dict):
        if "материал" in node and isinstance(node["материал"], (str, int, float)):
            ref = str(node["материал"]).strip()
            if ref and is_id_shaped(ref) and (
                    parent_key in PARENT_KEYS or (COMPANION_KEYS & set(node.keys()))):
                out.append({"ref": ref, "поле": parent_key or "материал",
                            "часть": str(node.get("часть") or "")})
        for key, val in node.items():
            if key == "материал":
                continue
            walk_struct_refs(val, str(key), out)
    elif isinstance(node, list):
        for item in node:
            walk_struct_refs(item, parent_key, out)


def scan_zone_files(zone: pathlib.Path, recursive: bool):
    """Карточки зоны: файлы *.md, кроме сводных _*.md (кроме _index.md — карточки)."""
    if not zone.is_dir():
        return []
    it = zone.rglob("*.md") if recursive else zone.glob("*.md")
    return [p for p in sorted(it)
            if not (p.name.startswith("_") and p.name != "_index.md")]


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    root = pathlib.Path(args[0]).resolve() if args else \
        pathlib.Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"! Корень не найден: {root}")
        return 2

    mat_dir = root / "реальные данные" / "материалы"

    # ── 1. существующие материалы: стемы файлов + id карточек ──────────────
    known: set[str] = set()
    for p in scan_zone_files(mat_dir, recursive=False):
        known.add(p.stem)
        fm = read_frontmatter(p) or {}
        mid = str(fm.get("id") or "")
        if mid:
            known.add(mid)
            known.add(ref_to_stem(mid))
    n_cards = len(scan_zone_files(mat_dir, recursive=False))
    # фантастические (canon) материалы и обёртки §12.7 (работа и и/материалы) —
    # не «висячая» ссылка: карточка существует, пустой шаблон не создаём
    for zone in (root / "фантастические данные" / "материалы",
                 root / "работа и и" / "материалы"):
        for p in scan_zone_files(zone, recursive=False):
            known.add(ref_to_stem(p.stem))
            fm_w = read_frontmatter(p) or {}
            wid = str(fm_w.get("id") or "")
            if wid:
                known.add(wid)
                known.add(ref_to_stem(wid))
    # карточки-компоненты (изделия/компоненты/**) — не материалы, но содержат
    # описание материала; в шаблоне даём ссылку для заполнения
    komponenty: dict[str, str] = {}
    komp_root = root / "реальные данные" / "изделия" / "компоненты"
    if komp_root.is_dir():
        for p in komp_root.rglob("_index.md"):
            komponenty[p.parent.name] = str(p.relative_to(root))
            fm_k = read_frontmatter(p) or {}
            kid = ref_to_stem(str(fm_k.get("id") or ""))
            if kid:
                komponenty.setdefault(kid, str(p.relative_to(root)))

    # ── 2. сбор ссылок ──────────────────────────────────────────────────────
    refs: dict[str, list[dict]] = {}   # стем → откуда ссылаются
    resolved: dict[str, str] = {}      # синоним → канонический (для диагностики)

    def add_ref(ref: str, источник: pathlib.Path, поле: str, часть: str = ""):
        stem = ref_to_stem(ref)
        if not stem or not is_id_shaped(ref):
            return
        if stem in known or ref in known:
            return
        canon = resolve_alias(stem)
        if canon != stem:
            resolved[stem] = canon
            if canon in known:
                return                       # каноническая карточка есть
            stem = canon                    # иначе — шаблон для канонического имени
        if stem in known:
            return
        place = {"файл": str(источник.relative_to(root)), "поле": поле, "часть": часть}
        lst = refs.setdefault(stem, [])
        if place not in lst:
            lst.append(place)

    # 2а. изделия и части: структурные ссылки BOM + material_* в тексте
    for zone in (root / "реальные данные" / "изделия", root / "работа и и" / "изделия"):
        for p in scan_zone_files(zone, recursive=True):
            fm = read_frontmatter(p)
            if fm is None:
                continue
            struct: list = []
            walk_struct_refs(fm, "", struct)
            for r in struct:
                add_ref(r["ref"], p, r["поле"], r["часть"])
            for m in REF_RE.findall(p.read_text(encoding="utf-8").lower()):
                add_ref(m, p, "ссылка в тексте")

    # 2б. технологии: материалы процессов + material_* в тексте
    for zone in (root / "реальные данные" / "технологии", root / "работа и и" / "технологии"):
        for p in scan_zone_files(zone, recursive=False):
            fm = read_frontmatter(p)
            if fm is None:
                continue
            struct: list = []
            walk_struct_refs(fm, "", struct)
            for r in struct:
                add_ref(r["ref"], p, r["поле"])
            for m in REF_RE.findall(p.read_text(encoding="utf-8").lower()):
                add_ref(m, p, "ссылка в тексте")

    # 2в. альтернативы/аналоги материалов: material_* в тексте карточек материалов
    for zone in (mat_dir, root / "работа и и" / "материалы"):
        for p in scan_zone_files(zone, recursive=False):
            fm = read_frontmatter(p) or {}
            own = str(fm.get("id") or "")
            for m in REF_RE.findall(p.read_text(encoding="utf-8").lower()):
                if ref_to_stem(m) == ref_to_stem(own):
                    continue          # карточка ссылается на себя
                add_ref(m, p, "альтернатива/аналог")

    # ── 3. отчёт и создание пустых шаблонов ─────────────────────────────────
    print(f"Материалов в зоне: {n_cards}; ссылок без карточки: {len(refs)}")
    if resolved:
        print(f"Синонимы → канонические карточки: {len(resolved)}")
        for syn, canon in sorted(resolved.items())[:20]:
            print(f"    {syn} → {canon}")
        if len(resolved) > 20:
            print(f"    … всего {len(resolved)}")
    if not refs:
        print("СИНХРОНИЗАЦИЯ: пробелов нет — все ссылки ведут на карточки")
        return 0

    created, skipped = [], []
    for stem in sorted(refs):
        if len(stem) > 80:
            skipped.append(stem)
            continue
        places = refs[stem]
        if check_only:
            continue
        komponent = komponenty.get(stem)
        (mat_dir / f"{stem}.md").write_text(stub_text(stem, places, komponent),
                                           encoding="utf-8")
        created.append(stem)

    for stem in sorted(refs)[:60]:
        n = len(refs[stem])
        first = refs[stem][0]
        print(f"  ? {stem} — {n} ссылок, например: {first['файл']} ({first['поле']})")
    if len(refs) > 60:
        print(f"  … всего {len(refs)}")

    if check_only:
        print(f"ПРОВЕРКА: {len(refs)} материалов упомянуты без карточки — "
              f"запустите без --check для создания пустых шаблонов")
        return 1
    if skipped:
        print(f"  ! пропущено (имя длиннее 80): {', '.join(skipped)}")
    print(f"Создано пустых шаблонов: {len(created)} → реальные данные/материалы/")
    print("Далее: python3 scripts/generate_lists.py (списки включат новые карточки)")
    return 0


def stub_text(stem: str, places: list[dict], komponent: str | None = None) -> str:
    """Пустой шаблон карточки материала по мотивам шаблоны/шаблон_материала.md (v10.1)."""
    lines_refs = []
    for pl in places[:40]:
        part = f", часть `{pl['часть']}`" if pl.get("часть") else ""
        lines_refs.append(f"- `{pl['файл']}` — {pl['поле']}{part}")
    if len(places) > 40:
        lines_refs.append(f"- … ещё {len(places) - 40} ссылок")
    body_refs = "\n".join(lines_refs)
    section_komp = ""
    if komponent:
        section_komp = f"""
## Родственная карточка (компонент)

В базе есть карточка-компонент с данным материалом — использовать её данные при
заполнении: [`{komponent}`]({pathlib.Path(komponent).as_posix()})
"""

    return f"""---
id: material_{stem}
тип: материал
класс: прочее                    # авто: класс не установлен при создании — уточнить
химический_состав: null          # заполнить (реальный состав; НЕ выдумывать)
исследовательская_группа: требует_верификации
стандарты: []
метаданные:
  версия_схемы: 10.1
  версия_данных: реальная
  реальность: реальный
  доступность_tlr: null
  статус: пустой_шаблон          # заполнить: извлечено | верифицировано | оптимизировано
  ии_перепроектирован: нет
  источник:
    тип: вывод_ии
    разбор: автоссылка           # карточка создана автоматически из ссылок базы
    url: null
    проверено: null
  создано: {TODAY}
  обновлено: {TODAY}
---

# {stem} (пустой шаблон)

> **Пустой шаблон, создан автоматически** скриптом `{GENERATOR}`:
> материал упомянут в других карточках базы, но карточки с данными ещё нет.
> Заполните по `шаблоны/шаблон_материала.md` (v10.1) и смените
> `метаданные.статус`: `пустой_шаблон` → `извлечено`.

## Упомянут в (обратные ссылки, авто)

{body_refs}
{section_komp}
## Чек-лист заполнения

- [ ] `класс`: заменить `прочее` на фактический (металл|сплав|керамика|полупроводник|полимер|композит|радиоизотоп|прочее)
- [ ] `структурные_варианты`: ≥1 вариант, ровно один `основной: да` (F5)
- [ ] свойства варианта: механические/термические/электрические + `химическая_стойкость`
- [ ] `экономика` варианта: `цена_usd_kg`, `форма_поставки`
- [ ] `исследовательская_группа`: верифицировать
- [ ] `метаданные.статус`: `пустой_шаблон` → `извлечено`
"""


if __name__ == "__main__":
    sys.exit(main())
