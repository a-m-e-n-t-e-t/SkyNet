#!/usr/bin/env python3
"""
SkyNet — генератор трёх графов связей репозитория.

Граф 1 (data):    изделия ↔ материалы ↔ технологии ↔ стандарты ↔ ИГ
Граф 2 (meta):    скрипты ↔ спецификация ↔ индексы ↔ документация
Граф 3 (trace):   метрика → скрипт → файл (прослеживаемость требований)

Source of truth: graphs/graph{1,2,3}_*.json
Mermaid-рендеры: graphs/mermaid/*.md (для чтения человеком)

Usage:
  python3 scripts/generate_graphs.py --all           # всё
  python3 scripts/generate_graphs.py --graph 1       # только граф 1
  python3 scripts/generate_graphs.py --graph 1 --mermaid  # граф 1 + рендеры
  python3 scripts/generate_graphs.py --fill-backrefs  # заполнить обратные рёбра в файлах (одноразовая миграция)
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
REAL_DATA = REPO / "реальные данные"
SCRIPTS_DIR = REPO / "scripts"
GRAPHS_DIR = REPO / "graphs"
MERMAID_DIR = GRAPHS_DIR / "mermaid"

SPEC_FILE = REPO / "SkyNet_PROMPT_v9.31.md"
CATALOG_FILE = SCRIPTS_DIR / "_CATALOG.md"
README_FILE = REPO / "README.md"

# Подсистемы (§11.1 спецификации)
SUBSYSTEMS = [
    "вычислительная", "энергетическая", "каркас", "навигация",
    "приводная_система", "прочее", "сенсоры", "система_охлаждения",
    "система_связи", "встроенное_оружие",
]


# ============================================================================
# YAML frontmatter — через PyYAML (надёжно)
# ============================================================================

def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Парсит YAML frontmatter через PyYAML. Возвращает (dict, yaml_text, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, "", text
    fm_text = m.group(1)
    body = m.group(2)
    try:
        data = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        data = {}
    return data, fm_text, body


def read_md(path: Path) -> dict:
    """Прочитать .md и вернуть frontmatter + путь."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    data, _, _ = parse_frontmatter(text)
    try:
        data["_path"] = str(path.resolve().relative_to(REPO))
    except ValueError:
        data["_path"] = str(path)
    data["_filename"] = path.name
    return data


# ============================================================================
# ГРАФ 1 — граф данных
# ============================================================================

