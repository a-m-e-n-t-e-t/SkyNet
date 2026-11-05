#!/usr/bin/env python3
"""SkyNet — Добавить недостающие структурные поля §12.4.1-§12.4.X в файлы моделей.

Читает:
  • фантастические данные/модели/*.md (41 файл)

Для каждого файла модели добавляет недостающие структурные поля с
placeholder'ом `[]` (пустой список):
  - требования_выживаемости
  - маскировка_инфильтратора
  - тактико_технические_характеристики
  - защита_от_собственной_радиации
  - кибербезопасность
  - эмс_внутренняя
  - компоновка_изделий
  - трассировка_соединителей
  - программное_обеспечение
  - единая_эми_стратегия
  - единая_герметичность
  - сертификация_модели_целого
  - журнал_экземпляра
  - утилизация_после_120_лет
  - экипаж_оператор
  - промышленная_база
  - alice_specs
  - original_improved

Для t1000.md и t1001.md (жидкий металл) — также добавляет
многослойная_броня: [] (неприменимо для жидкого металла).
"""

from __future__ import annotations
import os
import re
from pathlib import Path

REPO = Path("/home/z/my-project/skynet_clone/SkyNet")
MODELS_DIR = REPO / "фантастические данные" / "модели"
TODAY = "2026-11-03"

# Структурные поля §12.4.1-§12.4.X — добавляются как [] (placeholder)
STRUCTURAL_FIELDS = [
    "требования_выживаемости",
    "маскировка_инфильтратора",
    "тактико_технические_характеристики",
    "защита_от_собственной_радиации",
    "кибербезопасность",
    "эмс_внутренняя",
    "компоновка_изделий",
    "трассировка_соединителей",
    "программное_обеспечение",
    "единая_эми_стратегия",
    "единая_герметичность",
    "сертификация_модели_целого",
    "журнал_экземпляра",
    "утилизация_после_120_лет",
    "экипаж_оператор",
    "промышленная_база",
    "alice_specs",
    "original_improved",
]

# Для жидких металлов (t1000, t1001) — многослойная_броня неприменима
LIQUID_METAL_FILES = {"t1000.md", "t1001.md"}


def add_missing_fields(filepath: Path) -> tuple[bool, list[str]]:
    """Добавляет недостающие поля в YAML frontmatter файла модели.
    
    Returns:
        (changed, added_fields) — был ли файл изменён и какие поля добавлены.
    """
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False, []
    
    # Найти конец YAML frontmatter
    end_match = re.search(r"\n---\s*\n", text[3:])
    if not end_match:
        return False, []
    yaml_end_pos = 3 + end_match.start()
    yaml_text = text[3:yaml_end_pos]
    
    # Какие поля уже есть
    existing_fields = set()
    for line in yaml_text.split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("#") and not line.startswith("-"):
            field = line.split(":", 1)[0].strip()
            existing_fields.add(field)
    
    # Какие поля нужно добавить
    fields_to_add = [f for f in STRUCTURAL_FIELDS if f not in existing_fields]
    
    # Для жидкого металла — также многослойная_броня
    if filepath.name in LIQUID_METAL_FILES and "многослойная_броня" not in existing_fields:
        fields_to_add.insert(0, "многослойная_броня")
    
    if not fields_to_add:
        return False, []
    
    # Сгенерировать YAML-блок для добавления
    # Комментарий объясняет что это structural placeholder
    new_yaml_block = "\n# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder\n"
    new_yaml_block += "# Реальные значения будут заполнены через web_search для каждой модели.\n"
    for field in fields_to_add:
        new_yaml_block += f"{field}: []\n"
    
    # Обновить дата_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"дата_обновления: {TODAY}",
        yaml_text,
        count=1,
        flags=re.MULTILINE,
    )
    
    # Вставить новые поля перед "дата_создания:" (или в конец YAML если нет)
    # Найти позицию для вставки — после последнего существующего поля, перед "дата_создания:"
    insert_position = None
    date_pos = re.search(r"^дата_создания:", new_yaml, re.MULTILINE)
    if date_pos:
        insert_position = date_pos.start()
    
    if insert_position is not None:
        new_yaml = new_yaml[:insert_position] + new_yaml_block.lstrip("\n") + new_yaml[insert_position:]
    else:
        # Если нет дата_создания — добавить в конец YAML
        new_yaml = new_yaml.rstrip("\n") + "\n" + new_yaml_block
    
    # Собрать новый текст файла
    new_text = "---\n" + new_yaml + text[yaml_end_pos:]
    
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return True, fields_to_add
    
    return False, []


def main():
    print("=== SkyNet — Add structural §12.4 fields to model files ===")
    print()
    
    total = 0
    updated = 0
    total_fields_added = 0
    
    for f in sorted(MODELS_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue
        total += 1
        changed, added = add_missing_fields(f)
        if changed:
            updated += 1
            total_fields_added += len(added)
            liquid = " (+многослойная_броня)" if f.name in LIQUID_METAL_FILES else ""
            print(f"  ✓ {f.name:30s} +{len(added)} полей{liquid}")
        else:
            print(f"    {f.name:30s} (no change)")
    
    print()
    print(f"=== Сводка ===")
    print(f"  Всего моделей: {total}")
    print(f"  Обновлено: {updated}")
    print(f"  Полей добавлено: {total_fields_added}")
    print(f"  Среднее на модель: {total_fields_added / max(1, updated):.1f}")


if __name__ == "__main__":
    main()
