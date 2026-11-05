# Граф 1 — подсистема «приводная_система»

```mermaid
graph LR
    izdelie_tsa[прочее]
    izdelie_belleville_shaiby[прочее]
    izdelie_ipmc[прочее]
    izdelie_tcp[прочее]
    izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov[прочее]
    izdelie_fleksury_8_diskov_po_0_15_mm[прочее]
    izdelie_pezoelektricheskii_gromkogovoritel[прочее]
    izdelie_bldc_+_enkoder[прочее]
    izdelie_apa[прочее]
    izdelie_zubchataya_mufta[прочее]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena[прочее]
    izdelie_dea[прочее]
    izdelie_elektroflyuidnye_volokna_mit[прочее]
    izdelie_bldc[прочее]
    izdelie_3d_pechatnye_dea[прочее]
    izdelie_povorotnoe_uplotnenie[прочее]
    izdelie_hasel[прочее]
    часть_tsa_connectors[разъёмы]
    часть_tsa_housing[корпус]
    часть_tsa_core[основной_элемент]
    часть_tsa_mounting[крепёж]
    часть_belleville_shaiby_connectors[разъёмы]
    часть_belleville_shaiby_core[основной_элемент]
    часть_belleville_shaiby_housing[корпус]
    часть_belleville_shaiby_mounting[крепёж]
    часть_ipmc_housing[корпус]
    часть_ipmc_connectors[разъёмы]
    часть_ipmc_core[основной_элемент]
    часть_ipmc_mounting[крепёж]
    часть_tcp_housing[корпус]
    часть_tcp_connectors[разъёмы]
    часть_tcp_mounting[крепёж]
    часть_tcp_core[основной_элемент]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting[крепёж]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing[корпус]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors[разъёмы]
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core[основной_элемент]
    часть_fleksury_8_diskov_po_0_15_mm_housing[корпус]
    часть_fleksury_8_diskov_po_0_15_mm_mounting[крепёж]
    часть_fleksury_8_diskov_po_0_15_mm_core[основной_элемент]
    часть_fleksury_8_diskov_po_0_15_mm_connectors[разъёмы]
    часть_pezoelektricheskii_gromkogovoritel_connectors[разъёмы]
    часть_pezoelektricheskii_gromkogovoritel_core[основной_элемент]
    часть_pezoelektricheskii_gromkogovoritel_mounting[крепёж]
    часть_pezoelektricheskii_gromkogovoritel_housing[корпус]
    часть_bldc_+_enkoder_connectors[разъёмы]
    часть_bldc_+_enkoder_mounting[крепёж]
    часть_bldc_+_enkoder_core[основной_элемент]
    часть_bldc_+_enkoder_housing[корпус]
    часть_apa_housing[корпус]
    часть_apa_connectors[разъёмы]
    часть_apa_core[основной_элемент]
    часть_apa_mounting[крепёж]
    часть_zubchataya_mufta_housing[корпус]
    часть_zubchataya_mufta_mounting[крепёж]
    часть_zubchataya_mufta_core[основной_элемент]
    часть_zubchataya_mufta_connectors[разъёмы]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing[корпус]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting[крепёж]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors[разъёмы]
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core[основной_элемент]
    часть_dea_connectors[разъёмы]
    часть_dea_housing[корпус]
    часть_dea_core[основной_элемент]
    часть_dea_mounting[крепёж]
    часть_elektroflyuidnye_volokna_mit_housing[корпус]
    часть_elektroflyuidnye_volokna_mit_core[основной_элемент]
    часть_elektroflyuidnye_volokna_mit_connectors[разъёмы]
    часть_elektroflyuidnye_volokna_mit_mounting[крепёж]
    часть_bldc_housing[корпус]
    часть_bldc_connectors[разъёмы]
    часть_bldc_mounting[крепёж]
    часть_bldc_core[основной_элемент]
    часть_3d_pechatnye_dea_connectors[разъёмы]
    часть_3d_pechatnye_dea_core[основной_элемент]
    часть_3d_pechatnye_dea_mounting[крепёж]
    часть_3d_pechatnye_dea_housing[корпус]
    часть_povorotnoe_uplotnenie_core[основной_элемент]
    часть_povorotnoe_uplotnenie_connectors[разъёмы]
    часть_povorotnoe_uplotnenie_housing[корпус]
    часть_povorotnoe_uplotnenie_mounting[крепёж]
    часть_hasel_housing[корпус]
    часть_hasel_mounting[крепёж]
    часть_hasel_connectors[разъёмы]
    часть_hasel_core[основной_элемент]
    material_ti_6al_4v[Ti-6Al-4V]
    material_al_6061_t6[Al 6061-T6]
    material_stal_st3[Сталь Ст3]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_becu[BeCu]
    izdelie_3d_pechatnye_dea -->|материал| material_becu
    часть_tsa_connectors -->|материал| material_al_6061_t6
    часть_tsa_housing -->|материал| material_al_6061_t6
    часть_tsa_mounting -->|материал| material_al_6061_t6
    часть_belleville_shaiby_core -->|материал| material_stal_st3
    часть_belleville_shaiby_housing -->|материал| material_al_6061_t6
    часть_ipmc_housing -->|материал| material_al_6061_t6
    часть_ipmc_mounting -->|материал| material_latun_c36000
    часть_tcp_housing -->|материал| material_al_6061_t6
    часть_tcp_mounting -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing -->|материал| material_al_6061_t6
    часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_housing -->|материал| material_al_6061_t6
    часть_fleksury_8_diskov_po_0_15_mm_core -->|материал| material_becu
    часть_fleksury_8_diskov_po_0_15_mm_connectors -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_connectors -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_core -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_mounting -->|материал| material_latun_c36000
    часть_pezoelektricheskii_gromkogovoritel_housing -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_connectors -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_mounting -->|материал| material_stal_st3
    часть_bldc_+_enkoder_core -->|материал| material_al_6061_t6
    часть_bldc_+_enkoder_housing -->|материал| material_al_6061_t6
    часть_apa_housing -->|материал| material_al_6061_t6
    часть_apa_connectors -->|материал| material_al_6061_t6
    часть_apa_core -->|материал| material_ti_6al_4v
    часть_apa_mounting -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_housing -->|материал| material_al_6061_t6
    часть_zubchataya_mufta_mounting -->|материал| material_stal_st3
    часть_zubchataya_mufta_core -->|материал| material_stal_st3
    часть_zubchataya_mufta_connectors -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting -->|материал| material_al_6061_t6
    часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors -->|материал| material_al_6061_t6
    часть_dea_connectors -->|материал| material_latun_c36000
    часть_dea_housing -->|материал| material_al_6061_t6
    часть_dea_mounting -->|материал| material_al_6061_t6
    часть_elektroflyuidnye_volokna_mit_housing -->|материал| material_al_6061_t6
    часть_bldc_housing -->|материал| material_al_6061_t6
    часть_bldc_connectors -->|материал| material_al_6061_t6
    часть_bldc_mounting -->|материал| material_al_6061_t6
    часть_bldc_core -->|материал| material_al_6061_t6
    часть_3d_pechatnye_dea_connectors -->|материал| material_becu
    часть_povorotnoe_uplotnenie_connectors -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_housing -->|материал| material_al_6061_t6
    часть_povorotnoe_uplotnenie_mounting -->|материал| material_stal_st3
    часть_hasel_housing -->|материал| material_al_6061_t6
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 32 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 6 |
| `Сталь Ст3` | 5 |
| `Нейлон 6/66` | 4 |
| `Полиимид` | 4 |
| `BeCu` | 3 |
| `SS AISI 304` | 3 |
| `Силикон 40–50 Shore A` | 2 |
| `Spectra (UHMWPE волокно Honeywell)` | 1 |
| `100Cr6 (EN 683-17) / AISI 52100 / ГОСТ ШХ15: C 0.95–1.10 %, Cr 1.35–1.65 %, Mn 0.25–0.45 %, Si 0.15–0.35 %` | 1 |
| `ионогель` | 1 |
| `медный провод` | 1 |
| `Ti-6Al-4V` | 1 |
| `Silicone-Textile composite` | 1 |
| `Эластомерная матрица` | 1 |