def _slug(s) -> str:
    """'Ti-6Al-4V'→'ti-6al-4v', 'bi2te3'≡'bi2te3' (subscript-цифры нормализуются)."""
    s = str(s).translate(str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789"))
    return re.sub(r"[^a-z0-9а-яё]+", "-", s.lower()).strip("-")


def graph1_build() -> dict:
    """Построить граф данных."""
    nodes: list[dict] = []
    edges: list[dict] = []
    by_id: dict[str, dict] = {}
    _seen_edges: set[tuple[str, str, str]] = set()

    # Индекс материалов: 'bi2te3'→'material_bi2te3' (матчинг упоминаний с файлами)
    mat_index: dict[str, str] = {}
    for _mf in sorted((REAL_DATA / "материалы").glob("*.md")):
        _md = read_md(_mf)
        _mid = _md.get("id")
        if not _mid:
            continue
        for _cand in (_mid, _mid[len("material_"):] if _mid.startswith("material_") else _mid, _mf.stem):
            mat_index[_slug(_cand)] = _mid
    def add_node(nid: str, ntype: str, label: str, path: str = "", subsystem: str = ""):
        if nid in by_id:
            return
        node = {
            "id": nid,
            "type": ntype,
            "label": label,
            "path": path,
            "subsystem": subsystem,
        }
        nodes.append(node)
        by_id[nid] = node

    def add_edge(src: str, dst: str, etype: str, meta: dict | None = None):
        # Дедупликация рёбер: одна и та же пара (src,dst,type) встречается
        # многократно (например, материал в 5 частях одного изделия); мы
        # оставляем первое вхождение, чтобы граф был минимальным.
        key = (src, dst, etype)
        if key in _seen_edges:
            return
        _seen_edges.add(key)
        edges.append({
            "src": src, "dst": dst, "type": etype,
            "meta": meta or {},
        })

    # 1) Изделия и части (v9.40 вариант D: реальные данные/ + работа и и/)
    IZD_FILES = []
    for izd_root in [REAL_DATA / "изделия", REPO / "работа и и" / "изделия"]:
        if izd_root.is_dir():
            IZD_FILES.extend(izd_root.rglob("_index.md"))
    for f in IZD_FILES:
        d = read_md(f)
        if not d or "id" not in d:
            continue
        nid = d["id"]
        ntype = "izdelie" if d.get("уровень_номер") in (1, "1") else "chast"
        subsystem = d.get("подсистема", "")
        label = d.get("подтип", nid)
        add_node(nid, ntype, label, d.get("_path", ""), subsystem)

        # has_part (canonical direction — parent→child; reverse index built on load)
        # v9.62: mirror-рёбра (child_of, part_of, used_in, researches) убраны —
        # экономия ~277 KB в graph1_data.json; reverse-index строится на лету.
        children = d.get("дочерние_части", []) or []
        if isinstance(children, list):
            for c in children:
                add_edge(nid, c, "has_part")

        # uses_material — YAML-список словарей, парсим текстом (parse_frontmatter не читает списки словарей)
        _txt = f.read_text(encoding="utf-8")
        _lines = _txt.split("\n")
        _start = None
        for _i, _ln in enumerate(_lines):
            if re.match(r"^материалы_частей:\s*$", _ln):
                _start = _i + 1
                break
        if _start is not None:
            for _ln in _lines[_start:]:
                if _ln and not _ln[0].isspace():   # следующий top-level ключ — конец блока
                    break
                _mm = re.search(r"\bматериал:\s*(\S+)", _ln)
                if _mm:
                    _raw = _mm.group(1).strip("'\"")
                    if _raw in ("null", ""):
                        continue
                    target = mat_index.get(_slug(_raw)) or (_raw if _raw.startswith("material_") else f"material_{_raw}")
                    add_edge(nid, target, "uses_material")

        # complies_with (стандарты)
        stds = d.get("стандарты", []) or []
        if isinstance(stds, list):
            for s in stds:
                # v9.44 fix: стандарт может быть dict/числом (мусор CSV) —
                # краш 'dict' object has no attribute 'startswith' ронял
                # генератор графов целиком (и pre-commit). Нестроки — skip.
                if not isinstance(s, str) or not s or s == "null":
                    continue
                target = s if s.startswith("standart_") else f"standart_{s}"
                add_edge(nid, target, "complies_with")

        # researched_by (исследовательская группа)
        ig = d.get("исследовательская_группа")
        if ig and ig not in ("null", "", "требует_верификации"):
            target = ig if str(ig).startswith("group_") else f"group_{ig}"
            add_edge(nid, target, "researched_by")

    for f in sorted((REAL_DATA / "материалы").glob("*.md")):
        d = read_md(f)
        if not d or "id" not in d:
            continue
        nid = d["id"]
        add_node(nid, "material", d.get("химический_состав", nid), d.get("_path", ""))

        # complies_with
        stds = d.get("стандарты", []) or []
        if isinstance(stds, list):
            for s in stds:
                # v9.44 fix: стандарт может быть dict/числом (мусор CSV) —
                # краш 'dict' object has no attribute 'startswith' ронял
                # генератор графов целиком (и pre-commit). Нестроки — skip.
                if not isinstance(s, str) or not s or s == "null":
                    continue
                target = s if s.startswith("standart_") else f"standart_{s}"
                add_edge(nid, target, "complies_with")

        # researched_by
        ig = d.get("исследовательская_группа")
        if ig and ig not in ("null", "требует_верификации"):
            target = ig if ig.startswith("group_") else f"group_{ig}"
            add_edge(nid, target, "researched_by")

    # 3) Технологии
    for f in sorted((REAL_DATA / "технологии").glob("*.md")):
        d = read_md(f)
        if not d or "id" not in d:
            continue
        nid = d["id"]
        add_node(nid, "tekhnologia", d.get("категория", nid), d.get("_path", ""))

        stds = d.get("стандарты", []) or []
        if isinstance(stds, list):
            for s in stds:
                # v9.44 fix: стандарт может быть dict/числом (мусор CSV) —
                # краш 'dict' object has no attribute 'startswith' ронял
                # генератор графов целиком (и pre-commit). Нестроки — skip.
                if not isinstance(s, str) or not s or s == "null":
                    continue
                target = s if s.startswith("standart_") else f"standart_{s}"
                add_edge(nid, target, "complies_with")

    # 4) Стандарты
    for f in sorted((REAL_DATA / "стандарты").glob("*.md")):
        d = read_md(f)
        if not d or "id" not in d:
            continue
        nid = d["id"]
        add_node(nid, "standart", d.get("организация", nid), d.get("_path", ""))

    # 5) Исследовательские группы
    ig_dir = REAL_DATA / "исследовательские_группы"
    if ig_dir.exists():
        for f in sorted(ig_dir.glob("*.md")):
            d = read_md(f)
            if not d or "id" not in d:
                continue
            nid = d["id"]
            add_node(nid, "issledovatelskaya_gruppa", d.get("название", nid), d.get("_path", ""))

    # Синтез обратных рёбер (в памяти графа; для записи в файлы см. --fill-backrefs)
    # Фильтр висячих: ребро включается в граф только если ОБА конца — существующие вершины;
    # висячие цели выносятся в отдельный блок (честный отчёт о неполноте данных).
    ids = set(by_id)
    clean, dangling = [], defaultdict(set)
    for e in edges:
        if e["src"] in ids and e["dst"] in ids:
            clean.append(e)
        else:
            dangling[e["type"]].add(e["dst"] if e["dst"] not in ids else e["src"])
    edges = clean
    # v9.62: mirror-рёбра убраны (used_in, part_of, researches, referenced_by)
    # reverse-index строится на лету при загрузке графа
    # Оставляем только canonical directions: has_part, uses_material, researched_by, complies_with

    return {
        "kind": "graph1_data",
        "description": "Граф данных: изделия ↔ материалы ↔ технологии ↔ стандарты ↔ исследовательские группы",
        "nodes": nodes,
        "edges": edges,
        "висячие_цели": {t: sorted(v) for t, v in sorted(dangling.items())},
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "dangling": {t: len(v) for t, v in sorted(dangling.items())},
            "by_type": {t: sum(1 for n in nodes if n["type"] == t) for t in sorted(set(n["type"] for n in nodes))},
        },
    }


