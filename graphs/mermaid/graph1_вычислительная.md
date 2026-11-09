# Граф 1 — подсистема «вычислительная»

```mermaid
graph LR
    izdelie_sot_mram[память_MRAM]
    izdelie_nvidia_jetson_orin_nano[edge_AI_модуль]
    izdelie_brainchip_akida_2[нейроморфный_процессор]
    izdelie_stm32h743[прочее]
    izdelie_ibm_northpole[AI_инференс_чип]
    izdelie_polyimide_fpc[прочее]
    izdelie_gr801_noel_v_risc_v[RISC-V_процессор]
    izdelie_intel_loihi_2[нейроморфный_процессор]
    izdelie_memristornye_matritsy[memristor_массив]
    izdelie_pcm[phase_change_память]
    izdelie_sic_mosfet[силовой_транзистор]
    izdelie_kondensatory_keramicheskie[керамический_конденсатор]
    izdelie_stm32[прочее]
    izdelie_halve[нейроморфный_процессор]
    часть_sot_mram_periphery[периферия]
    часть_sot_mram_io_interface[I/O_интерфейс]
    часть_sot_mram_row_decoders[дешифраторы_строк]
    часть_sot_mram_cell_array[массив_ячеек]
    часть_sot_mram_sense_amplifiers[sense_amplifiers]
    часть_nvidia_jetson_orin_nano_pcb[плата]
    часть_nvidia_jetson_orin_nano_pmic[PMIC_питание]
    часть_nvidia_jetson_orin_nano_connectors[разъёмы]
    часть_nvidia_jetson_orin_nano_storage[eMMC_флеш]
    часть_nvidia_jetson_orin_nano_memory[LPDDR_память]
    часть_nvidia_jetson_orin_nano_heat_sink[радиатор]
    часть_nvidia_jetson_orin_nano_wifi_bt[WiFi_BT_модуль]
    часть_nvidia_jetson_orin_nano_enclosure[корпус]
    часть_brainchip_akida_2_encapsulant[инкапсулянт]
    часть_brainchip_akida_2_substrate[подложка_FR5_BT]
    часть_brainchip_akida_2_pins_balls[пины_BGA]
    часть_brainchip_akida_2_capacitors[блокировка_питания]
    часть_brainchip_akida_2_die[кремниевый_кристалл]
    часть_brainchip_akida_2_pcb[плата_носитель]
    часть_brainchip_akida_2_thermal_spreader[теплораспределитель]
    часть_stm32h743_connectors[разъёмы]
    часть_stm32h743_mounting[крепёж]
    часть_stm32h743_core[основной_элемент]
    часть_stm32h743_housing[корпус]
    часть_ibm_northpole_hbm[память_HBM]
    часть_ibm_northpole_capacitors[MLCC_блок]
    часть_ibm_northpole_die[инференс_кристалл]
    часть_ibm_northpole_thermal_spreader[теплораспределитель]
    часть_ibm_northpole_substrate[органическая_подложка]
    часть_ibm_northpole_package[корпус_FCBGA]
    часть_polyimide_fpc_housing[корпус]
    часть_polyimide_fpc_mounting[крепёж]
    часть_polyimide_fpc_connectors[разъёмы]
    часть_polyimide_fpc_core[основной_элемент]
    часть_gr801_noel_v_risc_v_die[risc_v_кристалл]
    часть_gr801_noel_v_risc_v_capacitors[конденсаторы]
    часть_gr801_noel_v_risc_v_flash[флеш_память]
    часть_gr801_noel_v_risc_v_crystal_osc[кварцевый_резонатор]
    часть_gr801_noel_v_risc_v_thermal_pad[термопрокладка]
    часть_gr801_noel_v_risc_v_pcb[плата]
    часть_gr801_noel_v_risc_v_sram[SRAM_кэш]
    часть_gr801_noel_v_risc_v_substrate[подложка]
    часть_gr801_noel_v_risc_v_pins[пины]
    часть_gr801_noel_v_risc_v_package[корпус_FCTEBGA]
    часть_intel_loihi_2_pcb[плата_носитель]
    часть_intel_loihi_2_die[кремниевый_кристалл]
    часть_intel_loihi_2_substrate[подложка_FR5_BT]
    часть_intel_loihi_2_capacitors[блокировка_питания]
    часть_intel_loihi_2_encapsulant[инкапсулянт]
    часть_intel_loihi_2_pins_balls[пины_BGA]
    часть_intel_loihi_2_thermal_spreader[теплораспределитель]
    часть_memristornye_matritsy_word_drivers[драйверы_строк]
    часть_memristornye_matritsy_controller[контроллер]
    часть_memristornye_matritsy_bit_sense[sense_amplifiers]
    часть_memristornye_matritsy_crossbar[кроссбар_матрица]
    часть_memristornye_matritsy_adc[АЦП]
    часть_pcm_cell_array[массив_PCM_ячеек]
    часть_pcm_selector[селектор_устройство]
    часть_pcm_io_interface[I/O]
    часть_pcm_periphery[периферия]
    часть_pcm_controller[контроллер]
    часть_sic_mosfet_wire_bonds[проволочные_соединения]
    часть_sic_mosfet_gate_terminal[затвор]
    часть_sic_mosfet_solder[пайка_кристалла]
    часть_sic_mosfet_encapsulant[эпоксидный_корпус]
    часть_sic_mosfet_die[sic_кристалл]
    часть_sic_mosfet_lead_frame[силовые_выводы]
    часть_kondensatory_keramicheskie_inner_electrodes[внутренние_электроды]
    часть_kondensatory_keramicheskie_termination[терминалы]
    часть_kondensatory_keramicheskie_ceramic_layers[керамические_слои]
    часть_kondensatory_keramicheskie_plating[гальваническое_покрытие]
    часть_kondensatory_keramicheskie_outer_electrodes[внешние_электроды]
    часть_stm32_core[основной_элемент]
    часть_stm32_housing[корпус]
    часть_stm32_connectors[разъёмы]
    часть_stm32_mounting[крепёж]
    часть_halve_capacitors[блокировка_питания]
    часть_halve_thermal_spreader[теплораспределитель]
    часть_halve_die[кремниевый_кристалл]
    часть_halve_pcb[плата_носитель]
    часть_halve_substrate[подложка_FR5_BT]
    часть_halve_encapsulant[инкапсулянт]
    часть_halve_pins_balls[пины_BGA]
    часть_t800_cpu[neural_net_cpu]
    часть_t600_cpu[early_neural_cpu]
    часть_cameron_cpu[neural_net_cpu_cameron]
    часть_t_x_cpu[neural_net_cpu_tx]
    часть_rev9_полисплав_оболочка[mimetic_polyalloy_sheath]
    часть_marcus_человеческий_мозг[human_brain_hybrid]
    часть_t850_cpu[neural_net_cpu_v2]
    izdelie_SkyNet_T1000[прочее]
    izdelie_SkyNet_T1001[прочее]
    часть_t1000_миметический_полисплав[mimetic_polyalloy]
    часть_t1001_миметический_полисплав[mimetic_polyalloy_t1001]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_copper[Cu ≥99.9% (электролити…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    izdelie_nvidia_jetson_orin_nano -->|материал| material_aluminum
    izdelie_brainchip_akida_2 -->|материал| material_copper
    izdelie_stm32h743 -->|материал| material_aluminum
    izdelie_ibm_northpole -->|материал| material_copper
    izdelie_polyimide_fpc -->|материал| material_aluminum
    izdelie_intel_loihi_2 -->|материал| material_copper
    izdelie_sic_mosfet -->|материал| material_aluminum
    izdelie_kondensatory_keramicheskie -->|материал| material_copper
    izdelie_stm32 -->|материал| material_aluminum
    izdelie_halve -->|материал| material_copper
    часть_nvidia_jetson_orin_nano_enclosure -->|материал| material_al_6061_t6
    часть_brainchip_akida_2_thermal_spreader -->|материал| material_copper
    часть_stm32h743_mounting -->|материал| material_al_6061_t6
    часть_stm32h743_housing -->|материал| material_al_6061_t6
    часть_ibm_northpole_thermal_spreader -->|материал| material_copper
    часть_polyimide_fpc_housing -->|материал| material_al_6061_t6
    часть_intel_loihi_2_thermal_spreader -->|материал| material_copper
    часть_sic_mosfet_lead_frame -->|материал| material_copper
    часть_kondensatory_keramicheskie_termination -->|материал| material_copper
    часть_kondensatory_keramicheskie_outer_electrodes -->|материал| material_copper
    часть_stm32_housing -->|материал| material_al_6061_t6
    часть_stm32_connectors -->|материал| material_stal_st3
    часть_halve_thermal_spreader -->|материал| material_copper
    часть_t_x_cpu -->|материал| material_al_6061_t6
    часть_marcus_человеческий_мозг -->|материал| material_ti_6al_4v
    часть_t850_cpu -->|материал| material_al_6061_t6
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Si (кремний); электронный сорт ≥99.9999999% (9N) для подложек ИС, солнечный ≥99.9999% (6N), металлургический ~98–99% (Si-Fe, Si-Ca примеси)` | 25 |
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 12 |
| `BaTiO3 ≥98.5% (титанат бария, перовскит ABO3); для X5R/X7R-диэлектриков MLCC легируется Dy2O3, Ho2O3, Y2O3, Mg, Si, Mn (core-shell BME с Ni-электродами)` | 7 |
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 7 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 6 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 5 |
| `Sn 63 ± 0.5 %, Pb — остальное (~37 %); примеси не более: Sb 0.20 %, Bi 0.10 %, Cu 0.08 %, Ag 0.10 %, Fe 0.02 %, As 0.03 %, Zn 0.003 %, Cd 0.002 %, Ni 0.01 %, Al 0.001 %, Au 0.05 %, In 0.10 % (TDS 63Sn/37Pb CRM); российский аналог ПОС-61 по ГОСТ 21930-76: Sn 59–61 %, Pb — остальное` | 5 |
| `BT (bismaleimide-triazine) — сополимерная сшитая сеть бисмалеимида (тип. 4,4'-бисмалеимидодифенилметан, BMI-M) и цианатного эфира (тип. 2,2-бис(4-цианатофенил)пропан, BE); триазиновые кольца образуются при тримеризации –O–C≡N групп цианата с присоединением бималеимидных двойных связей; товарные композиции MGC модифицируются эпоксидными смолами (BT-epoxy), кварцевым наполнителем (SiO₂) и E-стеклотканью в ламинатах; безгалогенные марки HFBT — без бром/хлор замедлителей горения` | 4 |
| `CuCr1Zr (EN CW106C, UNS C18400): Cu — основа (баланс); Cr 0.8 % (0.5–1.2); Zr 0.06–0.08 % (0.03–0.3) — дисперсионно-твердеющий высокопроводящий медный сплав; примеси по EN ≤0.05 (Sn+Fe+Ni суммарно)` | 4 |
| `(C₂F₄)ₙ — политетрафторэтилен (PTFE, Teflon), полностью фторированный парафиновый полимер (~76 масс.% фтора); virgin-сорт без наполнителей, CAS 9002-84-0` | 3 |
| `SiO2 ≥99.99% (синтетический пьезокварц, гидротермальный автоклавный синтез; природный — α-кварц)` | 2 |
| `Ni ≥99.0% (электролитический никель; для паст BME-электродов — мелкодисперсный Ni-порошок, напр. сферический 0.3–0.8 мкм)` | 2 |
| `TiN — нитрид титана, стехиометрия TiN_x (x = 0.6–1.0; рабочая ~1.0); тонкие плёнки PVD/CVD, объёмный спечённый` | 2 |
| `TiO₂ (диоксид титана, рутил как равновесная фаза); мемристорная форма — бислой TiO₂ (стехиометрический, высокоомный) / TiO₂₋ₓ (дефицит по кислороду, проводящий); вакансии кислорода V_O — мобильные двухзарядные доноры; проводящая предельная фаза — Magnéli TinO₂n−1 (Ti₄O₇ … Ti₁₀O₁₉)` | 1 |
| `SAC305 (Sn-3.0Ag-0.5Cu, IPC J-STD-006 обозначение Sn96.5Ag3.0Cu0.5): Sn 96.5 ± 0.5 %, Ag 3.0 ± 0.2 %, Cu 0.5 ± 0.2 %, Pb ≤ 0.05 % (RoHS-лимит ≤ 0.1 %); примеси нормируются J-STD-006; свинец отсутствует — отличие от legacy Sn63Pb37 (файл material_splav_sn-pb): бессвинцовый припой не та субстанция, а самостоятельный сплав семейства Sn-Ag-Cu` | 1 |
