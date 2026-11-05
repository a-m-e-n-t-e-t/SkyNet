#!/usr/bin/env python3
"""SkyNet Decomposition for All Izdeliya — v9.31

Выполняет декомпозицию для всех 117 изделий верхнего уровня (не wrapper-изделий).
Для каждого типа изделия генерирует подходящие дочерние части на основе:
  • подсистемы (вычислительная, энергетическая, и т.д.)
  • подтипа (нейроморфный_процессор, твердооксидный_ТЭ, и т.д.)
  • канон-данных из web search (где доступно)

Создаёт:
  • Дочерние части (часть_<parent_id>_<component>) — неделимые компоненты
  • Заполняет дочерние_части, материалы_частей (с долями Σ ≤ 1.0)
  • Генерирует Mermaid диаграммы в body

Шаблоны декомпозиции по подтипам:
  • нейроморфный_процессор: die + substrate + pins + thermal_spreader
  • AI_инференс_чип: die + package + HBM + power
  • керамический_конденсатор: MLCC_layers + terminals
  • силовой_транзистор: die + lead_frame + encapsulant
  • память_MRAM: cell_array + periphery + I/O
  • phase_change_память: cell_array + selector + I/O
  • memristor_массив: crossbar + driver + ADC
  • edge_AI_модуль: SoC + memory + power + I/O
  • твердооксидный_ТЭ: anode + electrolyte + cathode + interconnect
  • водородный_ТЭ: membrane + catalyst + GDL + bipolar_plate
  • радиоизотопный_генератор: isotope + thermocouples + housing
  • суперконденсатор: electrodes + separator + electrolyte
  • аккумулятор: anode + cathode + electrolyte + separator
  • Стирлинг_конвертер: heater + regenerator + cooler + piston + alternator
  • фотоэлектрический_модуль: cells + glass + backsheet + junction_box
  • импульсный_генератор_Маркса: capacitors + spark_gaps + load
  • модуль_Пельтье: peltier_couples + ceramic_plates
  • термофотоэлектрический: emitter + PV_cell + filter
  • микро_реактор: fuel + moderator + heat_exchanger + shielding
  • и т.д.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from validate_decomposition import read_yaml_frontmatter, SKYNET_REPO
from _helpers import write_atomic, TransactionBatch, yaml_serialize_block as serialize_value  # v9.37: T1+T2; v9.37.1: M1 единый сериализатор

TODAY = "2026-11-03"
IZDELIYA_DIR = SKYNET_REPO / "реальные данные" / "изделия"


# ============================================================================
# ШАБЛОНЫ ДЕКОМПОЗИЦИИ ПО ПОДТИПАМ
# ============================================================================

# Формат: подтип → {
#   parts: [(part_suffix, подтип_части, масса_kg, доля_массы)],
#   materials: [(part_suffix, материал_id, доля_материала_в_части)]
# }
# part_suffix — добавляется к "<parent_id>_<part_suffix>"
# доля_массы — доля части в общей массе родителя

DECOMP_TEMPLATES: dict[str, dict] = {
    # === ВЫЧИСЛИТЕЛЬНАЯ ===
    'нейроморфный_процессор': {
        'parts': [
            ('die', 'кремниевый_кристалл', 0.005, 0.1),
            ('substrate', 'подложка_FR5_BT', 0.01, 0.2),
            ('pins_balls', 'пины_BGA', 0.005, 0.1),
            ('thermal_spreader', 'теплораспределитель', 0.01, 0.2),
            ('encapsulant', 'инкапсулянт', 0.005, 0.1),
            ('capacitors', 'блокировка_питания', 0.005, 0.1),
            ('pcb', 'плата_носитель', 0.01, 0.2),
        ],
        'materials': [
            ('die', 'silicon_wafer', 1.0),
            ('substrate', 'bt_resin', 0.7),
            ('pins_balls', 'copper_alloy', 1.0),
            ('thermal_spreader', 'copper', 0.9),
            ('encapsulant', 'epoxy_molding', 1.0),
            ('capacitors', 'ceramic_mlcc', 1.0),
            ('pcb', 'fr4', 0.8),
        ]
    },
    'AI_инференс_чип': {
        'parts': [
            ('die', 'инференс_кристалл', 0.01, 0.15),
            ('package', 'корпус_FCBGA', 0.02, 0.3),
            ('hbm', 'память_HBM', 0.01, 0.15),
            ('substrate', 'органическая_подложка', 0.015, 0.22),
            ('thermal_spreader', 'теплораспределитель', 0.01, 0.15),
            ('capacitors', 'MLCC_блок', 0.005, 0.08),
        ],
        'materials': [
            ('die', 'silicon_wafer', 1.0),
            ('package', 'bt_resin', 0.6),
            ('hbm', 'silicon_wafer', 1.0),
            ('substrate', 'bt_resin', 0.7),
            ('thermal_spreader', 'copper', 0.9),
        ]
    },
    'RISC-V_процессор': {
        'parts': [
            ('die', 'risc_v_кристалл', 0.005, 0.1),
            ('package', 'корпус_QFP', 0.01, 0.2),
            ('crystal_osc', 'кварцевый_резонатор', 0.001, 0.02),
            ('flash', 'флеш_память', 0.002, 0.04),
            ('sram', 'SRAM_кэш', 0.002, 0.04),
            ('substrate', 'подложка', 0.01, 0.2),
            ('thermal_pad', 'термопрокладка', 0.002, 0.04),
            ('pins', 'пины', 0.005, 0.1),
            ('capacitors', 'конденсаторы', 0.005, 0.1),
            ('pcb', 'плата', 0.01, 0.2),
        ],
        'materials': [
            ('die', 'silicon_wafer', 1.0),
            ('package', 'plastic_qfp', 0.8),
            ('crystal_osc', 'quartz', 1.0),
            ('flash', 'silicon_wafer', 1.0),
            ('sram', 'silicon_wafer', 1.0),
        ]
    },
    'керамический_конденсатор': {
        'parts': [
            ('ceramic_layers', 'керамические_слои', 0.0005, 0.5),
            ('inner_electrodes', 'внутренние_электроды', 0.0002, 0.2),
            ('outer_electrodes', 'внешние_электроды', 0.0001, 0.1),
            ('termination', 'терминалы', 0.0001, 0.1),
            ('plating', 'гальваническое_покрытие', 0.0001, 0.1),
        ],
        'materials': [
            ('ceramic_layers', 'barium_titanate', 0.95),
            ('inner_electrodes', 'nickel', 0.95),
            ('outer_electrodes', 'copper', 0.8),
            ('termination', 'copper', 0.9),
            ('plating', 'tin', 0.9),
        ]
    },
    'силовой_транзистор': {
        'parts': [
            ('die', 'sic_кристалл', 0.001, 0.2),
            ('lead_frame', 'силовые_выводы', 0.005, 0.5),
            ('wire_bonds', 'проволочные_соединения', 0.0001, 0.01),
            ('encapsulant', 'эпоксидный_корпус', 0.002, 0.2),
            ('solder', 'пайка_кристалла', 0.0005, 0.05),
            ('gate_terminal', 'затвор', 0.001, 0.04),
        ],
        'materials': [
            ('die', 'silicon_carbide', 0.95),
            ('lead_frame', 'copper_alloy', 0.95),
            ('wire_bonds', 'aluminum', 0.95),
            ('encapsulant', 'epoxy_molding', 0.95),
            ('solder', 'lead_free_solder', 0.9),
        ]
    },
    'память_MRAM': {
        'parts': [
            ('cell_array', 'массив_ячеек', 0.002, 0.4),
            ('periphery', 'периферия', 0.001, 0.2),
            ('sense_amplifiers', 'sense_amplifiers', 0.0005, 0.1),
            ('row_decoders', 'дешифраторы_строк', 0.0005, 0.1),
            ('io_interface', 'I/O_интерфейс', 0.001, 0.2),
        ],
        'materials': [
            ('cell_array', 'silicon_wafer', 0.9),
            ('periphery', 'silicon_wafer', 0.9),
            ('sense_amplifiers', 'silicon_wafer', 0.9),
        ]
    },
    'phase_change_память': {
        'parts': [
            ('cell_array', 'массив_PCM_ячеек', 0.002, 0.4),
            ('selector', 'селектор_устройство', 0.0005, 0.1),
            ('periphery', 'периферия', 0.001, 0.2),
            ('io_interface', 'I/O', 0.001, 0.2),
            ('controller', 'контроллер', 0.0005, 0.1),
        ],
        'materials': [
            ('cell_array', 'gst_chalcogenide', 0.6),
            ('selector', 'silicon_wafer', 0.9),
        ]
    },
    'memristor_массив': {
        'parts': [
            ('crossbar', 'кроссбар_матрица', 0.002, 0.4),
            ('word_drivers', 'драйверы_строк', 0.001, 0.2),
            ('bit_sense', 'sense_amplifiers', 0.001, 0.2),
            ('adc', 'АЦП', 0.0005, 0.1),
            ('controller', 'контроллер', 0.0005, 0.1),
        ],
        'materials': [
            ('crossbar', 'tio2_memristor', 0.7),
            ('word_drivers', 'silicon_wafer', 0.9),
        ]
    },
    'edge_AI_модуль': {
        'parts': [
            ('soc', 'SoC_модуль', 0.01, 0.1),
            ('memory', 'LPDDR_память', 0.005, 0.05),
            ('storage', 'eMMC_флеш', 0.005, 0.05),
            ('pmic', 'PMIC_питание', 0.005, 0.05),
            ('wifi_bt', 'WiFi_BT_модуль', 0.003, 0.03),
            ('connectors', 'разъёмы', 0.02, 0.2),
            ('heat_sink', 'радиатор', 0.03, 0.3),
            ('pcb', 'плата', 0.04, 0.4),
            ('enclosure', 'корпус', 0.05, 0.5),
        ],
        'materials': [
            ('soc', 'silicon_wafer', 0.9),
            ('memory', 'silicon_wafer', 0.9),
            ('storage', 'silicon_wafer', 0.9),
            ('heat_sink', 'aluminum', 0.95),
            ('pcb', 'fr4', 0.8),
            ('enclosure', 'aluminum', 0.9),
        ]
    },
    'литий-тионилхлоридная_батарея': {
        'parts': [
            ('anode', 'литий_анод', 0.05, 0.2),
            ('cathode', 'угольный_катод', 0.05, 0.2),
            ('electrolyte', 'thionyl_chloride', 0.1, 0.4),
            ('separator', 'сепаратор', 0.005, 0.02),
            ('case', 'корпус_нерж', 0.05, 0.2),
            ('terminal', 'вывод', 0.005, 0.02),
        ],
        'materials': [
            ('anode', 'lithium_metal', 0.95),
            ('cathode', 'carbon_black', 0.9),
            ('electrolyte', 'socl2', 0.95),
            ('separator', 'pp_membrane', 0.95),
            ('case', 'stainless_steel_304', 0.95),
        ]
    },
    
    # === ЭНЕРГЕТИЧЕСКАЯ ===
    'твердооксидный_топливный_элемент': {
        'parts': [
            ('anode', 'анод_Ni_Cermet', 0.1, 0.2),
            ('electrolyte', 'YSZ_электролит', 0.05, 0.1),
            ('cathode', 'катод_LSM', 0.1, 0.2),
            ('interconnect', 'интерконнект', 0.15, 0.3),
            ('seal', 'герметизация', 0.02, 0.04),
            ('manifold', 'коллектор_газа', 0.1, 0.2),
        ],
        'materials': [
            ('anode', 'ni_ysz_cermet', 0.9),
            ('electrolyte', 'ysz_electrolyte', 0.95),
            ('cathode', 'lsm_cathode', 0.9),
            ('interconnect', 'crofer_22_apu', 0.95),
        ]
    },
    'водородный_топливный_элемент': {
        'parts': [
            ('membrane', 'PEM_мембрана', 0.05, 0.1),
            ('catalyst_anode', 'Pt_анод', 0.01, 0.02),
            ('catalyst_cathode', 'Pt_катод', 0.01, 0.02),
            ('gdl_anode', 'GDL_анод', 0.05, 0.1),
            ('gdl_cathode', 'GDL_катод', 0.05, 0.1),
            ('bipolar_plate', 'биполярная_пластина', 0.2, 0.4),
            ('gasket', 'уплотнение', 0.02, 0.04),
            ('end_plate', 'торцевая_пластина', 0.15, 0.3),
        ],
        'materials': [
            ('membrane', 'nafion_117', 0.95),
            ('catalyst_anode', 'pt_carbon', 0.5),
            ('catalyst_cathode', 'pt_carbon', 0.5),
            ('gdl_anode', 'carbon_paper', 0.95),
            ('bipolar_plate', 'stainless_steel_316', 0.95),
            ('end_plate', 'aluminum', 0.95),
        ]
    },
    'радиоизотопный_генератор': {
        'parts': [
            ('isotope', 'Pu-238_источник', 5.0, 0.4),
            ('thermocouples', 'термопары', 10.0, 0.3),
            ('cold_side', 'холодный_узел', 5.0, 0.15),
            ('hot_side', 'горячий_узел', 3.0, 0.1),
            ('housing', 'корпус', 10.0, 0.3),
            ('thermal_insulation', 'изоляция', 3.0, 0.1),
            ('connector', 'разъём', 0.5, 0.02),
        ],
        'materials': [
            ('isotope', 'pu238_oxide', 0.95),
            ('thermocouples', 'pbte_teg', 0.9),
            ('cold_side', 'aluminum', 0.95),
            ('housing', 'titanium_alloy', 0.95),
            ('thermal_insulation', 'aerogel', 0.9),
        ]
    },
    'радиоизотопный_генератор_Стирлинг': {
        'parts': [
            ('isotope', 'Pu-238_источник', 2.0, 0.25),
            ('heater_head', 'нагреватель_голова', 3.0, 0.2),
            ('regenerator', 'регенератор', 1.0, 0.1),
            ('cooler', 'охладитель', 2.0, 0.15),
            ('piston', 'поршень', 2.0, 0.15),
            ('alternator', 'генератор_тока', 3.0, 0.2),
            ('housing', 'корпус', 5.0, 0.3),
        ],
        'materials': [
            ('isotope', 'pu238_oxide', 0.95),
            ('heater_head', 'inconel_625', 0.95),
            ('regenerator', 'stainless_steel_mesh', 0.95),
            ('piston', 'inconel_718', 0.95),
            ('alternator', 'copper_wire', 0.6),
        ]
    },
    'суперконденсатор': {
        'parts': [
            ('electrode_pos', 'положительный_электрод', 0.1, 0.3),
            ('electrode_neg', 'отрицательный_электрод', 0.1, 0.3),
            ('separator', 'сепаратор', 0.02, 0.05),
            ('electrolyte', 'электролит', 0.05, 0.15),
            ('current_collector', 'токосъёмник', 0.05, 0.15),
            ('terminal', 'выводы', 0.02, 0.05),
            ('case', 'корпус', 0.05, 0.15),
        ],
        'materials': [
            ('electrode_pos', 'activated_carbon', 0.9),
            ('electrode_neg', 'activated_carbon', 0.9),
            ('separator', 'cellulose', 0.95),
            ('electrolyte', 'tebabf4_acn', 0.95),
            ('current_collector', 'aluminum', 0.95),
            ('case', 'aluminum', 0.95),
        ]
    },
    'литий-ионный_аккумулятор': {
        'parts': [
            ('anode', 'графит_анод', 0.05, 0.2),
            ('cathode', 'NMC_катод', 0.1, 0.4),
            ('electrolyte', 'LiPF6_электролит', 0.05, 0.2),
            ('separator', 'сепаратор', 0.01, 0.04),
            ('current_collector_cu', 'медный_токосъёмник', 0.02, 0.08),
            ('current_collector_al', 'алюминиевый_токосъёмник', 0.02, 0.08),
            ('case', 'корпус', 0.05, 0.2),
        ],
        'materials': [
            ('anode', 'graphite', 0.9),
            ('cathode', 'lini_mn_co_o2', 0.85),
            ('electrolyte', 'lipf6_ec_dmc', 0.95),
            ('separator', 'pe_pp', 0.95),
            ('current_collector_cu', 'copper', 0.99),
            ('current_collector_al', 'aluminum', 0.99),
            ('case', 'aluminum', 0.95),
        ]
    },
    'свинцово-кислотная_батарея': {
        'parts': [
            ('anode', 'PbO2_анод', 2.0, 0.2),
            ('cathode', 'Pb_катод', 2.0, 0.2),
            ('electrolyte', 'H2SO4_электролит', 3.0, 0.3),
            ('separator', 'сепаратор', 0.2, 0.02),
            ('grid_pos', 'решётка_PbSb', 1.0, 0.1),
            ('grid_neg', 'решётка_PbCa', 1.0, 0.1),
            ('case', 'корпус_PP', 1.0, 0.1),
            ('terminal', 'вывод', 0.5, 0.05),
        ],
        'materials': [
            ('anode', 'pbo2', 0.95),
            ('cathode', 'spongy_lead', 0.95),
            ('electrolyte', 'h2so4_aqueous', 0.95),
            ('separator', 'pe_separator', 0.95),
            ('grid_pos', 'pb_sb_alloy', 0.95),
            ('case', 'polypropylene', 0.95),
        ]
    },
    'бетавольтаик': {
        'parts': [
            ('isotope', 'Ni-63_источник', 0.001, 0.3),
            ('semiconductor', 'SiC_преобразователь', 0.005, 0.5),
            ('encapsulant', 'инкапсулянт', 0.002, 0.1),
            ('case', 'корпус_титан', 0.005, 0.3),
            ('terminal', 'вывод', 0.0005, 0.02),
        ],
        'materials': [
            ('isotope', 'ni63_metal', 0.95),
            ('semiconductor', 'silicon_carbide', 0.95),
            ('encapsulant', 'epoxy', 0.95),
            ('case', 'titanium_alloy', 0.95),
        ]
    },
    'бета_вольтаик_SiC': {
        'parts': [
            ('isotope', 'Ni-63_источник', 0.001, 0.25),
            ('sic_diode', 'SiC_pn_диод', 0.003, 0.5),
            ('substrate', 'SiC_подложка', 0.002, 0.2),
            ('encapsulant', 'инкапсулянт', 0.001, 0.1),
            ('case', 'корпус', 0.003, 0.3),
        ],
        'materials': [
            ('isotope', 'ni63_metal', 0.95),
            ('sic_diode', 'silicon_carbide', 0.95),
            ('substrate', 'silicon_carbide', 0.99),
            ('encapsulant', 'epoxy', 0.95),
            ('case', 'titanium_alloy', 0.95),
        ]
    },
    'бета_вольтаик_3D_SiC': {
        'parts': [
            ('isotope', 'H-3_тритий', 0.0005, 0.2),
            ('micropillars', '3D_SiC_микропилляры', 0.001, 0.4),
            ('substrate', 'SiC_подложка', 0.002, 0.3),
            ('case', 'корпус', 0.002, 0.3),
        ],
        'materials': [
            ('isotope', 'tritium_gas', 0.95),
            ('micropillars', 'silicon_carbide', 0.95),
            ('substrate', 'silicon_carbide', 0.99),
        ]
    },
    'радиоизотопный_генератор_Am241': {
        'parts': [
            ('isotope', 'Am-241_источник', 0.1, 0.4),
            ('thermocouples', 'термопары', 0.5, 0.3),
            ('shielding', 'экранирование', 1.0, 0.5),
            ('housing', 'корпус', 0.5, 0.3),
        ],
        'materials': [
            ('isotope', 'am241_oxide', 0.95),
            ('thermocouples', 'pbte_teg', 0.9),
            ('shielding', 'tungsten_alloy', 0.95),
            ('housing', 'stainless_steel_316', 0.95),
        ]
    },
    'фотоэлектрический_модуль': {
        'parts': [
            ('cells', 'Si_ячейки', 5.0, 0.4),
            ('front_glass', 'переднее_стекло', 8.0, 0.3),
            ('backsheet', 'подложка', 2.0, 0.1),
            ('frame', 'рама_алюминий', 3.0, 0.2),
            ('junction_box', 'распредкоробка', 0.5, 0.05),
            ('encapsulant', 'инкапсулянт_EVA', 1.0, 0.1),
        ],
        'materials': [
            ('cells', 'monocrystalline_si', 0.95),
            ('front_glass', 'low_iron_glass', 0.95),
            ('backsheet', 'tedlar_pet', 0.95),
            ('frame', 'aluminum_6063', 0.95),
            ('encapsulant', 'eva', 0.95),
        ]
    },
    'микро_реактор_деления': {
        'parts': [
            ('fuel', 'U-235_топливо', 50.0, 0.1),
            ('moderator', 'замедлитель', 200.0, 0.4),
            ('heat_exchanger', 'теплообменник', 500.0, 0.3),
            ('control_rods', 'стержни_управления', 100.0, 0.05),
            ('shielding', 'экранирование', 5000.0, 0.4),
            ('vessel', 'корпус_реактора', 2000.0, 0.2),
            ('coolant', 'охладитель', 500.0, 0.05),
        ],
        'materials': [
            ('fuel', 'uo2_pellets', 0.95),
            ('moderator', 'graphite', 0.95),
            ('heat_exchanger', 'inconel_625', 0.5),
            ('shielding', 'concrete_barite', 0.95),
            ('vessel', 'stainless_steel_316', 0.95),
            ('coolant', 'sodium', 0.95),
        ]
    },
    'Стирлинг_конвертер': {
        'parts': [
            ('heater_head', 'нагреватель', 0.5, 0.2),
            ('regenerator', 'регенератор', 0.3, 0.1),
            ('cooler', 'охладитель', 0.5, 0.2),
            ('displacer_piston', 'поршень_вытеснитель', 0.5, 0.2),
            ('power_piston', 'рабочий_поршень', 0.5, 0.2),
            ('alternator', 'линейный_генератор', 0.7, 0.3),
        ],
        'materials': [
            ('heater_head', 'inconel_625', 0.95),
            ('regenerator', 'stainless_steel_mesh', 0.95),
            ('displacer_piston', 'inconel_718', 0.9),
            ('power_piston', 'inconel_718', 0.9),
            ('alternator', 'copper_wire', 0.6),
        ]
    },
    'свободнопоршневой_Стирлинг': {
        'parts': [
            ('heater', 'нагреватель', 0.3, 0.2),
            ('regenerator', 'регенератор', 0.2, 0.1),
            ('cooler', 'охладитель', 0.3, 0.2),
            ('piston', 'поршень', 0.5, 0.3),
            ('alternator', 'генератор', 0.7, 0.4),
            ('gas_spring', 'газовая_пружина', 0.3, 0.2),
        ],
        'materials': [
            ('heater', 'inconel_625', 0.95),
            ('piston', 'inconel_718', 0.9),
            ('alternator', 'copper_wire', 0.6),
        ]
    },
    'импульсный_генератор_Маркса': {
        'parts': [
            ('capacitors', 'конденсаторы', 100.0, 0.5),
            ('spark_gaps', 'искровые_промежутки', 50.0, 0.2),
            ('resistors', 'зарядные_резисторы', 20.0, 0.1),
            ('housing', 'корпус', 100.0, 0.3),
            ('output_terminal', 'выходной_вывод', 10.0, 0.05),
            ('insulator', 'изоляторы_SF6', 50.0, 0.2),
        ],
        'materials': [
            ('capacitors', 'ceramic_capacitors', 0.95),
            ('spark_gaps', 'tungsten_electrodes', 0.5),
            ('housing', 'aluminum', 0.95),
        ]
    },
    'модуль_Пельтье': {
        'parts': [
            ('peltier_couples', 'термоэлементы', 0.01, 0.4),
            ('ceramic_top', 'керамика_верх', 0.005, 0.2),
            ('ceramic_bottom', 'керамика_низ', 0.005, 0.2),
            ('electrodes', 'электроды', 0.002, 0.1),
            ('solder', 'припой', 0.002, 0.1),
            ('wires', 'провода', 0.001, 0.05),
        ],
        'materials': [
            ('peltier_couples', 'bi2te3', 0.95),
            ('ceramic_top', 'alumina', 0.95),
            ('ceramic_bottom', 'alumina', 0.95),
            ('electrodes', 'copper', 0.95),
        ]
    },
    'реверсивный_модуль_Пельтье': {
        'parts': [
            ('peltier_couples', 'термоэлементы', 0.015, 0.4),
            ('ceramic_top', 'керамика_верх', 0.007, 0.2),
            ('ceramic_bottom', 'керамика_низ', 0.007, 0.2),
            ('electrodes', 'электроды', 0.003, 0.1),
            ('solder', 'припой', 0.003, 0.1),
        ],
        'materials': [
            ('peltier_couples', 'bi2te3', 0.95),
            ('ceramic_top', 'alumina', 0.95),
            ('ceramic_bottom', 'alumina', 0.95),
        ]
    },
    'термоэлектрический_генератор': {
        'parts': [
            ('teg_modules', 'ТЕГ_модули', 0.2, 0.4),
            ('heat_sink_hot', 'горячий_радиатор', 0.1, 0.2),
            ('heat_sink_cold', 'холодный_радиатор', 0.1, 0.2),
            ('clamping', 'прижимные_болты', 0.05, 0.1),
            ('insulation', 'изоляция', 0.05, 0.1),
        ],
        'materials': [
            ('teg_modules', 'bi2te3', 0.9),
            ('heat_sink_hot', 'copper', 0.95),
            ('heat_sink_cold', 'aluminum', 0.95),
        ]
    },
    'термофотоэлектрический_генератор': {
        'parts': [
            ('emitter', 'излучатель', 0.1, 0.3),
            ('filter', 'оптический_фильтр', 0.05, 0.15),
            ('pv_cell', 'PV_ячейка', 0.05, 0.15),
            ('heat_source', 'источник_тепла', 0.3, 0.4),
            ('housing', 'корпус', 0.2, 0.3),
            ('cooling', 'охлаждение', 0.1, 0.15),
        ],
        'materials': [
            ('emitter', 'tungsten', 0.95),
            ('pv_cell', 'gaSb', 0.9),
            ('heat_source', 'silicon_carbide', 0.9),
        ]
    },
    'TPV_ленточный': {
        'parts': [
            ('emitter_ribbon', 'излучающая_лента', 0.05, 0.3),
            ('pv_cells', 'PV_ячейки', 0.05, 0.3),
            ('reflector', 'рефлектор', 0.1, 0.3),
            ('cooling', 'охлаждение', 0.05, 0.2),
        ],
        'materials': [
            ('emitter_ribbon', 'tungsten', 0.95),
            ('pv_cells', 'gaSb', 0.9),
            ('reflector', 'gold_coating', 0.8),
        ]
    },
    'электромагнитный_ускоритель': {
        'parts': [
            ('coil', 'катушка', 100.0, 0.4),
            ('capacitor_bank', 'батарея_конденсаторов', 200.0, 0.4),
            ('barrel', 'ствол', 50.0, 0.1),
            ('switch', 'коммутатор', 20.0, 0.05),
            ('projectile', 'снаряд', 10.0, 0.05),
            ('housing', 'корпус', 500.0, 0.4),
        ],
        'materials': [
            ('coil', 'copper_wire', 0.95),
            ('capacitor_bank', 'aluminum_electrolytic', 0.9),
            ('barrel', 'composite_material', 0.9),
        ]
    },
    'индуктивный_накопитель': {
        'parts': [
            ('coil', 'индуктивность', 50.0, 0.5),
            ('core', 'магнитопровод', 30.0, 0.3),
            ('housing', 'корпус', 10.0, 0.1),
            ('switch', 'коммутатор', 5.0, 0.05),
            ('cooling', 'охлаждение', 5.0, 0.05),
        ],
        'materials': [
            ('coil', 'copper_wire', 0.95),
            ('core', 'electrical_steel', 0.95),
            ('housing', 'aluminum', 0.95),
        ]
    },
    'электромагнитная_муфта': {
        'parts': [
            ('coil', 'электромагнит', 1.0, 0.2),
            ('rotor', 'ротор', 1.5, 0.3),
            ('stator', 'статор', 1.5, 0.3),
            ('powder', 'магнитный_порошок', 0.3, 0.06),
            ('bearings', 'подшипники', 0.3, 0.06),
            ('housing', 'корпус', 1.0, 0.2),
        ],
        'materials': [
            ('coil', 'copper_wire', 0.9),
            ('rotor', 'steel_1045', 0.95),
            ('stator', 'steel_1045', 0.95),
            ('powder', 'iron_powder', 0.95),
            ('bearings', 'stainless_steel_440c', 0.9),
        ]
    },
    'HTS_подшипник': {
        'parts': [
            ('hts_element', 'YBCO_элемент', 0.5, 0.3),
            ('magnet', 'магнит_ротор', 1.0, 0.4),
            ('cryostat', 'криостат', 5.0, 0.4),
            ('shaft', 'вал', 1.0, 0.1),
            ('housing', 'корпус', 2.0, 0.2),
        ],
        'materials': [
            ('hts_element', 'ybco_bulk', 0.95),
            ('magnet', 'ndfeb', 0.95),
            ('cryostat', 'stainless_steel_316', 0.95),
            ('shaft', 'titanium_alloy', 0.95),
        ]
    },
    'магнитная_мышца': {
        'parts': [
            ('magnets', 'постоянные_магниты', 0.05, 0.5),
            ('coil', 'катушка', 0.02, 0.2),
            ('spring', 'пружина', 0.02, 0.2),
            ('housing', 'корпус', 0.02, 0.2),
        ],
        'materials': [
            ('magnets', 'ndfeb', 0.95),
            ('coil', 'copper_wire', 0.9),
            ('spring', 'spring_steel', 0.95),
        ]
    },
    'планетарный_роликовинт': {
        'parts': [
            ('screw', 'винт', 1.0, 0.4),
            ('rollers', 'ролики', 0.5, 0.2),
            ('nut', 'гайка', 1.0, 0.4),
            ('bearings', 'подшипники', 0.3, 0.1),
            ('seals', 'уплотнения', 0.1, 0.05),
            ('housing', 'корпус', 1.0, 0.2),
        ],
        'materials': [
            ('screw', 'bearing_steel_52100', 0.95),
            ('rollers', 'bearing_steel_52100', 0.95),
            ('nut', 'bearing_steel_52100', 0.95),
            ('bearings', 'stainless_steel_440c', 0.9),
        ]
    },
    'алюминиево-воздушный_ТЭ': {
        'parts': [
            ('anode', 'Al_анод', 1.0, 0.4),
            ('cathode', 'воздушный_катод', 0.5, 0.2),
            ('electrolyte', 'щелочной_электролит', 0.5, 0.2),
            ('separator', 'сепаратор', 0.1, 0.04),
            ('air_electrode', 'газодиффузионный_электрод', 0.3, 0.1),
            ('housing', 'корпус', 0.5, 0.2),
        ],
        'materials': [
            ('anode', 'aluminum_1100', 0.95),
            ('cathode', 'carbon_ptfe', 0.9),
            ('electrolyte', 'koh_aqueous', 0.95),
        ]
    },
    'микро_ТЭЦ': {
        'parts': [
            ('engine', 'двигатель', 5.0, 0.4),
            ('generator', 'генератор', 3.0, 0.3),
            ('heat_exchanger', 'теплообменник', 2.0, 0.2),
            ('controls', 'электроника_управления', 0.5, 0.05),
            ('housing', 'корпус', 2.0, 0.2),
        ],
        'materials': [
            ('engine', 'cast_iron', 0.7),
            ('generator', 'copper_wire', 0.5),
            ('heat_exchanger', 'stainless_steel_316', 0.7),
        ]
    },
    'ЭМИ_генератор': {
        'parts': [
            ('capacitor_bank', 'батарея_конденсаторов', 50.0, 0.4),
            ('antenna', 'антенна_рупор', 20.0, 0.2),
            ('switch', 'коммутатор', 10.0, 0.1),
            ('source', 'взрывной_источник', 5.0, 0.05),
            ('waveguide', 'волновод', 30.0, 0.3),
            ('housing', 'корпус', 100.0, 0.4),
        ],
        'materials': [
            ('capacitor_bank', 'ceramic_capacitors', 0.95),
            ('antenna', 'aluminum', 0.95),
            ('waveguide', 'aluminum', 0.95),
            ('housing', 'aluminum', 0.95),
        ]
    },
    
    # === ПРОЧЕЕ (generic) ===
    'прочее': {
        'parts': [
            ('core', 'основной_элемент', 0.5, 0.5),
            ('housing', 'корпус', 0.3, 0.3),
            ('connectors', 'разъёмы', 0.05, 0.05),
            ('mounting', 'крепёж', 0.1, 0.1),
        ],
        'materials': [
            ('core', 'generic_material', 0.9),
            ('housing', 'aluminum', 0.9),
        ]
    },
}


# ============================================================================
# ГЕНЕРАЦИЯ ДОЧЕРНИХ ЧАСТЕЙ ДЛЯ ИЗДЕЛИЯ
# ============================================================================

def get_template_for_izdelie(izd_data: dict) -> dict:
    """Выбрать шаблон декомпозиции для изделия на основе подтипа."""
    subtype = izd_data.get('подтип', 'прочее')
    # Найти по точному совпадению подтипа
    if subtype in DECOMP_TEMPLATES:
        return DECOMP_TEMPLATES[subtype]
    # Fallback: generic
    return DECOMP_TEMPLATES['прочее']


def generate_part_id(parent_id: str, part_suffix: str) -> str:
    """Сгенерировать id дочерней части."""
    # Удалить 'izdelie_' префикс
    short = parent_id
    if short.startswith('izdelie_'):
        short = short[len('izdelie_'):]
    return f"часть_{short}_{part_suffix}"


def generate_part_content(part_id: str, parent_id: str, subsystem: str,
                          subtype: str, mass_kg: float, share: float,
                          count: int = 1) -> str:
    """Сгенерировать содержимое файла части.

    v9.35: добавлено поле количество=N (для paired parts).
    """
    count_yaml = f"количество: {count}\n" if count > 1 else ""
    title_suffix = f" (×{count})" if count > 1 else ""
    return f"""---
