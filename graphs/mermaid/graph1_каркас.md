# Граф 1 — подсистема «каркас»

```mermaid
graph LR
    izdelie_reshetchatyi_karkas[прочее]
    izdelie_kompensatory[прочее]
    часть_reshetchatyi_karkas_mounting[крепёж]
    часть_reshetchatyi_karkas_connectors[разъёмы]
    часть_reshetchatyi_karkas_core[основной_элемент]
    часть_reshetchatyi_karkas_housing[корпус]
    часть_kompensatory_mounting[крепёж]
    часть_kompensatory_connectors[разъёмы]
    часть_kompensatory_housing[корпус]
    часть_kompensatory_core[основной_элемент]
    izdelie_SkyNet_Cameron[прочее]
    izdelie_SkyNet_HKAerial[прочее]
    izdelie_SkyNet_Rev9[прочее]
    izdelie_SkyNet_MarcusWright[прочее]
    izdelie_SkyNet_T600[прочее]
    izdelie_SkyNet_HKTank[прочее]
    izdelie_SkyNet_TX[прочее]
    izdelie_SkyNet_T800[прочее]
    izdelie_SkyNet_T850[прочее]
    часть_cameron_эндоскелет[titanium_endoskeleton_small]
    часть_hk_aerial_крылья[wings]
    часть_hk_aerial_фюзеляж[fuselage]
    часть_rev9_endoskeleton[carbon_endoskeleton]
    часть_marcus_эндоскелет[cybernetic_endoskeleton]
    часть_t600_эндоскелет[titanium_endoskeleton]
    часть_hk_tank_корпус[tank_body]
    часть_hk_tank_башня[turret]
    часть_t_x_эндоскелет[hyperalloy_endoskeleton_tx]
    часть_t800_эндоскелет_торс[hyperalloy_endoskeleton]
    часть_t850_эндоскелет[hyperalloy_endoskeleton]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_cfrp_t1100g[углеродное волокно Tor…]
    material_inconel_718[Ni+Co 50.0–55.0; Cr 17…]
    material_poliimid[Ароматический полиимид…]
    material_si[Si (кремний); электрон…]
    material_ss_aisi_304[нержавеющая сталь AISI…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    часть_reshetchatyi_karkas_mounting -->|материал| material_stal_st3
    часть_reshetchatyi_karkas_connectors -->|материал| material_al_6061_t6
    часть_reshetchatyi_karkas_core -->|материал| material_al_6061_t6
    часть_reshetchatyi_karkas_housing -->|материал| material_stal_st3
    часть_kompensatory_mounting -->|материал| material_ss_aisi_304
    часть_kompensatory_connectors -->|материал| material_stal_st3
    часть_kompensatory_housing -->|материал| material_al_6061_t6
    часть_kompensatory_core -->|материал| material_inconel_718
    izdelie_SkyNet_HKAerial -->|материал| material_inconel_718
    izdelie_SkyNet_T800 -->|материал| material_si
    izdelie_SkyNet_T800 -->|материал| material_poliimid
    izdelie_SkyNet_T800 -->|материал| material_al_6061_t6
    часть_cameron_эндоскелет -->|материал| material_ti_6al_4v
    часть_hk_aerial_крылья -->|материал| material_ti_6al_4v
    часть_hk_aerial_фюзеляж -->|материал| material_ti_6al_4v
    часть_rev9_endoskeleton -->|материал| material_cfrp_t1100g
    часть_marcus_эндоскелет -->|материал| material_al_6061_t6
    часть_t600_эндоскелет -->|материал| material_ti_6al_4v
    часть_t_x_эндоскелет -->|материал| material_ti_6al_4v
    часть_t800_эндоскелет_торс -->|материал| material_ti_6al_4v
    часть_t850_эндоскелет -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 7 |
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 5 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 3 |
| `Ni+Co 50.0–55.0; Cr 17.0–21.0; Fe баланс; Nb+Ta 4.75–5.50; Mo 2.80–3.30; Ti 0.65–1.15; Al 0.35–0.80; Co ≤1.0; C ≤0.08; Mn ≤0.35; Si ≤0.35; Cu ≤0.15; B 0.001–0.006; P ≤0.015; S ≤0.015` | 2 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 1 |
| `Si (кремний); электронный сорт ≥99.9999999% (9N) для подложек ИС, солнечный ≥99.9999% (6N), металлургический ~98–99% (Si-Fe, Si-Ca примеси)` | 1 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 1 |
| `углеродное волокно Toray TORAYCA T1100G (PAN-based, intermediate modulus) ~60 об.% + эпоксидная матрица (система 3960, отверждение 177 °C) ~40 об.%` | 1 |
