#!/usr/bin/env python3
"""SkyNet — миграция #256 вариант D.

Пользователь (2026-11-05) выбрал вариант D из предложенных D/E/F:
  - 11 модельных обёрток + 70 дочерних частей покидают фантастические данные
    (куда они были перенесены вариантом A в коммите 152107e)
  - переносятся в работа и и/изделия/{каркас,вычислительная}/
  - frontmatter обёрток (только корневой _index.md):
      подтип:        модель_обёртка → прочее
      версия:        реальная       → ии-улучшенная
      доступность:   промышленный   → ии_проект
      ии_перепроектирован.статус: false → true
      дополнительные.канон_источник: '<фильмы>' → 'фантастические данные/модели/<модель>.md'
  - frontmatter частей НЕ меняется (они остаются реальными компонентами)
  - ID сохраняются (izdelie_SkyNet-*)
  - относительные md-ссылки пересчитываются от нового местоположения
  - пустые каталоги реализация/ в фантастические данные/модели/<модель>/ удаляются
  - материалы остаются в реальные данные/материалы/ (вещества реальны)
"""
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (src_path_in_repo, dest_subsystem, dest_wrapper_name, canon_model_file)
MAPPING = [
    ("фантастические данные/модели/t600/реализация/t600",                "каркас",         "t600",          "фантастические данные/модели/t600.md"),
    ("фантастические данные/модели/t800/реализация/t800",                "каркас",         "t800",          "фантастические данные/модели/t800.md"),
    ("фантастические данные/модели/t850/реализация/t850",                "каркас",         "t850",          "фантастические данные/модели/t850.md"),
    ("фантастические данные/модели/t_x/реализация/tx",                   "каркас",         "tx",            "фантастические данные/модели/t_x.md"),
    ("фантастические данные/модели/cameron_phillips/реализация/cameron", "каркас",         "cameron",       "фантастические данные/модели/cameron_phillips.md"),
    ("фантастические данные/модели/rev9/реализация/rev9",                 "каркас",         "rev9",          "фантастические данные/модели/rev9.md"),
    ("фантастические данные/модели/marcus_wright/реализация/marcuswright","каркас",         "marcuswright",  "фантастические данные/модели/marcus_wright.md"),
    ("фантастические данные/модели/hk_tank/реализация/hktank",           "каркас",         "hktank",        "фантастические данные/модели/hk_tank.md"),
    ("фантастические данные/модели/hk_aerial/реализация/hkaerial",       "каркас",         "hkaerial",      "фантастические данные/модели/hk_aerial.md"),
    ("фантастические данные/модели/t1000/реализация/t1000",              "вычислительная", "t1000",         "фантастические данные/модели/t1000.md"),
    ("фантастические данные/модели/t1001/реализация/t1001",              "вычислительная", "t1001",         "фантастические данные/модели/t1001.md"),
]

LINK_RE = re.compile(r"\((\.\./[^)\s]*(?:%20[^)\s]*)*)\)")


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"git {' '.join(args)} FAILED:\n{r.stderr}")
        sys.exit(1)
    return r.stdout


def update_wrapper_frontmatter(file_path: Path, canon_model_file: str) -> int:
    """4 подстановки + канон_источник в дополнительные:."""
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print(f"WARN: нет frontmatter в {file_path}")
        return 0
    end = text.index("\n---", 3)
    fm = text[3:end]
    body = text[end + 4:]

    orig = fm
    # 1. подтип: модель_обёртка → прочее
    fm = re.sub(r"^подтип:\s*модель_обёртка\s*$",
                "подтип: прочее", fm, count=1, flags=re.MULTILINE)
    # 2. версия: реальная → ии-улучшенная
    fm = re.sub(r"^версия:\s*реальная\s*$",
                "версия: ии-улучшенная", fm, count=1, flags=re.MULTILINE)
    # 3. доступность: промышленный → ии_проект
    fm = re.sub(r"^доступность:\s*промышленный\s*$",
                "доступность: ии_проект", fm, count=1, flags=re.MULTILINE)
    # 4. ии_перепроектирован.статус: false → true
    fm = re.sub(r"^(ии_перепроектирован:\s*\n\s*статус:\s*)false",
                r"\1true", fm, count=1, flags=re.MULTILINE)
    # 5. дополнительные.канон_источник: '<фильмы>' → 'фантастические данные/модели/<модель>.md'
    fm = re.sub(r"^(  канон_источник:\s*).*$",
                lambda m: m.group(1) + f"'{canon_model_file}'",
                fm, count=1, flags=re.MULTILINE)

    if fm != orig:
        new_text = f"---\n{fm}\n---\n{body}"
        file_path.write_text(new_text, encoding="utf-8")
        return 1
    return 0