def graph1_mermaid_overview(g: dict) -> str:
    """Сводный Mermaid: подсистемы и их изделия (без материалов)."""
    lines = [
        "# Граф 1 — обзор по подсистемам",
        "",
        "```mermaid",
        "graph LR",
    ]
    # Узлы-подсистемы
    sub_izd: dict[str, list[str]] = defaultdict(list)
    for n in g["nodes"]:
        if n["type"] == "izdelie":
            sub_izd[n.get("subsystem", "прочее")].append(n["id"])
    for sub, izds in sorted(sub_izd.items()):
        safe = sub.replace(" ", "_")
        lines.append(f"    sub_{safe}[{sub}<br/>{len(izds)} изд.]")
    # Связи подсистем через общие материалы (упрощённо: просто перечислим)
    lines.append("```")
    lines.append("")
    # Стат-таблица
    lines.append("| Подсистема | Изделий |")
    lines.append("|---|---:|")
    for sub, izds in sorted(sub_izd.items()):
        lines.append(f"| {sub} | {len(izds)} |")
    return "\n".join(lines) + "\n"


def graph1_mermaid_subsystem(g: dict, subsystem: str) -> str:
    """Mermaid-рендер графа для одной подсистемы."""
    lines = [
        f"# Граф 1 — подсистема «{subsystem}»",
        "",
        "```mermaid",
        "graph LR",
    ]
    # Все изделия этой подсистемы
    sub_nodes = [n for n in g["nodes"] if n.get("subsystem") == subsystem]
    sub_ids = {n["id"] for n in sub_nodes}
    # Материалы, используемые этими изделиями
    mat_ids: set[str] = set()
    for e in g["edges"]:
        if e["type"] == "uses_material" and e["src"] in sub_ids:
            mat_ids.add(e["dst"])
    # Ограничим для читаемости: если материалов > 15 — только топ-5
    mat_list = sorted(mat_ids)
    if len(mat_list) > 15:
        # взять 5 самых часто используемых
        cnt: dict[str, int] = defaultdict(int)
        for e in g["edges"]:
            if e["type"] == "uses_material" and e["dst"] in mat_ids:
                cnt[e["dst"]] += 1
        mat_list = sorted(cnt.items(), key=lambda x: -x[1])[:5]
        mat_list = [m[0] for m in mat_list]
        truncated = True
    else:
        truncated = False
    # Рёбра между изделиями и материалами
    for n in sub_nodes:
        safe = n["id"].replace(" ", "_").replace("-", "_")
        short = n["label"] or n["id"]
        if len(short) > 30:
            short = short[:27] + "…"
        lines.append(f"    {safe}[{short}]")
    for m in mat_list:
        safe = m.replace(" ", "_").replace("-", "_").replace("₂", "2")
        m_node = next((n for n in g["nodes"] if n["id"] == m), None)
        if m_node:
            label = m_node["label"]
            if len(label) > 25:
                label = label[:22] + "…"
            lines.append(f"    {safe}[{label}]")
    # Рёбра
    for e in g["edges"]:
        if e["type"] != "uses_material":
            continue
        if e["src"] in sub_ids and e["dst"] in set(mat_list):
            s = e["src"].replace(" ", "_").replace("-", "_")
            d = e["dst"].replace(" ", "_").replace("-", "_").replace("₂", "2")
            lines.append(f"    {s} -->|материал| {d}")
    lines.append("```")
    if truncated:
        lines.append("")
        lines.append("_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._")
    # Таблица материалов с количеством использований
    cnt2: dict[str, int] = defaultdict(int)
    for e in g["edges"]:
        if e["type"] == "uses_material" and e["src"] in sub_ids:
            cnt2[e["dst"]] += 1
    if cnt2:
        lines.append("")
        lines.append("| Материал | Используется в частях |")
        lines.append("|---|---:|")
        for m, c in sorted(cnt2.items(), key=lambda x: -x[1])[:15]:
            m_label = next((n["label"] for n in g["nodes"] if n["id"] == m), m)
            lines.append(f"| `{m_label}` | {c} |")
    return "\n".join(lines) + "\n"


def graph1_mermaid_materials(g: dict) -> str:
    """Mermaid-рендер: 10 самых используемых материалов."""
    cnt: dict[str, int] = defaultdict(int)
    for e in g["edges"]:
        if e["type"] == "uses_material":
            cnt[e["dst"]] += 1
    top = sorted(cnt.items(), key=lambda x: -x[1])[:10]
    lines = [
        "# Граф 1 — топ-10 материалов по использованию",
        "",
        "```mermaid",
        "graph LR",
        "    ROOT((10 материалов))",
    ]
    for i, (mid, c) in enumerate(top):
        m_node = next((n for n in g["nodes"] if n["id"] == mid), None)
        label = m_node["label"] if m_node else mid
        if len(label) > 20:
            label = label[:17] + "…"
        safe = f"M{i}"
        lines.append(f"    {safe}[{label}<br/>{c} исп.]")
        lines.append(f"    ROOT --> {safe}")
    lines.append("```")
    lines.append("")
    lines.append("| Материал | Используется в частях |")
    lines.append("|---|---:|")
    for mid, c in top:
        m_node = next((n for n in g["nodes"] if n["id"] == mid), None)
        label = m_node["label"] if m_node else mid
        lines.append(f"| `{label}` | {c} |")
    return "\n".join(lines) + "\n"


# ============================================================================
# ГРАФ 2 — мета-граф (скрипты ↔ спецификация ↔ индексы ↔ документация)
# ============================================================================

