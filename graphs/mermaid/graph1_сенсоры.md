# Граф 1 — подсистема «сенсоры»

```mermaid
graph LR
    izdelie_mems_imu[прочее]
    izdelie_event_cameras[прочее]
    izdelie_mwir_nbn_640[прочее]
    izdelie_sensora_volnovogo_fronta[прочее]
    izdelie_quantum_cascade_laser[прочее]
    izdelie_mwir_2[прочее]
    izdelie_multispektralnye_cmos_matritsy_s_ik_diapazonom[прочее]
    izdelie_metalinza[прочее]
    izdelie_poristyi_gazovyi_podshipnik_iz_sic[прочее]
    izdelie_akusticheskaya_linza[прочее]
    izdelie_dvs[прочее]
    izdelie_lwir_boson_1024[прочее]
    izdelie_tverdotelnyi_mmwave_radar[прочее]
    izdelie_iridium_sbd[прочее]
    izdelie_flir[прочее]
    izdelie_lidar[прочее]
    izdelie_pezo_sensor[прочее]
    izdelie_ads_b_priemnik[прочее]
    izdelie_lidar_robosense_ac1[прочее]
    izdelie_pezoelektricheskie_mems[прочее]
    izdelie_ultrakorotkoimpulsnye_lazery[прочее]
    izdelie_eo_ir_kamera[прочее]
    izdelie_cw_lazer[прочее]
    izdelie_kaskadnyi_stirling_kriokuler[прочее]
    izdelie_pmut[прочее]
    izdelie_ferritovye_klinya_na_kabelyah_sensorov[прочее]
    izdelie_flir_lwir_2[прочее]
    izdelie_pezo_mems[прочее]
    izdelie_aesa_radar[прочее]
    izdelie_starlink_mini[прочее]
    izdelie_ipg_yls_eco[прочее]
    izdelie_flir_boson_640[прочее]
    izdelie_mems_mikrofonov[прочее]
    часть_mems_imu_connectors[разъёмы]
    часть_mems_imu_core[основной_элемент]
    часть_mems_imu_housing[корпус]
    часть_mems_imu_mounting[крепёж]
    часть_event_cameras_housing[корпус]
    часть_event_cameras_mounting[крепёж]
    часть_event_cameras_core[основной_элемент]
    часть_event_cameras_connectors[разъёмы]
    часть_mwir_nbn_640_mounting[крепёж]
    часть_mwir_nbn_640_connectors[разъёмы]
    часть_mwir_nbn_640_housing[корпус]
    часть_mwir_nbn_640_core[основной_элемент]
    часть_sensora_volnovogo_fronta_connectors[разъёмы]
    часть_sensora_volnovogo_fronta_housing[корпус]
    часть_sensora_volnovogo_fronta_core[основной_элемент]
    часть_sensora_volnovogo_fronta_mounting[крепёж]
    часть_quantum_cascade_laser_mounting[крепёж]
    часть_quantum_cascade_laser_connectors[разъёмы]
    часть_quantum_cascade_laser_core[основной_элемент]
    часть_quantum_cascade_laser_housing[корпус]
    часть_mwir_2_connectors[разъёмы]
    часть_mwir_2_mounting[крепёж]
    часть_mwir_2_core[основной_элемент]
    часть_mwir_2_housing[корпус]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_housing[корпус]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_core[основной_элемент]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_mounting[крепёж]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_connectors[разъёмы]
    часть_metalinza_core[основной_элемент]
    часть_metalinza_mounting[крепёж]
    часть_metalinza_housing[корпус]
    часть_metalinza_connectors[разъёмы]
    часть_poristyi_gazovyi_podshipnik_iz_sic_housing[корпус]
    часть_poristyi_gazovyi_podshipnik_iz_sic_mounting[крепёж]
    часть_poristyi_gazovyi_podshipnik_iz_sic_core[основной_элемент]
    часть_poristyi_gazovyi_podshipnik_iz_sic_connectors[разъёмы]
    часть_akusticheskaya_linza_connectors[разъёмы]
    часть_akusticheskaya_linza_core[основной_элемент]
    часть_akusticheskaya_linza_housing[корпус]
    часть_akusticheskaya_linza_mounting[крепёж]
    часть_dvs_housing[корпус]
    часть_dvs_connectors[разъёмы]
    часть_dvs_mounting[крепёж]
    часть_dvs_core[основной_элемент]
    часть_lwir_boson_1024_core[основной_элемент]
    часть_lwir_boson_1024_connectors[разъёмы]
    часть_lwir_boson_1024_housing[корпус]
    часть_lwir_boson_1024_mounting[крепёж]
    часть_tverdotelnyi_mmwave_radar_mounting[крепёж]
    часть_tverdotelnyi_mmwave_radar_core[основной_элемент]
    часть_tverdotelnyi_mmwave_radar_housing[корпус]
    часть_tverdotelnyi_mmwave_radar_connectors[разъёмы]
    часть_iridium_sbd_mounting[крепёж]
    часть_iridium_sbd_housing[корпус]
    часть_iridium_sbd_connectors[разъёмы]
    часть_iridium_sbd_core[основной_элемент]
    часть_flir_mounting[крепёж]
    часть_flir_housing[корпус]
    часть_flir_connectors[разъёмы]
    часть_flir_core[основной_элемент]
    часть_lidar_mounting[крепёж]
    часть_lidar_connectors[разъёмы]
    часть_lidar_core[основной_элемент]
    часть_lidar_housing[корпус]
    часть_pezo_sensor_core[основной_элемент]
    часть_pezo_sensor_connectors[разъёмы]
    часть_pezo_sensor_housing[корпус]
    часть_pezo_sensor_mounting[крепёж]
    часть_ads_b_priemnik_core[основной_элемент]
    часть_ads_b_priemnik_connectors[разъёмы]
    часть_ads_b_priemnik_mounting[крепёж]
    часть_ads_b_priemnik_housing[корпус]
    часть_lidar_robosense_ac1_connectors[разъёмы]
    часть_lidar_robosense_ac1_mounting[крепёж]
    часть_lidar_robosense_ac1_housing[корпус]
    часть_lidar_robosense_ac1_core[основной_элемент]
    часть_pezoelektricheskie_mems_connectors[разъёмы]
    часть_pezoelektricheskie_mems_housing[корпус]
    часть_pezoelektricheskie_mems_core[основной_элемент]
    часть_pezoelektricheskie_mems_mounting[крепёж]
    часть_ultrakorotkoimpulsnye_lazery_mounting[крепёж]
    часть_ultrakorotkoimpulsnye_lazery_core[основной_элемент]
    часть_ultrakorotkoimpulsnye_lazery_housing[корпус]
    часть_ultrakorotkoimpulsnye_lazery_connectors[разъёмы]
    часть_eo_ir_kamera_core[основной_элемент]
    часть_eo_ir_kamera_connectors[разъёмы]
    часть_eo_ir_kamera_mounting[крепёж]
    часть_eo_ir_kamera_housing[корпус]
    часть_cw_lazer_core[основной_элемент]
    часть_cw_lazer_mounting[крепёж]
    часть_cw_lazer_housing[корпус]
    часть_cw_lazer_connectors[разъёмы]
    часть_kaskadnyi_stirling_kriokuler_connectors[разъёмы]
    часть_kaskadnyi_stirling_kriokuler_core[основной_элемент]
    часть_kaskadnyi_stirling_kriokuler_mounting[крепёж]
    часть_kaskadnyi_stirling_kriokuler_housing[корпус]
    часть_pmut_housing[корпус]
    часть_pmut_mounting[крепёж]
    часть_pmut_core[основной_элемент]
    часть_pmut_connectors[разъёмы]
    часть_ferritovye_klinya_na_kabelyah_sensorov_connectors[разъёмы]
    часть_ferritovye_klinya_na_kabelyah_sensorov_housing[корпус]
    часть_ferritovye_klinya_na_kabelyah_sensorov_core[основной_элемент]
    часть_ferritovye_klinya_na_kabelyah_sensorov_mounting[крепёж]
    часть_flir_lwir_2_mounting[крепёж]
    часть_flir_lwir_2_connectors[разъёмы]
    часть_flir_lwir_2_core[основной_элемент]
    часть_flir_lwir_2_housing[корпус]
    часть_pezo_mems_mounting[крепёж]
    часть_pezo_mems_connectors[разъёмы]
    часть_pezo_mems_housing[корпус]
    часть_pezo_mems_core[основной_элемент]
    часть_aesa_radar_housing[корпус]
    часть_aesa_radar_mounting[крепёж]
    часть_aesa_radar_core[основной_элемент]
    часть_aesa_radar_connectors[разъёмы]
    часть_starlink_mini_mounting[крепёж]
    часть_starlink_mini_connectors[разъёмы]
    часть_starlink_mini_core[основной_элемент]
    часть_starlink_mini_housing[корпус]
    часть_ipg_yls_eco_core[основной_элемент]
    часть_ipg_yls_eco_housing[корпус]
    часть_ipg_yls_eco_mounting[крепёж]
    часть_ipg_yls_eco_connectors[разъёмы]
    часть_flir_boson_640_housing[корпус]
    часть_flir_boson_640_mounting[крепёж]
    часть_flir_boson_640_core[основной_элемент]
    часть_flir_boson_640_connectors[разъёмы]
    часть_mems_mikrofonov_core[основной_элемент]
    часть_mems_mikrofonov_mounting[крепёж]
    часть_mems_mikrofonov_connectors[разъёмы]
    часть_mems_mikrofonov_housing[корпус]
    izdelie_zvukovaya_linza__ii[прочее]
    часть_hk_tank_сенсоры[radar_sensor]
    часть_t_x_сенсоры[optical_audio_array]
    часть_hk_aerial_сенсоры[multi_sensor_array]
    часть_t850_сенсоры[optical_audio_array]
    часть_cameron_сенсоры[optical_audio_array]
    часть_t800_аудио_сенсор[audio_microphone]
    часть_t800_оптический_сенсор_1[optical_camera]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aln[AlN]
    material_becu[Cu основа; Be 1.90–2.1…]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_magnitnaya_rezina_ferritovyi_poroshok[Fe₃O₄ (магнетит) 1–20 …]
    material_metapoverhnost[метаповерхность]
    material_monokristallicheskogo_sic[SiC — стехиометрически…]
    material_peek[PEEK — полиэфирэфиркет…]
    material_poliimid[Ароматический полиимид…]
    material_si[Si (кремний); электрон…]
    material_silikon_80_shore_a_steklyannye_mikrosfery[Матрица — сшитый VMQ-с…]
    material_ss_aisi_304[нержавеющая сталь AISI…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    izdelie_aesa_radar -->|материал| material_al_6061_t6
    часть_mems_imu_connectors -->|материал| material_poliimid
    часть_mems_imu_core -->|материал| material_si
    часть_mems_imu_housing -->|материал| material_al_6061_t6
    часть_mems_imu_mounting -->|материал| material_al_6061_t6
    часть_event_cameras_housing -->|материал| material_al_6061_t6
    часть_event_cameras_mounting -->|материал| material_al_6061_t6
    часть_event_cameras_core -->|материал| material_al_6061_t6
    часть_event_cameras_connectors -->|материал| material_becu
    часть_mwir_nbn_640_mounting -->|материал| material_al_6061_t6
    часть_mwir_nbn_640_connectors -->|материал| material_becu
    часть_mwir_nbn_640_housing -->|материал| material_al_6061_t6
    часть_mwir_nbn_640_core -->|материал| material_al_6061_t6
    часть_sensora_volnovogo_fronta_connectors -->|материал| material_latun_c36000
    часть_sensora_volnovogo_fronta_housing -->|материал| material_al_6061_t6
    часть_sensora_volnovogo_fronta_core -->|материал| material_al_6061_t6
    часть_sensora_volnovogo_fronta_mounting -->|материал| material_al_6061_t6
    часть_quantum_cascade_laser_mounting -->|материал| material_becu
    часть_quantum_cascade_laser_connectors -->|материал| material_latun_c36000
    часть_quantum_cascade_laser_core -->|материал| material_al_6061_t6
    часть_quantum_cascade_laser_housing -->|материал| material_al_6061_t6
    часть_mwir_2_connectors -->|материал| material_becu
    часть_mwir_2_mounting -->|материал| material_ti_6al_4v
    часть_mwir_2_core -->|материал| material_al_6061_t6
    часть_mwir_2_housing -->|материал| material_al_6061_t6
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_housing -->|материал| material_al_6061_t6
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_core -->|материал| material_al_6061_t6
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_mounting -->|материал| material_al_6061_t6
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_connectors -->|материал| material_poliimid
    часть_metalinza_core -->|материал| material_metapoverhnost
    часть_metalinza_mounting -->|материал| material_al_6061_t6
    часть_metalinza_housing -->|материал| material_al_6061_t6
    часть_metalinza_connectors -->|материал| material_poliimid
    часть_poristyi_gazovyi_podshipnik_iz_sic_housing -->|материал| material_al_6061_t6
    часть_poristyi_gazovyi_podshipnik_iz_sic_mounting -->|материал| material_ss_aisi_304
    часть_poristyi_gazovyi_podshipnik_iz_sic_core -->|материал| material_monokristallicheskogo_sic
    часть_poristyi_gazovyi_podshipnik_iz_sic_connectors -->|материал| material_al_6061_t6
    часть_akusticheskaya_linza_connectors -->|материал| material_latun_c36000
    часть_akusticheskaya_linza_core -->|материал| material_silikon_80_shore_a_steklyannye_mikrosfery
    часть_akusticheskaya_linza_housing -->|материал| material_al_6061_t6
    часть_akusticheskaya_linza_mounting -->|материал| material_al_6061_t6
    часть_dvs_housing -->|материал| material_al_6061_t6
    часть_dvs_connectors -->|материал| material_latun_c36000
    часть_dvs_mounting -->|материал| material_al_6061_t6
    часть_dvs_core -->|материал| material_al_6061_t6
    часть_lwir_boson_1024_core -->|материал| material_al_6061_t6
    часть_lwir_boson_1024_connectors -->|материал| material_becu
    часть_lwir_boson_1024_housing -->|материал| material_al_6061_t6
    часть_lwir_boson_1024_mounting -->|материал| material_ti_6al_4v
    часть_tverdotelnyi_mmwave_radar_mounting -->|материал| material_al_6061_t6
    часть_tverdotelnyi_mmwave_radar_core -->|материал| material_al_6061_t6
    часть_tverdotelnyi_mmwave_radar_housing -->|материал| material_al_6061_t6
    часть_tverdotelnyi_mmwave_radar_connectors -->|материал| material_latun_c36000
    часть_iridium_sbd_mounting -->|материал| material_al_6061_t6
    часть_iridium_sbd_housing -->|материал| material_al_6061_t6
    часть_iridium_sbd_connectors -->|материал| material_latun_c36000
    часть_iridium_sbd_core -->|материал| material_al_6061_t6
    часть_flir_mounting -->|материал| material_al_6061_t6
    часть_flir_housing -->|материал| material_al_6061_t6
    часть_flir_connectors -->|материал| material_latun_c36000
    часть_flir_core -->|материал| material_si
    часть_lidar_mounting -->|материал| material_al_6061_t6
    часть_lidar_connectors -->|материал| material_latun_c36000
    часть_lidar_core -->|материал| material_al_6061_t6
    часть_lidar_housing -->|материал| material_al_6061_t6
    часть_pezo_sensor_core -->|материал| material_aln
    часть_pezo_sensor_connectors -->|материал| material_stal_st3
    часть_pezo_sensor_housing -->|материал| material_al_6061_t6
    часть_pezo_sensor_mounting -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_core -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_connectors -->|материал| material_latun_c36000
    часть_ads_b_priemnik_mounting -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_housing -->|материал| material_al_6061_t6
    часть_lidar_robosense_ac1_connectors -->|материал| material_latun_c36000
    часть_lidar_robosense_ac1_mounting -->|материал| material_al_6061_t6
    часть_lidar_robosense_ac1_housing -->|материал| material_al_6061_t6
    часть_lidar_robosense_ac1_core -->|материал| material_al_6061_t6
    часть_pezoelektricheskie_mems_connectors -->|материал| material_latun_c36000
    часть_pezoelektricheskie_mems_housing -->|материал| material_al_6061_t6
    часть_pezoelektricheskie_mems_core -->|материал| material_aln
    часть_pezoelektricheskie_mems_mounting -->|материал| material_al_6061_t6
    часть_ultrakorotkoimpulsnye_lazery_mounting -->|материал| material_al_6061_t6
    часть_ultrakorotkoimpulsnye_lazery_core -->|материал| material_al_6061_t6
    часть_ultrakorotkoimpulsnye_lazery_housing -->|материал| material_stal_st3
    часть_ultrakorotkoimpulsnye_lazery_connectors -->|материал| material_latun_c36000
    часть_eo_ir_kamera_core -->|материал| material_al_6061_t6
    часть_eo_ir_kamera_connectors -->|материал| material_latun_c36000
    часть_eo_ir_kamera_mounting -->|материал| material_al_6061_t6
    часть_eo_ir_kamera_housing -->|материал| material_al_6061_t6
    часть_cw_lazer_core -->|материал| material_al_6061_t6
    часть_cw_lazer_mounting -->|материал| material_al_6061_t6
    часть_cw_lazer_housing -->|материал| material_al_6061_t6
    часть_cw_lazer_connectors -->|материал| material_al_6061_t6
    часть_kaskadnyi_stirling_kriokuler_connectors -->|материал| material_becu
    часть_kaskadnyi_stirling_kriokuler_core -->|материал| material_al_6061_t6
    часть_kaskadnyi_stirling_kriokuler_mounting -->|материал| material_stal_st3
    часть_kaskadnyi_stirling_kriokuler_housing -->|материал| material_stal_st3
    часть_pmut_housing -->|материал| material_al_6061_t6
    часть_pmut_mounting -->|материал| material_ss_aisi_304
    часть_pmut_core -->|материал| material_aln
    часть_pmut_connectors -->|материал| material_latun_c36000
    часть_ferritovye_klinya_na_kabelyah_sensorov_connectors -->|материал| material_stal_st3
    часть_ferritovye_klinya_na_kabelyah_sensorov_housing -->|материал| material_al_6061_t6
    часть_ferritovye_klinya_na_kabelyah_sensorov_core -->|материал| material_magnitnaya_rezina_ferritovyi_poroshok
    часть_ferritovye_klinya_na_kabelyah_sensorov_mounting -->|материал| material_peek
    часть_flir_lwir_2_mounting -->|материал| material_al_6061_t6
    часть_flir_lwir_2_connectors -->|материал| material_becu
    часть_flir_lwir_2_core -->|материал| material_al_6061_t6
    часть_flir_lwir_2_housing -->|материал| material_al_6061_t6
    часть_pezo_mems_mounting -->|материал| material_ss_aisi_304
    часть_pezo_mems_connectors -->|материал| material_latun_c36000
    часть_pezo_mems_housing -->|материал| material_al_6061_t6
    часть_pezo_mems_core -->|материал| material_aln
    часть_aesa_radar_housing -->|материал| material_al_6061_t6
    часть_aesa_radar_mounting -->|материал| material_al_6061_t6
    часть_aesa_radar_core -->|материал| material_al_6061_t6
    часть_aesa_radar_connectors -->|материал| material_latun_c36000
    часть_starlink_mini_mounting -->|материал| material_ss_aisi_304
    часть_starlink_mini_connectors -->|материал| material_latun_c36000
    часть_starlink_mini_core -->|материал| material_al_6061_t6
    часть_starlink_mini_housing -->|материал| material_al_6061_t6
    часть_ipg_yls_eco_core -->|материал| material_stal_st3
    часть_ipg_yls_eco_housing -->|материал| material_stal_st3
    часть_ipg_yls_eco_mounting -->|материал| material_stal_st3
    часть_ipg_yls_eco_connectors -->|материал| material_al_6061_t6
    часть_flir_boson_640_housing -->|материал| material_al_6061_t6
    часть_flir_boson_640_mounting -->|материал| material_al_6061_t6
    часть_flir_boson_640_core -->|материал| material_al_6061_t6
    часть_flir_boson_640_connectors -->|материал| material_becu
    часть_mems_mikrofonov_core -->|материал| material_si
    часть_mems_mikrofonov_mounting -->|материал| material_al_6061_t6
    часть_mems_mikrofonov_connectors -->|материал| material_poliimid
    часть_mems_mikrofonov_housing -->|материал| material_al_6061_t6
    часть_t_x_сенсоры -->|материал| material_ti_6al_4v
    часть_hk_aerial_сенсоры -->|материал| material_al_6061_t6
    часть_t850_сенсоры -->|материал| material_ti_6al_4v
    часть_cameron_сенсоры -->|материал| material_poliimid
    часть_t800_аудио_сенсор -->|материал| material_si
    часть_t800_оптический_сенсор_1 -->|материал| material_si
```

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 79 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 17 |
| `Cu основа; Be 1.90–2.15 %; Co 0.20–0.60 % (сумма Co+Ni ≥ 0.20 %) — термообрабатываемый сплав C17200 (Alloy 25, CuBe2, UNS C17200 / EN CW101C)` | 8 |
| `Ст3сп/Ст3пс (ГОСТ 380-2005): C 0.14–0.22 %, Si 0.15–0.30 %, Mn 0.40–0.65 %, Cr/Ni/Cu ≤0.30 %, Fe ост.` | 8 |
| `Ароматический полиимид PMDA-ODA (тип Kapton): повторяющееся звено C22H10N2O5 (M ≈ 382.2 г/моль) из пиромеллитового диангидрида (PMDA) и 4,4′-оксианилина (ODA); чередующиеся имидные циклы C(=O)–N–C(=O) и фениленовые/дифениловый эфирный сегменты` | 5 |
| `Si (кремний); электронный сорт ≥99.9999999% (9N) для подложек ИС, солнечный ≥99.9999% (6N), металлургический ~98–99% (Si-Fe, Si-Ca примеси)` | 5 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 4 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 4 |
| `AlN` | 4 |
| `метаповерхность` | 1 |
| `SiC — стехиометрический карбид кремния (50 ат.% Si / 50 ат.% C); монокристалл 4H-SiC, n-легирование азотом (подложки) или высокочистый без легирования` | 1 |
| `Матрица — сшитый VMQ-силикон твёрдостью 80 Shore A (PDMS, –[Si(CH₃)₂–O]ₙ–, пероксидная/платиновая сшивка); наполнитель — полые стеклянные микросферы (содово-известково-боросиликатное стекло) 10–40 мас.% (~20–50 об.%): типовые марки 3M iM16K (ρ 0.46 г/см³, прочность смятия 110 МПа, d50 ~20 мкм), K25 (0.25 г/см³, 5.2 МПа), S-серия (до 0.60 г/см³)` | 1 |
| `Fe₃O₄ (магнетит) 1–20 wt% + силиконовый каучук (Ecoflex/PDMS)` | 1 |
| `PEEK — полиэфирэфиркетон (PAEK): повторяющееся звено (C19H12O3)n, M = 288.3 г/моль; синтез из 4,4′-дифторбензофенона и динатриевой соли гидрохинона в дифенилсульфоне при ~300 °C` | 1 |
