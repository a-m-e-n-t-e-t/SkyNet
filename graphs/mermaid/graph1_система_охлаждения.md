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
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_copper[Cu ≥99.9% (электролити…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    часть_loop_heat_pipe_housing -->|материал| material_al_6061_t6
    часть_loop_heat_pipe_connectors -->|материал| material_al_6061_t6
    часть_loop_heat_pipe_mounting -->|материал| material_ti_6al_4v
    часть_loop_heat_pipe_core -->|материал| material_stal_st3
    часть_kapillyarnaya_teplovaya_trubka_core -->|материал| material_copper
    часть_kapillyarnaya_teplovaya_trubka_connectors -->|материал| material_latun_c36000
    часть_kapillyarnaya_teplovaya_trubka_housing -->|материал| material_al_6061_t6
    часть_kapillyarnaya_teplovaya_trubka_mounting -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core -->|материал| material_copper
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 6 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 2 |
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 2 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 1 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
