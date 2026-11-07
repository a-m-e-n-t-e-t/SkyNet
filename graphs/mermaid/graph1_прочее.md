# Граф 1 — подсистема «прочее»

```mermaid
graph LR
    izdelie_dielektricheskie_elastomernye_datchiki[прочее]
    izdelie_provodnikovaya_nanoreshetka[прочее]
    izdelie_gibkii_pcb[прочее]
    izdelie_elastomernyh_dempferah[прочее]
    izdelie_gidrostaticheskie_gazovye_podshipniki_na_gelii[прочее]
    izdelie_slm_eos_m290[прочее]
    izdelie_polyimide_fpc[прочее]
    izdelie_copv[прочее]
    часть_dielektricheskie_elastomernye_datchiki_housing[корпус]
    часть_dielektricheskie_elastomernye_datchiki_connectors[разъёмы]
    часть_dielektricheskie_elastomernye_datchiki_core[основной_элемент]
    часть_dielektricheskie_elastomernye_datchiki_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_connectors[разъёмы]
    часть_provodnikovaya_nanoreshetka_housing[корпус]
    часть_provodnikovaya_nanoreshetka_mounting[крепёж]
    часть_provodnikovaya_nanoreshetka_core[основной_элемент]
    часть_gibkii_pcb_housing[корпус]
    часть_gibkii_pcb_core[основной_элемент]
    часть_gibkii_pcb_mounting[крепёж]
    часть_gibkii_pcb_connectors[разъёмы]
    часть_elastomernyh_dempferah_mounting[крепёж]
    часть_elastomernyh_dempferah_connectors[разъёмы]
    часть_elastomernyh_dempferah_core[основной_элемент]
    часть_elastomernyh_dempferah_housing[корпус]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core[основной_элемент]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing[корпус]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_connectors[разъёмы]
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting[крепёж]
    часть_slm_eos_m290_core[основной_элемент]
    часть_slm_eos_m290_connectors[разъёмы]
    часть_slm_eos_m290_housing[корпус]
    часть_slm_eos_m290_mounting[крепёж]
    часть_polyimide_fpc_connectors[разъёмы]
    часть_polyimide_fpc_housing[корпус]
    часть_polyimide_fpc_mounting[крепёж]
    часть_polyimide_fpc_core[основной_элемент]
    часть_copv_connectors[разъёмы]
    часть_copv_housing[корпус]
    часть_copv_mounting[крепёж]
    часть_copv_core[основной_элемент]
    часть_cameron_ткань_кожа[living_tissue_female]
    часть_marcus_человеческая_кожа[human_tissue]
    часть_t600_резиновая_кожа[rubber_skin]
    часть_t_x_ткань_кожа[living_tissue_female]
    часть_t800_ткань_кожа[living_tissue]
    часть_t850_ткань_кожа[living_tissue]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_si[Si (кремний); электрон…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    часть_dielektricheskie_elastomernye_datchiki_housing -->|материал| material_al_6061_t6
    часть_dielektricheskie_elastomernye_datchiki_connectors -->|материал| material_latun_c36000
    часть_provodnikovaya_nanoreshetka_housing -->|материал| material_al_6061_t6
    часть_provodnikovaya_nanoreshetka_mounting -->|материал| material_al_6061_t6
    часть_gibkii_pcb_housing -->|материал| material_al_6061_t6
    часть_elastomernyh_dempferah_mounting -->|материал| material_stal_st3
    часть_elastomernyh_dempferah_housing -->|материал| material_al_6061_t6
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_core -->|материал| material_stal_st3
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_housing -->|материал| material_al_6061_t6
    часть_gidrostaticheskie_gazovye_podshipniki_na_gelii_mounting -->|материал| material_latun_c36000
    часть_slm_eos_m290_core -->|материал| material_stal_st3
    часть_slm_eos_m290_connectors -->|материал| material_al_6061_t6
    часть_slm_eos_m290_housing -->|материал| material_stal_st3
    часть_polyimide_fpc_housing -->|материал| material_al_6061_t6
    часть_copv_connectors -->|материал| material_al_6061_t6
    часть_copv_housing -->|материал| material_stal_st3
    часть_copv_mounting -->|материал| material_ti_6al_4v
    часть_t_x_ткань_кожа -->|материал| material_ti_6al_4v
    часть_t800_ткань_кожа -->|материал| material_si
    часть_t850_ткань_кожа -->|материал| material_si
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 9 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 5 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 5 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 2 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 2 |
| `Полидиметилсилоксан (PDMS, VMQ): основа –[Si(CH₃)₂–O]ₙ– с винильными сшивочными группами (~0.05–0.5 мол. %), наполнитель — пирогенный кремнезём SiO₂ 10–30 мас.% (типа HDK®), вулканизация пероксидная (HCR-марки) или платиновая присоединительная (RTV-2/LSR)` | 2 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 2 |
| `Si (кремний); электронный сорт ≥99.9999999% (9N) для подложек ИС, солнечный ≥99.9999% (6N), металлургический ~98–99% (Si-Fe, Si-Ca примеси)` | 2 |
| `Терполимер винилиденфторид–трифторэтилен–хлорфторэтилен P(VDF-TrFE-CFE): типично 58.5–72.2 мол.% VDF / 17.8–31.5 TrFE / 7–11.5 CFE (референс LIST/Arkema: 64.8/27.4/7.8 мол.%); Mw 400–600 кг/моль (Piezotech RT); полукристаллический, кристалличность 20–35%` | 1 |
| `полиметилметакрилат [–CH2–C(CH3)(COOCH3)–]n (атактический) + бензотриазольный УФ-абсорбер (класс 2-(2H-бензотриазол-2-ил)-фенолов, ~0.2–1 масс.%) в объёме листа` | 1 |
| `Ti₃C₂Tx — карбид титана с поверхностными терминациями –O/–OH/–F (Tx)` | 1 |
| `двухкомпонентный ненаполненный эпоксидный адгезив EPO-TEK 301-2: эпоксидная смола Part A (SG 1.02) + отвердитель Part B (SG 0.89), пропорция 100:35 по массе; без наполнителей — оптически прозрачный` | 1 |
| `Полиамид 6/6 (PA66, нейлон 6/6): продукт поликонденсации гексаметилендиамина (6 C) и адипиновой кислоты (6 C), повторяющееся звено –[NH–(CH₂)₆–NH–OC–(CH₂)₄–CO]ₙ–; промышленные марки: Zytel 101 (DuPont), Ultramid A3K (BASF), Durethan A (Lanxess)` | 1 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 1 |
| `углеродное волокно Toray TORAYCA T1100G (PAN-based, intermediate modulus) ~60 об.% + эпоксидная матрица (система 3960, отверждение 177 °C) ~40 об.%` | 1 |
