#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v9.61 Фаза 4: Обновить BOM-ссылки в файлах изделий.

Для каждой мигрировавшей сущности (73 компонента) — найти все файлы, которые
ссылались на старый material_id, и обновить ссылки на canonical-материал.

Пример:
  было: материал: ceramic_mlcc
  стало: материал: batio3  (canonical)

Также обновить markdown-ссылки в body:
  было: [ceramic_mlcc.md](../материалы/ceramic_mlcc.md)
  стало: [batio3.md](../материалы/batio3.md)
"""
import os
import re
import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, '/home/z/my-project/SkyNet/scripts')
from _helpers import write_atomic

REPO = Path('/home/z/my-project/SkyNet')
TODAY = date.today().isoformat()

# Mapping: old_material_id → canonical_material_id (canonical-вещество)
# Это 73 мигрировавших + устаревшие references
MATERIAL_REPLACEMENTS = {
    # электронные
    'ceramic_mlcc': 'batio3',
    'ceramic_capacitors': 'batio3',
    'plastic_qfp': 'epoxy_molding',
    'fr4': 'epoxy',
    'bt_abf_substrate': 'bt_resin',
    'emc_underfill': 'epoxy',
    'epoxy_molding': 'epoxy',
    'aluminum_electrolytic': 'aluminum',
    'silicon_wafer': 'si',
    'silicon_carbide': 'monokristallicheskogo_sic',
    'barium_titanate': 'batio3',
    'gst_chalcogenide': 'gst',
    'lithium_metal': 'lithium',
    'monocrystalline_si': 'si',
    'fto-steklo': 'sio2_amorphous',
    # электромеханические
    'ndfeb-magnity': 'ndfeb',
    'neodimovye_magnitnye_diski': 'ndfeb',
    'copper_wire': 'copper',
    'al_bondwire': 'aluminum',
    'tungsten_electrodes': 'tungsten',
    # механические
    'bearing_steel_52100': '100cr6',
    'stainless_steel_304': 'ss_aisi_304',
    'tin_metal': 'tin',
    'gold_coating': 'silver',
    'iron_powder': 'karbonilnoe_zhelezo',
    'composite_material': 'cnt',
    'uo2_pellets': 'uo2',
    'pu238_oxide': 'dioksid_plutoniya-238',
    # термические
    'silica_aerogel_blanket': 'sio2_amorphous',
    'aerogel': 'sio2_amorphous',
    'grafen-aerogel': 'cnt',
    'ag-pena': 'silver',
    'cu-pena_duocel': 'copper',
    'cu-aerogel_regenerator': 'copper',
    'mnogosloinoe_dlar': 'alumina',
    'sapfir_ar': 'alumina',
    'agm_steklovolokno': 'sio2_amorphous',
    # мембраны
    'nafion_117': 'nafion',
    'pp_membrane': 'polypropylene',
    'pe_separator': 'pe',
    'anodisc_47': 'alumina',
    'carbon_ptfe': 'ptfe',
    # композитные
    'uhmwpe_dyneema': 'uhmwpe',
    'spectra': 'uhmwpe',
    'kevlar_49': 'aramid',
    'cfrp_t1100g': 'cnt',
    'cfrp_t800s': 'cnt',
    'karbon': 'cnt',
    'tedlar': 'pvf',
    'tedlar_pet': 'pet',
    'mylar': 'pet',
    'peek-volokno': 'peek',
    'cnt-volokno': 'cnt',
    'cnt-kompozit': 'cnt',
    'sacnt-sf': 'cnt',
    'neilonovaya_nit': 'neilon_6_66',
    'pof': 'pet',
    'ptfe-kompozit_du_vtulki': 'ptfe',
    'ptfe-kompozit_vtulki': 'ptfe',
    'epotek_301-2': 'epoxy',
    'epoksid_epon_828_teta': 'epoxy',
    'silan-praimer': 'silane',
    'mikrokapsuly_dcpd': 'dcpd',
    'mikrokapsuly_dcpd_v_elastomere': 'dcpd',
    'silicone-textile_composite': 'ptfe',
    'low_iron_glass': 'sio2_amorphous',
    'pcm_rt35': 'paraffin',
    'pcm': 'cacl2_6h2o',
    'fotonnyi_kristall-filtr': 'sio2_amorphous',
    'lumotive_metasurface': 'silicon',
    'ni63_metal': 'ni-63',
    'ybco_bulk': 'ybco',
    'pt_carbon': 'pt',
    # Дополнительные replacements для stubs из Phase 2.5b
    'ni_ysz_cermet': 'ni-ysz',
    'ysz_electrolyte': '8ysz',
    'nafion_117': 'nafion',
    'pt_carbon': 'pt',
    'carbon_paper': 'graphite',
    'titanium_alloy': 'ti-6al-4v',
    'am241_oxide': 'am-241',
    'tritium_gas': 'tritium',  # canonical создать при необходимости
    'tungsten_alloy': 'tungsten',
    'monocrystalline_si': 'si',
    'lipf6_ec_dmc': 'lipf6_ec_dmc',  # уже canonical stub
    'koh_aqueous': 'koh_aqueous',
    'cast_iron': 'cast_iron',
    'epoxy': 'epoxy',
    'steel_1045': 'steel_1045',
    'iron_powder': 'karbonilnoe_zhelezo',
    'copper_wire': 'copper',
    'ceramic_capacitors': 'batio3',
    'ceramic_mlcc': 'batio3',
    'tungsten_electrodes': 'tungsten',
    'alumina': 'alumina',
    'gaSb': 'gaSb',
    'gold_coating': 'silver',
    'aluminum_electrolytic': 'aluminum',
    'composite_material': 'cnt',
    'aluminum_1100': 'aluminum_1100',
    'generic_material': 'generic_material',
    'activated_carbon': 'activated_carbon',
    'aerogel': 'sio2_amorphous',
    'copper_wire': 'copper',
    'eva': 'eva',
    'monocrystalline_si': 'si',
    'pu238_oxide': 'dioksid_plutoniya-238',
    'uo2_pellets': 'uo2',
    'stainless_steel_316': 'ss_316l',
}


def update_file(file_path: Path) -> tuple:
    """Обновить ссылки в файле. Возвращает (были_изменения, количество_замен)."""
    text = file_path.read_text(encoding='utf-8')
    original_text = text
    changes = 0

    # 1. Заменить в frontmatter YAML: 'материал: <old>' → 'материал: <new>'
    for old_id, new_id in MATERIAL_REPLACEMENTS.items():
        if old_id == new_id:
            continue
        # YAML field 'материал:'
        pattern = re.compile(rf'(^материал:\s*){re.escape(old_id)}(\s|$)', re.MULTILINE)
        new_text, n = pattern.subn(rf'\g<1>{new_id}\g<2>', text)
        if n:
            text = new_text
            changes += n

    # 2. Заменить в frontmatter YAML: '- материал: <old>' → '- материал: <new>'
    for old_id, new_id in MATERIAL_REPLACEMENTS.items():
        if old_id == new_id:
            continue
        pattern = re.compile(rf'(^(\s*)-\s*материал:\s*){re.escape(old_id)}(\s|$)', re.MULTILINE)
        new_text, n = pattern.subn(rf'\g<1>{new_id}\g<3>', text)
        if n:
            text = new_text
            changes += n

    # 3. Заменить markdown-ссылки: [old.md](../материалы/old.md) → [new.md](../материалы/new.md)
    for old_id, new_id in MATERIAL_REPLACEMENTS.items():
        if old_id == new_id:
            continue
        # Ссылки в markdown body
        pattern1 = re.compile(rf'\[`{re.escape(old_id)}\.md`\]\(([^)]*материалы/){re.escape(old_id)}\.md\)')
        new_text, n = pattern1.subn(rf'[`{new_id}.md`](\g<1>{new_id}.md)', text)
        if n:
            text = new_text
            changes += n
        # Без .md в label
        pattern2 = re.compile(rf'\[`{re.escape(old_id)}`\]\(([^)]*материалы/){re.escape(old_id)}\.md\)')
        new_text, n = pattern2.subn(rf'[`{new_id}`](\g<1>{new_id}.md)', text)
        if n:
            text = new_text
            changes += n

    if text != original_text:
        write_atomic(file_path, text)
        return True, changes
    return False, 0


def main():
    print("=== v9.61 Фаза 4: Обновление BOM-ссылок ===\n")
    print(f"Правил замены: {len(MATERIAL_REPLACEMENTS)}")
    print()

    # Найти все .md файлы в реальные данные/изделия/ и работа и и/изделия/
    all_files = []
    for root in ['реальные данные/изделия', 'работа и и/изделия']:
        full = REPO / root
        if full.exists():
            all_files.extend(full.rglob('_index.md'))
            all_files.extend(full.rglob('*.md'))

    # Дедуплицировать
    all_files = list(set(all_files))
    print(f"Файлов к проверке: {len(all_files)}")

    updated = 0
    total_changes = 0
    for f in all_files:
        try:
            changed, n = update_file(f)
            if changed:
                updated += 1
                total_changes += n
        except Exception as e:
            print(f"  ERROR {f}: {e}")

    print(f"\nОбновлено файлов: {updated}")
    print(f"Всего замен: {total_changes}")


if __name__ == '__main__':
    main()
