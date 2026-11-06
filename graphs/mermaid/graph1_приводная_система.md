# Граф 1 — подсистема «приводная_система»

```mermaid
graph LR
    izdelie_tsa[прочее]
    izdelie_elektroflyuidnye_volokna_mit[прочее]
    izdelie_apa[прочее]
    izdelie_bldc[прочее]
    izdelie_povorotnoe_uplotnenie[прочее]
    izdelie_fleksury_8_diskov_po_0_15_mm[прочее]
    izdelie_3d_pechatnye_dea[прочее]
    izdelie_belleville_shaiby[прочее]
    izdelie_dea[прочее]
    izdelie_bldc_+_enkoder[прочее]
    izdelie_pezoelektricheskii_gromkogovoritel[прочее]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena[прочее]
    izdelie_tcp[прочее]
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov[прочее]
    izdelie_zubchataya_mufta[прочее]
    izdelie_ipmc[прочее]
    izdelie_hasel[прочее]
    часть_tsa_core[основной_элемент]
    часть_tsa_housing[корпус]
    часть_tsa_mounting[крепёж]
    часть_tsa_connectors[разъёмы]
    часть_elektroflyuidnye_volokna_mit_connectors[разъёмы]
    часть_elektroflyuidnye_volokna_mit_core[основной_элемент]
    часть_elektroflyuidnye_volokna_mit_housing[корпус]
    часть_elektroflyuidnye_volokna_mit_mounting[крепёж]
    часть_apa_connectors[разъёмы]
    часть_apa_mounting[крепёж]
    часть_apa_housing[корпус]
    часть_apa_core[основной_элемент]
    часть_bldc_core[основной_элемент]
    часть_bldc_mounting[крепёж]
    часть_bldc_connectors[разъёмы]
    часть_bldc_housing[корпус]
    часть_povorotnoe_uplotnenie_mounting[крепёж]
    часть_povorotnoe_uplotnenie_housing[корпус]
    часть_povorotnoe_uplotnenie_core[основной_элемент]
    часть_povorotnoe_uplotnenie_connectors[разъёмы]
    часть_fleksury_8_diskov_po_0_15_mm_core[основной_элемент]
    часть_fleksury_8_diskov_po_0_15_mm_mounting[крепёж]
    часть_fleksury_8_diskov_po_0_15_mm_housing[корпус]
    часть_fleksury_8_diskov_po_0_15_mm_connectors[разъёмы]
    часть_3d_pechatnye_dea_housing[корпус]
    часть_3d_pechatnye_dea_mounting[крепёж]
    часть_3d_pechatnye_dea_connectors[разъёмы]
    часть_3d_pechatnye_dea_core[основной_элемент]
    часть_belleville_shaiby_core[основной_элемент]
    часть_belleville_shaiby_housing[корпус]
    часть_belleville_shaiby_mounting[крепёж]
    часть_belleville_shaiby_connectors[разъёмы]
    часть_dea_mounting[крепёж]
    часть_dea_housing[корпус]
    часть_dea_connectors[разъёмы]
    часть_dea_core[основной_элемент]
    часть_bldc_+_enkoder_mounting[крепёж]
    часть_bldc_+_enkoder_housing[корпус]
    часть_bldc_+_enkoder_core[основной_элемент]
    часть_bldc_+_enkoder_connectors[разъёмы]
    часть_pezoelektricheskii_gromkogovoritel_housing[корпус]
    часть_pezoelektricheskii_gromkogovoritel_connectors[разъёмы]
    часть_pezoelektricheskii_gromkogovoritel_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_mounting[крепёж]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing[корпус]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors[разъёмы]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core[основной_элемент]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting[крепёж]
    часть_tcp_housing[корпус]
    часть_tcp_core[основной_элемент]
    часть_tcp_connectors[разъёмы]
    часть_tcp_mounting[крепёж]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting[крепёж]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors[разъёмы]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core[основной_элемент]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing[корпус]
    часть_zubchataya_mufta_mounting[крепёж]
    часть_zubchataya_mufta_housing[корпус]
    часть_zubchataya_mufta_connectors[разъёмы]
    часть_zubchataya_mufta_core[основной_элемент]
    часть_ipmc_connectors[разъёмы]
    часть_ipmc_mounting[крепёж]
    часть_ipmc_core[основной_элемент]
    часть_ipmc_housing[корпус]
    часть_hasel_core[основной_элемент]
    часть_hasel_housing[корпус]
    часть_hasel_mounting[крепёж]
    часть_hasel_connectors[разъёмы]
    часть_t_x_рука_левая[servo_arm]
    часть_t_x_нога_левая[servo_leg]
    часть_marcus_рука_левая[servo_arm]
    часть_marcus_нога_левая[servo_leg]
    часть_t600_нога_левая[servo_leg]
    часть_t600_рука_левая[servo_arm]
    часть_hk_tank_гусеница_левая[tank_track]
    часть_t850_рука_левая[servo_arm_improved]
    часть_t850_нога_левая[servo_leg_improved]
    часть_cameron_рука_левая[servo_arm_small]
    часть_cameron_нога_левая[servo_leg_small]
    часть_t800_нога_левая[servo_leg]
    часть_t800_рука_левая[servo_arm]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_ti_6al_4v[Ti-6Al-4V]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_ss_aisi_304[SS AISI 304]
    часть_tsa_housing -->|материал| material_al_6061_t6
    часть_tsa_mounting -->|материал| material_al_6061_t6
    часть_tsa_connectors -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_housing -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_mounting -->|материал| material_ss_aisi_304
    часть_apa_connectors -->|материал| material_al_6061_t6
    часть_apa_mounting -->|материал| material_al_6061_t6
    часть_apa_housing -->|материал| material_al_6061_t6
    часть_apa_core -->|материал| material_ti_6al_4v
    часть_bldc_core -->|материал| material_al_6061_t6
    часть_bldc_mounting -->|материал| material_al_6061_t6
    часть_bldc_connectors -->|материал| material_al_6061_t6
    часть_bldc_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_mounting -->|материал| material_stal_st3
    часть_povorotnoe_uplotnenie_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_connectors -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_mounting -->|материал| material_ss_aisi_304
    часть_fleksury_8_diskov_po_0_15_mm_housing -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_connectors -->|материал| material_latun_c36000
    часть_belleville_shaiby_core -->|материал| material_stal_st3
    часть_belleville_shaiby_housing -->|материал| material_al_6061_t6
    часть_dea_mounting -->|материал| material_al_6061_t6
    часть_dea_housing -->|материал| material_al_6061_t6
    часть_dea_connectors -->|материал| material_latun_c36000
    часть_bldc_+_enkoder_mounting -->|материал| material_stal_st3
    часть_bldc_+_enkoder_housing -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_core -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_connectors -->|материал| material_al_6061_t6
    часть_pezoelektricheskii_gromkogovoritel_housing -->|материал| material_al_6061_t6
    часть_pezoelektricheskii_gromkogovoritel_connectors -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_core -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_mounting -->|материал| material_latun_c36000
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting -->|материал| material_al_6061_t6
    часть_tcp_housing -->|материал| material_al_6061_t6
    часть_tcp_mounting -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting -->|материал| material_ss_aisi_304
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_mounting -->|материал| material_stal_st3
    часть_zubchataya_mufta_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_connectors -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_core -->|материал| material_stal_st3
    часть_ipmc_mounting -->|материал| material_latun_c36000
    часть_ipmc_housing -->|материал| material_al_6061_t6
    часть_hasel_housing -->|материал| material_al_6061_t6
    часть_t_x_рука_левая -->|материал| material_ti_6al_4v
    часть_t_x_нога_левая -->|материал| material_ti_6al_4v
    часть_marcus_рука_левая -->|материал| material_ti_6al_4v
    часть_marcus_нога_левая -->|материал| material_ti_6al_4v
    часть_t600_нога_левая -->|материал| material_ti_6al_4v
    часть_t600_рука_левая -->|материал| material_ti_6al_4v
    часть_t850_рука_левая -->|материал| material_ti_6al_4v
    часть_t850_нога_левая -->|материал| material_ti_6al_4v
    часть_cameron_рука_левая -->|материал| material_ti_6al_4v
    часть_cameron_нога_левая -->|материал| material_ti_6al_4v
    часть_t800_нога_левая -->|материал| material_ti_6al_4v
    часть_t800_рука_левая -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 32 |
| `Ti-6Al-4V` | 13 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 6 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 5 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 4 |
| `Полиамид 6/6 (PA66, нейлон 6/6): продукт поликонденсации гексаметилендиамина (6 C) и адипиновой кислоты (6 C), повторяющееся звено –[NH–(CH₂)₆–NH–OC–(CH₂)₄–CO]ₙ–; промышленные марки: Zytel 101 (DuPont), Ultramid A3K (BASF), Durethan A (Lanxess)` | 4 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 3 |
| `SS AISI 304` | 3 |
| `Силикон 40–50 Shore A` | 2 |
| `Spectra (UHMWPE волокно Honeywell)` | 1 |
| `Ионная жидкость [EMIM][TFSI]` | 1 |
| `PTFE-композит DU втулки` | 1 |
| `100Cr6 (ISO 683-17) / AISI 52100 / ГОСТ ШХ15: C 0.95–1.10 %, Cr 1.35–1.65 %, Mn 0.25–0.45 %, Si 0.15–0.35 %` | 1 |
| `PDMS — полидиметилсилоксан (эталонная система Dow SYLGARD 184: двухкомпонентный силиконовый эластомер 10:1, ненаполненный, прозрачный)` | 1 |
| `Silicone-Textile composite` | 1 |
