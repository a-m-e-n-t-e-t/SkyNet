# Граф 1 — подсистема «система_охлаждения»

```mermaid
graph LR
    izdelie_loop_heat_pipe[прочее]
    izdelie_kapillyarnaya_teplovaya_trubka[прочее]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny[прочее]
    часть_loop_heat_pipe_housing[корпус]
    часть_loop_heat_pipe_connectors[разъёмы]
    часть_loop_heat_pipe_mounting[крепёж]
    часть_loop_heat_pipe_core[основной_элемент]
    часть_kapillyarnaya_teplovaya_trubka_core[основной_элемент]
    часть_kapillyarnaya_teplovaya_trubka_connectors[разъёмы]
    часть_kapillyarnaya_teplovaya_trubka_housing[корпус]
    часть_kapillyarnaya_teplovaya_trubka_mounting[крепёж]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors[разъёмы]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core[основной_элемент]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing[корпус]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting[крепёж]
    material_ti_6al_4v[Ti-6Al-4V]
    часть_loop_heat_pipe_housing -->|материал| material_ti_6al_4v
    часть_loop_heat_pipe_mounting -->|материал| material_ti_6al_4v
    часть_loop_heat_pipe_core -->|материал| material_ti_6al_4v
    часть_kapillyarnaya_teplovaya_trubka_core -->|материал| material_ti_6al_4v
    часть_kapillyarnaya_teplovaya_trubka_housing -->|материал| material_ti_6al_4v
    часть_kapillyarnaya_teplovaya_trubka_mounting -->|материал| material_ti_6al_4v
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core -->|материал| material_ti_6al_4v
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing -->|материал| material_ti_6al_4v
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Ti-6Al-4V` | 9 |
