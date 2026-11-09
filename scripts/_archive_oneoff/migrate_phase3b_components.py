#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 3b: Мигрировать 64 закупочных файла из материалы/ в изделия/компоненты/<cat>/.

Для каждого закупочного:
1. Создать директорию изделия/компоненты/<cat>/<name>/
2. Перенести материал .md → _index.md с обновлением frontmatter:
   - тип: материал → тип: изделие
   - подсистема: <не было> → подсистема: компоненты
   - добавить: уровень_иерархии: верхний, уровень_номер: 1
   - id: material_X → izdelie_X
   - канонический_id → убираем (это уже не alias)
3. Удалить старый .md из материалы/

Категории компонент (по 6 подкатегориям):
- электронные: MLCC, FR4, QFP, диоды, конденсаторы
- электромеханические: BLDC, моторы, реле
- механические: подшипники, шестерни, пружины, COPV
- термические: aerogel, теплоизоляция, радиаторы
- мембраны: nafion, PEM, сепараторы
- композитные: ламинаты, prepreg, ткани (kevlar, spectra, mylar)
"""
import os
import re
import sys
import shutil
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
MAT_DIR = REPO / 'реальные данные' / 'материалы'
COMP_DIR = REPO / 'реальные данные' / 'изделия' / 'компоненты'
TODAY = date.today().isoformat()


# 64 файла для миграции: (filename, category, new_id, canonical_material_id)
# canonical_material_id — нужен для определения canonical-основы (для stubs)
MIGRATIONS = [
    # === электронные (15 файлов) ===
    ('ceramic_mlcc.md', 'электронные', 'izdelie_ceramic_mlcc', 'batio3'),
    ('ceramic_capacitors.md', 'электронные', 'izdelie_ceramic_capacitors', 'batio3'),
    ('plastic_qfp.md', 'электронные', 'izdelie_plastic_qfp', 'epoxy_molding'),
    ('fr4.md', 'электронные', 'izdelie_fr4', 'epoxy'),
    ('bt_abf_substrate.md', 'электронные', 'izdelie_bt_abf_substrate', 'bt_resin'),
    ('emc_underfill.md', 'электронные', 'izdelie_emc_underfill', 'epoxy'),
    ('epoxy_molding.md', 'электронные', 'izdelie_epoxy_molding', 'epoxy'),
    ('aluminum_electrolytic.md', 'электронные', 'izdelie_aluminum_electrolytic', 'aluminum'),
    ('silicon_wafer.md', 'электронные', 'izdelie_silicon_wafer', 'si'),
    ('silicon_carbide.md', 'электронные', 'izdelie_silicon_carbide', 'monokristallicheskogo_sic'),
    ('barium_titanate.md', 'электронные', 'izdelie_barium_titanate', 'batio3'),
    ('gst_chalcogenide.md', 'электронные', 'izdelie_gst_chalcogenide', 'gst'),
    ('lithium_metal.md', 'электронные', 'izdelie_lithium_metal', 'lithium'),
    ('monocrystalline_si.md', 'электронные', 'izdelie_monocrystalline_si', 'si'),
    ('fto-steklo.md', 'электронные', 'izdelie_fto_steklo', 'sio2_amorphous'),

    # === электромеханические (5 файлов) ===
    ('ndfeb-magnity.md', 'электромеханические', 'izdelie_ndfeb_magnity', 'ndfeb'),
    ('neodimovye_magnitnye_diski.md', 'электромеханические', 'izdelie_neodimovye_magnitnye_diski', 'ndfeb'),
    ('copper_wire.md', 'электромеханические', 'izdelie_copper_wire', 'copper'),
    ('al_bondwire.md', 'электромеханические', 'izdelie_al_bondwire', 'aluminum'),
    ('tungsten_electrodes.md', 'электромеханические', 'izdelie_tungsten_electrodes', 'tungsten'),

    # === механические (8 файлов) ===
    ('bearing_steel_52100.md', 'механические', 'izdelie_bearing_steel_52100', '100cr6'),
    ('stainless_steel_304.md', 'механические', 'izdelie_stainless_steel_304', 'ss_aisi_304'),
    ('tin_metal.md', 'механические', 'izdelie_tin_metal', 'tin'),
    ('gold_coating.md', 'механические', 'izdelie_gold_coating', 'silver'),
    ('iron_powder.md', 'механические', 'izdelie_iron_powder', 'karbonilnoe_zhelezo'),
    ('composite_material.md', 'механические', 'izdelie_composite_material', 'cnt'),
    ('uo2_pellets.md', 'механические', 'izdelie_uo2_pellets', 'uo2'),
    ('pu238_oxide.md', 'механические', 'izdelie_pu238_oxide', 'dioksid_plutoniya-238'),

    # === термические (10 файлов) ===
    ('silica_aerogel_blanket.md', 'термические', 'izdelie_silica_aerogel_blanket', 'sio2_amorphous'),
    ('aerogel.md', 'термические', 'izdelie_aerogel', 'sio2_amorphous'),
    ('grafen-aerogel.md', 'термические', 'izdelie_grafen_aerogel', 'cnt'),
    ('ag-pena.md', 'термические', 'izdelie_ag_pena', 'silver'),
    ('cu-pena_duocel.md', 'термические', 'izdelie_cu_pena_duocel', 'copper'),
    ('cu-aerogel_regenerator.md', 'термические', 'izdelie_cu_aerogel_regenerator', 'copper'),
    ('mnogosloinoe_dlar.md', 'термические', 'izdelie_mnogosloinoe_dlar', 'alumina'),
    ('sapfir_ar.md', 'термические', 'izdelie_sapfir_ar', 'alumina'),
    ('agm_steklovolokno.md', 'термические', 'izdelie_agm_steklovolokno', 'sio2_amorphous'),
    ('graphite_composite_bpp.md', 'термические', 'izdelie_graphite_composite_bpp', 'graphite'),

    # === мембраны (5 файлов) ===
    ('nafion_117.md', 'мембраны', 'izdelie_nafion_117', 'nafion'),
    ('pp_membrane.md', 'мембраны', 'izdelie_pp_membrane', 'polypropylene'),
    ('pe_separator.md', 'мембраны', 'izdelie_pe_separator', 'pe'),
    ('anodisc_47.md', 'мембраны', 'izdelie_anodisc_47', 'alumina'),
    ('carbon_ptfe.md', 'мембраны', 'izdelie_carbon_ptfe', 'ptfe'),

    # === композитные (21 файл) ===
    ('uhmwpe_dyneema.md', 'композитные', 'izdelie_uhmwpe_dyneema', 'uhmwpe'),
    ('spectra.md', 'композитные', 'izdelie_spectra', 'uhmwpe'),
    ('kevlar_49.md', 'композитные', 'izdelie_kevlar_49', 'aramid'),
    ('cfrp_t1100g.md', 'композитные', 'izdelie_cfrp_t1100g', 'cnt'),
    ('cfrp_t800s.md', 'композитные', 'izdelie_cfrp_t800s', 'cnt'),
    ('karbon.md', 'композитные', 'izdelie_karbon', 'cnt'),
    ('tedlar.md', 'композитные', 'izdelie_tedlar', 'pvf'),
    ('tedlar_pet.md', 'композитные', 'izdelie_tedlar_pet', 'pet'),
    ('mylar.md', 'композитные', 'izdelie_mylar', 'pet'),
    ('peek-volokno.md', 'композитные', 'izdelie_peek_volokno', 'peek'),
    ('cnt-volokno.md', 'композитные', 'izdelie_cnt_volokno', 'cnt'),
    ('cnt-kompozit.md', 'композитные', 'izdelie_cnt_kompozit', 'cnt'),
    ('sacnt-sf.md', 'композитные', 'izdelie_sacnt_sf', 'cnt'),
    ('neilonovaya_nit.md', 'композитные', 'izdelie_neilonovaya_nit', 'neilon_6_66'),
    ('pof.md', 'композитные', 'izdelie_pof', 'pet'),
    ('ptfe-kompozit_du_vtulki.md', 'композитные', 'izdelie_ptfe_kompozit_du_vtulki', 'ptfe'),
    ('ptfe-kompozit_vtulki.md', 'композитные', 'izdelie_ptfe_kompozit_vtulki', 'ptfe'),
    ('epotek_301-2.md', 'композитные', 'izdelie_epotek_301_2', 'epoxy'),
    ('epoksid_epon_828_teta.md', 'композитные', 'izdelie_epoksid_epon_828_teta', 'epoxy'),
    ('silan-praimer.md', 'композитные', 'izdelie_silan_praimer', 'silane'),
    ('mikrokapsuly_dcpd.md', 'композитные', 'izdelie_mikrokapsuly_dcpd', 'dcpd'),
    ('mikrokapsuly_dcpd_v_elastomere.md', 'композитные', 'izdelie_mikrokapsuly_dcpd_v_elastomere', 'dcpd'),
    ('silicone-textile_composite.md', 'композитные', 'izdelie_silicone_textile_composite', 'ptfe'),
    ('low_iron_glass.md', 'композитные', 'izdelie_low_iron_glass', 'sio2_amorphous'),
    ('pcm_rt35.md', 'композитные', 'izdelie_pcm_rt35', 'paraffin'),
    ('pcm.md', 'композитные', 'izdelie_pcm', 'cacl2_6h2o'),
    ('fotonnyi_kristall-filtr.md', 'композитные', 'izdelie_fotonnyi_kristall_filtr', 'sio2_amorphous'),
    ('lumotive_metasurface.md', 'композитные', 'izdelie_lumotive_metasurface', 'silicon'),
    ('ni63_metal.md', 'композитные', 'izdelie_ni63_metal', 'ni-63'),
    ('ybco_bulk.md', 'композитные', 'izdelie_ybco_bulk', 'ybco'),
    ('pt_carbon.md', 'композитные', 'izdelie_pt_carbon', 'pt'),
    ('ndfeb-magnity.md', 'композитные', 'izdelie_ndfeb_magnity_alt', 'ndfeb'),  # alt duplicate
]


def transform_frontmatter(text: str, old_id: str, new_id: str, canonical: str) -> str:
    """Преобразовать frontmatter материала в frontmatter изделия."""
    # Заменить id
    text = re.sub(rf'(^id:\s*){re.escape(old_id)}', rf'\g<1>{new_id}', text, count=1, flags=re.MULTILINE)
    # Заменить тип: материал → изделие
    text = re.sub(r'^тип:\s*материал\s*$', 'тип: изделие', text, count=1, flags=re.MULTILINE)
    # Заменить канонический_id → ссылка на canonical материал
    text = re.sub(rf'(^канонический_id:\s*)material_{re.escape(canonical)}',
                  rf'\g<1>material_{canonical}', text, count=1, flags=re.MULTILINE)
    # Если канонический_id ссылался на себя (material_X), заменить на canonical
    if re.search(rf'^канонический_id:\s*{re.escape(old_id)}', text, re.MULTILINE):
        text = re.sub(rf'^канонический_id:\s*{re.escape(old_id)}',
                      f'канонический_id: material_{canonical}', text, count=1, flags=re.MULTILINE)

    # Убрать псевдонимы (для изделий они не нужны)
    text = re.sub(r'^псевдонимы:\s*\[\]\s*$', 'псевдонимы: []', text, count=1, flags=re.MULTILINE)

    # Добавить поля изделия после тип: строка
    # уровень_иерархии: верхний, уровень_номер: 1, подсистема: компоненты
    # Если уже есть уровень_иерархии — обновить; иначе добавить
    if not re.search(r'^уровень_иерархии:', text, re.MULTILINE):
        # Вставить после тип:
        text = re.sub(r'^(тип:\s*изделие\s*)$',
                      r'\1уровень_иерархии: верхний\nуровень_номер: 1\nподсистема: компоненты',
                      text, count=1, flags=re.MULTILINE)
    else:
        text = re.sub(r'^уровень_иерархии:\s*\S+', 'уровень_иерархии: верхний', text, count=1, flags=re.MULTILINE)
        if not re.search(r'^уровень_номер:', text, re.MULTILINE):
            text = re.sub(r'^(уровень_иерархии:\s*верхний\s*)$',
                          r'\1уровень_номер: 1', text, count=1, flags=re.MULTILINE)
        if not re.search(r'^подсистема:', text, re.MULTILINE):
            text = re.sub(r'^(уровень_номер:\s*1\s*)$',
                          r'\1подсистема: компоненты', text, count=1, flags=re.MULTILINE)
        else:
            text = re.sub(r'^подсистема:\s*\S+', 'подсистема: компоненты', text, count=1, flags=re.MULTILINE)

    # Обновить дата_обновления
    text = re.sub(r'^дата_обновления:\s*\S+',
                  f'дата_обновления: {TODAY}', text, count=1, flags=re.MULTILINE)

    return text


def migrate_one(filename: str, category: str, new_id: str, canonical: str) -> bool:
    """Перенести .md файл из материалы/ в изделия/компоненты/<cat>/<name>/_index.md."""
    src = MAT_DIR / filename
    if not src.exists():
        print(f"  SKIP: {filename} не найден")
        return False

    # Извлечь old_id из frontmatter
    text = src.read_text(encoding='utf-8')
    old_id_match = re.search(r'^id:\s*(\S+)', text, re.MULTILINE)
    if not old_id_match:
        print(f"  SKIP: {filename} — нет id в frontmatter")
        return False
    old_id = old_id_match.group(1)

    # Создать директорию
    name = new_id.replace('izdelie_', '')
    dst_dir = COMP_DIR / category / name
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / '_index.md'

    # Трансформировать frontmatter
    new_text = transform_frontmatter(text, old_id, new_id, canonical)

    # git mv файла с новым содержимым
    write_atomic(dst, new_text)
    os.system(f'cd "{REPO}" && git rm -q "{src}"')
    os.system(f'cd "{REPO}" && git add "{dst}"')

    print(f"  OK: {filename} → изделия/компоненты/{category}/{name}/_index.md (canonical: {canonical})")
    return True


def main():
    print("=== v9.61 Фаза 3b: Миграция закупочных в изделия/компоненты/ ===\n")
    success = 0
    skipped = 0
    for entry in MIGRATIONS:
        if migrate_one(*entry):
            success += 1
        else:
            skipped += 1
    print(f"\nИтого: {success} мигрировано, {skipped} пропущено")

    # Проверить что осталось в материалы/
    remaining = list(MAT_DIR.glob('*.md'))
    print(f"\nВ материалы/ осталось: {len(remaining)} файлов")


if __name__ == '__main__':
    main()
