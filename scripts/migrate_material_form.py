#!/usr/bin/env python3
"""migrate_material_form.py — добавить `форма` в материалы_частей + построить наследуемые_материалы.

Архитектурное изменение (по запросу пользователя):
  1. Каждая запись материалы_частей должна указывать не только материал, но и его ФОРМУ
     (конкретный вариант: forged_bar / electroplated_foil / 4h-sic_wafer / ...).
  2. Родитель (izdelie) наследует все материалы всех дочерних частей в агрегированном
     виде: наследуемые_материалы (BOM — дедупликация по (материал, форма), сумма долей,
     источники_частей).

Пилот: izdelie_ni-63_betavoltaik_4h-sic (5 частей + родитель).
Идемпотентно (F20): повторный запуск не меняет файлы, где форма уже указана.

Usage:
    python3 scripts/migrate_material_form.py --izdelie izdelie_ni-63_betavoltaik_4h-sic
    python3 scripts/migrate_material_form.py --izdelie izdelie_ni-63_betavoltaik_4h-sic --dry-run
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
IZDELIYA_DIR = REPO / "реальные данные" / "изделия"

# Формы для пилота — на основе вебпоиска Widetronix Firefli-N (commit 1658e03).
# Позже (full-migration): автоматически из оптимальная_структура.применение_по_умолчанию
# или первый ключ варианты_по_применению материала; пока — ручное отображение.
PILOT_FORMAS = {
    "часть_ni-63_betavoltaik_4h-sic_case": {
        "ti-6al-4v": "forged_bar_ams_4928",            # AMS 4928 уже в стандартах части
    },
    "часть_ni-63_betavoltaik_4h-sic_encapsulant": {
        "epoksid_epon_828_teta": "cast_resin_ambient_cure",  # EPON 828 + TETA, комнатная полимеризация
    },
    "часть_ni-63_betavoltaik_4h-sic_isotope": {
        "ni-63": "electroplated_foil",                  # Widetronix: Ni-63 plated on foil
    },
    "часть_ni-63_betavoltaik_4h-sic_sic_diode": {
        "monokristallicheskogo_sic": "4h-sic_monocrystal_wafer",  # betavoltaic 4H-SiC
    },
    "часть_ni-63_betavoltaik_4h-sic_substrate": {
        "monokristallicheskogo_sic": "4h-sic_monocrystal_wafer",
    },
}


def read_frontmatter(path: Path) -> tuple[dict, str, str]:
    """Вернуть (data, yaml_text, body). Робастный парсер (как в валидаторе):
    ищет первый markdown-заголовок `#` — всё до него = YAML, после = body.
    Это корректно обрабатывает случаи, когда закрывающий `---` приклеен к
    значению (напр. `пользовательский ввод---`) или отсутствует.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, "", text
    rest = text[3:].lstrip("\n")
    body_match = re.search(r"^(#+\s+\S)", rest, re.MULTILINE)
    if body_match:
        yaml_section = rest[: body_match.start()].rstrip()
        body = rest[body_match.start() :]
        closing = re.search(r"\n---\s*$", yaml_section, re.MULTILINE)
        if closing:
            yaml_text = yaml_section[: closing.start()].rstrip()
        else:
            yaml_text = yaml_section
    else:
        yaml_text = rest.rstrip()
        closing = re.search(r"\n---\s*$", yaml_text, re.MULTILINE)
        if closing:
            yaml_text = yaml_text[: closing.start()].rstrip()
        body = ""
    try:
        data = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError:
        data = {}
    return data, yaml_text, body


def add_forma_to_entry(yaml_text: str, part_id: str, material_id: str, forma: str) -> str:
    """Вставить `    форма: <forma>` после `    материал: <material_id>` в блоке
    `  - часть: <part_id>` внутри yaml_text. Идемпотентно: если форма уже есть — no-op.
    """
    # Найти блок `  - часть: <part_id>` ... `    материал: <material_id>` ... `    доля_массы:`
    # и вставить форма: перед доля_массы:, если форма: ещё не указана.
    pattern = re.compile(
        r"(  - часть:\s*" + re.escape(part_id) + r"\s*\n"
        r"    материал:\s*" + re.escape(material_id) + r"\s*\n)"
        r"(?!\s*форма:)"  # negative lookahead: форма ещё не вставлена
        r"(    доля_массы:)",
        re.MULTILINE,
    )
    new_text, n = pattern.subn(r"\1    форма: " + forma + r"\n\2", yaml_text, count=1)
    if n == 0:
        # форма уже есть — проверить, что значение совпадает (иначе предупредить)
        check = re.search(
            r"(  - часть:\s*" + re.escape(part_id) + r"\s*\n"
            r"    материал:\s*" + re.escape(material_id) + r"\s*\n"
            r"    форма:\s*(\S+))",
            yaml_text,
        )
        if check and check.group(2) != forma:
            print(f"  ⚠ {part_id}/{material_id}: форма уже '{check.group(2)}', не перезаписываю (хотели '{forma}')")
        # else: форма уже совпадает — тихий no-op
    return new_text


