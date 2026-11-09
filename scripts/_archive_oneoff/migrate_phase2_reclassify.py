#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 2: Реклассификация misclassified изделий.

Перемещает 18 misclassified + распускает прочее/:
- 5 батарей из энергетическая → система_питания
- 2 модуля Пельте из энергетическая → система_охлаждения
- 4 муфты/подшипника из энергетическая → приводная_система
- 3 оружия из энергетическая → встроенное_оружие
- 4 связи/навигации из сенсоры → система_связи или навигация

Распускание прочее/:
- slm_eos_m290 → технологии/ (это 3D-принтер, не изделие)
- provodnikovaya_nanoreshetka → материалы/ (это материал)
- polyimide_fpc + gibkii_pcb → дедуплицировать (оставить polyimide_fpc)
- 4 других → в правильные подсистемы

Для каждого перемещения:
1. git mv file
2. Обновить YAML поле 'подсистема:' в frontmatter
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
IZDELIYA = REPO / 'реальные данные' / 'изделия'

# Список перемещений: (old_subdir, izdelie_id, new_subdir)
# old_subdir — для поиска (find); izdelie_id — для проверки id в frontmatter
MIGRATIONS = [
    # Группа A: батареи → система_питания
    ('энергетическая/superkondensatory', 'superkondensatory', 'система_питания'),
    ('энергетическая/svintsovo-kislotnye_akb', 'svintsovo-kislotnye_akb', 'система_питания'),
    ('энергетическая/tverdotelnye_akkumulyatory', 'tverdotelnye_akkumulyatory', 'система_питания'),
    ('энергетическая/induktivnyi_nakopitel', 'induktivnyi_nakopitel', 'система_питания'),
    ('вычислительная/litii-tionilhloridnye_batarei', 'litii-tionilhloridnye_batarei', 'система_питания'),
    # Группа B: Пельте → система_охлаждения
    ('энергетическая/termomoduli_pelte', 'termomoduli_pelte', 'система_охлаждения'),
    ('энергетическая/reversivnye_pelte', 'reversivnye_pelte', 'система_охлаждения'),
    # Группа C: приводы → приводная_система
    ('энергетическая/elektromagnitnye_poroshkovye_mufty_i_tormoza', 'elektromagnitnye_poroshkovye_mufty_i_tormoza', 'приводная_система'),
    ('энергетическая/vysokotemperaturnyi_sverhprovodyaschii_podshipnik', 'vysokotemperaturnyi_sverhprovodyaschii_podshipnik', 'приводная_система'),
    ('энергетическая/dvoinaya_sshitaya_magnitnaya_myshtsa_unist', 'dvoinaya_sshitaya_magnitnaya_myshtsa_unist', 'приводная_система'),
    ('энергетическая/planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami', 'planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami', 'приводная_система'),
    # Группа D: оружие → встроенное_оружие
    ('энергетическая/coilgun', 'coilgun', 'встроенное_оружие'),
    ('энергетическая/emi-generator', 'emi-generator', 'встроенное_оружие'),
    # Группа E: связь/навигация
    ('сенсоры/starlink_mini', 'starlink_mini', 'система_связи'),
    ('сенсоры/iridium_sbd', 'iridium_sbd', 'система_связи'),
    ('сенсоры/ads-b_priemnik', 'ads-b_priemnik', 'навигация'),
    ('система_связи/stm32', 'stm32', 'вычислительная'),
    ('система_связи/stm32h743', 'stm32h743', 'вычислительная'),
]


def update_subsystem_field(file_path: Path, new_subsystem: str) -> bool:
    """Обновить YAML поле 'подсистема:' в frontmatter."""
    text = file_path.read_text(encoding='utf-8')
    # Заменить только в frontmatter (до первой ---\n... ---\n)
    new_text = re.sub(
        r'(^подсистема:)\s*\S+',
        lambda m: f'подсистема: {new_subsystem}',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if new_text != text:
        write_atomic(file_path, new_text)
        return True
    return False


def migrate_izdelie(old_subdir: str, izdelie_id: str, new_subdir: str) -> bool:
    """Переместить изделие (директорию) из old_subdir в new_subdir, обновить YAML."""
    old_path = IZDELIYA / old_subdir
    new_path = IZDELIYA / new_subdir / izdelie_id

    if not old_path.exists():
        print(f"  SKIP: {old_path} не существует")
        return False

    if new_path.exists():
        print(f"  SKIP: {new_path} уже существует")
        return False

    # Создать родителя если нужно
    new_path.parent.mkdir(parents=True, exist_ok=True)

    # git mv
    os.system(f'cd "{REPO}" && git mv "{old_path}" "{new_path}"')

    # Обновить YAML в _index.md и всех поддиректориях часть_*
    index_file = new_path / '_index.md'
    if index_file.exists():
        update_subsystem_field(index_file, new_subdir)

    # Обновить во всех часть_* поддиректориях
    for child in new_path.rglob('_index.md'):
        if child != index_file:
            update_subsystem_field(child, new_subdir)

    print(f"  OK: {old_subdir} → {new_subdir}/{izdelie_id}")
    return True


def main():
    print("=== v9.61 Фаза 2a: Реклассификация misclassified ===\n")
    success = 0
    skipped = 0
    for old_subdir, izdelie_id, new_subdir in MIGRATIONS:
        if migrate_izdelie(old_subdir, izdelie_id, new_subdir):
            success += 1
        else:
            skipped += 1
    print(f"\nИтого: {success} перемещено, {skipped} пропущено")


if __name__ == '__main__':
    main()
