# Граф 1 — подсистема «приводная_система»

```mermaid
graph LR
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov[прочее]
    izdelie_elektroflyuidnye_volokna_mit[прочее]
    izdelie_bldc[прочее]
    izdelie_tsa[прочее]
    izdelie_hasel[прочее]
    izdelie_pezoelektricheskii_gromkogovoritel[прочее]
    izdelie_bldc_+_enkoder[прочее]
    izdelie_fleksury_8_diskov_po_0_15_mm[прочее]
    izdelie_tcp[прочее]
    izdelie_povorotnoe_uplotnenie[прочее]
    izdelie_3d_pechatnye_dea[прочее]
    izdelie_ipmc[прочее]
    izdelie_dea[прочее]
    izdelie_zubchataya_mufta[прочее]
    izdelie_belleville_shaiby[прочее]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena[прочее]
    izdelie_apa[прочее]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core[основной_элемент]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing[корпус]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors[разъёмы]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting[крепёж]
    часть_elektroflyuidnye_volokna_mit_housing[корпус]
    часть_elektroflyuidnye_volokna_mit_core[основной_элемент]
    часть_elektroflyuidnye_volokna_mit_connectors[разъёмы]
    часть_elektroflyuidnye_volokna_mit_mounting[крепёж]
    часть_bldc_mounting[крепёж]
    часть_bldc_connectors[разъёмы]
    часть_bldc_core[основной_элемент]
    часть_bldc_housing[корпус]
    часть_tsa_housing[корпус]
    часть_tsa_core[основной_элемент]
    часть_tsa_connectors[разъёмы]
    часть_tsa_mounting[крепёж]
    часть_hasel_mounting[крепёж]
    часть_hasel_connectors[разъёмы]
    часть_hasel_housing[корпус]
    часть_hasel_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_mounting[крепёж]
    часть_pezoelektricheskii_gromkogovoritel_housing[корпус]
    часть_pezoelektricheskii_gromkogovoritel_connectors[разъёмы]
    часть_bldc_+_enkoder_core[основной_элемент]
    часть_bldc_+_enkoder_mounting[крепёж]
    часть_bldc_+_enkoder_housing[корпус]
    часть_bldc_+_enkoder_connectors[разъёмы]
    часть_fleksury_8_diskov_po_0_15_mm_housing[корпус]
    часть_fleksury_8_diskov_po_0_15_mm_core[основной_элемент]
    часть_fleksury_8_diskov_po_0_15_mm_mounting[крепёж]
    часть_fleksury_8_diskov_po_0_15_mm_connectors[разъёмы]
    часть_tcp_connectors[разъёмы]
    часть_tcp_core[основной_элемент]
    часть_tcp_mounting[крепёж]
    часть_tcp_housing[корпус]
    часть_povorotnoe_uplotnenie_core[основной_элемент]
    часть_povorotnoe_uplotnenie_housing[корпус]
    часть_povorotnoe_uplotnenie_connectors[разъёмы]
    часть_povorotnoe_uplotnenie_mounting[крепёж]
    часть_3d_pechatnye_dea_core[основной_элемент]
    часть_3d_pechatnye_dea_mounting[крепёж]
    часть_3d_pechatnye_dea_connectors[разъёмы]
    часть_3d_pechatnye_dea_housing[корпус]
    часть_ipmc_mounting[крепёж]
    часть_ipmc_connectors[разъёмы]
    часть_ipmc_housing[корпус]
    часть_ipmc_core[основной_элемент]
    часть_dea_housing[корпус]
    часть_dea_connectors[разъёмы]
    часть_dea_core[основной_элемент]
    часть_dea_mounting[крепёж]
    часть_zubchataya_mufta_core[основной_элемент]
    часть_zubchataya_mufta_mounting[крепёж]
    часть_zubchataya_mufta_housing[корпус]
    часть_zubchataya_mufta_connectors[разъёмы]
    часть_belleville_shaiby_core[основной_элемент]
    часть_belleville_shaiby_housing[корпус]
    часть_belleville_shaiby_connectors[разъёмы]
    часть_belleville_shaiby_mounting[крепёж]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors[разъёмы]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core[основной_элемент]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing[корпус]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting[крепёж]
    часть_apa_core[основной_элемент]
    часть_apa_mounting[крепёж]
    часть_apa_housing[корпус]
    часть_apa_connectors[разъёмы]
    часть_cameron_рука_левая[servo_arm_small]
    часть_cameron_нога_левая[servo_leg_small]
    часть_t850_рука_левая[servo_arm_improved]
    часть_t850_нога_левая[servo_leg_improved]
    часть_t800_рука_левая[servo_arm]
    часть_t800_нога_левая[servo_leg]
    часть_hk_tank_гусеница_левая[tank_track]
    часть_marcus_рука_левая[servo_arm]
    часть_marcus_нога_левая[servo_leg]
    часть_t_x_нога_левая[servo_leg]
    часть_t_x_рука_левая[servo_arm]
    часть_t600_нога_левая[servo_leg]
    часть_t600_рука_левая[servo_arm]
    material_ti_6al_4v[Ti-6Al-4V]
    material_al_6061_t6[Al 6061-T6]
    material_stal_st3[Сталь Ст3]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_poliimid[Полиимид]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_housing -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_connectors -->|материал| material_poliimid
    часть_bldc_mounting -->|материал| material_al_6061_t6
    часть_bldc_connectors -->|материал| material_al_6061_t6
    часть_bldc_core -->|материал| material_al_6061_t6
    часть_bldc_housing -->|материал| material_al_6061_t6
    часть_tsa_housing -->|материал| material_al_6061_t6
    часть_tsa_connectors -->|материал| material_al_6061_t6
    часть_tsa_mounting -->|материал| material_al_6061_t6
    часть_hasel_connectors -->|материал| material_poliimid
    часть_hasel_housing -->|материал| material_al_6061_t6
    часть_pezoelektricheskii_gromkogovoritel_core -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_mounting -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_housing -->|материал| material_al_6061_t6
    часть_pezoelektricheskii_gromkogovoritel_connectors -->|материал| material_latun_c36000
    часть_bldc_+_enkoder_core -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_mounting -->|материал| material_stal_st3
    часть_bldc_+_enkoder_housing -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_connectors -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_housing -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_connectors -->|материал| material_latun_c36000
    часть_tcp_connectors -->|материал| material_poliimid
    часть_tcp_mounting -->|материал| material_al_6061_t6
    часть_tcp_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_connectors -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_mounting -->|материал| material_stal_st3
    часть_ipmc_mounting -->|материал| material_latun_c36000
    часть_ipmc_connectors -->|материал| material_poliimid
    часть_ipmc_housing -->|материал| material_al_6061_t6
    часть_dea_housing -->|материал| material_al_6061_t6
    часть_dea_connectors -->|материал| material_latun_c36000
    часть_dea_mounting -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_core -->|материал| material_stal_st3
    часть_zubchataya_mufta_mounting -->|материал| material_stal_st3
    часть_zubchataya_mufta_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_connectors -->|материал| material_al_6061_t6
    часть_belleville_shaiby_core -->|материал| material_stal_st3
    часть_belleville_shaiby_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting -->|материал| material_al_6061_t6
    часть_apa_core -->|материал| material_ti_6al_4v
    часть_apa_mounting -->|материал| material_al_6061_t6
    часть_apa_housing -->|материал| material_al_6061_t6
    часть_apa_connectors -->|материал| material_al_6061_t6
    часть_cameron_рука_левая -->|материал| material_ti_6al_4v
    часть_cameron_нога_левая -->|материал| material_ti_6al_4v
    часть_t850_рука_левая -->|материал| material_ti_6al_4v
    часть_t850_нога_левая -->|материал| material_ti_6al_4v
    часть_t800_рука_левая -->|материал| material_ti_6al_4v
    часть_t800_нога_левая -->|материал| material_ti_6al_4v
    часть_marcus_рука_левая -->|материал| material_ti_6al_4v
    часть_marcus_нога_левая -->|материал| material_ti_6al_4v
    часть_t_x_нога_левая -->|материал| material_ti_6al_4v
    часть_t_x_рука_левая -->|материал| material_ti_6al_4v
    часть_t600_нога_левая -->|материал| material_ti_6al_4v
    часть_t600_рука_левая -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 32 |
| `Ti-6Al-4V` | 13 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 6 |
| `Сталь Ст3` | 5 |
| `Полиимид` | 4 |
| `Нейлон 6/66` | 4 |
| `BeCu` | 3 |
| `SS AISI 304` | 3 |
| `Силикон 40–50 Shore A` | 2 |
| `медный провод` | 1 |
| `Ионная жидкость [EMIM][TFSI]` | 1 |
| `Spectra (UHMWPE волокно Honeywell)` | 1 |
| `PEEK` | 1 |
| `HALVE P` | 1 |
| `PTFE-композит DU втулки` | 1 |