def rewrite_links(new_file: Path, old_dir: Path) -> int:
    """Пересчитать относительные ../ ссылки от старого каталога к новому.

    old_dir — каталог, где файл лежал до переноса (в фантастические данные/.../реализация/...).
    new_file — путь файла после переноса (в работа и и/изделия/...).
    """
    text = new_file.read_text(encoding="utf-8")
    count = 0

    def _sub(m: re.Match) -> str:
        nonlocal count
        old_rel = m.group(1)
        target_abs = (old_dir / old_rel.replace("%20", " ")).resolve()
        if not target_abs.exists():
            # старая цель не существует — оставить как есть (мёртворождённая)
            return m.group(0)
        new_rel = os.path.relpath(target_abs, new_file.parent.resolve())
        new_link = new_rel.replace(" ", "%20")
        if new_link != old_rel:
            count += 1
        return f"({new_link})"

    new_text = LINK_RE.sub(_sub, text)
    if count:
        new_file.write_text(new_text, encoding="utf-8")
    return count


def main() -> int:
    work_root = REPO / "работа и и" / "изделия"
    work_root.mkdir(parents=True, exist_ok=True)

    moved: list[tuple[Path, Path]] = []  # (new_dir, old_dir)
    fm_updates = 0

    for src_rel, subsystem, wrapper_name, canon_model_file in MAPPING:
        src_dir = REPO / src_rel
        if not src_dir.is_dir():
            print(f"ERROR: нет источника {src_dir}")
            return 1
        dest_dir = work_root / subsystem / wrapper_name
        if dest_dir.exists():
            print(f"ERROR: цель уже существует {dest_dir}")
            return 1
        dest_dir.parent.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            ["git", "mv", str(src_dir), str(dest_dir)],
            cwd=REPO, check=True, capture_output=True, text=True,
        )
        n_idx = len(list(dest_dir.rglob("_index.md")))
        print(f"  ✓ {src_rel} → работа и и/изделия/{subsystem}/{wrapper_name} ({n_idx} _index.md)")

        # frontmatter обёртки
        wrapper_idx = dest_dir / "_index.md"
        if wrapper_idx.exists():
            fm_updates += update_wrapper_frontmatter(wrapper_idx, canon_model_file)

        moved.append((dest_dir, src_dir))

    print(f"Frontmatter обёрток обновлено: {fm_updates}/11")

    # Пересчёт ссылок во всех .md внутри перемещённых каталогов
    total_links = 0
    for new_dir, old_dir in moved:
        for f in new_dir.rglob("*.md"):
            total_links += rewrite_links(f, old_dir)
    print(f"Пересчитано ссылок: {total_links}")

    # Удаление пустых реализация/ под каждую модель
    cleaned = 0
    seen_models = set()
    for src_rel, *_ in MAPPING:
        # src_rel = фантастические данные/модели/<модель>/реализация/<wrapper>
        parts = src_rel.split("/")
        model_dir = REPO / parts[0] / parts[1] / parts[2]  # фантастические данные/модели/<модель>
        if model_dir in seen_models:
            continue
        seen_models.add(model_dir)
        realiz_dir = model_dir / "реализация"
        if realiz_dir.exists() and not any(realiz_dir.iterdir()):
            realiz_dir.rmdir()
            cleaned += 1
            print(f"  ✓ rm empty {realiz_dir.relative_to(REPO)}")
    print(f"Удалено пустых реализация/: {cleaned}")

    # Контроль: в фантастические данные не осталось модельных обёрток
    leftovers = subprocess.run(
        ["grep", "-rl", "подтип: модель_обёртка", str(REPO / "фантастические данные")],
        capture_output=True, text=True,
    )
    if leftovers.stdout.strip():
        print(f"ERROR: остались обёртки в фантастических данных:\n{leftovers.stdout}")
        return 1

    # Контроль: ID сохранены (11 izdelie_SkyNet-* в работа и и)
    ids = subprocess.run(
        ["grep", "-rh", "^id: izdelie_SkyNet", str(work_root)],
        capture_output=True, text=True,
    )
    n_ids = len([l for l in ids.stdout.splitlines() if l.strip()])
    print(f"ID izdelie_SkyNet-* в работа и и/изделия/: {n_ids} (ожидалось 11)")
    if n_ids != 11:
        print("ERROR: количество ID не совпало")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