def build_nasleduemue_materialy(parent_data: dict, part_formas: dict) -> list:
    """Построить наследуемые_материалы из дочерних частей.

    part_formas: {part_id: {material_id: forma, ...}, ...}
    parent_data['материалы_частей']: [{часть, материал, доля_массы}, ...] (доли от родителя)

    Возвращает: [{материал, форма, суммарная_доля_массы, источники_частей}, ...]
    Агрегация по (материал, форма) — дедупликация (напр. SiC в diode+substrate).
    """
    # Собираем (part_id → доля_массы от родителя)
    part_shares = {}
    for entry in parent_data.get("материалы_частей", []) or []:
        pid = entry.get("часть")
        share = entry.get("доля_массы")
        if pid and share is not None:
            part_shares[pid] = share

    # Агрегация по (материал, форма)
    agg = {}  # (material, forma) → {сумма, источники}
    for part_id, formas in part_formas.items():
        share = part_shares.get(part_id)
        if share is None:
            # часть не найдена в parent.материалы_частей — пропустить (orphan)
            continue
        for material_id, forma in formas.items():
            key = (material_id, forma)
            if key not in agg:
                agg[key] = {"суммарная_доля_массы": 0.0, "источники_частей": []}
            agg[key]["суммарная_доля_массы"] += share
            agg[key]["источники_частей"].append(part_id)

    # Финальный список — сортировка по убыванию суммарной доли (крупнейший материал первым)
    result = []
    for (material_id, forma), info in sorted(
        agg.items(), key=lambda kv: -kv[1]["суммарная_доля_массы"]
    ):
        result.append(
            {
                "материал": material_id,
                "форма": forma,
                "суммарная_доля_массы": round(info["суммарная_доля_массы"], 6),
                "источники_частей": sorted(info["источники_частей"]),
            }
        )
    return result


def serialize_nasleduemue_materialy(items: list, indent: str = "  ") -> str:
    """Сериализовать наследуемые_материалы в YAML block-style (без ruamel)."""
    if not items:
        return "наследуемые_материалы: []\n"
    lines = ["наследуемые_материалы:"]
    for item in items:
        lines.append(f"{indent}- материал: {item['материал']}")
        lines.append(f"{indent}  форма: {item['форма']}")
        lines.append(f"{indent}  суммарная_доля_массы: {item['суммарная_доля_массы']}")
        srcs = item["источники_частей"]
        if len(srcs) == 1:
            lines.append(f"{indent}  источники_частей: [{srcs[0]}]")
        else:
            lines.append(f"{indent}  источники_частей:")
            for s in srcs:
                lines.append(f"{indent}    - {s}")
    return "\n".join(lines) + "\n"


def insert_nasleduemue_block(yaml_text: str, block_text: str) -> str:
    """Вставить block_text (наследуемые_материалы) после блока материалы_частей.
    Идемпотентно: если наследуемые_материалы уже есть — заменить блок целиком.

    v2: корректное удаление существующего блока — заголовок + ВСЕ последующие
    строки с отступом (элементы блока), до следующего top-level ключа.
    """
    # Удалить существующий блок: `\nнаследуемые_материалы:` + все indented-строки после
    yaml_text = re.sub(
        r"\nнаследуемые_материалы:\s*\n(?:[ \t].*\n)*",
        "\n",
        yaml_text,
    )
    # Также удалить inline-форму `наследуемые_материалы: []` (пустой список)
    yaml_text = re.sub(r"\nнаследуемые_материалы:\s*\[\]\s*\n", "\n", yaml_text)

    # Найти конец блока материалы_частей: последний `    доля_массы:` перед след. top-level
    # Вставить block_text сразу после блока материалы_частей (block_text уже заканчивается \n).
    m = re.search(r"^материалы_частей:\s*\n((?:  .*\n)+)", yaml_text, re.MULTILINE)
    if not m:
        # нет блока материалы_частей — добавить в конец yaml
        return yaml_text.rstrip() + "\n" + block_text
    insert_pos = m.end()
    return yaml_text[:insert_pos] + block_text + yaml_text[insert_pos:]


