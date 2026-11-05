# Граф 1 — подсистема «вычислительная»

```mermaid
graph LR
    izdelie_halve[нейроморфный_процессор]
    izdelie_litii_tionilhloridnye_batarei[литий-тионилхлоридная_батарея]
    izdelie_memristornye_matritsy[memristor_массив]
    izdelie_sot_mram[память_MRAM]
    izdelie_sic_mosfet[силовой_транзистор]
    izdelie_brainchip_akida_2[нейроморфный_процессор]
    izdelie_intel_loihi_2[нейроморфный_процессор]
    izdelie_pcm[phase_change_память]
    izdelie_kondensatory_keramicheskie[керамический_конденсатор]
    izdelie_gr801_noel_v_risc_v[RISC-V_процессор]
    izdelie_ibm_northpole[AI_инференс_чип]
    izdelie_nvidia_jetson_orin_nano[edge_AI_модуль]
    часть_halve_capacitors[блокировка_питания]
    часть_halve_encapsulant[инкапсулянт]
    часть_halve_substrate[подложка_FR5_BT]
    часть_halve_thermal_spreader[теплораспределитель]
    часть_halve_pcb[плата_носитель]
    часть_halve_die[кремниевый_кристалл]
    часть_halve_pins_balls[пины_BGA]
    часть_litii_tionilhloridnye_batarei_cathode[угольный_катод]
    часть_litii_tionilhloridnye_batarei_case[корпус_нерж]
    часть_litii_tionilhloridnye_batarei_terminal[вывод]
    часть_litii_tionilhloridnye_batarei_electrolyte[thionyl_chloride]
    часть_litii_tionilhloridnye_batarei_separator[сепаратор]
    часть_litii_tionilhloridnye_batarei_anode[литий_анод]
    часть_memristornye_matritsy_crossbar[кроссбар_матрица]
    часть_memristornye_matritsy_word_drivers[драйверы_строк]
    часть_memristornye_matritsy_adc[АЦП]
    часть_memristornye_matritsy_controller[контроллер]
    часть_memristornye_matritsy_bit_sense[sense_amplifiers]
    часть_sot_mram_periphery[периферия]
    часть_sot_mram_sense_amplifiers[sense_amplifiers]
    часть_sot_mram_row_decoders[дешифраторы_строк]
    часть_sot_mram_cell_array[массив_ячеек]
    часть_sot_mram_io_interface[I/O_интерфейс]
    часть_sic_mosfet_encapsulant[эпоксидный_корпус]
    часть_sic_mosfet_die[sic_кристалл]
    часть_sic_mosfet_wire_bonds[проволочные_соединения]
    часть_sic_mosfet_lead_frame[силовые_выводы]
    часть_sic_mosfet_gate_terminal[затвор]
    часть_sic_mosfet_solder[пайка_кристалла]
    часть_brainchip_akida_2_pcb[плата_носитель]
    часть_brainchip_akida_2_thermal_spreader[теплораспределитель]
    часть_brainchip_akida_2_capacitors[блокировка_питания]
    часть_brainchip_akida_2_substrate[подложка_FR5_BT]
    часть_brainchip_akida_2_pins_balls[пины_BGA]
    часть_brainchip_akida_2_encapsulant[инкапсулянт]
    часть_brainchip_akida_2_die[кремниевый_кристалл]
    часть_intel_loihi_2_pcb[плата_носитель]
    часть_intel_loihi_2_pins_balls[пины_BGA]
    часть_intel_loihi_2_substrate[подложка_FR5_BT]
    часть_intel_loihi_2_thermal_spreader[теплораспределитель]
    часть_intel_loihi_2_die[кремниевый_кристалл]
    часть_intel_loihi_2_encapsulant[инкапсулянт]
    часть_intel_loihi_2_capacitors[блокировка_питания]
    часть_pcm_controller[контроллер]
    часть_pcm_cell_array[массив_PCM_ячеек]
    часть_pcm_selector[селектор_устройство]
    часть_pcm_periphery[периферия]
    часть_pcm_io_interface[I/O]
    часть_kondensatory_keramicheskie_inner_electrodes[внутренние_электроды]
    часть_kondensatory_keramicheskie_plating[гальваническое_покрытие]
    часть_kondensatory_keramicheskie_termination[терминалы]
    часть_kondensatory_keramicheskie_ceramic_layers[керамические_слои]
    часть_kondensatory_keramicheskie_outer_electrodes[внешние_электроды]
    часть_gr801_noel_v_risc_v_die[risc_v_кристалл]
    часть_gr801_noel_v_risc_v_crystal_osc[кварцевый_резонатор]
    часть_gr801_noel_v_risc_v_flash[флеш_память]
    часть_gr801_noel_v_risc_v_substrate[подложка]
    часть_gr801_noel_v_risc_v_pcb[плата]
    часть_gr801_noel_v_risc_v_pins[пины]
    часть_gr801_noel_v_risc_v_sram[SRAM_кэш]
    часть_gr801_noel_v_risc_v_capacitors[конденсаторы]
    часть_gr801_noel_v_risc_v_thermal_pad[термопрокладка]
    часть_gr801_noel_v_risc_v_package[корпус_FCTEBGA]
    часть_ibm_northpole_package[корпус_FCBGA]
    часть_ibm_northpole_substrate[органическая_подложка]
    часть_ibm_northpole_die[инференс_кристалл]
    часть_ibm_northpole_hbm[память_HBM]
    часть_ibm_northpole_capacitors[MLCC_блок]
    часть_ibm_northpole_thermal_spreader[теплораспределитель]
    часть_nvidia_jetson_orin_nano_pcb[плата]
    часть_nvidia_jetson_orin_nano_enclosure[корпус]
    часть_nvidia_jetson_orin_nano_connectors[разъёмы]
    часть_nvidia_jetson_orin_nano_wifi_bt[WiFi_BT_модуль]
    часть_nvidia_jetson_orin_nano_pmic[PMIC_питание]
    часть_nvidia_jetson_orin_nano_storage[eMMC_флеш]
    часть_nvidia_jetson_orin_nano_heat_sink[радиатор]
    часть_nvidia_jetson_orin_nano_memory[LPDDR_память]
    часть_cameron_cpu[neural_net_cpu_cameron]
    часть_t850_cpu[neural_net_cpu_v2]
    часть_rev9_полисплав_оболочка[mimetic_polyalloy_sheath]
    часть_t800_cpu[neural_net_cpu]
    часть_marcus_человеческий_мозг[human_brain_hybrid]
    часть_t_x_cpu[neural_net_cpu_tx]
    часть_t600_cpu[early_neural_cpu]
    izdelie_SkyNet_T1000[прочее]
    izdelie_SkyNet_T1001[прочее]
    часть_t1000_миметический_полисплав[mimetic_polyalloy]
    часть_t1001_миметический_полисплав[mimetic_polyalloy_t1001]
    material_al_6061_t6[Al 6061-T6]
    material_ti_6al_4v[Ti-6Al-4V]
    material_stal_st3[Сталь Ст3]
    material_si[Si]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    часть_halve_die -->|материал| material_si
    часть_litii_tionilhloridnye_batarei_terminal -->|материал| material_stal_st3
    часть_memristornye_matritsy_word_drivers -->|материал| material_si
    часть_memristornye_matritsy_adc -->|материал| material_si
    часть_memristornye_matritsy_controller -->|материал| material_si
    часть_memristornye_matritsy_bit_sense -->|материал| material_si
    часть_sot_mram_periphery -->|материал| material_si
    часть_sot_mram_sense_amplifiers -->|материал| material_si
    часть_sot_mram_row_decoders -->|материал| material_si
    часть_sot_mram_io_interface -->|материал| material_si
    часть_brainchip_akida_2_die -->|материал| material_si
    часть_intel_loihi_2_die -->|материал| material_si
    часть_pcm_controller -->|материал| material_si
    часть_pcm_periphery -->|материал| material_si
    часть_pcm_io_interface -->|материал| material_si
    часть_kondensatory_keramicheskie_inner_electrodes -->|материал| material_ti_6al_4v
    часть_gr801_noel_v_risc_v_die -->|материал| material_si
    часть_gr801_noel_v_risc_v_flash -->|материал| material_si
    часть_gr801_noel_v_risc_v_sram -->|материал| material_si
    часть_ibm_northpole_package -->|материал| material_ti_6al_4v
    часть_ibm_northpole_substrate -->|материал| material_ti_6al_4v
    часть_ibm_northpole_die -->|материал| material_si
    часть_ibm_northpole_hbm -->|материал| material_si
    часть_nvidia_jetson_orin_nano_enclosure -->|материал| material_al_6061_t6
    часть_nvidia_jetson_orin_nano_connectors -->|материал| material_latun_c36000
    часть_t850_cpu -->|материал| material_al_6061_t6
    часть_t800_cpu -->|материал| material_si
    часть_marcus_человеческий_мозг -->|материал| material_ti_6al_4v
    часть_t_x_cpu -->|материал| material_al_6061_t6
    часть_t600_cpu -->|материал| material_si
    часть_t1001_миметический_полисплав -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Si` | 21 |
| `Эпоксид Epon 828 + TETA` | 8 |
| `Сплав Sn-Pb` | 5 |
| `Ti-6Al-4V` | 5 |
| `PTFE` | 3 |
| `Al 6061-T6` | 3 |
| `Полиимид` | 2 |
| `Галлинстан` | 2 |
| `TiN` | 1 |
| `углеродная сажа (токопроводящий наполнитель) + PTFE 20% (связующее), опционально катализатор MnO₂; токосъёмник — никелевая сетка` | 1 |
| `SS AISI 304` | 1 |
| `Сталь Ст3` | 1 |
| `HfO₂` | 1 |
| `Epotek 301-2` | 1 |
| `монокристаллического SiC` | 1 |
