# Граф 1 — подсистема «сенсоры»

```mermaid
graph LR
    часть_cameron_сенсоры[optical_audio_array]
    часть_hk_aerial_сенсоры[multi_sensor_array]
    часть_hk_tank_сенсоры[radar_sensor]
    часть_t_x_сенсоры[optical_audio_array]
    часть_t800_оптический_сенсор_1[optical_camera]
    часть_t800_оптический_сенсор_2[optical_camera]
    часть_t800_аудио_сенсор[audio_microphone]
    часть_t850_сенсоры[optical_audio_array]
    izdelie_ipg_yls_eco[прочее]
    izdelie_ferritovye_klinya_na_kabelyah_sensorov[прочее]
    izdelie_sensora_volnovogo_fronta[прочее]
    izdelie_dvs[прочее]
    izdelie_eo_ir_kamera[прочее]
    izdelie_kaskadnyi_stirling_kriokuler[прочее]
    izdelie_iridium_sbd[прочее]
    izdelie_ads_b_priemnik[прочее]
    izdelie_metalinza[прочее]
    izdelie_pezoelektricheskie_mems[прочее]
    izdelie_mwir_2[прочее]
    izdelie_lwir_boson_1024[прочее]
    izdelie_poristyi_gazovyi_podshipnik_iz_sic[прочее]
    izdelie_quantum_cascade_laser[прочее]
    izdelie_lidar_robosense_ac1[прочее]
    izdelie_aesa_radar[прочее]
    izdelie_lidar[прочее]
    izdelie_multispektralnye_cmos_matritsy_s_ik_diapazonom[прочее]
    izdelie_flir_boson_640[прочее]
    izdelie_pezo_sensor[прочее]
    izdelie_ultrakorotkoimpulsnye_lazery[прочее]
    izdelie_tverdotelnyi_mmwave_radar[прочее]
    izdelie_mems_imu[прочее]
    izdelie_akusticheskaya_linza[прочее]
    izdelie_flir[прочее]
    izdelie_starlink_mini[прочее]
    izdelie_event_cameras[прочее]
    izdelie_mwir_nbn_640[прочее]
    izdelie_pmut[прочее]
    izdelie_pezo_mems[прочее]
    izdelie_mems_mikrofonov[прочее]
    izdelie_cw_lazer[прочее]
    izdelie_flir_lwir_2[прочее]
    часть_ipg_yls_eco_housing[корпус]
    часть_ipg_yls_eco_core[основной_элемент]
    часть_ipg_yls_eco_connectors[разъёмы]
    часть_ipg_yls_eco_mounting[крепёж]
    часть_ferritovye_klinya_na_kabelyah_sensorov_connectors[разъёмы]
    часть_ferritovye_klinya_na_kabelyah_sensorov_core[основной_элемент]
    часть_ferritovye_klinya_na_kabelyah_sensorov_housing[корпус]
    часть_ferritovye_klinya_na_kabelyah_sensorov_mounting[крепёж]
    часть_sensora_volnovogo_fronta_connectors[разъёмы]
    часть_sensora_volnovogo_fronta_core[основной_элемент]
    часть_sensora_volnovogo_fronta_housing[корпус]
    часть_sensora_volnovogo_fronta_mounting[крепёж]
    часть_dvs_core[основной_элемент]
    часть_dvs_housing[корпус]
    часть_dvs_connectors[разъёмы]
    часть_dvs_mounting[крепёж]
    часть_eo_ir_kamera_housing[корпус]
    часть_eo_ir_kamera_core[основной_элемент]
    часть_eo_ir_kamera_connectors[разъёмы]
    часть_eo_ir_kamera_mounting[крепёж]
    часть_kaskadnyi_stirling_kriokuler_core[основной_элемент]
    часть_kaskadnyi_stirling_kriokuler_housing[корпус]
    часть_kaskadnyi_stirling_kriokuler_mounting[крепёж]
    часть_kaskadnyi_stirling_kriokuler_connectors[разъёмы]
    часть_iridium_sbd_housing[корпус]
    часть_iridium_sbd_core[основной_элемент]
    часть_iridium_sbd_mounting[крепёж]
    часть_iridium_sbd_connectors[разъёмы]
    часть_ads_b_priemnik_mounting[крепёж]
    часть_ads_b_priemnik_connectors[разъёмы]
    часть_ads_b_priemnik_core[основной_элемент]
    часть_ads_b_priemnik_housing[корпус]
    часть_metalinza_mounting[крепёж]
    часть_metalinza_core[основной_элемент]
    часть_metalinza_connectors[разъёмы]
    часть_metalinza_housing[корпус]
    часть_pezoelektricheskie_mems_connectors[разъёмы]
    часть_pezoelektricheskie_mems_core[основной_элемент]
    часть_pezoelektricheskie_mems_housing[корпус]
    часть_pezoelektricheskie_mems_mounting[крепёж]
    часть_mwir_2_core[основной_элемент]
    часть_mwir_2_housing[корпус]
    часть_mwir_2_connectors[разъёмы]
    часть_mwir_2_mounting[крепёж]
    часть_lwir_boson_1024_core[основной_элемент]
    часть_lwir_boson_1024_housing[корпус]
    часть_lwir_boson_1024_mounting[крепёж]
    часть_lwir_boson_1024_connectors[разъёмы]
    часть_poristyi_gazovyi_podshipnik_iz_sic_core[основной_элемент]
    часть_poristyi_gazovyi_podshipnik_iz_sic_housing[корпус]
    часть_poristyi_gazovyi_podshipnik_iz_sic_connectors[разъёмы]
    часть_poristyi_gazovyi_podshipnik_iz_sic_mounting[крепёж]
    часть_quantum_cascade_laser_mounting[крепёж]
    часть_quantum_cascade_laser_connectors[разъёмы]
    часть_quantum_cascade_laser_core[основной_элемент]
    часть_quantum_cascade_laser_housing[корпус]
    часть_lidar_robosense_ac1_housing[корпус]
    часть_lidar_robosense_ac1_core[основной_элемент]
    часть_lidar_robosense_ac1_connectors[разъёмы]
    часть_lidar_robosense_ac1_mounting[крепёж]
    часть_aesa_radar_connectors[разъёмы]
    часть_aesa_radar_housing[корпус]
    часть_aesa_radar_core[основной_элемент]
    часть_aesa_radar_mounting[крепёж]
    часть_lidar_housing[корпус]
    часть_lidar_mounting[крепёж]
    часть_lidar_core[основной_элемент]
    часть_lidar_connectors[разъёмы]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_connectors[разъёмы]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_housing[корпус]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_mounting[крепёж]
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_core[основной_элемент]
    часть_flir_boson_640_core[основной_элемент]
    часть_flir_boson_640_connectors[разъёмы]
    часть_flir_boson_640_mounting[крепёж]
    часть_flir_boson_640_housing[корпус]
    часть_pezo_sensor_connectors[разъёмы]
    часть_pezo_sensor_core[основной_элемент]
    часть_pezo_sensor_housing[корпус]
    часть_pezo_sensor_mounting[крепёж]
    часть_ultrakorotkoimpulsnye_lazery_core[основной_элемент]
    часть_ultrakorotkoimpulsnye_lazery_mounting[крепёж]
    часть_ultrakorotkoimpulsnye_lazery_housing[корпус]
    часть_ultrakorotkoimpulsnye_lazery_connectors[разъёмы]
    часть_tverdotelnyi_mmwave_radar_connectors[разъёмы]
    часть_tverdotelnyi_mmwave_radar_mounting[крепёж]
    часть_tverdotelnyi_mmwave_radar_core[основной_элемент]
    часть_tverdotelnyi_mmwave_radar_housing[корпус]
    часть_mems_imu_mounting[крепёж]
    часть_mems_imu_connectors[разъёмы]
    часть_mems_imu_core[основной_элемент]
    часть_mems_imu_housing[корпус]
    часть_akusticheskaya_linza_housing[корпус]
    часть_akusticheskaya_linza_mounting[крепёж]
    часть_akusticheskaya_linza_core[основной_элемент]
    часть_akusticheskaya_linza_connectors[разъёмы]
    часть_flir_core[основной_элемент]
    часть_flir_connectors[разъёмы]
    часть_flir_mounting[крепёж]
    часть_flir_housing[корпус]
    часть_starlink_mini_mounting[крепёж]
    часть_starlink_mini_connectors[разъёмы]
    часть_starlink_mini_housing[корпус]
    часть_starlink_mini_core[основной_элемент]
    часть_event_cameras_mounting[крепёж]
    часть_event_cameras_core[основной_элемент]
    часть_event_cameras_connectors[разъёмы]
    часть_event_cameras_housing[корпус]
    часть_mwir_nbn_640_mounting[крепёж]
    часть_mwir_nbn_640_connectors[разъёмы]
    часть_mwir_nbn_640_housing[корпус]
    часть_mwir_nbn_640_core[основной_элемент]
    часть_pmut_mounting[крепёж]
    часть_pmut_connectors[разъёмы]
    часть_pmut_housing[корпус]
    часть_pmut_core[основной_элемент]
    часть_pezo_mems_core[основной_элемент]
    часть_pezo_mems_mounting[крепёж]
    часть_pezo_mems_connectors[разъёмы]
    часть_pezo_mems_housing[корпус]
    часть_mems_mikrofonov_mounting[крепёж]
    часть_mems_mikrofonov_connectors[разъёмы]
    часть_mems_mikrofonov_housing[корпус]
    часть_mems_mikrofonov_core[основной_элемент]
    часть_cw_lazer_core[основной_элемент]
    часть_cw_lazer_housing[корпус]
    часть_cw_lazer_connectors[разъёмы]
    часть_cw_lazer_mounting[крепёж]
    часть_flir_lwir_2_housing[корпус]
    часть_flir_lwir_2_connectors[разъёмы]
    часть_flir_lwir_2_mounting[крепёж]
    часть_flir_lwir_2_core[основной_элемент]
    material_al_6061_t6[Al 6061-T6]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_si[Si]
    material_ti_6al_4v[Ti-6Al-4V]
    часть_cameron_сенсоры -->|материал| material_ti_6al_4v
    часть_hk_aerial_сенсоры -->|материал| material_al_6061_t6
    часть_hk_tank_сенсоры -->|материал| material_ti_6al_4v
    часть_t_x_сенсоры -->|материал| material_ti_6al_4v
    часть_t800_оптический_сенсор_1 -->|материал| material_si
    часть_t800_оптический_сенсор_2 -->|материал| material_si
    часть_t800_аудио_сенсор -->|материал| material_ti_6al_4v
    часть_t850_сенсоры -->|материал| material_ti_6al_4v
    izdelie_ipg_yls_eco -->|материал| material_generic_material
    izdelie_ipg_yls_eco -->|материал| material_aluminum
    izdelie_ferritovye_klinya_na_kabelyah_sensorov -->|материал| material_generic_material
    izdelie_ferritovye_klinya_na_kabelyah_sensorov -->|материал| material_aluminum
    izdelie_sensora_volnovogo_fronta -->|материал| material_generic_material
    izdelie_sensora_volnovogo_fronta -->|материал| material_aluminum
    izdelie_dvs -->|материал| material_generic_material
    izdelie_dvs -->|материал| material_aluminum
    izdelie_eo_ir_kamera -->|материал| material_generic_material
    izdelie_eo_ir_kamera -->|материал| material_aluminum
    izdelie_kaskadnyi_stirling_kriokuler -->|материал| material_generic_material
    izdelie_kaskadnyi_stirling_kriokuler -->|материал| material_aluminum
    izdelie_iridium_sbd -->|материал| material_generic_material
    izdelie_iridium_sbd -->|материал| material_aluminum
    izdelie_ads_b_priemnik -->|материал| material_generic_material
    izdelie_ads_b_priemnik -->|материал| material_aluminum
    izdelie_metalinza -->|материал| material_generic_material
    izdelie_metalinza -->|материал| material_aluminum
    izdelie_pezoelektricheskie_mems -->|материал| material_generic_material
    izdelie_pezoelektricheskie_mems -->|материал| material_aluminum
    izdelie_mwir_2 -->|материал| material_generic_material
    izdelie_mwir_2 -->|материал| material_aluminum
    izdelie_lwir_boson_1024 -->|материал| material_generic_material
    izdelie_lwir_boson_1024 -->|материал| material_aluminum
    izdelie_poristyi_gazovyi_podshipnik_iz_sic -->|материал| material_generic_material
    izdelie_poristyi_gazovyi_podshipnik_iz_sic -->|материал| material_aluminum
    izdelie_quantum_cascade_laser -->|материал| material_generic_material
    izdelie_quantum_cascade_laser -->|материал| material_aluminum
    izdelie_lidar_robosense_ac1 -->|материал| material_generic_material
    izdelie_lidar_robosense_ac1 -->|материал| material_aluminum
    izdelie_aesa_radar -->|материал| material_generic_material
    izdelie_aesa_radar -->|материал| material_al_6061_t6
    izdelie_lidar -->|материал| material_generic_material
    izdelie_lidar -->|материал| material_aluminum
    izdelie_multispektralnye_cmos_matritsy_s_ik_diapazonom -->|материал| material_generic_material
    izdelie_multispektralnye_cmos_matritsy_s_ik_diapazonom -->|материал| material_aluminum
    izdelie_flir_boson_640 -->|материал| material_generic_material
    izdelie_flir_boson_640 -->|материал| material_aluminum
    izdelie_pezo_sensor -->|материал| material_generic_material
    izdelie_pezo_sensor -->|материал| material_aluminum
    izdelie_ultrakorotkoimpulsnye_lazery -->|материал| material_generic_material
    izdelie_ultrakorotkoimpulsnye_lazery -->|материал| material_aluminum
    izdelie_tverdotelnyi_mmwave_radar -->|материал| material_generic_material
    izdelie_tverdotelnyi_mmwave_radar -->|материал| material_aluminum
    izdelie_mems_imu -->|материал| material_generic_material
    izdelie_mems_imu -->|материал| material_aluminum
    izdelie_akusticheskaya_linza -->|материал| material_generic_material
    izdelie_akusticheskaya_linza -->|материал| material_aluminum
    izdelie_flir -->|материал| material_generic_material
    izdelie_flir -->|материал| material_aluminum
    izdelie_starlink_mini -->|материал| material_generic_material
    izdelie_starlink_mini -->|материал| material_aluminum
    izdelie_event_cameras -->|материал| material_generic_material
    izdelie_event_cameras -->|материал| material_aluminum
    izdelie_mwir_nbn_640 -->|материал| material_generic_material
    izdelie_mwir_nbn_640 -->|материал| material_aluminum
    izdelie_pmut -->|материал| material_generic_material
    izdelie_pmut -->|материал| material_aluminum
    izdelie_pezo_mems -->|материал| material_generic_material
    izdelie_pezo_mems -->|материал| material_aluminum
    izdelie_mems_mikrofonov -->|материал| material_generic_material
    izdelie_mems_mikrofonov -->|материал| material_aluminum
    izdelie_cw_lazer -->|материал| material_generic_material
    izdelie_cw_lazer -->|материал| material_aluminum
    izdelie_flir_lwir_2 -->|материал| material_generic_material
    izdelie_flir_lwir_2 -->|материал| material_aluminum
    часть_ipg_yls_eco_housing -->|материал| material_ti_6al_4v
    часть_ipg_yls_eco_core -->|материал| material_ti_6al_4v
    часть_ipg_yls_eco_connectors -->|материал| material_cu
    часть_ipg_yls_eco_mounting -->|материал| material_ti_6al_4v
    часть_ferritovye_klinya_na_kabelyah_sensorov_connectors -->|материал| material_cu
    часть_ferritovye_klinya_na_kabelyah_sensorov_core -->|материал| material_ti_6al_4v
    часть_ferritovye_klinya_na_kabelyah_sensorov_housing -->|материал| material_ti_6al_4v
    часть_ferritovye_klinya_na_kabelyah_sensorov_mounting -->|материал| material_ti_6al_4v
    часть_sensora_volnovogo_fronta_connectors -->|материал| material_cu
    часть_sensora_volnovogo_fronta_core -->|материал| material_ti_6al_4v
    часть_sensora_volnovogo_fronta_housing -->|материал| material_ti_6al_4v
    часть_sensora_volnovogo_fronta_mounting -->|материал| material_ti_6al_4v
    часть_dvs_core -->|материал| material_ti_6al_4v
    часть_dvs_housing -->|материал| material_ti_6al_4v
    часть_dvs_connectors -->|материал| material_cu
    часть_dvs_mounting -->|материал| material_ti_6al_4v
    часть_eo_ir_kamera_housing -->|материал| material_ti_6al_4v
    часть_eo_ir_kamera_core -->|материал| material_ti_6al_4v
    часть_eo_ir_kamera_connectors -->|материал| material_cu
    часть_eo_ir_kamera_mounting -->|материал| material_ti_6al_4v
    часть_kaskadnyi_stirling_kriokuler_core -->|материал| material_ti_6al_4v
    часть_kaskadnyi_stirling_kriokuler_housing -->|материал| material_ti_6al_4v
    часть_kaskadnyi_stirling_kriokuler_mounting -->|материал| material_ti_6al_4v
    часть_kaskadnyi_stirling_kriokuler_connectors -->|материал| material_cu
    часть_iridium_sbd_housing -->|материал| material_ti_6al_4v
    часть_iridium_sbd_core -->|материал| material_ti_6al_4v
    часть_iridium_sbd_mounting -->|материал| material_ti_6al_4v
    часть_iridium_sbd_connectors -->|материал| material_cu
    часть_ads_b_priemnik_mounting -->|материал| material_al_6061_t6
    часть_ads_b_priemnik_connectors -->|материал| material_cu
    часть_ads_b_priemnik_core -->|материал| material_ti_6al_4v
    часть_ads_b_priemnik_housing -->|материал| material_al_6061_t6
    часть_metalinza_mounting -->|материал| material_ti_6al_4v
    часть_metalinza_core -->|материал| material_ti_6al_4v
    часть_metalinza_connectors -->|материал| material_cu
    часть_metalinza_housing -->|материал| material_ti_6al_4v
    часть_pezoelektricheskie_mems_connectors -->|материал| material_cu
    часть_pezoelektricheskie_mems_core -->|материал| material_ti_6al_4v
    часть_pezoelektricheskie_mems_housing -->|материал| material_ti_6al_4v
    часть_pezoelektricheskie_mems_mounting -->|материал| material_ti_6al_4v
    часть_mwir_2_core -->|материал| material_ti_6al_4v
    часть_mwir_2_housing -->|материал| material_ti_6al_4v
    часть_mwir_2_connectors -->|материал| material_cu
    часть_mwir_2_mounting -->|материал| material_ti_6al_4v
    часть_lwir_boson_1024_core -->|материал| material_ti_6al_4v
    часть_lwir_boson_1024_housing -->|материал| material_ti_6al_4v
    часть_lwir_boson_1024_mounting -->|материал| material_ti_6al_4v
    часть_lwir_boson_1024_connectors -->|материал| material_cu
    часть_poristyi_gazovyi_podshipnik_iz_sic_core -->|материал| material_ti_6al_4v
    часть_poristyi_gazovyi_podshipnik_iz_sic_housing -->|материал| material_ti_6al_4v
    часть_poristyi_gazovyi_podshipnik_iz_sic_connectors -->|материал| material_cu
    часть_poristyi_gazovyi_podshipnik_iz_sic_mounting -->|материал| material_ti_6al_4v
    часть_quantum_cascade_laser_mounting -->|материал| material_ti_6al_4v
    часть_quantum_cascade_laser_connectors -->|материал| material_cu
    часть_quantum_cascade_laser_core -->|материал| material_ti_6al_4v
    часть_quantum_cascade_laser_housing -->|материал| material_ti_6al_4v
    часть_lidar_robosense_ac1_housing -->|материал| material_ti_6al_4v
    часть_lidar_robosense_ac1_core -->|материал| material_ti_6al_4v
    часть_lidar_robosense_ac1_connectors -->|материал| material_cu
    часть_lidar_robosense_ac1_mounting -->|материал| material_ti_6al_4v
    часть_aesa_radar_connectors -->|материал| material_cu
    часть_aesa_radar_housing -->|материал| material_al_6061_t6
    часть_aesa_radar_core -->|материал| material_ti_6al_4v
    часть_aesa_radar_mounting -->|материал| material_al_6061_t6
    часть_lidar_housing -->|материал| material_ti_6al_4v
    часть_lidar_mounting -->|материал| material_ti_6al_4v
    часть_lidar_core -->|материал| material_ti_6al_4v
    часть_lidar_connectors -->|материал| material_latun_c36000
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_connectors -->|материал| material_cu
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_housing -->|материал| material_ti_6al_4v
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_mounting -->|материал| material_ti_6al_4v
    часть_multispektralnye_cmos_matritsy_s_ik_diapazonom_core -->|материал| material_ti_6al_4v
    часть_flir_boson_640_core -->|материал| material_ti_6al_4v
    часть_flir_boson_640_connectors -->|материал| material_cu
    часть_flir_boson_640_mounting -->|материал| material_ti_6al_4v
    часть_flir_boson_640_housing -->|материал| material_ti_6al_4v
    часть_pezo_sensor_connectors -->|материал| material_cu
    часть_pezo_sensor_core -->|материал| material_ti_6al_4v
    часть_pezo_sensor_housing -->|материал| material_ti_6al_4v
    часть_pezo_sensor_mounting -->|материал| material_ti_6al_4v
    часть_ultrakorotkoimpulsnye_lazery_core -->|материал| material_ti_6al_4v
    часть_ultrakorotkoimpulsnye_lazery_mounting -->|материал| material_ti_6al_4v
    часть_ultrakorotkoimpulsnye_lazery_housing -->|материал| material_ti_6al_4v
    часть_ultrakorotkoimpulsnye_lazery_connectors -->|материал| material_cu
    часть_tverdotelnyi_mmwave_radar_connectors -->|материал| material_cu
    часть_tverdotelnyi_mmwave_radar_mounting -->|материал| material_ti_6al_4v
    часть_tverdotelnyi_mmwave_radar_core -->|материал| material_ti_6al_4v
    часть_tverdotelnyi_mmwave_radar_housing -->|материал| material_ti_6al_4v
    часть_mems_imu_mounting -->|материал| material_ti_6al_4v
    часть_mems_imu_connectors -->|материал| material_cu
    часть_mems_imu_core -->|материал| material_ti_6al_4v
    часть_mems_imu_housing -->|материал| material_ti_6al_4v
    часть_akusticheskaya_linza_housing -->|материал| material_ti_6al_4v
    часть_akusticheskaya_linza_mounting -->|материал| material_ti_6al_4v
    часть_akusticheskaya_linza_core -->|материал| material_ti_6al_4v
    часть_akusticheskaya_linza_connectors -->|материал| material_cu
    часть_flir_core -->|материал| material_ti_6al_4v
    часть_flir_connectors -->|материал| material_cu
    часть_flir_mounting -->|материал| material_ti_6al_4v
    часть_flir_housing -->|материал| material_ti_6al_4v
    часть_starlink_mini_mounting -->|материал| material_ti_6al_4v
    часть_starlink_mini_connectors -->|материал| material_cu
    часть_starlink_mini_housing -->|материал| material_ti_6al_4v
    часть_starlink_mini_core -->|материал| material_ti_6al_4v
    часть_event_cameras_mounting -->|материал| material_ti_6al_4v
    часть_event_cameras_core -->|материал| material_ti_6al_4v
    часть_event_cameras_connectors -->|материал| material_cu
    часть_event_cameras_housing -->|материал| material_ti_6al_4v
    часть_mwir_nbn_640_mounting -->|материал| material_ti_6al_4v
    часть_mwir_nbn_640_connectors -->|материал| material_cu
    часть_mwir_nbn_640_housing -->|материал| material_ti_6al_4v
    часть_mwir_nbn_640_core -->|материал| material_ti_6al_4v
    часть_pmut_mounting -->|материал| material_ti_6al_4v
    часть_pmut_connectors -->|материал| material_cu
    часть_pmut_housing -->|материал| material_ti_6al_4v
    часть_pmut_core -->|материал| material_ti_6al_4v
    часть_pezo_mems_core -->|материал| material_ti_6al_4v
    часть_pezo_mems_mounting -->|материал| material_ti_6al_4v
    часть_pezo_mems_connectors -->|материал| material_cu
    часть_pezo_mems_housing -->|материал| material_ti_6al_4v
    часть_mems_mikrofonov_mounting -->|материал| material_ti_6al_4v
    часть_mems_mikrofonov_connectors -->|материал| material_cu
    часть_mems_mikrofonov_housing -->|материал| material_ti_6al_4v
    часть_mems_mikrofonov_core -->|материал| material_ti_6al_4v
    часть_cw_lazer_core -->|материал| material_ti_6al_4v
    часть_cw_lazer_housing -->|материал| material_ti_6al_4v
    часть_cw_lazer_connectors -->|материал| material_cu
    часть_cw_lazer_mounting -->|материал| material_ti_6al_4v
    часть_flir_lwir_2_housing -->|материал| material_ti_6al_4v
    часть_flir_lwir_2_connectors -->|материал| material_cu
    часть_flir_lwir_2_mounting -->|материал| material_ti_6al_4v
    часть_flir_lwir_2_core -->|материал| material_ti_6al_4v
```

| Материал | Используется в частях |
|---|---:|
| `Ti-6Al-4V` | 100 |
| `material_generic_material` | 33 |
| `material_aluminum` | 32 |
| `material_cu` | 32 |
| `Al 6061-T6` | 6 |
| `Si` | 2 |
| `Cu 60–63% (основа), Zn баланс, Pb 2.5–3.5% (UNS C36000 / CuZn39Pb3, CW614N)` | 1 |
