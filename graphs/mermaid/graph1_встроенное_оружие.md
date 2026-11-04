# Граф 1 — подсистема «встроенное_оружие»

```mermaid
graph LR
    часть_hk_aerial_плазма_пушка[plasma_cannon]
    часть_hk_tank_плазма_пушка_2[plasma_cannon]
    часть_hk_tank_плазма_пушка_1[plasma_cannon]
    часть_t_x_нанотех_инъектор[nanotech_injector]
    часть_t_x_плазма_пушка[built_in_plasma_cannon]
    izdelie_granatomet_m320[прочее]
    izdelie_minigun_m134[прочее]
    часть_granatomet_m320_mounting[крепёж]
    часть_granatomet_m320_core[основной_элемент]
    часть_granatomet_m320_housing[корпус]
    часть_granatomet_m320_connectors[разъёмы]
    часть_minigun_m134_housing[корпус]
    часть_minigun_m134_connectors[разъёмы]
    часть_minigun_m134_mounting[крепёж]
    часть_minigun_m134_core[основной_элемент]
    material_al_6061_t6[Al 6061-T6]
    material_becu[BeCu]
    material_gallinstan[Галлинстан]
    material_stal_st3[Сталь Ст3]
    material_ti_6al_4v[Ti-6Al-4V]
    material_w_ni_fe[W-Ni-Fe]
    часть_hk_aerial_плазма_пушка -->|материал| material_w_ni_fe
    часть_hk_tank_плазма_пушка_2 -->|материал| material_w_ni_fe
    часть_hk_tank_плазма_пушка_1 -->|материал| material_w_ni_fe
    часть_t_x_нанотех_инъектор -->|материал| material_gallinstan
    часть_t_x_плазма_пушка -->|материал| material_ti_6al_4v
    izdelie_granatomet_m320 -->|материал| material_al_6061_t6
    izdelie_granatomet_m320 -->|материал| material_becu
    часть_granatomet_m320_mounting -->|материал| material_al_6061_t6
    часть_granatomet_m320_core -->|материал| material_al_6061_t6
    часть_granatomet_m320_housing -->|материал| material_al_6061_t6
    часть_granatomet_m320_connectors -->|материал| material_becu
    часть_minigun_m134_housing -->|материал| material_ti_6al_4v
    часть_minigun_m134_mounting -->|материал| material_stal_st3
    часть_minigun_m134_core -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 4 |
| `W-Ni-Fe` | 3 |
| `Ti-6Al-4V` | 3 |
| `BeCu` | 2 |
| `Галлинстан` | 1 |
| `Сталь Ст3` | 1 |
