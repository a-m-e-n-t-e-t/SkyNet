# Граф 1 — подсистема «приводная_система»

```mermaid
graph LR
    izdelie_bldc_enkoder[прочее]
    izdelie_apa[прочее]
    izdelie_belleville_shaiby[прочее]
    izdelie_bldc[прочее]
    izdelie_tsa[прочее]
    izdelie_hasel[прочее]
    izdelie_zubchataya_mufta[прочее]
    izdelie_povorotnoe_uplotnenie[прочее]
    izdelie_tcp[прочее]
    izdelie_pezoelektricheskii_gromkogovoritel[прочее]
    izdelie_elektroflyuidnye_volokna_mit[прочее]
    izdelie_fleksury_8_diskov_po_0_15_mm[прочее]
    izdelie_ipmc[прочее]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena[прочее]
    izdelie_dea[прочее]
    izdelie_3d_pechatnye_dea[прочее]
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov[прочее]
    часть_bldc_enkoder_core_encoder[основной_элемент]
    часть_bldc_enkoder_mounting[крепёж]
    часть_bldc_enkoder_housing[корпус]
    часть_bldc_enkoder_core_rotor[основной_элемент]
    часть_bldc_enkoder_connectors[разъёмы]
    часть_bldc_enkoder_core_stator[основной_элемент]
    часть_bldc_enkoder_core[основной_элемент]
    часть_apa_core[основной_элемент]
    часть_apa_connectors[разъёмы]
    часть_apa_mounting[крепёж]
    часть_apa_housing[корпус]
    часть_apa_core_shell[упругий_элемент]
    часть_apa_core_piezostack[пьезоэлемент]
    часть_belleville_shaiby_connectors[разъёмы]
    часть_belleville_shaiby_mounting[крепёж]
    часть_belleville_shaiby_housing[корпус]
    часть_belleville_shaiby_core[основной_элемент]
    часть_bldc_housing[корпус]
    часть_bldc_connectors[разъёмы]
    часть_bldc_core[основной_элемент]
    часть_bldc_mounting[крепёж]
    часть_tsa_mounting[крепёж]
    часть_tsa_housing[корпус]
    часть_tsa_core[основной_элемент]
    часть_tsa_connectors[разъёмы]
    часть_hasel_housing[корпус]
    часть_hasel_mounting[крепёж]
    часть_hasel_connectors[разъёмы]
    часть_hasel_core[основной_элемент]
    часть_zubchataya_mufta_core[основной_элемент]
    часть_zubchataya_mufta_mounting[крепёж]
    часть_zubchataya_mufta_housing[корпус]
    часть_zubchataya_mufta_connectors[разъёмы]
    часть_povorotnoe_uplotnenie_connectors[разъёмы]
    часть_povorotnoe_uplotnenie_housing[корпус]
    часть_povorotnoe_uplotnenie_mounting[крепёж]
    часть_povorotnoe_uplotnenie_core[уплотнение]
    часть_tcp_connectors[разъёмы]
    часть_tcp_mounting[крепёж]
    часть_tcp_housing[корпус]
    часть_tcp_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_connectors[разъёмы]
    часть_pezoelektricheskii_gromkogovoritel_mounting[крепёж]
    часть_pezoelektricheskii_gromkogovoritel_housing[корпус]
    часть_elektroflyuidnye_volokna_mit_core[основной_элемент]
    часть_elektroflyuidnye_volokna_mit_connectors[разъёмы]
    часть_elektroflyuidnye_volokna_mit_housing[корпус]
    часть_elektroflyuidnye_volokna_mit_mounting[крепёж]
    часть_fleksury_8_diskov_po_0_15_mm_mounting[крепёж]
    часть_fleksury_8_diskov_po_0_15_mm_housing[корпус]
    часть_fleksury_8_diskov_po_0_15_mm_connectors[разъёмы]
    часть_fleksury_8_diskov_po_0_15_mm_core[основной_элемент]
    часть_ipmc_connectors[разъёмы]
    часть_ipmc_housing[корпус]
    часть_ipmc_core[основной_элемент]
    часть_ipmc_mounting[крепёж]
    часть_ipmc_core_electrodes[электроды]
    часть_ipmc_core_membrane[PEM_мембрана]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core[основной_элемент]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors[разъёмы]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing[корпус]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting[крепёж]
    часть_dea_housing[корпус]
    часть_dea_core[основной_элемент]
    часть_dea_connectors[разъёмы]
    часть_dea_mounting[крепёж]
    часть_3d_pechatnye_dea_connectors[разъёмы]
    часть_3d_pechatnye_dea_mounting[крепёж]
    часть_3d_pechatnye_dea_core[основной_элемент]
    часть_3d_pechatnye_dea_housing[корпус]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing[корпус]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran[экранирование]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors[разъёмы]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting[крепёж]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda[сигнальные_цепи]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda[силовые_цепи]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core[основной_элемент]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_zashchitnaya_obmotka[изоляция]
    часть_cameron_рука_левая[servo_arm_small]
    часть_cameron_нога_левая[servo_leg_small]
    часть_t_x_нога_левая[servo_leg]
    часть_t_x_рука_левая[servo_arm]
    часть_t600_нога_левая[servo_leg]
    часть_t600_рука_левая[servo_arm]
    часть_hk_tank_гусеница_левая[tank_track]
    часть_t800_нога_левая[servo_leg]
    часть_t800_рука_левая[servo_arm]
    часть_marcus_нога_левая[servo_leg]
    часть_marcus_рука_левая[servo_arm]
    часть_t850_рука_левая[servo_arm_improved]
    часть_t850_нога_левая[servo_leg_improved]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_copper[Cu ≥99.9% (электролити…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    izdelie_bldc_enkoder -->|материал| material_al_6061_t6
    izdelie_bldc_enkoder -->|материал| material_aluminum
    izdelie_apa -->|материал| material_aluminum
    izdelie_belleville_shaiby -->|материал| material_stal_st3
    izdelie_belleville_shaiby -->|материал| material_aluminum
    izdelie_bldc -->|материал| material_al_6061_t6
    izdelie_bldc -->|материал| material_aluminum
    izdelie_tsa -->|материал| material_aluminum
    izdelie_hasel -->|материал| material_al_6061_t6
    izdelie_zubchataya_mufta -->|материал| material_stal_st3
    izdelie_zubchataya_mufta -->|материал| material_al_6061_t6
    izdelie_povorotnoe_uplotnenie -->|материал| material_aluminum
    izdelie_tcp -->|материал| material_aluminum
    izdelie_pezoelektricheskii_gromkogovoritel -->|материал| material_aluminum
    izdelie_elektroflyuidnye_volokna_mit -->|материал| material_aluminum
    izdelie_fleksury_8_diskov_po_0_15_mm -->|материал| material_aluminum
    izdelie_ipmc -->|материал| material_aluminum
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena -->|материал| material_aluminum
    izdelie_dea -->|материал| material_aluminum
    izdelie_3d_pechatnye_dea -->|материал| material_aluminum
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov -->|материал| material_copper
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov -->|материал| material_aluminum
    часть_bldc_enkoder_mounting -->|материал| material_stal_st3
    часть_bldc_enkoder_housing -->|материал| material_al_6061_t6
    часть_bldc_enkoder_connectors -->|материал| material_al_6061_t6
    часть_bldc_enkoder_core_stator -->|материал| material_copper
    часть_bldc_enkoder_core -->|материал| material_al_6061_t6
    часть_apa_core -->|материал| material_ti_6al_4v
    часть_apa_connectors -->|материал| material_al_6061_t6
    часть_apa_mounting -->|материал| material_al_6061_t6
    часть_apa_housing -->|материал| material_al_6061_t6
    часть_apa_core_shell -->|материал| material_ti_6al_4v
    часть_belleville_shaiby_housing -->|материал| material_al_6061_t6
    часть_belleville_shaiby_core -->|материал| material_stal_st3
    часть_bldc_housing -->|материал| material_al_6061_t6
    часть_bldc_connectors -->|материал| material_al_6061_t6
    часть_bldc_core -->|материал| material_al_6061_t6
    часть_bldc_mounting -->|материал| material_al_6061_t6
    часть_tsa_mounting -->|материал| material_al_6061_t6
    часть_tsa_housing -->|материал| material_al_6061_t6
    часть_tsa_connectors -->|материал| material_al_6061_t6
    часть_hasel_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_core -->|материал| material_stal_st3
    часть_zubchataya_mufta_mounting -->|материал| material_stal_st3
    часть_zubchataya_mufta_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_connectors -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_connectors -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_mounting -->|материал| material_stal_st3
    часть_tcp_mounting -->|материал| material_al_6061_t6
    часть_tcp_housing -->|материал| material_al_6061_t6
    часть_pezoelektricheskii_gromkogovoritel_housing -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_housing -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_housing -->|материал| material_al_6061_t6
    часть_ipmc_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting -->|материал| material_al_6061_t6
    часть_dea_housing -->|материал| material_al_6061_t6
    часть_dea_mounting -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_ekran -->|материал| material_copper
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_signalnye_provoda -->|материал| material_copper
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core_silovye_provoda -->|материал| material_copper
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core -->|материал| material_copper
    часть_cameron_рука_левая -->|материал| material_ti_6al_4v
    часть_cameron_нога_левая -->|материал| material_ti_6al_4v
    часть_t_x_нога_левая -->|материал| material_ti_6al_4v
    часть_t_x_рука_левая -->|материал| material_ti_6al_4v
    часть_t600_нога_левая -->|материал| material_ti_6al_4v
    часть_t600_рука_левая -->|материал| material_ti_6al_4v
    часть_t800_нога_левая -->|материал| material_ti_6al_4v
    часть_t800_рука_левая -->|материал| material_ti_6al_4v
    часть_marcus_нога_левая -->|материал| material_ti_6al_4v
    часть_marcus_рука_левая -->|материал| material_ti_6al_4v
    часть_t850_рука_левая -->|материал| material_ti_6al_4v
    часть_t850_нога_левая -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 36 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 15 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 14 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 7 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 7 |
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 6 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 5 |
| `Полиамид 6/6 (PA66, нейлон 6/6): продукт поликонденсации гексаметилендиамина (6 C) и адипиновой кислоты (6 C), повторяющееся звено –[NH–(CH₂)₆–NH–OC–(CH₂)₄–CO]ₙ–; промышленные марки: Zytel 101 (DuPont), Ultramid A3K (BASF), Durethan A (Lanxess)` | 5 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 4 |
| `BaTiO3 ≥98.5% (титанат бария, перовскит ABO3); для X5R/X7R-диэлектриков MLCC легируется Dy2O3, Ho2O3, Y2O3, Mg, Si, Mn (core-shell BME с Ni-электродами)` | 3 |
| `перфторсульфоновая кислота (PFSA): PTFE-подобная основа с боковыми цепями –O–CF₂–CF(CF₃)–O–CF₂–CF₂–SO₃H, EW ≈1100 г/моль (Nafion 117, Chemours)` | 3 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 3 |
| `ультравысокомолекулярный полиэтилен (UHMWPE), -(CH2-CH2)n-, молекулярная масса >1.5 млн г/моль; гель-прядёное волокно Honeywell (марки S-900, S-1000, HT)` | 2 |
| `Терполимер P(VDF-TrFE-CFE): звенья винилиденфторида CH2=CF2 (VDF), трифторэтилена CHF=CF2 (TrFE) и хлорфтормонофторэтилена (CFE); типовой состав 64.8/27.4/7.8 мол.% (J. Materiomics 2023); промышленная марка Piezotech RT-FS (Arkema)` | 2 |
| `PEEK — полиэфирэфиркетон (PAEK): повторяющееся звено (C19H12O3)n, M = 288.3 г/моль; синтез из 4,4′-дифторбензофенона и динатриевой соли гидрохинона в дифенилсульфоне при ~300 °C` | 2 |
