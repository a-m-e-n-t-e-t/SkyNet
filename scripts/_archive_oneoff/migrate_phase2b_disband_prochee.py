#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 2b: Распустить прочее/.

8 файлов:
- slm_eos_m290 → технологии/ (это 3D-принтер, не изделие)
- provodnikovaya_nanoreshetka → материалы/ (это материал)
- polyimide_fpc + gibkii_pcb → дедуплицировать (оставить polyimide_fpc в вычислительная/)
- copv → система_питания (Composite Overwrapped Pressure Vessel — газовый баллон)
- dielektricheskie_elastomernye_datchiki → сенсоры (DEA sensors)
- elastomernyh_dempferah → каркас (упругий элемент)
- gidrostaticheskie_gazovye_podshipniki_na_gelii → приводная_система (газовый подшипник)
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
IZDELIYA = REPO / 'реальные данные' / 'изделия'
TECH_DIR = REPO / 'реальные данные' / 'технологии'
MAT_DIR = REPO / 'реальные данные' / 'материалы'


def update_subsystem_field(file_path: Path, new_subsystem: str) -> bool:
    text = file_path.read_text(encoding='utf-8')
    new_text = re.sub(
        r'(^подсистема:)\s*\S+',
        lambda m: f'подсистема: {new_subsystem}',
        text, count=1, flags=re.MULTILINE,
    )
    if new_text != text:
        write_atomic(file_path, new_text)
        return True
    return False


def update_field(file_path: Path, field: str, new_value: str) -> bool:
    """Обновить любое top-level YAML поле."""
    text = file_path.read_text(encoding='utf-8')
    pattern = re.compile(rf'(^{re.escape(field)}:)\s*\S+', re.MULTILINE)
    new_text = pattern.sub(lambda m: f'{field}: {new_value}', text, count=1)
    if new_text != text:
        write_atomic(file_path, new_text)
        return True
    return False


def main():
    print("=== v9.61 Фаза 2b: Распустить прочее/ ===\n")

    # 1. slm_eos_m290 → технологии/ (это 3D-принтер, технология)
    src = IZDELIYA / 'прочее' / 'slm_eos_m290'
    dst = TECH_DIR / 'slm_eos_m290'
    if src.exists():
        # Обновить тип: изделие → технология
        idx = src / '_index.md'
        if idx.exists():
            update_field(idx, 'тип', 'технология')
        # git mv
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        print("  OK: slm_eos_m290 → технологии/ (тип: технология)")

    # 2. provodnikovaya_nanoreshetka → материалы/
    src = IZDELIYA / 'прочее' / 'provodnikovaya_nanoreshetka'
    dst_mat = MAT_DIR / 'provodnikovaya_nanoreshetka.md'
    if src.exists():
        # Это материал, не изделие. Перенести как .md файл (упростить структуру).
        idx = src / '_index.md'
        if idx.exists():
            # Обновить тип: изделие → материал
            update_field(idx, 'тип', 'материал')
            # git mv файла в материалы/
            os.system(f'cd "{REPO}" && git mv "{idx}" "{dst_mat}"')
        # Удалить пустую директорию
        try:
            src.rmdir()
        except OSError:
            pass
        print("  OK: provodnikovaya_nanoreshetka → материалы/ (тип: материал)")

    # 3. gibkii_pcb (дубликат polyimide_fpc) → удалить
    src = IZDELIYA / 'прочее' / 'gibkii_pcb'
    if src.exists():
        os.system(f'cd "{REPO}" && git rm -r "{src}"')
        print("  OK: gibkii_pcb удалён (дубликат polyimide_fpc)")

    # 4. polyimide_fpc → вычислительная (гибкий PCB — это электроника)
    src = IZDELIYA / 'прочее' / 'polyimide_fpc'
    dst = IZDELIYA / 'вычислительная' / 'polyimide_fpc'
    if src.exists():
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        # Обновить подсистема
        for child in dst.rglob('_index.md'):
            update_subsystem_field(child, 'вычислительная')
        print("  OK: polyimide_fpc → вычислительная/")

    # 5. copv → система_питания (Composite Overwrapped Pressure Vessel — газовый баллон)
    src = IZDELIYA / 'прочее' / 'copv'
    dst = IZDELIYA / 'система_питания' / 'copv'
    if src.exists():
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        for child in dst.rglob('_index.md'):
            update_subsystem_field(child, 'система_питания')
        print("  OK: copv → система_питания/")

    # 6. dielektricheskie_elastomernye_datchiki → сенсоры (DEA sensors)
    src = IZDELIYA / 'прочее' / 'dielektricheskie_elastomernye_datchiki'
    dst = IZDELIYA / 'сенсоры' / 'dielektricheskie_elastomernye_datchiki'
    if src.exists():
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        for child in dst.rglob('_index.md'):
            update_subsystem_field(child, 'сенсоры')
        print("  OK: dielektricheskie_elastomernye_datchiki → сенсоры/")

    # 7. elastomernyh_dempferah → каркас (упругий элемент)
    src = IZDELIYA / 'прочее' / 'elastomernyh_dempferah'
    dst = IZDELIYA / 'каркас' / 'elastomernyh_dempferah'
    if src.exists():
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        for child in dst.rglob('_index.md'):
            update_subsystem_field(child, 'каркас')
        print("  OK: elastomernyh_dempferah → каркас/")

    # 8. gidrostaticheskie_gazovye_podshipniki_na_gelii → приводная_система
    src = IZDELIYA / 'прочее' / 'gidrostaticheskie_gazovye_podshipniki_na_gelii'
    dst = IZDELIYA / 'приводная_система' / 'gidrostaticheskie_gazovye_podshipniki_na_gelii'
    if src.exists():
        os.system(f'cd "{REPO}" && git mv "{src}" "{dst}"')
        for child in dst.rglob('_index.md'):
            update_subsystem_field(child, 'приводная_система')
        print("  OK: gidrostaticheskie_gazovye_podshipniki_na_gelii → приводная_система/")

    # Проверить что прочее/ пустая
    leftover = list((IZDELIYA / 'прочее').iterdir()) if (IZDELIYA / 'прочее').exists() else []
    if leftover:
        print(f"\n  WARN: в прочее/ осталось {len(leftover)} файлов:")
        for f in leftover:
            print(f"    - {f.name}")
    else:
        # Удалить пустую директорию
        try:
            (IZDELIYA / 'прочее').rmdir()
            print("\n  OK: прочее/ удалена (пустая)")
        except OSError as e:
            print(f"\n  WARN: не удалось удалить прочее/: {e}")


if __name__ == '__main__':
    main()