def graph2_build() -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []
    by_id: dict[str, dict] = {}
    _seen_edges: set[tuple[str, str, str]] = set()

    def add_node(nid: str, ntype: str, label: str, path: str = ""):
        if nid in by_id:
            return
        node = {"id": nid, "type": ntype, "label": label, "path": path}
        nodes.append(node)
        by_id[nid] = node

    def add_edge(src: str, dst: str, etype: str, meta: dict | None = None):
        key = (src, dst, etype)
        if key in _seen_edges:
            return
        _seen_edges.add(key)
        edges.append({"src": src, "dst": dst, "type": etype, "meta": meta or {}})

    # 1) Скрипты
    if SCRIPTS_DIR.exists():
        for f in sorted(SCRIPTS_DIR.glob("*.py")):
            nid = f"script:{f.name}"
            # читаем docstring
            text = f.read_text(encoding="utf-8")
            doc = ""
            m = re.search(r'^"""(.*?)"""', text, re.DOTALL | re.MULTILINE)
            if m:
                doc = m.group(1).strip().split("\n")[0][:80]
            add_node(nid, "script", f.name, str(f.relative_to(REPO)))

            # imports между скриптами
            for m2 in re.finditer(r"^\s*(?:from|import)\s+(\w+)", text, re.MULTILINE):
                mod = m2.group(1)
                tgt_path = SCRIPTS_DIR / f"{mod}.py"
                if tgt_path.exists():
                    tgt = f"script:{mod}.py"
                    add_edge(nid, tgt, "imports")

            # генерируемые индексы: ищем rglob/write_text с упоминаниями
            for m2 in re.finditer(r'(?:rglob|glob|write_text|open)\s*\(\s*[fr]?["\']([^"\']+?)["\']', text):
                pat = m2.group(1)
                if any(k in pat for k in ["_иерархия", "_индекс", "_CATALOG", "_список"]):
                    # ищем соответствующий файл
                    for cand in REPO.rglob("*.md"):
                        if cand.name in pat or any(k in cand.name for k in ["_иерарх", "_индекс", "_CATALOG", "_список"]):
                            tgt = f"index:{cand.relative_to(REPO)}"
                            if tgt not in by_id:
                                add_node(tgt, "index", cand.name, str(cand.relative_to(REPO)))
                            add_edge(nid, tgt, "generates")
                            break

    # 2) Спецификация
    if SPEC_FILE.exists():
        add_node("spec:SkyNet_PROMPT_v9.31.md", "spec", "SkyNet_PROMPT_v9.31.md",
                 str(SPEC_FILE.relative_to(REPO)))
        spec_text = SPEC_FILE.read_text(encoding="utf-8")
        # секции §
        for m in re.finditer(r"^### (§[0-9.]+[^\n]*)$", spec_text, re.MULTILINE):
            title = m.group(1).strip()
            line_no = spec_text[:m.start()].count("\n") + 1
            sid = f"section:{title[:60]}"
            add_node(sid, "spec_section", title,
                     f"SkyNet_PROMPT_v9.31.md:{line_no}")
            add_edge(sid, "spec:SkyNet_PROMPT_v9.31.md", "part_of")

    # 3) Каталог
    if CATALOG_FILE.exists():
        add_node("catalog:scripts/_CATALOG.md", "catalog", "scripts/_CATALOG.md",
                 str(CATALOG_FILE.relative_to(REPO)))
        cat_text = CATALOG_FILE.read_text(encoding="utf-8")
        # упоминания скриптов в каталоге
        for s in by_id:
            if s.startswith("script:"):
                fname = s.split(":", 1)[1]
                if fname in cat_text:
                    add_edge("catalog:scripts/_CATALOG.md", s, "references")

    # 4) README
    if README_FILE.exists():
        add_node("readme:README.md", "readme", "README.md",
                 str(README_FILE.relative_to(REPO)))
        rm_text = README_FILE.read_text(encoding="utf-8")
        for s in by_id:
            if s.startswith("script:"):
                fname = s.split(":", 1)[1]
                if fname in rm_text:
                    add_edge("readme:README.md", s, "documents")

    # 5) Концепт-документы
    for sub in ["концепции", "гипотезы", "улучшения", "требования_к_ии", "диалог"]:
        d = REPO / sub
        if d.exists():
            for f in sorted(d.glob("*.md")):
                nid = f"concept:{sub}/{f.name}"
                add_node(nid, "concept_doc", f.name, str(f.relative_to(REPO)))
                # упоминает ли какие-то скрипты/метрики
                txt = f.read_text(encoding="utf-8")
                for s in by_id:
                    if s.startswith("script:"):
                        fname = s.split(":", 1)[1]
                        if fname in txt:
                            add_edge(nid, s, "describes")

    # 6) implements: script → spec_section (по метрикам FXX в docstring)
    for n in nodes:
        if n["type"] != "script":
            continue
        sfile = REPO / n["path"]
        if not sfile.exists():
            continue
        stext = sfile.read_text(encoding="utf-8")
        metrics_in_script = set(re.findall(r"\bF\d+[a-z]?\b", stext))
        for sec in nodes:
            if sec["type"] != "spec_section":
                continue
            sec_title = sec["label"]
            # если в заголовке секции есть метрика FXX и скрипт её упоминает
            for m in sorted(metrics_in_script):  # sorted: порядок рёбер детерминирован (set-итерация зависит от hashseed)
                if m in sec_title:
                    add_edge(n["id"], sec["id"], "implements")

    return {
        "kind": "graph2_meta",
        "description": "Мета-граф: скрипты ↔ спецификация ↔ индексы ↔ документация",
        "nodes": nodes,
        "edges": edges,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "by_type": {t: sum(1 for n in nodes if n["type"] == t) for t in sorted(set(n["type"] for n in nodes))},
        },
    }


