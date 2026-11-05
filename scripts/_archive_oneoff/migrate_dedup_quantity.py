#!/usr/bin/env python3
"""SkyNet Dedup Migration — v9.35

Объединяет within-product дубликаты (левая+правая, _1+_2) в один файл часть_*
с полем количество=N. Это решает:
  • Дублирование файлов с идентичными данными (масса, габариты, материал)
  • Анти-шаблон "шаблонная подстановка" (F25, F26)
  • Согласованность с принципом P085 (канонизация — не дублировать идентичные сущности)

Алгоритм:
  1. Найти все группы часть_* с одинаковым (родитель, подтип) и идентичными данными
     (масса + габариты + материал) — N≥2 файлов в одной группе
  2. Выбрать survivor — лексикографически первый id
  3. Установить survivor.количество = N (если было 1)
  4. Удалить остальные файлы из группы
  5. Обновить родительский файл:
     - дочерние_части: убрать удалённые id
     - материалы_частей: убрать удалённые id, суммировать их доля_массы в survivor
  6. Обновить body markdown survivor'а — отметить "×N" в заголовке и описании

Запуск:
  python scripts/migrate_dedup_quantity.py            # dry-run (только отчёт)
  python scripts/migrate_dedup_quantity.py --apply    # применить изменения
"""

from __future__ import annotations
import os
import re
import sys
import argparse
import shutil
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import (
    read_yaml_frontmatter,
    load_all_izdeliya,
    SKYNET_REPO,
)

IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"
TODAY = "2026-11-05"


# ============================================================================
# ПОИСК ГРУПП ДУБЛИКАТОВ
# ============================================================================

def find_dup_groups(izdeliya: dict[str, dict]) -> list[tuple[str, str, list[str]]]:
    """Найти группы часть_* с одинаковым (родитель, подтип) и идентичными данными."""
    by_key: dict[tuple[str, str], list[tuple[str, dict]]] = defaultdict(list)
    for izd_id, data in izdeliya.items():
        if not izd_id.startswith("часть_"):
            continue
        parent = data.get("родитель", "") or ""
        subtype = data.get("подтип", "") or ""
        if not parent or not subtype:
            continue
        by_key[(parent, subtype)].append((izd_id, data))

    groups = []
    for (parent, subtype), items in by_key.items():
        if len(items) < 2:
            continue
        sigs = set()
        for pid, d in items:
            basic = d.get("основные", {})
            if not isinstance(basic, dict):
                basic = {}
            dims = basic.get("габариты_mm", {})
            if not isinstance(dims, dict):
                dims = {}
            mass = basic.get("масса_kg")
            mats = d.get("материалы_частей", [])
            mat = ""
            if isinstance(mats, list) and mats:
                m0 = mats[0]
                if isinstance(m0, dict):
                    mat = str(m0.get("материал", ""))
            sig = (dims.get("l"), dims.get("w"), dims.get("h"), mass, mat)
            sigs.add(sig)

        if len(sigs) == 1:
            ids = sorted(pid for pid, _ in items)
            groups.append((parent, subtype, ids))
    return groups


# ============================================================================
# ОБНОВЛЕНИЕ SURVIVOR ФАЙЛА
# ============================================================================