def migrate_part(part_dir: Path, part_id: str, dry_run: bool) -> tuple[bool, str]:
    """Применить миграцию к части. Возвращает (changed, forma_summary)."""
    idx = part_dir / "_index.md"
    if not idx.exists():
        return False, ""
    data, yaml_text, body = read_frontmatter(idx)
    formas = PILOT_FORMAS.get(part_id, {})
    if not formas:
        return False, ""

    new_text = yaml_text
    for material_id, forma in formas.items():
        new_text = add_forma_to_entry(new_text, part_id, material_id, forma)

    if new_text != yaml_text:
        if not dry_run:
            # rstrip + "\n" гарантирует, что --- (closing) на отдельной строке
            idx.write_text("---\n" + new_text.rstrip() + "\n---\n" + body, encoding="utf-8")
        return True, ", ".join(f"{m}={f}" for m, f in formas.items())
    return False, ""


def migrate_parent(parent_dir: Path, parent_id: str, part_formas: dict, dry_run: bool) -> bool:
    """Применить миграцию к родителю: добавить форма в материалы_частей + наследуемые_материалы."""
    idx = parent_dir / "_index.md"
    if not idx.exists():
        return False
    data, yaml_text, body = read_frontmatter(idx)

    # 1. Добавить форма в parent.материалы_частей (по part_id → первая форма из part_formas)
    new_text = yaml_text
    for entry in data.get("материалы_частей", []) or []:
        pid = entry.get("часть")
        mid = entry.get("материал")
        if not pid or not mid:
            continue
        formas = part_formas.get(pid, {})
        # parent ссылается на generic material (titanium_alloy), но форма — из части
        # Найдём форму по part_id (первую, если материал generic)
        forma = None
        if mid in formas:
            forma = formas[mid]
        elif formas:
            # generic material в parent — взять форму из реального материала части
            forma = next(iter(formas.values()))
        if forma:
            new_text = add_forma_to_entry(new_text, pid, mid, forma)

    # 2. Построить наследуемые_материалы
    items = build_nasleduemue_materialy(data, part_formas)
    block_text = serialize_nasleduemue_materialy(items)
    new_text = insert_nasleduemue_block(new_text, block_text)

    if new_text != yaml_text:
        if not dry_run:
            idx.write_text("---\n" + new_text.rstrip() + "\n---\n" + body, encoding="utf-8")
        return True
    return False


def find_izdelie(izdelie_id: str) -> Path | None:
    """Найти каталог изделия по id."""
    for d in IZDELIYA_DIR.rglob("_index.md"):
        data, _, _ = read_frontmatter(d)
        if data.get("id") == izdelie_id:
            return d.parent
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--izdelie", required=True, help="id изделия (напр. izdelie_ni-63_betavoltaik_4h-sic)")
    ap.add_argument("--dry-run", action="store_true", help="показать изменения без записи")
    args = ap.parse_args()

    parent_dir = find_izdelie(args.izdelie)
    if not parent_dir:
        print(f"❌ Изделие '{args.izdelie}' не найдено", file=sys.stderr)
        sys.exit(1)

    print(f"=== Миграция {args.izdelie} ===")
    print(f"Каталог: {parent_dir}")
    if args.dry_run:
        print("[DRY-RUN] изменения не записываются")

    # 1. Части
    parent_idx = parent_dir / "_index.md"
    pdata, _, _ = read_frontmatter(parent_idx)
    dochernie = pdata.get("дочерние_части", []) or []
    part_formas = {}  # part_id → {material: forma} (собранные из PILOT_FORMAS)
    for part_id in dochernie:
        part_dir = parent_dir / part_id
        if not part_dir.exists():
            print(f"  ⚠ часть {part_id} — каталог не найден, пропуск")
            continue
        formas = PILOT_FORMAS.get(part_id)
        if not formas:
            print(f"  · {part_id}: нет форм в PILOT_FORMAS — пропуск (full-migration добавит default)")
            continue
        changed, summary = migrate_part(part_dir, part_id, args.dry_run)
        part_formas[part_id] = formas
        mark = "✓" if changed else "="
        print(f"  {mark} {part_id}: {summary}" if summary else f"  = {part_id}: уже мигрирован")

    # 2. Родитель
    changed = migrate_parent(parent_dir, args.izdelie, part_formas, args.dry_run)
    mark = "✓" if changed else "="
    print(f"  {mark} {args.izdelie} (родитель): наследуемые_материалы + форма в материалы_частей")

    # 3. Сводка для родителя
    items = build_nasleduemue_materialy(pdata, part_formas)
    if items:
        print(f"\nнаследуемые_материалы ({len(items)} уникальных):")
        for it in items:
            srcs = ", ".join(s.replace("часть_ni-63_betavoltaik_4h-sic_", "..._") for s in it["источники_частей"])
            print(f"  {it['материал']} / {it['форма']} → {it['суммарная_доля_массы']} ({srcs})")


if __name__ == "__main__":
    main()