def graph2_mermaid(g: dict) -> str:
    lines = [
        "# Граф 2 — мета-граф репозитория",
        "",
        "```mermaid",
        "graph TB",
    ]
    # Группируем узлы по типам
    for n in g["nodes"]:
        nid = n["id"].replace(":", "_").replace("/", "_").replace(".", "_").replace(" ", "_")
        label = n["label"][:40]
        shape_a, shape_b = "((", "))" if n["type"] == "script" else ("[", "]")
        if n["type"] == "spec":
            shape_a, shape_b = "{{", "}}"
        elif n["type"] == "spec_section":
            shape_a, shape_b = "(/", "/)"
        elif n["type"] == "index":
            shape_a, shape_b = "[/", "/]"
        elif n["type"] == "catalog":
            shape_a, shape_b = "[[", "]]"
        lines.append(f"    {nid}{shape_a}\"{label}\"{shape_b}")
    # Рёбра (ограничиваем для читаемости)
    edge_count: dict[tuple[str, str, str], int] = defaultdict(int)
    for e in g["edges"]:
        key = (e["src"], e["dst"], e["type"])
        edge_count[key] += 1
    for (src, dst, etype), c in sorted(edge_count.items(), key=lambda x: -x[1])[:50]:
        s = src.replace(":", "_").replace("/", "_").replace(".", "_").replace(" ", "_")
        d = dst.replace(":", "_").replace("/", "_").replace(".", "_").replace(" ", "_")
        lines.append(f"    {s} -.->|{etype}| {d}")
    lines.append("```")
    lines.append("")
    lines.append(f"_Узлов: {len(g['nodes'])}, рёбер: {len(g['edges'])} (показано топ-50)._")
    lines.append("")
    lines.append("| Тип узла | Количество |")
    lines.append("|---|---:|")
    for t, c in sorted(g["stats"]["by_type"].items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} |")
    return "\n".join(lines) + "\n"


# ============================================================================
# ГРАФ 3 — traceability (метрика → скрипт → файл)
# ============================================================================

