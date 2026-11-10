# Граф 1 — подсистема «система_охлаждения»

```mermaid
graph LR
    izdelie_reversivnye_pelte[реверсивный_модуль_Пельтье]
    izdelie_loop_heat_pipe[прочее]
    izdelie_termomoduli_pelte[модуль_Пельтье]
    izdelie_kapillyarnaya_teplovaya_trubka[прочее]
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny[прочее]
    часть_reversivnye_pelte_ceramic_top[керамика_верх]
    часть_reversivnye_pelte_peltier_couples[термоэлементы]
    часть_reversivnye_pelte_electrodes[электроды]
    часть_reversivnye_pelte_solder[припой]
    часть_loop_heat_pipe_housing[корпус]
    часть_loop_heat_pipe_core[основной_элемент]
    часть_loop_heat_pipe_mounting[крепёж]
    часть_loop_heat_pipe_connectors[разъёмы]
    часть_termomoduli_pelte_ceramic_top[керамика_верх]
    часть_termomoduli_pelte_electrodes[электроды]
    часть_termomoduli_pelte_peltier_couples[термоэлементы]
    часть_termomoduli_pelte_solder[припой]
    часть_termomoduli_pelte_wires[провода]
    часть_kapillyarnaya_teplovaya_trubka_connectors[разъёмы]
    часть_kapillyarnaya_teplovaya_trubka_housing[корпус]
    часть_kapillyarnaya_teplovaya_trubka_core[основной_элемент]
    часть_kapillyarnaya_teplovaya_trubka_mounting[крепёж]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors[разъёмы]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core[основной_элемент]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing[корпус]
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting[крепёж]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_bi2te3[Bi₂Te₃ (теллурид висму…]
    material_copper[Cu ≥99.9% (электролити…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_oksid_alyuminiya[Оксид алюминия Al₂O₃ (…]
    material_splav_sn_pb[Sn 63 ± 0.5 %, Pb — ос…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    izdelie_reversivnye_pelte -->|материал| material_bi2te3
    izdelie_reversivnye_pelte -->|материал| material_oksid_alyuminiya
    izdelie_reversivnye_pelte -->|материал| material_copper
    izdelie_reversivnye_pelte -->|материал| material_splav_sn_pb
    izdelie_loop_heat_pipe -->|материал| material_stal_st3
    izdelie_loop_heat_pipe -->|материал| material_al_6061_t6
    izdelie_termomoduli_pelte -->|материал| material_bi2te3
    izdelie_termomoduli_pelte -->|материал| material_oksid_alyuminiya
    izdelie_termomoduli_pelte -->|материал| material_copper
    izdelie_termomoduli_pelte -->|материал| material_splav_sn_pb
    izdelie_kapillyarnaya_teplovaya_trubka -->|материал| material_copper
    izdelie_kapillyarnaya_teplovaya_trubka -->|материал| material_aluminum
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny -->|материал| material_copper
    izdelie_mikrokanalnye_ohlazhdayuschie_plastiny -->|материал| material_al_6061_t6
    часть_reversivnye_pelte_ceramic_top -->|материал| material_oksid_alyuminiya
    часть_reversivnye_pelte_peltier_couples -->|материал| material_bi2te3
    часть_reversivnye_pelte_electrodes -->|материал| material_copper
    часть_reversivnye_pelte_solder -->|материал| material_splav_sn_pb
    часть_loop_heat_pipe_housing -->|материал| material_al_6061_t6
    часть_loop_heat_pipe_core -->|материал| material_stal_st3
    часть_loop_heat_pipe_mounting -->|материал| material_ti_6al_4v
    часть_loop_heat_pipe_connectors -->|материал| material_al_6061_t6
    часть_termomoduli_pelte_ceramic_top -->|материал| material_oksid_alyuminiya
    часть_termomoduli_pelte_electrodes -->|материал| material_copper
    часть_termomoduli_pelte_peltier_couples -->|материал| material_bi2te3
    часть_termomoduli_pelte_solder -->|материал| material_splav_sn_pb
    часть_termomoduli_pelte_wires -->|материал| material_copper
    часть_kapillyarnaya_teplovaya_trubka_connectors -->|материал| material_latun_c36000
    часть_kapillyarnaya_teplovaya_trubka_housing -->|материал| material_al_6061_t6
    часть_kapillyarnaya_teplovaya_trubka_core -->|материал| material_copper
    часть_kapillyarnaya_teplovaya_trubka_mounting -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_connectors -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_core -->|материал| material_copper
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_housing -->|материал| material_al_6061_t6
    часть_mikrokanalnye_ohlazhdayuschie_plastiny_mounting -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 9 |
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 8 |
| `Bi₂Te₃ (теллурид висмута; промышленные марки легированы: p-тип — Bi₀.₅Sb₁.₅Te₃ (Sb), n-тип — Bi₂Te₂.₇Se₀.₃ (Se); M = 800.8 г/моль)` | 4 |
| `Оксид алюминия Al₂O₃ (глинозём): 52.9 масс.% Al / 47.1 масс.% O; технические марки 96–99.9% Al₂O₃ (остальное SiO₂, MgO, CaO — спекающие добавки); высокочистый корунд ≥99.99%` | 4 |
| `Sn 63 ± 0.5 %, Pb — остальное (~37 %); примеси не более: Sb 0.20 %, Bi 0.10 %, Cu 0.08 %, Ag 0.10 %, Fe 0.02 %, As 0.03 %, Zn 0.003 %, Cd 0.002 %, Ni 0.01 %, Al 0.001 %, Au 0.05 %, In 0.10 % (TDS 63Sn/37Pb CRM); российский аналог ПОС-61 по ГОСТ 21930-76: Sn 59–61 %, Pb — остальное` | 4 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 2 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 2 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 1 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