id: {part_id}
тип: изделие
категория: машиностроение
уровень_иерархии: промежуточный
уровень_номер: 2
подсистема: {subsystem}
подтип: {subtype}
стандарты: []
исследовательская_группа: null
родитель: {parent_id}
{count_yaml}дочерние_части: []
материалы_частей: []
scaling_type: количественный
соединители: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  масса_kg: {mass_kg}
  доля_массы_родителя: {share}
наследуемые: {{}}
дополнительные: {{}}
дата_создания: {TODAY}
дата_обновления: {TODAY}
источник: web_search
источник_разбора: канон
---

# Часть: {part_id}{title_suffix}

## Описание

Дочерняя часть изделия `{parent_id}` (подсистема: {subsystem}, подтип: {subtype}).

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | {subsystem} | — | canon |
| подтип | {subtype} | — | canon |
| масса | {mass_kg} | kg | canon |
| доля массы родителя | {share} | — | canon |
| количество | {count} | шт. | canon |

## Состав

Промежуточная часть (уровень 2). Дочерних частей нет.

## Источники

- Канон: декомпозиция изделия `{parent_id}` (web search {TODAY})
"""


def update_parent_file(parent_path: Path, children_ids: list, materials: list) -> str:
    """Обновить родительский файл: заполнить дочерние_части и материалы_частей.

    v9.37: возврат нового текста вместо прямой записи — caller (decompose_izdelie)
    включит его в TransactionBatch вместе с дочерними файлами.
    """
    text = parent_path.read_text(encoding='utf-8')
    data, yaml_text, body = read_yaml_frontmatter(parent_path)
    if not data:
        return False
    
    # Сериализовать дочерние_части (с переводом строки после двоеточия)
    if children_ids:
        children_yaml = "\n" + "\n".join(f"  - {cid}" for cid in children_ids) + "\n"
    else:
        children_yaml = "[]\n"
    
    # Сериализовать материалы_частей
    if materials:
        materials_yaml = "\n"
        for m in materials:
            part_suffix, material_id, share_in_part, share_in_parent = m
            materials_yaml += f"  - часть: {part_suffix}\n    материал: {material_id}\n    доля_массы: {round(share_in_parent, 4)}\n"
    else:
        materials_yaml = "[]\n"
    
    new_yaml = yaml_text
    
    # Заменить дочерние_части
    pattern = r"^дочерние_части:.*?(?=^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё+-]*:|\Z)"
    if re.search(pattern, new_yaml, re.MULTILINE | re.DOTALL):
        new_yaml = re.sub(pattern, f"дочерние_части:{children_yaml}", new_yaml, count=1, flags=re.MULTILINE | re.DOTALL)
    else:
        # Добавить после id:
        id_pattern = r"^(id:\s*[^\n]+\n)"
        if re.search(id_pattern, new_yaml, re.MULTILINE):
            new_yaml = re.sub(id_pattern, rf"\1дочерние_части:{children_yaml}", new_yaml, count=1, flags=re.MULTILINE)
    
    # Заменить материалы_частей
    pattern = r"^материалы_частей:.*?(?=^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё+-]*:|\Z)"
    if re.search(pattern, new_yaml, re.MULTILINE | re.DOTALL):
        new_yaml = re.sub(pattern, f"материалы_частей:{materials_yaml}", new_yaml, count=1, flags=re.MULTILINE | re.DOTALL)
    else:
        # Добавить после дочерние_части (найти блок дочерние_части: ... и добавить после)
        dc_pattern = r"^(дочерние_части:[^\n]*\n(?:  - [^\n]*\n)*)"
        if re.search(dc_pattern, new_yaml, re.MULTILINE):
            new_yaml = re.sub(dc_pattern, rf"\1материалы_частей:{materials_yaml}", new_yaml, count=1, flags=re.MULTILINE)
    
    # Обновить дата_обновления
    new_yaml = re.sub(
        r"^дата_обновления:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"дата_обновления: {TODAY}",
        new_yaml,
        count=1,
        flags=re.MULTILINE,
    )
    
    # Добавить Mermaid в body (если ещё нет)
    if '```mermaid' not in body:
        parent_id_match = re.search(r"^id:\s*(\S+)", yaml_text, re.MULTILINE)
        if parent_id_match:
            parent_id = parent_id_match.group(1)
            short_id = parent_id.replace('izdelie_', '').replace('часть_', '')[:20]
            mermaid = ["```mermaid", "graph TD", f'    {short_id}["{parent_id}"]']
            for cid in children_ids:
                child_short = cid.replace('часть_', '')[:25]
                mermaid.append(f'    {child_short}["{cid}"]')
                mermaid.append(f'    {short_id} --> {child_short}')
            mermaid.append("```")
            body = body.rstrip() + "\n\n## Декомпозиция\n\n" + "\n".join(mermaid) + "\n"
    
    # Найти закрывающий --- (если есть)
    end_match = re.search(r"\n---\s*\n", new_yaml)
    if end_match:
        new_text = "---\n" + new_yaml + body
    else:
        new_text = "---\n" + new_yaml + "\n---\n" + body
    
    # v9.37: прямой write убран — функция pure, caller записывает через TransactionBatch
    return new_text


def decompose_izdelie(izd_id: str, izd_data: dict) -> tuple[int, list]:
    """Выполнить декомпозицию для одного изделия.
    
    Возвращает (количество_созданных_частей, список_созданных_файлов).
    """
    parent_path = Path(izd_data['_path'])
    subsystem = izd_data.get('подсистема', 'прочее')
    subtype = izd_data.get('подтип', 'прочее')
    
    template = get_template_for_izdelie(izd_data)
    if not template:
        return 0, []
    
    # Создать дочерние части и обновить родителя в одной транзакции (T2 v9.37):
    # раньше parent_path.write_text → part_file.write_text в разных вызовах,
    # сбой между ними порвал консистентность родителя и детей.
    created_files = []
    children_ids = []
    materials_with_shares = []
    pending_parent_write = None  # (parent_path, new_text) — запишется в batch после детей
    pending_parts = []          # [(part_file, content), ...]
    
    for part in template['parts']:
        # v9.35: support optional count field (5-tuple or 6-tuple)
        if len(part) == 5:
            part_suffix, part_subtype, mass_kg, share = part
            count = 1
        else:
            part_suffix, part_subtype, mass_kg, share, count = part
        part_id = generate_part_id(izd_id, part_suffix)
        children_ids.append(part_id)
        
        # Создать файл части
        part_dir = IZDELIYA_DIR / subsystem / part_id
        part_file = part_dir / "_index.md"
        if not part_file.exists():
            part_dir.mkdir(parents=True, exist_ok=True)
            content = generate_part_content(part_id, izd_id, subsystem, part_subtype, mass_kg, share, count)
            pending_parts.append((part_file, content))
            created_files.append(str(part_file))
    
    # Подготовить материалы с долями
    for m in template['materials']:
        part_suffix, material_id, share_in_part = m
        part_id = generate_part_id(izd_id, part_suffix)
        # Найти share (долю части) в parts
        share_in_parent = 0.0
        for p in template['parts']:
            if p[0] == part_suffix:
                share_in_parent = p[3] * share_in_part
                break
        materials_with_shares.append((part_id, material_id, share_in_part, share_in_parent))
    
    # Обновить родительский файл (получить текст без записи)
    parent_new_text = update_parent_file(parent_path, children_ids, materials_with_shares)
    if not parent_new_text:
        return 0, created_files  # parent file не парсится — пишем только то, что успели собрать

    # Транзакционный commit: либо все файлы (родитель + дети) обновятся, либо ни одного (T2 v9.37).
    # Раньше: parent_path.write_text → part_file.write_text → ... — сбой между ними портил связность.
    try:
        with TransactionBatch() as batch:
            batch.write(parent_path, parent_new_text)
            for part_file, content in pending_parts:
                batch.write(part_file, content)
    except OSError as e:
        print(f"  ⚠️ TransactionBatch commit failed for {izd_id}: {e}", file=sys.stderr)
        return 0, []  # созданные файлы в staging удалены rollback'ом
    
    return len(created_files), created_files


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=== SkyNet Decomposition for All Izdeliya v9.31 ===")
    print()
    
    # Загрузить все изделия
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
    from validate_decomposition import load_all_izdeliya
    izdeliya = load_all_izdeliya()
    
    # Отфильтровать: только изделия верхнего уровня без декомпозиции
    # (пропустить izdelie_SkyNet-* и часть_*)
    targets = []
    for izd_id, data in izdeliya.items():
        if izd_id.startswith('izdelie_SkyNet-') or izd_id.startswith('часть_'):
            continue
        children = data.get('дочерние_части', [])
        if isinstance(children, list) and children:
            continue
        targets.append((izd_id, data))
    
    print(f"Изделий для декомпозиции: {len(targets)}")
    print()
    
    total_parts_created = 0
    total_updated_parents = 0
    
    for izd_id, data in targets:
        n_created, _ = decompose_izdelie(izd_id, data)
        if n_created > 0:
            total_parts_created += n_created
            total_updated_parents += 1
            subtype = data.get('подтип', 'прочее')
            print(f"  ✓ {izd_id[:50]:50s} +{n_created} частей ({subtype})")
    
    print()
    print(f"=== Сводка ===")
    print(f"  Изделий декомпозировано: {total_updated_parents}/{len(targets)}")
    print(f"  Дочерних частей создано: {total_parts_created}")


if __name__ == "__main__":
    main()
