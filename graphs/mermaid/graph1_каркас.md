# Граф 1 — подсистема «каркас»

```mermaid
graph LR
    izdelie_kompensatory[прочее]
    izdelie_reshetchatyi_karkas[прочее]
    izdelie_elastomernyh_dempferah[прочее]
    часть_kompensatory_connectors[разъёмы]
    часть_kompensatory_mounting[крепёж]
    часть_kompensatory_housing[корпус]
    часть_kompensatory_core[основной_элемент]
    часть_kompensatory_core_диафрагмы[гофрированная_диафрагма]
    часть_kompensatory_core_фиттинги[концевое_кольцо]
    часть_reshetchatyi_karkas_housing[корпус]
    часть_reshetchatyi_karkas_core[основной_элемент]
    часть_reshetchatyi_karkas_mounting[крепёж]
    часть_reshetchatyi_karkas_connectors[разъёмы]
    часть_reshetchatyi_karkas_core_фиттинги[узловая_бобышка]
    часть_reshetchatyi_karkas_core_стрингеры[силовой_профиль]
    часть_reshetchatyi_karkas_core_диафрагмы[перфорированная_рамка]
    часть_elastomernyh_dempferah_housing[корпус]
    часть_elastomernyh_dempferah_connectors[разъёмы]
    часть_elastomernyh_dempferah_mounting[крепёж]
    часть_elastomernyh_dempferah_core[основной_элемент]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_becu[Cu основа; Be 1.90–2.1…]
    material_inconel_718[Ni+Co 50.0–55.0; Cr 17…]
    material_silikon_40_50_shore_a[Полидиметилсилоксан (P…]
    material_ss_aisi_304[нержавеющая сталь AISI…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    izdelie_kompensatory -->|материал| material_inconel_718
    izdelie_kompensatory -->|материал| material_al_6061_t6
    izdelie_elastomernyh_dempferah -->|материал| material_silikon_40_50_shore_a
    izdelie_elastomernyh_dempferah -->|материал| material_aluminum
    часть_kompensatory_connectors -->|материал| material_stal_st3
    часть_kompensatory_mounting -->|материал| material_ss_aisi_304
    часть_kompensatory_housing -->|материал| material_al_6061_t6
    часть_kompensatory_core -->|материал| material_inconel_718
    часть_kompensatory_core_диафрагмы -->|материал| material_inconel_718
    часть_kompensatory_core_фиттинги -->|материал| material_inconel_718
    часть_reshetchatyi_karkas_core_фиттинги -->|материал| material_al_6061_t6
    часть_reshetchatyi_karkas_core_стрингеры -->|материал| material_al_6061_t6
    часть_reshetchatyi_karkas_core_диафрагмы -->|материал| material_al_6061_t6
    часть_elastomernyh_dempferah_housing -->|материал| material_al_6061_t6
    часть_elastomernyh_dempferah_connectors -->|материал| material_becu
    часть_elastomernyh_dempferah_mounting -->|материал| material_stal_st3
    часть_elastomernyh_dempferah_core -->|материал| material_silikon_40_50_shore_a
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 6 |
| `Ni+Co 50.0–55.0; Cr 17.0–21.0; Fe баланс; Nb+Ta 4.75–5.50; Mo 2.80–3.30; Ti 0.65–1.15; Al 0.35–0.80; Co ≤1.0; C ≤0.08; Mn ≤0.35; Si ≤0.35; Cu ≤0.15; B 0.001–0.006; P ≤0.015; S ≤0.015` | 4 |
| `Полидиметилсилоксан (PDMS, VMQ): основа –[Si(CH₃)₂–O]ₙ– с винильными сшивочными группами (~0.05–0.5 мол. %), наполнитель — пирогенный кремнезём SiO₂ 10–30 мас.% (типа HDK®), вулканизация пероксидная (HCR-марки) или платиновая присоединительная (RTV-2/LSR)` | 2 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 2 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 1 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 1 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 1 |
