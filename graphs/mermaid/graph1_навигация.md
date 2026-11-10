# Граф 1 — подсистема «навигация»

```mermaid
graph LR
    izdelie_ads_b_priemnik[прочее]
    часть_ads_b_priemnik_core[основной_элемент]
    часть_ads_b_priemnik_connectors[разъёмы]
    часть_ads_b_priemnik_mounting[крепёж]
    часть_ads_b_priemnik_housing[корпус]
    часть_t800_гиро_навигация[imu_gyro]
    часть_hk_tank_навигация[gps_nav]
    часть_t850_навигация[imu_gyro]
    часть_hk_aerial_навигация[radar_navigation]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    izdelie_ads_b_priemnik -->|материал| material_al_6061_t6
    izdelie_ads_b_priemnik -->|материал| material_aluminum
    часть_ads_b_priemnik_core -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_connectors -->|материал| material_latun_c36000
    часть_ads_b_priemnik_mounting -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_housing -->|материал| material_al_6061_t6
    часть_t800_гиро_навигация -->|материал| material_al_6061_t6
    часть_t850_навигация -->|материал| material_al_6061_t6
    часть_hk_aerial_навигация -->|материал| material_al_6061_t6
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 7 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 1 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