def graph3_build() -> dict:
    nodes: list[dict] = []
    edges: list[dict] = []
    by_id: dict[str, dict] = {}
    _seen_edges: set[tuple[str, str, str]] = set()

    def add_node(nid: str, ntype: str, label: str, path: str = ""):
        if nid in by_id:
            return
        node = {"id": nid, "type": ntype, "label": label, "path": path}
        nodes.append(node)
        by_id[nid] = node

    def add_edge(src: str, dst: str, etype: str, meta: dict | None = None):
        # Дедупликация: один и тот же (src, dst, type) добавляем только один раз.
        # Раньше одно и то же упоминание F-метрики в 5 местах кода порождало 5 одинаковых рёбер.
        key = (src, dst, etype)
        if key in _seen_edges:
            return
        _seen_edges.add(key)
        edges.append({"src": src, "dst": dst, "type": etype, "meta": meta or {}})

    # 1) Спецификация — извлечь все метрики FXX, PXX и их контекст
    spec_text = SPEC_FILE.read_text(encoding="utf-8")
    metrics_in_spec: dict[str, str] = {}
    # Метрики в заголовках секций
    for m in re.finditer(r"^(###\s+§[0-9.]+.*?)(?:$|\n)", spec_text, re.MULTILINE):
        sec = m.group(1).strip()
        for mm in re.finditer(r"\b(F\d+[a-z]?|P\d+[a-z]?)\b", sec):
            mid = mm.group(1)
            metrics_in_spec[mid] = sec

    # Метрики, упомянутые в тексте спецификации (не только в заголовках)
    for mm in re.finditer(r"\b(F\d+[a-z]?|P\d+[a-z]?)\b", spec_text):
        mid = mm.group(1)
        if mid not in metrics_in_spec:
            # взять контекст — текущую §-секцию
            pos = mm.start()
            # найти ближайший предыдущий заголовок ###
            before = spec_text[:pos]
            sec_match = None
            for sm in re.finditer(r"^### (§[0-9.]+[^\n]*)$", before, re.MULTILINE):
                sec_match = sm.group(1).strip()
            metrics_in_spec[mid] = sec_match or "(без секции)"

    for mid, sec in metrics_in_spec.items():
        add_node(mid, "metric", mid)
        # секция, где упоминается
        sec_id = f"section:{sec[:60]}"
        if sec_id not in by_id:
            add_node(sec_id, "spec_section", sec, f"SkyNet_PROMPT_v9.31.md")
        add_edge(mid, sec_id, "defined_in")

    # 2) Скрипты — какие метрики они валидируют
    for f in sorted(SCRIPTS_DIR.glob("*.py")):
        sid = f"script:{f.name}"
        if sid not in by_id:
            add_node(sid, "script", f.name, str(f.relative_to(REPO)))
        stext = f.read_text(encoding="utf-8")
        # Метрики в docstring или комментариях
        script_metrics = set(re.findall(r"\b(F\d+[a-z]?|P\d+[a-z]?)\b", stext))
        # field contracts fc_*
        contracts = set(re.findall(r"\bfc_[а-яё_]+\b", stext))
        for c in sorted(contracts):  # sorted: детерминизм
            cid = f"contract:{c}"
            if cid not in by_id:
                add_node(cid, "field_contract", c)
            add_edge(sid, cid, "enforces_contract")
        for m in sorted(script_metrics):  # sorted: детерминизм
            if m in by_id:  # только метрики, упомянутые в спецификации
                add_edge(m, sid, "validated_by")
                add_edge(sid, m, "triggers_metric")
        # checks_files: какие файловые паттерны читает
        for m2 in re.finditer(r'(?:rglob|glob)\s*\(\s*[fr]?["\']([^"\']+?)["\']', stext):
            pat = m2.group(1)
            if pat and not pat.startswith("scripts/"):
                pid = f"pattern:{pat}"
                if pid not in by_id:
                    add_node(pid, "file_pattern", pat)
                add_edge(sid, pid, "checks_files")

    # 3) Каталог _CATALOG.md — извлечь связки скрипт → метрика → field_contract.
    #    каталог может упоминать «stub»-скрипты (функции в _stubs.py), которых
    #    нет как отдельных .py файлов — для них узел script:* НЕ создаётся,
    #    метрика всё равно остаётся (она валидируется кодом в _stubs.py через
    #    ребро validated_by на script:_stubs.py, см. шаг 4 ниже).
    def _clean_cell(s: str) -> str:
        """Убирает markdown-обрамление: `code` → code, лишние пробелы."""
        return s.strip().strip("`").strip()

    if CATALOG_FILE.exists():
        cat_text = CATALOG_FILE.read_text(encoding="utf-8")
        for line in cat_text.split("\n"):
            if not line.startswith("|") or "Скрипт" in line or "---" in line:
                continue
            cells = [_clean_cell(c) for c in line.split("|")[1:-1]]
            if len(cells) < 4:
                continue
            fname = cells[0]
            if not fname.endswith(".py"):
                continue
            sid = f"script:{fname}"
            # узел создаём только если .py реально существует на диске;
            # в противном случае это stub, обрабатываемый отдельно (шаг 4).
            if sid not in by_id:
                if not (SCRIPTS_DIR / fname).exists():
                    continue
                add_node(sid, "script", fname, f"scripts/{fname}")
            metrics_str = cells[2] if len(cells) > 2 else ""
            contracts_str = cells[3] if len(cells) > 3 else ""
            for m in re.findall(r"\b(F\d+[a-z]?|P\d+[a-z]?)\b", metrics_str):
                if m in by_id:
                    add_edge(m, sid, "validated_by")
            for c in re.findall(r"\bfc_[а-яё_]+\b", contracts_str):
                cid = f"contract:{c}"
                if cid not in by_id:
                    add_node(cid, "field_contract", c)
                add_edge(sid, cid, "enforces_contract")

    # 4) Stubs — функции в _stubs.py, упомянутые в каталоге как отдельные «скрипты»,
    #    но физически hosted в одном файле. Каждая получает узел stub:<name> с
    #    ребром hosted_in → script:_stubs.py, а метрики из каталога
    #    дополнительно привязываются к script:_stubs.py (так как именно там
    #    код стабов в конечном итоге окажется после реализации).
    stubs_path = SCRIPTS_DIR / "_stubs.py"
    if stubs_path.exists():
        stubs_text = stubs_path.read_text(encoding="utf-8")
        # Маркер `# === X ===` — это stub, если только X.py НЕ существует как отдельный
        # .py файл (например, `# === pipeline_engine ===` помечает РЕАЛЬНЫЙ скрипт,
        # а не stub — для него stub-узел не создаётся).
        all_markers = re.findall(r"^# === (\w+) ===", stubs_text, re.MULTILINE)
        stub_names = [m for m in all_markers if not (SCRIPTS_DIR / f"{m}.py").exists()]
        if stub_names:
            sid_stubs = "script:_stubs.py"
            if sid_stubs not in by_id:
                add_node(sid_stubs, "script", "_stubs.py", "scripts/_stubs.py")
            for name in stub_names:
                stub_id = f"stub:{name}"
                add_node(stub_id, "stub", name, "scripts/_stubs.py")
                add_edge(stub_id, sid_stubs, "hosted_in")
                # Если в каталоге у этого stub'а были метрики — привяжем к script:_stubs.py
                if CATALOG_FILE.exists():
                    cat_text = CATALOG_FILE.read_text(encoding="utf-8")
                    for line in cat_text.split("\n"):
                        if not line.startswith("|") or "Скрипт" in line or "---" in line:
                            continue
                        cells = [_clean_cell(c) for c in line.split("|")[1:-1]]
                        if len(cells) < 4 or cells[0] != f"{name}.py":
                            continue
                        for m in re.findall(r"\b(F\d+[a-z]?|P\d+[a-z]?)\b", cells[2]):
                            if m in by_id:
                                add_edge(m, sid_stubs, "validated_by")
                                add_edge(sid_stubs, m, "triggers_metric")
                        for c in re.findall(r"\bfc_[а-яё_]+\b", cells[3]):
                            cid = f"contract:{c}"
                            if cid not in by_id:
                                add_node(cid, "field_contract", c)
                            add_edge(sid_stubs, cid, "enforces_contract")
                        break

    return {
        "kind": "graph3_traceability",
        "description": "Traceability-граф: метрика → скрипт → файл",
        "nodes": nodes,
        "edges": edges,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "by_type": {t: sum(1 for n in nodes if n["type"] == t) for t in sorted(set(n["type"] for n in nodes))},
        },
    }


