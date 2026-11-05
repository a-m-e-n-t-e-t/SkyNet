# Граф 1 — подсистема «система_связи»

```mermaid
graph LR
    часть_hk_aerial_связь[skynet_link]
    часть_hk_tank_связь[skynet_link]
    часть_t850_связь[skyet_link]
    часть_t800_антенна[skyet_link_antenna]
    izdelie_stm32h743[прочее]
    izdelie_optovolokonnaya_shina[прочее]
    izdelie_usb_c[прочее]
    izdelie_radiatsionno_stoikii_neiromorfnyi_tmr[прочее]
    izdelie_flat_face_couplings_iso_16028[прочее]
    izdelie_stm32[прочее]
    izdelie_obd_ii[прочее]
    izdelie_razryvnye_mufty_iso_16028[прочее]
    часть_stm32h743_housing[корпус]
    часть_stm32h743_mounting[крепёж]
    часть_stm32h743_core[основной_элемент]
    часть_stm32h743_connectors[разъёмы]
    часть_optovolokonnaya_shina_connectors[разъёмы]
    часть_optovolokonnaya_shina_mounting[крепёж]
    часть_optovolokonnaya_shina_core[основной_элемент]
    часть_optovolokonnaya_shina_housing[корпус]
    часть_usb_c_connectors[разъёмы]
    часть_usb_c_housing[корпус]
    часть_usb_c_core[основной_элемент]
    часть_usb_c_mounting[крепёж]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_mounting[крепёж]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_core[основной_элемент]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_housing[корпус]
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_connectors[разъёмы]
    часть_flat_face_couplings_iso_16028_core[основной_элемент]
    часть_flat_face_couplings_iso_16028_mounting[крепёж]
    часть_flat_face_couplings_iso_16028_housing[корпус]
    часть_flat_face_couplings_iso_16028_connectors[разъёмы]
    часть_stm32_mounting[крепёж]
    часть_stm32_connectors[разъёмы]
    часть_stm32_housing[корпус]
    часть_stm32_core[основной_элемент]
    часть_obd_ii_core[основной_элемент]
    часть_obd_ii_connectors[разъёмы]
    часть_obd_ii_housing[корпус]
    часть_obd_ii_mounting[крепёж]
    часть_razryvnye_mufty_iso_16028_core[основной_элемент]
    часть_razryvnye_mufty_iso_16028_housing[корпус]
    часть_razryvnye_mufty_iso_16028_mounting[крепёж]
    часть_razryvnye_mufty_iso_16028_connectors[разъёмы]
    material_al_6061_t6[Al 6061-T6]
    material_becu[BeCu]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_peek[PEEK]
    material_poliimid[Полиимид]
    material_si[Si]
    material_stal_st3[Сталь Ст3]
    material_ti_6al_4v[Ti-6Al-4V]
    часть_hk_aerial_связь -->|материал| material_ti_6al_4v
    часть_t850_связь -->|материал| material_al_6061_t6
    часть_t800_антенна -->|материал| material_poliimid
    часть_stm32h743_housing -->|материал| material_al_6061_t6
    часть_stm32h743_mounting -->|материал| material_ti_6al_4v
    часть_stm32h743_core -->|материал| material_si
    часть_stm32h743_connectors -->|материал| material_becu
    часть_optovolokonnaya_shina_connectors -->|материал| material_poliimid
    часть_optovolokonnaya_shina_mounting -->|материал| material_ti_6al_4v
    часть_optovolokonnaya_shina_core -->|материал| material_al_6061_t6
    часть_optovolokonnaya_shina_housing -->|материал| material_al_6061_t6
    часть_usb_c_connectors -->|материал| material_latun_c36000
    часть_usb_c_housing -->|материал| material_al_6061_t6
    часть_usb_c_core -->|материал| material_becu
    часть_usb_c_mounting -->|материал| material_ti_6al_4v
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_mounting -->|материал| material_ti_6al_4v
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_core -->|материал| material_si
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_housing -->|материал| material_al_6061_t6
    часть_radiatsionno_stoikii_neiromorfnyi_tmr_connectors -->|материал| material_becu
    часть_flat_face_couplings_iso_16028_core -->|материал| material_stal_st3
    часть_flat_face_couplings_iso_16028_mounting -->|материал| material_ti_6al_4v
    часть_flat_face_couplings_iso_16028_housing -->|материал| material_al_6061_t6
    часть_flat_face_couplings_iso_16028_connectors -->|материал| material_latun_c36000
    часть_stm32_mounting -->|материал| material_ti_6al_4v
    часть_stm32_connectors -->|материал| material_stal_st3
    часть_stm32_housing -->|материал| material_al_6061_t6
    часть_stm32_core -->|материал| material_si
    часть_obd_ii_core -->|материал| material_peek
    часть_obd_ii_connectors -->|материал| material_stal_st3
    часть_obd_ii_housing -->|материал| material_al_6061_t6
    часть_obd_ii_mounting -->|материал| material_ti_6al_4v
    часть_razryvnye_mufty_iso_16028_core -->|материал| material_stal_st3
    часть_razryvnye_mufty_iso_16028_housing -->|материал| material_al_6061_t6
    часть_razryvnye_mufty_iso_16028_mounting -->|материал| material_ti_6al_4v
    часть_razryvnye_mufty_iso_16028_connectors -->|материал| material_latun_c36000
```

| Материал | Используется в частях |
|---|---:|
| `Al 6061-T6` | 10 |
| `Ti-6Al-4V` | 9 |
| `Сталь Ст3` | 4 |
| `Si` | 3 |
| `BeCu` | 3 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 3 |
| `Полиимид` | 2 |
| `PEEK` | 1 |
