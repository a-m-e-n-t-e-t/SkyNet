# Граф 1 — подсистема «система_охлаждения»

```mermaid
graph LR
    izdelie_loop_heat_pipe[прочее]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny[прочее]
    izdelie_kapillyarnaya_teplovaya_trubka[прочее]
    часть_loop_heat_pipe_connectors[разъёмы]
    часть_loop_heat_pipe_core[основной_элемент]
    часть_loop_heat_pipe_housing[корпус]
    часть_loop_heat_pipe_mounting[крепёж]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting[крепёж]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors[разъёмы]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing[корпус]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core[основной_элемент]
    часть_kapillyarnaya_teplovaya_trubka_housing[корпус]
    часть_kapillyarnaya_teplovaya_trubka_connectors[разъёмы]
    часть_kapillyarnaya_teplovaya_trubka_mounting[крепёж]
    часть_kapillyarnaya_teplovaya_trubka_core[основной_элемент]
    material_al_6061_t6[Al 6061-T6]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_mednyi_provod[медный провод]
    material_stal_st3[Сталь Ст3]
    material_ti_6al_4v[Ti-6Al-4V]
    часть_loop_heat_pipe_connectors -->|материал| material_al_6061_t6
    часть_loop_heat_pipe_core -->|материал| material_stal_st3
    часть_loop_heat_pipe_housing -->|материал| material_al_6061_t6
    часть_loop_heat_pipe_mounting -->|материал| material_ti_6al_4v
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting -->|материал| material_ti_6al_4v
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core -->|материал| material_mednyi_provod
    часть_kapillyarnaya_teplovaya_trubka_housing -->|материал| material_al_6061_t6
    часть_kapillyarnaya_teplovaya_trubka_connectors -->|материал| material_latun_c36000
    часть_kapillyarnaya_teplovaya_trubka_mounting -->|материал| material_ti_6al_4v
    часть_kapillyarnaya_teplovaya_trubka_core -->|материал| material_mednyi_provod
```

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 5 |
| `Ti-6Al-4V` | 3 |
| `медный провод` | 2 |
| `Сталь Ст3` | 1 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