def graph3_mermaid(g: dict) -> str:
    lines = [
        "# Граф 3 — прослеживаемость требований",
        "",
        "```mermaid",
        "graph LR",
    ]
    # Предрасчёт (O(n), не O(n²)) — для каждого скрипта множество контрактов
    script_contracts: dict[str, set[str]] = defaultdict(set)
    for e in g["edges"]:
        if e["type"] == "enforces_contract":
            script_contracts[e["src"]].add(e["dst"])
    # Метрики (только те, у которых есть validated_by)
    metrics_with_script: dict[str, set[str]] = defaultdict(set)
    for e in g["edges"]:
        if e["type"] == "validated_by":
            metrics_with_script[e["src"]].add(e["dst"])
    # Топ метрик по числу скриптов
    top = sorted(metrics_with_script.items(), key=lambda x: -len(x[1]))[:20]
    for mid, scripts in top:
        m_safe = mid.replace("-", "_")
        lines.append(f"    {m_safe}([{mid}])")
        for s in sorted(scripts):
            s_safe = s.replace(":", "_").replace("/", "_").replace(".", "_").replace(" ", "_")
            slabel = s.split(":", 1)[1] if ":" in s else s
            lines.append(f"    {s_safe}[{slabel}]")
            lines.append(f"    {m_safe} --> {s_safe}")
    lines.append("```")
    lines.append("")
    lines.append(f"_Показаны топ-20 метрик по числу скриптов-валидаторов (из {len(metrics_with_script)} метрик)._")
    lines.append("")
    # Полная таблица
    lines.append("| Метрика | Скрипты-валидаторы | Контракты |")
    lines.append("|---|---|---|")
    for mid, scripts in sorted(metrics_with_script.items()):
        contracts: set[str] = set()
        for s in scripts:
            contracts |= script_contracts.get(s, set())
        scripts_str = ", ".join(sorted(s.split(":", 1)[1] for s in scripts))
        contracts_str = ", ".join(sorted(c.split(":", 1)[1] for c in contracts)) or "—"
        lines.append(f"| `{mid}` | {scripts_str} | {contracts_str} |")
    return "\n".join(lines) + "\n"


# ============================================================================
# Заполнение обратных рёбер в файлах (миграция)
# ============================================================================

BACKREF_SECTION_TEMPLATES = {
    "material": "## Применение в изделиях",
    "tekhnologia": "## Используется в материалах",
    "standart": "## Применяется в",
    "issledovatelskaya_gruppa": "## Изделия и материалы",
}

# frontmatter-счётчики обратных ссылок (по типу вершины)
BACKREF_COUNT_FIELD = {
    "material": "применяется_в_изделиях_счёт",
    "tekhnologia": "используется_в_материалах_счёт",
    "standart": "применяется_в_изделиях_счёт",
    "issledovatelskaya_gruppa": "изделий_в_группе_счёт",
}


def fill_backrefs(g: dict) -> int:
    """Заполнить обратные рёбра в файлах (разделы '## Применение в изделиях' и т.д.).
    Возвращает количество обновлённых файлов.
    """
    # Построить map: target_id → list of (src_id, src_label, edge_type)
    backrefs: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for e in g["edges"]:
        if e["type"] in ("uses_material", "complies_with", "researched_by"):
            backrefs[e["dst"]].append((e["src"], "", e["type"]))

    # Заполнить метки
    id_to_label = {n["id"]: n["label"] for n in g["nodes"]}
    id_to_path = {n["id"]: n["path"] for n in g["nodes"]}
    for tgt, refs in backrefs.items():
        backrefs[tgt] = [(s, id_to_label.get(s, s), t) for s, _, t in refs]

    updated = 0
    for n in g["nodes"]:
        if n["type"] not in BACKREF_SECTION_TEMPLATES:
            continue
        nid = n["id"]
        npath = REPO / n["path"]
        if not npath.exists():
            continue
        refs = backrefs.get(nid, [])
        section_title = BACKREF_SECTION_TEMPLATES[n["type"]]
        text = npath.read_text(encoding="utf-8")
        # frontmatter-счётчик обратных ссылок (удобно для быстрого grep/сортировки)
        cnt_field = BACKREF_COUNT_FIELD.get(n["type"])
        if cnt_field:
            if re.search(rf"^{cnt_field}:", text, re.M):
                text = re.sub(rf"^{cnt_field}:\s*\d+", f"{cnt_field}: {len(refs)}",
                              text, count=1, flags=re.M)
            else:
                text = text.replace("---\n", f"---\n{cnt_field}: {len(refs)}\n", 1)
        # Проверим, есть ли уже секция
        if section_title in text:
            # заменим содержимое секции
            pattern = re.compile(
                rf"({re.escape(section_title)}\n\n).*?(?=\n## |\Z)",
                re.DOTALL,
            )
            new_body = build_backref_body(refs, n["type"])
            text = pattern.sub(rf"\1{new_body}\n", text)
        else:
            # добавим в конец
            new_body = build_backref_body(refs, n["type"])
            text = text.rstrip() + f"\n\n{section_title}\n\n{new_body}\n"
        npath.write_text(text, encoding="utf-8")
        updated += 1
    return updated


def build_backref_body(refs: list[tuple[str, str, str]], ntype: str) -> str:
    if not refs:
        return "_Обратные ссылки ещё не проставлены._"
    lines = []
    by_edge: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for src, label, etype in refs:
        by_edge[etype].append((src, label))
    type_labels = {
        "uses_material": "Используется в частях/изделиях",
        "complies_with": "Применяется в файлах",
        "researched_by": "Исследуется в группах",
    }
    for etype, items in by_edge.items():
        lines.append(f"**{type_labels.get(etype, etype)}:**")
        for src, label in sorted(items):
            lines.append(f"- `{src}` — {label}")
        lines.append("")
    return "\n".join(lines).rstrip()