def update_survivor_file(
    survivor_path: Path,
    survivor_id: str,
    n: int,
    sibling_ids: list[str],
) -> bool:
    """Обновить survivor файл: добавить количество=N, обновить body."""
    data, yaml_text, body = read_yaml_frontmatter(survivor_path)
    if not data:
        return False

    # 1. Добавить/обновить количество в YAML
    if re.search(r"^количество:\s*\d+", yaml_text, re.MULTILINE):
        new_yaml = re.sub(
            r"^количество:\s*\d+",
            f"количество: {n}",
            yaml_text,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Добавить после "родитель: ..." (или после id)
        if re.search(r"^родитель:.*$", yaml_text, re.MULTILINE):
            new_yaml = re.sub(
                r"^(родитель:.*\n)",
                rf"\1количество: {n}\n",
                yaml_text,
                count=1,
                flags=re.MULTILINE,
            )
        else:
            new_yaml = re.sub(
                r"^(id:.*\n)",
                rf"\1количество: {n}\n",
                yaml_text,
                count=1,
                flags=re.MULTILINE,
            )

    # 2. Обновить заголовок в body — добавить "(×N)"
    title_pattern = r"^(# Часть:\s*)" + re.escape(survivor_id) + r"\s*$"
    if re.search(title_pattern, body, re.MULTILINE):
        body = re.sub(
            title_pattern,
            rf"\g<1>{survivor_id} (×{n})",
            body,
            count=1,
            flags=re.MULTILINE,
        )

    # 3. Обновить дату_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )

    # 4. Добавить примечание в body про объединение
    if "## Примечание о количестве" not in body:
        siblings_str = ", ".join(f"`{s}`" for s in sibling_ids)
        note = f"""

## Примечание о количестве

Эта часть представляет собой **{n} идентичных экземпляра** (поле `количество: {n}`).
Ранее каждый экземпляр был отдельным файлом ({siblings_str}); объединено в v9.35
для устранения дублирования данных (принцип P085 — канонизация).
Масса и габариты указаны за **один** экземпляр; `доля_массы_родителя` — суммарная.
"""
        body = body.rstrip() + "\n" + note

    # 5. Склеить обратно — добавить закрывающий --- между YAML и body
    new_text = "---\n" + new_yaml + "\n---\n" + body
    if not new_text.endswith("\n"):
        new_text += "\n"
    survivor_path.write_text(new_text, encoding="utf-8")
    return True


# ============================================================================
# ОБНОВЛЕНИЕ РОДИТЕЛЬСКОГО ФАЙЛА
# ============================================================================

def update_parent_file(
    parent_path: Path,
    survivor_id: str,
    deleted_ids: list[str],
    subtype: str,
) -> bool:
    """Обновить родительский файл:
       - дочерние_части: убрать deleted_ids
       - материалы_частей: убрать deleted_ids, их доля_массы суммируется в survivor
    """
    if not parent_path.exists():
        return False

    data, yaml_text, body = read_yaml_frontmatter(parent_path)
    if not data:
        return False

    new_yaml = yaml_text

    # 1. Убрать deleted_ids из дочерние_части
    children_pattern = re.compile(
        r"^(дочерние_части:\s*\n(?:  - [^\n]+\n)*)",
        re.MULTILINE,
    )
    m = children_pattern.search(new_yaml)
    if m:
        block = m.group(1)
        for did in deleted_ids:
            block = re.sub(
                r"^  - " + re.escape(did) + r"\s*$\n",
                "",
                block,
                flags=re.MULTILINE,
            )
        new_yaml = new_yaml[: m.start()] + block + new_yaml[m.end() :]

    # 2. Обновить материалы_частей: линейный разбор по записям.
    lines = new_yaml.split("\n")
    out_lines = []
    i = 0
    deleted_share_sum = 0.0
    survivor_share_total = 0.0
    while i < len(lines):
        line = lines[i]
        if line.startswith("материалы_частей:"):
            out_lines.append(line)
            i += 1
            # Парсить записи: "  - часть: X" + следующие строки "    поле: значение"
            while i < len(lines):
                rec_line = lines[i]
                if rec_line.startswith("  - часть:"):
                    rec_lines = [rec_line]
                    i += 1
                    while i < len(lines) and (lines[i].startswith("    ") or lines[i] == ""):
                        rec_lines.append(lines[i])
                        i += 1
                    # Удалить trailing пустые строки (вернуть их в поток)
                    while rec_lines and rec_lines[-1] == "":
                        rec_lines.pop()
                        i -= 1
                    # Парсить часть + материал + доля_массы
                    pid_match = re.match(r"^  - часть:\s*(\S+)", rec_lines[0])
                    if not pid_match:
                        out_lines.extend(rec_lines)
                        continue
                    pid = pid_match.group(1).strip()
                    material = ""
                    share = 0.0
                    extra_lines = []
                    for rl in rec_lines[1:]:
                        m_mat = re.match(r"^    материал:\s*(\S+)", rl)
                        m_share = re.match(r"^    доля_массы:\s*([0-9.eE+-]+)", rl)
                        if m_mat:
                            material = m_mat.group(1).strip()
                        elif m_share:
                            share = float(m_share.group(1))
                        else:
                            extra_lines.append(rl)

                    if pid == survivor_id:
                        survivor_share_total += share
                        out_lines.append(f"  - часть: {pid}")
                        out_lines.append(f"    материал: {material}")
                        for el in extra_lines:
                            out_lines.append(el)
                        out_lines.append(f"    доля_массы: __PENDING__")
                    elif pid in deleted_ids:
                        deleted_share_sum += share
                    else:
                        out_lines.extend(rec_lines)
                else:
                    # Вышли из блока материалы_частей
                    break
            # Заменить __PENDING__ на финальное значение
            final_share = survivor_share_total + deleted_share_sum
            for j in range(len(out_lines) - 1, -1, -1):
                if out_lines[j] == "    доля_массы: __PENDING__":
                    out_lines[j] = f"    доля_массы: {final_share:.4f}"
                    break
            # Добавить текущую non-indented строку (она завершает блок)
            if i < len(lines):
                out_lines.append(lines[i])
                i += 1
        else:
            out_lines.append(line)
            i += 1

    new_yaml = "\n".join(out_lines)

    # 3. Обновить дату_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )

    new_text = "---\n" + new_yaml + "\n---\n" + body
    if not new_text.endswith("\n"):
        new_text += "\n"
    parent_path.write_text(new_text, encoding="utf-8")
    return True


# ============================================================================
# MAIN
# ============================================================================

def find_part_path(izd_id: str) -> Path | None:
    """Найти путь к файлу часть_<id>/_index.md."""
    for sub in IZDELIYA_DIR.iterdir():
        if not sub.is_dir():
            continue
        part_dir = sub / izd_id
        if (part_dir / "_index.md").exists():
            return part_dir / "_index.md"
        for sub2 in sub.iterdir():
            if not sub2.is_dir():
                continue
            part_dir = sub2 / izd_id
            if (part_dir / "_index.md").exists():
                return part_dir / "_index.md"
    return None


def find_parent_path(parent_id: str) -> Path | None:
    """Найти путь к файлу родителя."""
    if not parent_id:
        return None
    if parent_id.startswith("izdelie_"):
        short_full = parent_id[len("izdelie_") :]
        candidates = []
        if short_full.startswith("SkyNet-"):
            short = short_full[len("SkyNet-") :]
            candidates.append(short.lower())
            name_map = {
                "T800": "t800",
                "T1000": "t1000",
                "T1001": "t1001",
                "TX": "t_x",
                "Rev9": "rev9",
                "HKAerial": "hk_aerial",
                "HKTank": "hktank",
                "T600": "t600",
                "T850": "t850",
                "MarcusWright": "marcuswright",
                "Cameron": "cameron",
            }
            if short in name_map:
                candidates.append(name_map[short])
            candidates.append(short.lower().replace("-", "_"))
        candidates.append(short_full.lower().replace("-", "_"))

        for cand in candidates:
            for sub in IZDELIYA_DIR.iterdir():
                if not sub.is_dir():
                    continue
                parent_dir = sub / cand
                if (parent_dir / "_index.md").exists():
                    try:
                        text = (parent_dir / "_index.md").read_text(encoding="utf-8")
                        if f"id: {parent_id}" in text:
                            return parent_dir / "_index.md"
                    except Exception:
                        pass
    elif parent_id.startswith("SkyNet-"):
        short = parent_id[len("SkyNet-") :].lower().replace("-", "_")
        model_map = {
            "t800": "t800.md",
            "t1000": "t1000.md",
            "t1001": "t1001.md",
            "tx": "t_x.md",
            "rev9": "rev9.md",
            "hkaerial": "hk_aerial.md",
            "hktank": "hk_tank.md",
            "t600": "t600.md",
            "t850": "t850.md",
            "marcuswright": "marcus_wright.md",
            "cameron": "cameron_phillips.md",
        }
        fname = model_map.get(short)
        if fname:
            path = SKYNET_REPO / "фантастические данные" / "модели" / fname
            if path.exists():
                return path
    return None


def main():
    parser = argparse.ArgumentParser(description="SkyNet Dedup Migration v9.35")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Применить изменения (без флага — dry-run)",
    )
    args = parser.parse_args()

    print("=== SkyNet Dedup Migration v9.35 ===")
    print(f"Режим: {'APPLY' if args.apply else 'DRY-RUN'}")
    print()

    izdeliya = load_all_izdeliya()
    print(f"Загружено файлов: {len(izdeliya)}")

    groups = find_dup_groups(izdeliya)
    print(f"Найдено групп дубликатов: {len(groups)}")
    print()

    total_deleted = 0
    total_updated = 0
    total_files = 0
    errors = []

    for parent_id, subtype, ids in groups:
        n = len(ids)
        survivor_id = ids[0]
        deleted_ids = ids[1:]
        total_files += n

        print(f"  Group: parent={parent_id} subtype={subtype}")
        print(f"    survivor: {survivor_id}")
        print(f"    delete:   {deleted_ids}")

        survivor_path = find_part_path(survivor_id)
        if not survivor_path:
            errors.append(f"Не найден путь survivor: {survivor_id}")
            print(f"    ! Survivor path not found")
            continue

        parent_path = find_parent_path(parent_id)
        if not parent_path:
            errors.append(f"Не найден путь родителя: {parent_id}")
            print(f"    ! Parent path not found")
            continue

        if args.apply:
            ok = update_survivor_file(survivor_path, survivor_id, n, deleted_ids)
            if not ok:
                errors.append(f"Не удалось обновить survivor: {survivor_id}")
                continue

            for did in deleted_ids:
                dup_path = find_part_path(did)
                if dup_path and dup_path.exists():
                    dup_dir = dup_path.parent
                    shutil.rmtree(dup_dir)
                    total_deleted += 1
                    print(f"    - deleted: {did}")

            update_parent_file(parent_path, survivor_id, deleted_ids, subtype)
            total_updated += 1
            print(f"    ✓ updated parent: {parent_id}")

    print()
    print(f"=== Сводка ===")
    print(f"  Групп обработано: {total_updated}/{len(groups)}")
    print(f"  Файлов в группах: {total_files}")
    print(f"  Файлов удалено (дубликаты): {total_deleted}")
    if errors:
        print(f"  Ошибки: {len(errors)}")
        for e in errors:
            print(f"    - {e}")

    if not args.apply:
        print()
        print("Это был DRY-RUN. Для применения запустите с --apply")


if __name__ == "__main__":
    main()
