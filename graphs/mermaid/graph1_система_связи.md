# Граф 1 — подсистема «система_связи»

```mermaid
graph LR
    izdelie_iridium_sbd[прочее]
    izdelie_optovolokonnaya_shina[прочее]
    izdelie_razryvnye_mufty_iso_16028[прочее]
    izdelie_flat_face_couplings_iso_16028[прочее]
    izdelie_starlink_mini[прочее]
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr[прочее]
    izdelie_usb_c[прочее]
    izdelie_obd_ii[прочее]
    часть_iridium_sbd_housing[корпус]
    часть_iridium_sbd_mounting[крепёж]
    часть_iridium_sbd_core[основной_элемент]
    часть_iridium_sbd_connectors[разъёмы]
    часть_optovolokonnaya_shina_core[основной_элемент]
    часть_optovolokonnaya_shina_housing[корпус]
    часть_optovolokonnaya_shina_mounting[крепёж]
    часть_optovolokonnaya_shina_connectors[разъёмы]
    часть_razryvnye_mufty_iso_16028_connectors[разъёмы]
    часть_razryvnye_mufty_iso_16028_mounting[крепёж]
    часть_razryvnye_mufty_iso_16028_core[основной_элемент]
    часть_razryvnye_mufty_iso_16028_housing[корпус]
    часть_flat_face_couplings_iso_16028_mounting[крепёж]
    часть_flat_face_couplings_iso_16028_housing[корпус]
    часть_flat_face_couplings_iso_16028_core[основной_элемент]
    часть_flat_face_couplings_iso_16028_connectors[разъёмы]
    часть_starlink_mini_housing[корпус]
    часть_starlink_mini_core[основной_элемент]
    часть_starlink_mini_mounting[крепёж]
    часть_starlink_mini_connectors[разъёмы]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_connectors[разъёмы]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_core[основной_элемент]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_housing[корпус]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_mounting[крепёж]
    часть_usb_c_connectors[разъёмы]
    часть_usb_c_housing[корпус]
    часть_usb_c_core[основной_элемент]
    часть_usb_c_mounting[крепёж]
    часть_obd_ii_connectors[разъёмы]
    часть_obd_ii_housing[корпус]
    часть_obd_ii_core[основной_элемент]
    часть_obd_ii_mounting[крепёж]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_becu[Cu основа; Be 1.90–2.1…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_peek[PEEK — полиэфирэфиркет…]
    material_ss_aisi_304[нержавеющая сталь AISI…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    izdelie_iridium_sbd -->|материал| material_al_6061_t6
    izdelie_iridium_sbd -->|материал| material_aluminum
    izdelie_razryvnye_mufty_iso_16028 -->|материал| material_stal_st3
    izdelie_razryvnye_mufty_iso_16028 -->|материал| material_al_6061_t6
    izdelie_flat_face_couplings_iso_16028 -->|материал| material_stal_st3
    izdelie_flat_face_couplings_iso_16028 -->|материал| material_aluminum
    izdelie_obd_ii -->|материал| material_peek
    izdelie_obd_ii -->|материал| material_aluminum
    часть_iridium_sbd_housing -->|материал| material_al_6061_t6
    часть_iridium_sbd_mounting -->|материал| material_al_6061_t6
    часть_iridium_sbd_core -->|материал| material_al_6061_t6
    часть_iridium_sbd_connectors -->|материал| material_latun_c36000
    часть_razryvnye_mufty_iso_16028_connectors -->|материал| material_latun_c36000
    часть_razryvnye_mufty_iso_16028_mounting -->|материал| material_al_6061_t6
    часть_razryvnye_mufty_iso_16028_core -->|материал| material_stal_st3
    часть_razryvnye_mufty_iso_16028_housing -->|материал| material_al_6061_t6
    часть_flat_face_couplings_iso_16028_mounting -->|материал| material_stal_st3
    часть_flat_face_couplings_iso_16028_housing -->|материал| material_al_6061_t6
    часть_flat_face_couplings_iso_16028_core -->|материал| material_stal_st3
    часть_flat_face_couplings_iso_16028_connectors -->|материал| material_latun_c36000
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_connectors -->|материал| material_becu
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_mounting -->|материал| material_ss_aisi_304
    часть_obd_ii_connectors -->|материал| material_stal_st3
    часть_obd_ii_housing -->|материал| material_al_6061_t6
    часть_obd_ii_core -->|материал| material_peek
    часть_obd_ii_mounting -->|материал| material_al_6061_t6
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 10 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 6 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 3 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 3 |
| `PEEK — полиэфирэфиркетон (PAEK): повторяющееся звено (C19H12O3)n, M = 288.3 г/моль; синтез из 4,4′-дифторбензофенона и динатриевой соли гидрохинона в дифенилсульфоне при ~300 °C` | 2 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 1 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 1 |
