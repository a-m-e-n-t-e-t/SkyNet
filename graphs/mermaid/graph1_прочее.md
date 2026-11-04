# Граф 1 — подсистема «прочее»

```mermaid
graph LR
    izdelie_dielektricheskie_elastomernye_datchiki[прочее]
    izdelie_provodnikovaya_nanoreshetka[прочее]
    izdelie_gibkii_pcb[прочее]
    izdelie_elastomernyh_dempferah[прочее]
    izdelie_gidrostaticheskie_gazovye_podshipniki_na_gelii[прочее]
    izdelie_slm_eos_m290[прочее]
    izdelie_polyimide_fpc[прочее]
    izdelie_copv[прочее]
    часть_dielektricheskie_elastomernye_datchiki_housing[корпус]
    часть_dielektricheskie_elastomernye_datchiki_connectors[разъёмы]
    часть_dielektricheskie_elastomernye_datchiki_core[основной_элемент]
    часть_dielektricheskie_elastomernye_datchiki_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_connectors[разъёмы]
    часть_provodnikovaya_nanoreshetka_housing[корпус]
    часть_provodnikovaya_nanoreshetka_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_core[основной_элемент]
    часть_gibkii_pcb_housing[корпус]
    часть_gibkii_pcb_core[основной_элемент]
    часть_gibkii_pcb_mounting[крепёж]
    часть_gibkii_pcb_connectors[разъёмы]
    часть_elastomernyh_dempferah_mounting[крепёж]
    часть_elastomernyh_dempferah_connectors[разъёмы]
    часть_elastomernyh_dempferah_core[основной_элемент]
    часть_elastomernyh_dempferah_housing[корпус]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core[основной_элемент]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing[корпус]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_connectors[разъёмы]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting[крепёж]
    часть_slm_eos_m290_core[основной_элемент]
    часть_slm_eos_m290_connectors[разъёмы]
    часть_slm_eos_m290_housing[корпус]
    часть_slm_eos_m290_mounting[крепёж]
    часть_polyimide_fpc_connectors[разъёмы]
    часть_polyimide_fpc_housing[корпус]
    часть_polyimide_fpc_mounting[крепёж]
    часть_polyimide_fpc_core[основной_элемент]
    часть_copv_connectors[разъёмы]
    часть_copv_housing[корпус]
    часть_copv_mounting[крепёж]
    часть_copv_core[основной_элемент]
    часть_cameron_ткань_кожа[living_tissue_female]
    часть_marcus_человеческая_кожа[human_tissue]
    часть_t600_резиновая_кожа[rubber_skin]
    часть_t_x_ткань_кожа[living_tissue_female]
    часть_t800_ткань_кожа[living_tissue]
    часть_t850_ткань_кожа[living_tissue]
    material_si[Si]
    material_ti_6al_4v[Ti-6Al-4V]
    часть_dielektricheskie_elastomernye_datchiki_housing -->|материал| material_ti_6al_4v
    часть_dielektricheskie_elastomernye_datchiki_core -->|материал| material_ti_6al_4v
    часть_dielektricheskie_elastomernye_datchiki_mounting -->|материал| material_ti_6al_4v
    часть_provodnikovaya_nanoreshetka_housing -->|материал| material_ti_6al_4v
    часть_provodnikovaya_nanoreshetka_mounting -->|материал| material_ti_6al_4v
    часть_provodnikovaya_nanoreshetka_core -->|материал| material_ti_6al_4v
    часть_gibkii_pcb_housing -->|материал| material_ti_6al_4v
    часть_gibkii_pcb_core -->|материал| material_ti_6al_4v
    часть_gibkii_pcb_mounting -->|материал| material_ti_6al_4v
    часть_elastomernyh_dempferah_mounting -->|материал| material_ti_6al_4v
    часть_elastomernyh_dempferah_core -->|материал| material_ti_6al_4v
    часть_elastomernyh_dempferah_housing -->|материал| material_ti_6al_4v
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core -->|материал| material_ti_6al_4v
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing -->|материал| material_ti_6al_4v
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting -->|материал| material_ti_6al_4v
    часть_slm_eos_m290_core -->|материал| material_ti_6al_4v
    часть_slm_eos_m290_housing -->|материал| material_ti_6al_4v
    часть_slm_eos_m290_mounting -->|материал| material_ti_6al_4v
    часть_polyimide_fpc_housing -->|материал| material_ti_6al_4v
    часть_polyimide_fpc_mounting -->|материал| material_ti_6al_4v
    часть_polyimide_fpc_core -->|материал| material_ti_6al_4v
    часть_copv_housing -->|материал| material_ti_6al_4v
    часть_copv_mounting -->|материал| material_ti_6al_4v
    часть_copv_core -->|материал| material_ti_6al_4v
    часть_cameron_ткань_кожа -->|материал| material_ti_6al_4v
    часть_marcus_человеческая_кожа -->|материал| material_ti_6al_4v
    часть_t_x_ткань_кожа -->|материал| material_ti_6al_4v
    часть_t800_ткань_кожа -->|материал| material_si
    часть_t850_ткань_кожа -->|материал| material_si
```

| Материал | Используется в частях |
|---|---:|
| `Ti-6Al-4V` | 27 |
| `Si` | 2 |
