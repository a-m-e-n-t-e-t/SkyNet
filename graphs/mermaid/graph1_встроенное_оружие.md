# Граф 1 — подсистема «встроенное_оружие»

```mermaid
graph LR
    izdelie_minigun_m134[прочее]
    izdelie_granatomet_m320[прочее]
    часть_minigun_m134_core[основной_элемент]
    часть_minigun_m134_core_motor[электропривод]
    часть_minigun_m134_core_rotor[ротор]
    часть_minigun_m134_core_barrels[стволы]
    часть_minigun_m134_connectors[разъёмы]
    часть_minigun_m134_housing[корпус]
    часть_minigun_m134_mounting[крепёж]
    часть_granatomet_m320_core[основной_элемент]
    часть_granatomet_m320_connectors[разъёмы]
    часть_granatomet_m320_housing[корпус]
    часть_granatomet_m320_mounting[крепёж]
    часть_granatomet_m320_core_usm[ударно-спусковой_механизм]
    часть_granatomet_m320_core_resiver[ресивер]
    часть_granatomet_m320_core_stvol[ствол]
    часть_hk_tank_плазма_пушка_1[plasma_cannon]
    часть_hk_aerial_плазма_пушка[plasma_cannon]
    часть_t_x_нанотех_инъектор[nanotech_injector]
    часть_t_x_плазма_пушка[built_in_plasma_cannon]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_becu[Cu основа; Be 1.90–2.1…]
    material_gallinstan[Эвтектика Ga-In-Sn: Ga…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    material_w_ni_fe[Вольфрамовый тяжёлый с…]
    izdelie_granatomet_m320 -->|материал| material_al_6061_t6
    izdelie_granatomet_m320 -->|материал| material_becu
    часть_minigun_m134_core -->|материал| material_stal_st3
    часть_minigun_m134_core_motor -->|материал| material_stal_st3
    часть_minigun_m134_core_rotor -->|материал| material_stal_st3
    часть_minigun_m134_core_barrels -->|материал| material_stal_st3
    часть_minigun_m134_connectors -->|материал| material_al_6061_t6
    часть_minigun_m134_housing -->|материал| material_ti_6al_4v
    часть_minigun_m134_mounting -->|материал| material_stal_st3
    часть_granatomet_m320_core -->|материал| material_al_6061_t6
    часть_granatomet_m320_connectors -->|материал| material_becu
    часть_granatomet_m320_housing -->|материал| material_al_6061_t6
    часть_granatomet_m320_mounting -->|материал| material_al_6061_t6
    часть_granatomet_m320_core_usm -->|материал| material_al_6061_t6
    часть_granatomet_m320_core_resiver -->|материал| material_al_6061_t6
    часть_granatomet_m320_core_stvol -->|материал| material_al_6061_t6
    часть_hk_tank_плазма_пушка_1 -->|материал| material_w_ni_fe
    часть_hk_aerial_плазма_пушка -->|материал| material_w_ni_fe
    часть_t_x_нанотех_инъектор -->|материал| material_gallinstan
    часть_t_x_плазма_пушка -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 8 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 5 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 2 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 2 |
| `Вольфрамовый тяжёлый сплав (WHA) класса 1: W ~90 % (основа), Ni ~6–7 %, Fe ~3–4 % (номинал 90W-6Ni-4Fe; вендорские составы 90W-7Ni-3Fe), примеси O ≤0.01 % (ASTM B777 Grade 1 / MIL-T-21014 Class 1, Ni-Fe связка)` | 2 |
| `Эвтектика Ga-In-Sn: Ga 68.5% / In 21.5% / Sn 10.0% (коммерческий Galinstan); жидкий металл при комнатной температуре, нетоксичная замена ртути` | 1 |