# ============================================================================
# Main
# ============================================================================

def source_fingerprint() -> str:
    """Хэш всех входных данных генераторов (контент, не mtime).

    Оптимизация (2026-11-05): регенерация графов на каждом коммите занимала ~3.6 с
    даже когда данные не менялись (например, правки только в graphs/ или docs).
    Теперь: если контент-хэш входов совпал с кэшем и выходы существуют — пропускаем.
    Полная пересборка остаётся при любом изменении данных (корректность важнее скорости).
    """
    h = hashlib.sha256()
    excl_dirs = {'.git', 'graphs', 'архив'}
    count = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = sorted(d for d in dirs if d not in excl_dirs)
        for fn in sorted(files):
            if not fn.endswith(('.md', '.py', '.json', '.yaml')):
                continue
            p = Path(root) / fn
            try:
                h.update(str(p.relative_to(REPO)).encode())
                h.update(b'\0')
                h.update(hashlib.sha256(p.read_bytes()).digest())
                count += 1
            except OSError:
                continue
    return h.hexdigest() + f':{count}'


def outputs_exist() -> bool:
    """Все ожидаемые выходные файлы на месте?"""
    required = [
        GRAPHS_DIR / 'graph1_data.json',
        GRAPHS_DIR / 'graph2_meta.json',
        GRAPHS_DIR / 'graph3_traceability.json',
    ]
    return all(p.exists() for p in required)


def main() -> int:
    ap = argparse.ArgumentParser(description="SkyNet — генератор графов")
    ap.add_argument("--all", action="store_true", help="Сгенерировать все 3 графа")
    ap.add_argument("--force", action="store_true", help="Игнорировать fingerprint-кэш")
    ap.add_argument("--graph", type=int, choices=[1, 2, 3], help="Сгенерировать только указанный граф")
    ap.add_argument("--mermaid", action="store_true", help="Также сгенерировать Mermaid-рендеры")
    ap.add_argument("--fill-backrefs", action="store_true",
                    help="Заполнить обратные рёбра в файлах (одноразовая миграция)")
    args = ap.parse_args()

    if args.fill_backrefs:
        g1 = graph1_build()
        n = fill_backrefs(g1)
        print(f"Заполнено обратных рёбер в {n} файлах")
        return 0

    if not args.all and args.graph is None:
        ap.error("укажите --all или --graph N")

    GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
    MERMAID_DIR.mkdir(parents=True, exist_ok=True)

    # Инкрементальный режим: --all без изменений входов → пропуск
    fp_file = GRAPHS_DIR / '.source_fingerprint'
    if args.all and not args.force:
        fp = source_fingerprint()
        cached = fp_file.read_text(encoding='utf-8').strip() if fp_file.exists() else ''
        if fp == cached and outputs_exist():
            print("Графы актуальны (fingerprint совпал) — регенерация пропущена")
            return 0

    regenerated = False
    if args.all or args.graph == 1:
        regenerated = True
        print("Граф 1 (данные)...")
        g1 = graph1_build()
        (GRAPHS_DIR / "graph1_data.json").write_text(
            json.dumps(g1, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"  узлов: {g1['stats']['nodes']}, рёбер: {g1['stats']['edges']}")
        if args.mermaid or args.all:
            (MERMAID_DIR / "graph1_overview.md").write_text(graph1_mermaid_overview(g1), encoding="utf-8")
            (MERMAID_DIR / "graph1_materials.md").write_text(graph1_mermaid_materials(g1), encoding="utf-8")
            for sub in SUBSYSTEMS:
                # проверим, есть ли изделия в этой подсистеме
                if any(n["subsystem"] == sub and n["type"] == "izdelie" for n in g1["nodes"]):
                    safe = sub.replace(" ", "_")
                    (MERMAID_DIR / f"graph1_{safe}.md").write_text(
                        graph1_mermaid_subsystem(g1, sub), encoding="utf-8"
                    )
            print("  Mermaid-рендеры записаны")

    if args.all or args.graph == 2:
        regenerated = True
        print("Граф 2 (мета)...")
        g2 = graph2_build()
        (GRAPHS_DIR / "graph2_meta.json").write_text(
            json.dumps(g2, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"  узлов: {g2['stats']['nodes']}, рёбер: {g2['stats']['edges']}")
        if args.mermaid or args.all:
            (MERMAID_DIR / "graph2_meta.md").write_text(graph2_mermaid(g2), encoding="utf-8")
            print("  Mermaid-рендер записан")

    if args.all or args.graph == 3:
        regenerated = True
        print("Граф 3 (traceability)...")
        g3 = graph3_build()
        (GRAPHS_DIR / "graph3_traceability.json").write_text(
            json.dumps(g3, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"  узлов: {g3['stats']['nodes']}, рёбер: {g3['stats']['edges']}")
        if args.mermaid or args.all:
            (MERMAID_DIR / "graph3_traceability.md").write_text(graph3_mermaid(g3), encoding="utf-8")
            print("  Mermaid-рендер записан")

    # Сохранить fingerprint только после ПОЛНОЙ регенерации (--all),
    # чтобы частичные запуски (--graph N) не кэшировались как полные.
    if args.all and regenerated:
        (GRAPHS_DIR / '.source_fingerprint').write_text(source_fingerprint(), encoding='utf-8')

    return 0


if __name__ == "__main__":
    sys.exit(main())
