# Граф 1 — подсистема «вычислительная»

```mermaid
graph LR
    izdelie_nvidia_jetson_orin_nano[edge_AI_модуль]
    izdelie_gr801_noel_v_risc_v[RISC-V_процессор]
    izdelie_litii_tionilhloridnye_batarei[литий-тионилхлоридная_батарея]
    izdelie_memristornye_matritsy[memristor_массив]
    izdelie_sic_mosfet[силовой_транзистор]
    izdelie_intel_loihi_2[нейроморфный_процессор]
    izdelie_halve[нейроморфный_процессор]
    izdelie_pcm[phase_change_память]
    izdelie_sot_mram[память_MRAM]
    izdelie_ibm_northpole[AI_инференс_чип]
    izdelie_brainchip_akida_2[нейроморфный_процессор]
    izdelie_kondensatory_keramicheskie[керамический_конденсатор]
    часть_nvidia_jetson_orin_nano_connectors[разъёмы]
    часть_nvidia_jetson_orin_nano_memory[LPDDR_память]
    часть_nvidia_jetson_orin_nano_storage[eMMC_флеш]
    часть_nvidia_jetson_orin_nano_pmic[PMIC_питание]
    часть_nvidia_jetson_orin_nano_enclosure[корпус]
    часть_nvidia_jetson_orin_nano_wifi_bt[WiFi_BT_модуль]
    часть_nvidia_jetson_orin_nano_heat_sink[радиатор]
    часть_nvidia_jetson_orin_nano_pcb[плата]
    часть_gr801_noel_v_risc_v_pcb[плата]
    часть_gr801_noel_v_risc_v_thermal_pad[термопрокладка]
    часть_gr801_noel_v_risc_v_die[risc_v_кристалл]
    часть_gr801_noel_v_risc_v_sram[SRAM_кэш]
    часть_gr801_noel_v_risc_v_substrate[подложка]
    часть_gr801_noel_v_risc_v_pins[пины]
    часть_gr801_noel_v_risc_v_crystal_osc[кварцевый_резонатор]
    часть_gr801_noel_v_risc_v_package[корпус_FCTEBGA]
    часть_gr801_noel_v_risc_v_capacitors[конденсаторы]
    часть_gr801_noel_v_risc_v_flash[флеш_память]
    часть_litii_tionilhloridnye_batarei_anode[литий_анод]
    часть_litii_tionilhloridnye_batarei_electrolyte[thionyl_chloride]
    часть_litii_tionilhloridnye_batarei_case[корпус_нерж]
    часть_litii_tionilhloridnye_batarei_separator[сепаратор]
    часть_litii_tionilhloridnye_batarei_cathode[угольный_катод]
    часть_litii_tionilhloridnye_batarei_terminal[вывод]
    часть_memristornye_matritsy_bit_sense[sense_amplifiers]
    часть_memristornye_matritsy_word_drivers[драйверы_строк]
    часть_memristornye_matritsy_adc[АЦП]
    часть_memristornye_matritsy_controller[контроллер]
    часть_memristornye_matritsy_crossbar[кроссбар_матрица]
    часть_sic_mosfet_die[sic_кристалл]
    часть_sic_mosfet_encapsulant[эпоксидный_корпус]
    часть_sic_mosfet_lead_frame[силовые_выводы]
    часть_sic_mosfet_solder[пайка_кристалла]
    часть_sic_mosfet_wire_bonds[проволочные_соединения]
    часть_sic_mosfet_gate_terminal[затвор]
    часть_intel_loihi_2_pcb[плата_носитель]
    часть_intel_loihi_2_die[кремниевый_кристалл]
    часть_intel_loihi_2_thermal_spreader[теплораспределитель]
    часть_intel_loihi_2_capacitors[блокировка_питания]
    часть_intel_loihi_2_encapsulant[инкапсулянт]
    часть_intel_loihi_2_substrate[подложка_FR5_BT]
    часть_intel_loihi_2_pins_balls[пины_BGA]
    часть_halve_die[кремниевый_кристалл]
    часть_halve_thermal_spreader[теплораспределитель]
    часть_halve_substrate[подложка_FR5_BT]
    часть_halve_capacitors[блокировка_питания]
    часть_halve_encapsulant[инкапсулянт]
    часть_halve_pcb[плата_носитель]
    часть_halve_pins_balls[пины_BGA]
    часть_pcm_selector[селектор_устройство]
    часть_pcm_controller[контроллер]
    часть_pcm_io_interface[I/O]
    часть_pcm_periphery[периферия]
    часть_pcm_cell_array[массив_PCM_ячеек]
    часть_sot_mram_periphery[периферия]
    часть_sot_mram_cell_array[массив_ячеек]
    часть_sot_mram_io_interface[I/O_интерфейс]
    часть_sot_mram_sense_amplifiers[sense_amplifiers]
    часть_sot_mram_row_decoders[дешифраторы_строк]
    часть_ibm_northpole_capacitors[MLCC_блок]
    часть_ibm_northpole_substrate[органическая_подложка]
    часть_ibm_northpole_hbm[память_HBM]
    часть_ibm_northpole_die[инференс_кристалл]
    часть_ibm_northpole_package[корпус_FCBGA]
    часть_ibm_northpole_thermal_spreader[теплораспределитель]
    часть_brainchip_akida_2_encapsulant[инкапсулянт]
    часть_brainchip_akida_2_die[кремниевый_кристалл]
    часть_brainchip_akida_2_pcb[плата_носитель]
    часть_brainchip_akida_2_capacitors[блокировка_питания]
    часть_brainchip_akida_2_thermal_spreader[теплораспределитель]
    часть_brainchip_akida_2_substrate[подложка_FR5_BT]
    часть_brainchip_akida_2_pins_balls[пины_BGA]
    часть_kondensatory_keramicheskie_outer_electrodes[внешние_электроды]
    часть_kondensatory_keramicheskie_plating[гальваническое_покрытие]
    часть_kondensatory_keramicheskie_termination[терминалы]
    часть_kondensatory_keramicheskie_inner_electrodes[внутренние_электроды]
    часть_kondensatory_keramicheskie_ceramic_layers[керамические_слои]
    izdelie_SkyNet_T1000[прочее]
    izdelie_SkyNet_T1001[прочее]
    часть_t1000_миметический_полисплав[mimetic_polyalloy]
    часть_t1001_миметический_полисплав[mimetic_polyalloy_t1001]
    часть_t_x_cpu[neural_net_cpu_tx]
    часть_rev9_полисплав_оболочка[mimetic_polyalloy_sheath]
    часть_cameron_cpu[neural_net_cpu_cameron]
    часть_marcus_человеческий_мозг[human_brain_hybrid]
    часть_t850_cpu[neural_net_cpu_v2]
    часть_t800_cpu[neural_net_cpu]
    часть_t600_cpu[early_neural_cpu]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_copper[Cu ≥99.9% (электролити…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_si[Si (кремний); электрон…]
    izdelie_intel_loihi_2 -->|материал| material_copper
    izdelie_halve -->|материал| material_copper
    izdelie_ibm_northpole -->|материал| material_copper
    izdelie_brainchip_akida_2 -->|материал| material_copper
    izdelie_kondensatory_keramicheskie -->|материал| material_copper
    часть_nvidia_jetson_orin_nano_enclosure -->|материал| material_al_6061_t6
    часть_gr801_noel_v_risc_v_die -->|материал| material_si
    часть_gr801_noel_v_risc_v_sram -->|материал| material_si
    часть_gr801_noel_v_risc_v_flash -->|материал| material_si
    часть_litii_tionilhloridnye_batarei_terminal -->|материал| material_stal_st3
    часть_memristornye_matritsy_bit_sense -->|материал| material_si
    часть_memristornye_matritsy_word_drivers -->|материал| material_si
    часть_memristornye_matritsy_adc -->|материал| material_si
    часть_memristornye_matritsy_controller -->|материал| material_si
    часть_sic_mosfet_lead_frame -->|материал| material_copper
    часть_intel_loihi_2_die -->|материал| material_si
    часть_intel_loihi_2_thermal_spreader -->|материал| material_copper
    часть_halve_die -->|материал| material_si
    часть_halve_thermal_spreader -->|материал| material_copper
    часть_pcm_controller -->|материал| material_si
    часть_pcm_io_interface -->|материал| material_si
    часть_pcm_periphery -->|материал| material_si
    часть_sot_mram_periphery -->|материал| material_si
    часть_sot_mram_io_interface -->|материал| material_si
    часть_sot_mram_sense_amplifiers -->|материал| material_si
    часть_sot_mram_row_decoders -->|материал| material_si
    часть_ibm_northpole_hbm -->|материал| material_si
    часть_ibm_northpole_die -->|материал| material_si
    часть_ibm_northpole_thermal_spreader -->|материал| material_copper
    часть_brainchip_akida_2_die -->|материал| material_si
    часть_brainchip_akida_2_thermal_spreader -->|материал| material_copper
    часть_kondensatory_keramicheskie_outer_electrodes -->|материал| material_copper
    часть_kondensatory_keramicheskie_termination -->|материал| material_copper
    часть_t_x_cpu -->|материал| material_al_6061_t6
    часть_marcus_человеческий_мозг -->|материал| material_ti_6al_4v
    часть_t850_cpu -->|материал| material_al_6061_t6
    часть_t800_cpu -->|материал| material_si
    часть_t600_cpu -->|материал| material_si
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Si (кремний); электронный сорт ≥99.9999999% (9N) для подложек ИС, солнечный ≥99.9999% (6N), металлургический ~98–99% (Si-Fe, Si-Ca примеси)` | 21 |
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 12 |
| `Стеклотекстолит FR-4: ткань E-glass (~55 мас.%) + эпоксидная смола multifunctional (bis-/tetrafunctional, система Isola); медная фольга с двух сторон в ламинате` | 9 |
| `Эпоксид Epon 828 + TETA` | 8 |
| `BaTiO3 ≥98.5% (титанат бария, перовскит ABO3); для X5R/X7R-диэлектриков MLCC легируется Dy2O3, Ho2O3, Y2O3, Mg, Si, Mn (core-shell BME с Ni-электродами)` | 6 |
| `Sn 63 ± 0.5 %, Pb — остальное (~37 %); примеси не более: Sb 0.20 %, Bi 0.10 %, Cu 0.08 %, Ag 0.10 %, Fe 0.02 %, As 0.03 %, Zn 0.003 %, Cd 0.002 %, Ni 0.01 %, Al 0.001 %, Au 0.05 %, In 0.10 % (TDS 63Sn/37Pb CRM); российский аналог ПОС-61 по ГОСТ 21930-76: Sn 59–61 %, Pb — остальное` | 5 |
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 3 |
| `(C₂F₄)ₙ — политетрафторэтилен (PTFE, Teflon), полностью фторированный парафиновый полимер (~76 масс.% фтора); virgin-сорт без наполнителей, CAS 9002-84-0` | 3 |
| `SiO2 ≥99.99% (синтетический пьезокварц, гидротермальный автоклавный синтез; природный — α-кварц)` | 2 |
| `Ni ≥99.0% (электролитический никель; для паст BME-электродов — мелкодисперсный Ni-порошок, напр. сферический 0.3–0.8 мкм)` | 2 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 2 |
| `Al ≥99.99% (heavy bonding wire, класс Al-H11/Al-CR)` | 2 |
| `TiN — нитрид титана, стехиометрия TiN_x (x = 0.6–1.0; рабочая ~1.0); тонкие плёнки PVD/CVD, объёмный спечённый` | 1 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
| `Al 97.5–99.35% + Mg 0.45–0.9% + Si 0.2–0.6% (Fe ≤0.35%, Cr/Cu/Mn/Ti/Zn ≤0.1%)` | 1 |
