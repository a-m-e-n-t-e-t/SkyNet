# Граф 1 — подсистема «прочее»

```mermaid
graph LR
    izdelie_slm_eos_m290[прочее]
    izdelie_dielektricheskie_elastomernye_datchiki[прочее]
    izdelie_gidrostaticheskie_gazovye_podshipniki_na_gelii[прочее]
    izdelie_polyimide_fpc[прочее]
    izdelie_gibkii_pcb[прочее]
    izdelie_elastomernyh_dempferah[прочее]
    izdelie_copv[прочее]
    izdelie_provodnikovaya_nanoreshetka[прочее]
    часть_slm_eos_m290_mounting[крепёж]
    часть_slm_eos_m290_connectors[разъёмы]
    часть_slm_eos_m290_housing[корпус]
    часть_slm_eos_m290_core[основной_элемент]
    часть_dielektricheskie_elastomernye_datchiki_housing[корпус]
    часть_dielektricheskie_elastomernye_datchiki_mounting[крепёж]
    часть_dielektricheskie_elastomernye_datchiki_core[основной_элемент]
    часть_dielektricheskie_elastomernye_datchiki_connectors[разъёмы]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core[основной_элемент]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_connectors[разъёмы]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting[крепёж]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing[корпус]
    часть_polyimide_fpc_mounting[крепёж]
    часть_polyimide_fpc_core[основной_элемент]
    часть_polyimide_fpc_connectors[разъёмы]
    часть_polyimide_fpc_housing[корпус]
    часть_gibkii_pcb_housing[корпус]
    часть_gibkii_pcb_connectors[разъёмы]
    часть_gibkii_pcb_mounting[крепёж]
    часть_gibkii_pcb_core[основной_элемент]
    часть_elastomernyh_dempferah_housing[корпус]
    часть_elastomernyh_dempferah_core[основной_элемент]
    часть_elastomernyh_dempferah_mounting[крепёж]
    часть_elastomernyh_dempferah_connectors[разъёмы]
    часть_copv_housing[корпус]
    часть_copv_core[основной_элемент]
    часть_copv_connectors[разъёмы]
    часть_copv_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_core[основной_элемент]
    часть_provodnikovaya_nanoreshetka_connectors[разъёмы]
    часть_provodnikovaya_nanoreshetka_housing[корпус]
    часть_t600_резиновая_кожа[rubber_skin]
    часть_marcus_человеческая_кожа[human_tissue]
    часть_t850_ткань_кожа[living_tissue]
    часть_t800_ткань_кожа[living_tissue]
    часть_t_x_ткань_кожа[living_tissue_female]
    часть_cameron_ткань_кожа[living_tissue_female]
    material_al_6061_t6[Al 6061-T6]
    material_becu[BeCu]
    material_cfrp_t1100g[CFRP T1100G]
    material_epotek_301_2[Epotek 301-2]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_mxene[MXene]
    material_neilon_6_66[Нейлон 6/66]
    material_p_vdf_trfe_cfe[P]
    material_poliimid[Полиимид]
    material_si[Si]
    material_silikon_40_50_shore_a[Силикон 40–50 Shore A]
    material_ss_aisi_304[SS AISI 304]
    material_stal_st3[Сталь Ст3]
    material_ti_6al_4v[Ti-6Al-4V]
    material_uv_absorbing_pmma[UV-absorbing PMMA]
    часть_slm_eos_m290_mounting -->|материал| material_ss_aisi_304
    часть_slm_eos_m290_connectors -->|материал| material_al_6061_t6
    часть_slm_eos_m290_housing -->|материал| material_stal_st3
    часть_slm_eos_m290_core -->|материал| material_stal_st3
    часть_dielektricheskie_elastomernye_datchiki_housing -->|материал| material_al_6061_t6
    часть_dielektricheskie_elastomernye_datchiki_mounting -->|материал| material_uv_absorbing_pmma
    часть_dielektricheskie_elastomernye_datchiki_core -->|материал| material_p_vdf_trfe_cfe
    часть_dielektricheskie_elastomernye_datchiki_connectors -->|материал| material_latun_c36000
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core -->|материал| material_stal_st3
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_connectors -->|материал| material_neilon_6_66
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting -->|материал| material_latun_c36000
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing -->|материал| material_al_6061_t6
    часть_polyimide_fpc_mounting -->|материал| material_poliimid
    часть_polyimide_fpc_core -->|материал| material_poliimid
    часть_polyimide_fpc_connectors -->|материал| material_poliimid
    часть_polyimide_fpc_housing -->|материал| material_al_6061_t6
    часть_gibkii_pcb_housing -->|материал| material_al_6061_t6
    часть_gibkii_pcb_connectors -->|материал| material_poliimid
    часть_gibkii_pcb_mounting -->|материал| material_epotek_301_2
    часть_gibkii_pcb_core -->|материал| material_poliimid
    часть_elastomernyh_dempferah_housing -->|материал| material_al_6061_t6
    часть_elastomernyh_dempferah_core -->|материал| material_silikon_40_50_shore_a
    часть_elastomernyh_dempferah_mounting -->|материал| material_ti_6al_4v
    часть_elastomernyh_dempferah_connectors -->|материал| material_becu
    часть_copv_housing -->|материал| material_stal_st3
    часть_copv_core -->|материал| material_cfrp_t1100g
    часть_copv_connectors -->|материал| material_al_6061_t6
    часть_copv_mounting -->|материал| material_ti_6al_4v
    часть_provodnikovaya_nanoreshetka_mounting -->|материал| material_ti_6al_4v
    часть_provodnikovaya_nanoreshetka_core -->|материал| material_mxene
    часть_provodnikovaya_nanoreshetka_connectors -->|материал| material_becu
    часть_provodnikovaya_nanoreshetka_housing -->|материал| material_al_6061_t6
    часть_marcus_человеческая_кожа -->|материал| material_ti_6al_4v
    часть_t850_ткань_кожа -->|материал| material_si
    часть_t800_ткань_кожа -->|материал| material_si
    часть_t_x_ткань_кожа -->|материал| material_ti_6al_4v
    часть_cameron_ткань_кожа -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 8 |
| `Ti-6Al-4V` | 6 |
| `Полиимид` | 5 |
| `Сталь Ст3` | 4 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 2 |
| `BeCu` | 2 |
| `Si` | 2 |
| `SS AISI 304` | 1 |
| `UV-absorbing PMMA` | 1 |
| `P` | 1 |
| `Нейлон 6/66` | 1 |
| `Epotek 301-2` | 1 |
| `Силикон 40–50 Shore A` | 1 |
| `CFRP T1100G` | 1 |
| `MXene` | 1 |
