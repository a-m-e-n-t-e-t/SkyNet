#!/usr/bin/env python3
"""
SkyNet — миграция #256 вариант A: перенос модельных обёрток из реальные данные/изделия/
в фантастические данные/модели/<модель>/реализация/.

Правило пользователя (2026-11-05, жёсткое):
  «файлы в реальных данных не могут иметь элементы нижнего уровня
   из фантастических данных или работы ии».

11 обёрток (подтип: модель_обёртка) + 70 дочерних частей покидают реальные данные.
ID сохраняются (izdelie_SkyNet-*), ссылки izdelie_SkyNet-* в моделях остаются валидными.
Относительные md-ссылки пересчитываются от нового местоположения.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Обёртка (относительно реальные данные/изделия/) → стем канонической модели
MAPPING = {
    "каркас/t600": "t600",
    "каркас/t800": "t800",
    "каркас/t850": "t850",
    "каркас/tx": "t_x",
    "каркас/cameron": "cameron_phillips",
    "каркас/rev9": "rev9",
    "каркас/marcuswright": "marcus_wright",
    "каркас/hktank": "hk_tank",
    "каркас/hkaerial": "hk_aerial",
    "вычислительная/t1000": "t1000",
    "вычислительная/t1001": "t1001",
}

LINK_RE = re.compile(r"\((\.\./[^)\s]*(?:%20[^)\s]*)*)\)")


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"git {' '.join(args)} FAILED:\n{r.stderr}")
        sys.exit(1)
    return r.stdout


def rewrite_links(new_file: Path, old_dir: Path) -> int:
    """Пересчитать относительные ../ ссылки от старого каталога к новому."""
    text = new_file.read_text(encoding="utf-8")
    count = 0

    def _sub(m: re.Match) -> str:
        nonlocal count
        old_rel = m.group(1)
        # %20 → пробел для резолюции
        target_abs = (old_dir / old_rel.replace("%20", " ")).resolve()
        if not target_abs.exists():
            # старая цель не существует — оставить как есть (висячая и раньше)
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
    src_root = REPO / "реальные данные" / "изделия"
    models_root = REPO / "фантастические данные" / "модели"

    moved_files: list[tuple[Path, Path]] = []  # (new_file, old_dir)

    for src_rel, model_stem in MAPPING.items():
        src_dir = src_root / src_rel
        if not src_dir.is_dir():
            print(f"ERROR: не найден источник {src_dir}")
            return 1
        model_dir = models_root / model_stem / "реализация" / src_dir.name
        if model_dir.exists():
            print(f"ERROR: цель уже существует {model_dir}")
            return 1
        model_dir.parent.mkdir(parents=True, exist_ok=True)

        # git mv сохраняет историю
        subprocess.run(
            ["git", "mv", str(src_dir), str(model_dir)],
            cwd=REPO, check=True, capture_output=True, text=True,
        )
        n = len(list(model_dir.rglob("_index.md")))
        print(f"  ✓ {src_rel} → фантастические данные/модели/{model_stem}/реализация/{src_dir.name} ({n} _index.md)")
        for f in model_dir.rglob("*.md"):
            moved_files.append((f, src_dir))

    # Пересчёт ссылок
    total_links = 0
    for new_file, old_dir in moved_files:
        total_links += rewrite_links(new_file, old_dir)
    print(f"Пересчитано ссылок: {total_links}")

    # Контроль: в реальные данные/изделия/ не осталось модельных обёрток
    leftovers = subprocess.run(
        ["grep", "-rl", "подтип: модель_обёртка", str(src_root)],
        capture_output=True, text=True,
    )
    if leftovers.stdout.strip():
        print(f"ERROR: остались обёртки:\n{leftovers.stdout}")
        return 1

    # Контроль: ID сохранены
    ids = subprocess.run(
        ["grep", "-rh", "^id: izdelie_SkyNet", str(models_root)],
        capture_output=True, text=True,
    )
    n_ids = len([l for l in ids.stdout.splitlines() if l.strip()])
    print(f"ID izdelie_SkyNet-* в фантастических данных: {n_ids} (ожидалось 11)")
    if n_ids != 11:
        print("ERROR: количество ID не совпало")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
