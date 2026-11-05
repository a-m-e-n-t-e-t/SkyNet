# Граф 1 — подсистема «энергетическая»

```mermaid
graph LR
    izdelie_marx_generator[импульсный_генератор_Маркса]
    izdelie_perovskite_tandem[фотоэлектрический_модуль]
    izdelie_vysokotemperaturnyi_sverhprovodyaschii_podshipnik[HTS_подшипник]
    izdelie_asrg[радиоизотопный_генератор_Ст…]
    izdelie_3d_sic_mikropillarnyi_tritii_betavoltaik[бета_вольтаик_3D_SiC]
    izdelie_coilgun[электромагнитный_ускоритель]
    izdelie_svobodnoporshnevoi_stirling[свободнопоршневой_Стирлинг]
    izdelie_emi_generator[ЭМИ_генератор]
    izdelie_vodorodnye_toplivnye_elementy[водородный_топливный_элемент]
    izdelie_mmrtg[радиоизотопный_генератор]
    izdelie_elektromagnitnye_poroshkovye_mufty_i_tormoza[электромагнитная_муфта]
    izdelie_mptm[микро_ТЭЦ]
    izdelie_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami[планетарный_роликовинт]
    izdelie_tpv[термофотоэлектрический_гене…]
    izdelie_tverdooksidnyi_toplivnyi_element[твердооксидный_топливный_эл…]
    izdelie_dvoinaya_sshitaya_magnitnaya_myshtsa_unist[магнитная_мышца]
    izdelie_tverdotelnye_akkumulyatory[литий-ионный_аккумулятор]
    izdelie_superkondensatory[суперконденсатор]
    izdelie_termomoduli_pelte[модуль_Пельтье]
    izdelie_svintsovo_kislotnye_akb[свинцово-кислотная_батарея]
    izdelie_induktivnyi_nakopitel[индуктивный_накопитель]
    izdelie_termoelektricheskii_postoyannyi_magnit[термоэлектрический_генератор]
    izdelie_mikroreaktor_deleniya[микро_реактор_деления]
    izdelie_lt_sofc[твердооксидный_топливный_эл…]
    izdelie_reversivnye_pelte[реверсивный_модуль_Пельтье]
    izdelie_betavoltaiki[бетавольтаик]
    izdelie_zeno_power_am_241[радиоизотопный_генератор_Am241]
    izdelie_ni_63_betavoltaik_4h_sic[бета_вольтаик_SiC]
    izdelie_nasa_asc_e_srsc[Стирлинг_конвертер]
    izdelie_4h_sic_betavoltaik[бета_вольтаик_SiC]
    izdelie_alyuminievo_vozdushnye_toplivnye_elementy[алюминиево-воздушный_ТЭ]
    izdelie_tpv_lenty[TPV_ленточный]
    часть_marx_generator_output_terminal[выходной_вывод]
    часть_marx_generator_capacitors[конденсаторы]
    часть_marx_generator_spark_gaps[искровые_промежутки]
    часть_marx_generator_resistors[зарядные_резисторы]
    часть_marx_generator_housing[корпус]
    часть_marx_generator_insulator[изоляторы_SF6]
    часть_perovskite_tandem_encapsulant[инкапсулянт_EVA]
    часть_perovskite_tandem_junction_box[распредкоробка]
    часть_perovskite_tandem_backsheet[подложка]
    часть_perovskite_tandem_front_glass[переднее_стекло]
    часть_perovskite_tandem_frame[рама_алюминий]
    часть_perovskite_tandem_cells[Si_ячейки]
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat[криостат]
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft[вал]
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet[магнит_ротор]
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element[YBCO_элемент]
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing[корпус]
    часть_asrg_isotope[Pu-238_источник]
    часть_asrg_piston[поршень]
    часть_asrg_regenerator[регенератор]
    часть_asrg_cooler[охладитель]
    часть_asrg_alternator[генератор_тока]
    часть_asrg_heater_head[нагреватель_голова]
    часть_asrg_housing[корпус]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_case[корпус]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_isotope[H-3_тритий]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_substrate[SiC_подложка]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_micropillars[3D_SiC_микропилляры]
    часть_coilgun_coil[катушка]
    часть_coilgun_capacitor_bank[батарея_конденсаторов]
    часть_coilgun_projectile[снаряд]
    часть_coilgun_switch[коммутатор]
    часть_coilgun_barrel[ствол]
    часть_coilgun_housing[корпус]
    часть_svobodnoporshnevoi_stirling_piston[поршень]
    часть_svobodnoporshnevoi_stirling_heater[нагреватель]
    часть_svobodnoporshnevoi_stirling_alternator[генератор]
    часть_svobodnoporshnevoi_stirling_cooler[охладитель]
    часть_svobodnoporshnevoi_stirling_gas_spring[газовая_пружина]
    часть_svobodnoporshnevoi_stirling_regenerator[регенератор]
    часть_emi_generator_switch[коммутатор]
    часть_emi_generator_waveguide[волновод]
    часть_emi_generator_capacitor_bank[батарея_конденсаторов]
    часть_emi_generator_housing[корпус]
    часть_emi_generator_antenna[антенна_рупор]
    часть_emi_generator_source[взрывной_источник]
    часть_vodorodnye_toplivnye_elementy_catalyst_anode[Pt_анод]
    часть_vodorodnye_toplivnye_elementy_gasket[уплотнение]
    часть_vodorodnye_toplivnye_elementy_gdl_cathode[GDL_катод]
    часть_vodorodnye_toplivnye_elementy_catalyst_cathode[Pt_катод]
    часть_vodorodnye_toplivnye_elementy_membrane[PEM_мембрана]
    часть_vodorodnye_toplivnye_elementy_bipolar_plate[биполярная_пластина]
    часть_vodorodnye_toplivnye_elementy_end_plate[торцевая_пластина]
    часть_vodorodnye_toplivnye_elementy_gdl_anode[GDL_анод]
    часть_mmrtg_housing[корпус]
    часть_mmrtg_thermal_insulation[изоляция]
    часть_mmrtg_thermocouples[термопары]
    часть_mmrtg_isotope[Pu-238_источник]
    часть_mmrtg_hot_side[горячий_узел]
    часть_mmrtg_cold_side[холодный_узел]
    часть_mmrtg_connector[разъём]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder[магнитный_порошок]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil[электромагнит]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing[корпус]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator[статор]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor[ротор]
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings[подшипники]
    часть_mptm_generator[генератор]
    часть_mptm_heat_exchanger[теплообменник]
    часть_mptm_engine[двигатель]
    часть_mptm_controls[электроника_управления]
    часть_mptm_housing[корпус]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals[уплотнения]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers[ролики]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings[подшипники]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut[гайка]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing[корпус]
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw[винт]
    часть_tpv_emitter[излучатель]
    часть_tpv_housing[корпус]
    часть_tpv_pv_cell[PV_ячейка]
    часть_tpv_cooling[охлаждение]
    часть_tpv_filter[оптический_фильтр]
    часть_tpv_heat_source[источник_тепла]
    часть_tverdooksidnyi_toplivnyi_element_anode[анод_Ni_Cermet]
    часть_tverdooksidnyi_toplivnyi_element_seal[герметизация]
    часть_tverdooksidnyi_toplivnyi_element_interconnect[интерконнект]
    часть_tverdooksidnyi_toplivnyi_element_manifold[коллектор_газа]
    часть_tverdooksidnyi_toplivnyi_element_electrolyte[YSZ_электролит]
    часть_tverdooksidnyi_toplivnyi_element_cathode[катод_LSM]
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_magnets[постоянные_магниты]
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring[пружина]
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing[корпус]
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil[катушка]
    часть_tverdotelnye_akkumulyatory_separator[сепаратор]
    часть_tverdotelnye_akkumulyatory_case[корпус]
    часть_tverdotelnye_akkumulyatory_electrolyte[LiPF6_электролит]
    часть_tverdotelnye_akkumulyatory_anode[графит_анод]
    часть_tverdotelnye_akkumulyatory_current_collector_cu[медный_токосъёмник]
    часть_tverdotelnye_akkumulyatory_cathode[NMC_катод]
    часть_tverdotelnye_akkumulyatory_current_collector_al[алюминиевый_токосъёмник]
    часть_superkondensatory_separator[сепаратор]
    часть_superkondensatory_electrolyte[электролит]
    часть_superkondensatory_case[корпус]
    часть_superkondensatory_electrode_pos[положительный_электрод]
    часть_superkondensatory_current_collector[токосъёмник]
    часть_superkondensatory_terminal[выводы]
    часть_termomoduli_pelte_wires[провода]
    часть_termomoduli_pelte_solder[припой]
    часть_termomoduli_pelte_electrodes[электроды]
    часть_termomoduli_pelte_ceramic_top[керамика_верх]
    часть_termomoduli_pelte_peltier_couples[термоэлементы]
    часть_svintsovo_kislotnye_akb_anode[PbO2_анод]
    часть_svintsovo_kislotnye_akb_terminal[вывод]
    часть_svintsovo_kislotnye_akb_cathode[Pb_катод]
    часть_svintsovo_kislotnye_akb_grid_pos[решётка_PbSb]
    часть_svintsovo_kislotnye_akb_electrolyte[H2SO4_электролит]
    часть_svintsovo_kislotnye_akb_separator[сепаратор]
    часть_svintsovo_kislotnye_akb_case[корпус_PP]
    часть_induktivnyi_nakopitel_cooling[охлаждение]
    часть_induktivnyi_nakopitel_housing[корпус]
    часть_induktivnyi_nakopitel_coil[индуктивность]
    часть_induktivnyi_nakopitel_switch[коммутатор]
    часть_induktivnyi_nakopitel_core[магнитопровод]
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot[горячий_радиатор]
    часть_termoelektricheskii_postoyannyi_magnit_clamping[прижимные_болты]
    часть_termoelektricheskii_postoyannyi_magnit_insulation[изоляция]
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold[холодный_радиатор]
    часть_termoelektricheskii_postoyannyi_magnit_teg_modules[ТЕГ_модули]
    часть_mikroreaktor_deleniya_fuel[U-235_топливо]
    часть_mikroreaktor_deleniya_coolant[охладитель]
    часть_mikroreaktor_deleniya_moderator[замедлитель]
    часть_mikroreaktor_deleniya_control_rods[стержни_управления]
    часть_mikroreaktor_deleniya_heat_exchanger[теплообменник]
    часть_mikroreaktor_deleniya_vessel[корпус_реактора]
    часть_mikroreaktor_deleniya_shielding[экранирование]
    часть_lt_sofc_seal[герметизация]
    часть_lt_sofc_interconnect[интерконнект]
    часть_lt_sofc_electrolyte[YSZ_электролит]
    часть_lt_sofc_anode[анод_Ni_Cermet]
    часть_lt_sofc_cathode[катод_LSM]
    часть_lt_sofc_manifold[коллектор_газа]
    часть_reversivnye_pelte_peltier_couples[термоэлементы]
    часть_reversivnye_pelte_electrodes[электроды]
    часть_reversivnye_pelte_ceramic_top[керамика_верх]
    часть_reversivnye_pelte_solder[припой]
    часть_betavoltaiki_terminal[вывод]
    часть_betavoltaiki_encapsulant[инкапсулянт]
    часть_betavoltaiki_isotope[Ni-63_источник]
    часть_betavoltaiki_case[корпус_титан]
    часть_betavoltaiki_semiconductor[SiC_преобразователь]
    часть_zeno_power_am_241_isotope[Am-241_источник]
    часть_zeno_power_am_241_thermocouples[термопары]
    часть_zeno_power_am_241_housing[корпус]
    часть_zeno_power_am_241_shielding[экранирование]
    часть_ni_63_betavoltaik_4h_sic_isotope[Ni-63_источник]
    часть_ni_63_betavoltaik_4h_sic_case[корпус]
    часть_ni_63_betavoltaik_4h_sic_sic_diode[SiC_pn_диод]
    часть_ni_63_betavoltaik_4h_sic_encapsulant[инкапсулянт]
    часть_ni_63_betavoltaik_4h_sic_substrate[SiC_подложка]
    часть_nasa_asc_e_srsc_power_piston[рабочий_поршень]
    часть_nasa_asc_e_srsc_alternator[линейный_генератор]
    часть_nasa_asc_e_srsc_heater_head[нагреватель]
    часть_nasa_asc_e_srsc_cooler[охладитель]
    часть_nasa_asc_e_srsc_displacer_piston[поршень_вытеснитель]
    часть_nasa_asc_e_srsc_regenerator[регенератор]
    часть_4h_sic_betavoltaik_sic_diode[SiC_pn_диод]
    часть_4h_sic_betavoltaik_encapsulant[инкапсулянт]
    часть_4h_sic_betavoltaik_isotope[Ni-63_источник]
    часть_4h_sic_betavoltaik_case[корпус]
    часть_4h_sic_betavoltaik_substrate[SiC_подложка]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_separator[сепаратор]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_cathode[воздушный_катод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_anode[Al_анод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_housing[корпус]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_air_electrode[газодиффузионный_электрод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_electrolyte[щелочной_электролит]
    часть_tpv_lenty_reflector[рефлектор]
    часть_tpv_lenty_pv_cells[PV_ячейки]
    часть_tpv_lenty_emitter_ribbon[излучающая_лента]
    часть_tpv_lenty_cooling[охлаждение]
    material_ti_6al_4v[Ti-6Al-4V]
    material_al_6061_t6[Al 6061-T6]
    material_stal_st3[Сталь Ст3]
    material_latun_c36000[Cu 60–63% (основа), Zn…]
    material_ss_aisi_304[SS AISI 304]
    izdelie_nasa_asc_e_srsc -->|материал| material_al_6061_t6
    часть_marx_generator_output_terminal -->|материал| material_ti_6al_4v
    часть_marx_generator_capacitors -->|материал| material_ti_6al_4v
    часть_marx_generator_spark_gaps -->|материал| material_ti_6al_4v
    часть_marx_generator_resistors -->|материал| material_ti_6al_4v
    часть_marx_generator_housing -->|материал| material_stal_st3
    часть_marx_generator_insulator -->|материал| material_ti_6al_4v
    часть_perovskite_tandem_encapsulant -->|материал| material_ti_6al_4v
    часть_perovskite_tandem_backsheet -->|материал| material_ti_6al_4v
    часть_perovskite_tandem_front_glass -->|материал| material_ti_6al_4v
    часть_perovskite_tandem_frame -->|материал| material_ti_6al_4v
    часть_perovskite_tandem_cells -->|материал| material_ti_6al_4v
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat -->|материал| material_ti_6al_4v
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft -->|материал| material_ti_6al_4v
    часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing -->|материал| material_al_6061_t6
    часть_asrg_piston -->|материал| material_ti_6al_4v
    часть_asrg_regenerator -->|материал| material_ti_6al_4v
    часть_asrg_cooler -->|материал| material_ti_6al_4v
    часть_asrg_alternator -->|материал| material_ti_6al_4v
    часть_asrg_heater_head -->|материал| material_ti_6al_4v
    часть_asrg_housing -->|материал| material_al_6061_t6
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_case -->|материал| material_ti_6al_4v
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_substrate -->|материал| material_ti_6al_4v
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_micropillars -->|материал| material_ti_6al_4v
    часть_coilgun_coil -->|материал| material_ti_6al_4v
    часть_coilgun_capacitor_bank -->|материал| material_ti_6al_4v
    часть_coilgun_projectile -->|материал| material_ti_6al_4v
    часть_coilgun_switch -->|материал| material_ti_6al_4v
    часть_coilgun_barrel -->|материал| material_ti_6al_4v
    часть_coilgun_housing -->|материал| material_stal_st3
    часть_svobodnoporshnevoi_stirling_piston -->|материал| material_al_6061_t6
    часть_svobodnoporshnevoi_stirling_alternator -->|материал| material_ti_6al_4v
    часть_svobodnoporshnevoi_stirling_cooler -->|материал| material_ss_aisi_304
    часть_svobodnoporshnevoi_stirling_gas_spring -->|материал| material_ss_aisi_304
    часть_svobodnoporshnevoi_stirling_regenerator -->|материал| material_ti_6al_4v
    часть_emi_generator_switch -->|материал| material_ti_6al_4v
    часть_emi_generator_waveguide -->|материал| material_ti_6al_4v
    часть_emi_generator_capacitor_bank -->|материал| material_ti_6al_4v
    часть_emi_generator_housing -->|материал| material_stal_st3
    часть_emi_generator_antenna -->|материал| material_ti_6al_4v
    часть_emi_generator_source -->|материал| material_ti_6al_4v
    часть_vodorodnye_toplivnye_elementy_gasket -->|материал| material_ti_6al_4v
    часть_vodorodnye_toplivnye_elementy_gdl_cathode -->|материал| material_ti_6al_4v
    часть_vodorodnye_toplivnye_elementy_bipolar_plate -->|материал| material_ti_6al_4v
    часть_vodorodnye_toplivnye_elementy_end_plate -->|материал| material_ti_6al_4v
    часть_vodorodnye_toplivnye_elementy_gdl_anode -->|материал| material_ti_6al_4v
    часть_mmrtg_housing -->|материал| material_al_6061_t6
    часть_mmrtg_hot_side -->|материал| material_ti_6al_4v
    часть_mmrtg_cold_side -->|материал| material_al_6061_t6
    часть_mmrtg_connector -->|материал| material_al_6061_t6
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil -->|материал| material_ti_6al_4v
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing -->|материал| material_stal_st3
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator -->|материал| material_ti_6al_4v
    часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor -->|материал| material_ti_6al_4v
    часть_mptm_generator -->|материал| material_ti_6al_4v
    часть_mptm_heat_exchanger -->|материал| material_ti_6al_4v
    часть_mptm_engine -->|материал| material_ti_6al_4v
    часть_mptm_controls -->|материал| material_al_6061_t6
    часть_mptm_housing -->|материал| material_al_6061_t6
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut -->|материал| material_ti_6al_4v
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing -->|материал| material_al_6061_t6
    часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw -->|материал| material_ti_6al_4v
    часть_tpv_housing -->|материал| material_ti_6al_4v
    часть_tpv_pv_cell -->|материал| material_ti_6al_4v
    часть_tpv_cooling -->|материал| material_al_6061_t6
    часть_tpv_filter -->|материал| material_ti_6al_4v
    часть_tverdooksidnyi_toplivnyi_element_seal -->|материал| material_ti_6al_4v
    часть_tverdooksidnyi_toplivnyi_element_interconnect -->|материал| material_ti_6al_4v
    часть_tverdooksidnyi_toplivnyi_element_manifold -->|материал| material_ss_aisi_304
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_spring -->|материал| material_ti_6al_4v
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_housing -->|материал| material_al_6061_t6
    часть_dvoinaya_sshitaya_magnitnaya_myshtsa_unist_coil -->|материал| material_ti_6al_4v
    часть_tverdotelnye_akkumulyatory_case -->|материал| material_al_6061_t6
    часть_tverdotelnye_akkumulyatory_current_collector_cu -->|материал| material_ti_6al_4v
    часть_tverdotelnye_akkumulyatory_current_collector_al -->|материал| material_ti_6al_4v
    часть_superkondensatory_separator -->|материал| material_ti_6al_4v
    часть_superkondensatory_electrolyte -->|материал| material_ti_6al_4v
    часть_superkondensatory_case -->|материал| material_al_6061_t6
    часть_superkondensatory_current_collector -->|материал| material_ti_6al_4v
    часть_superkondensatory_terminal -->|материал| material_ti_6al_4v
    часть_termomoduli_pelte_wires -->|материал| material_ti_6al_4v
    часть_termomoduli_pelte_solder -->|материал| material_ti_6al_4v
    часть_termomoduli_pelte_electrodes -->|материал| material_ti_6al_4v
    часть_termomoduli_pelte_ceramic_top -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_anode -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_terminal -->|материал| material_latun_c36000
    часть_svintsovo_kislotnye_akb_cathode -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_grid_pos -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_electrolyte -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_separator -->|материал| material_ti_6al_4v
    часть_svintsovo_kislotnye_akb_case -->|материал| material_ti_6al_4v
    часть_induktivnyi_nakopitel_cooling -->|материал| material_ti_6al_4v
    часть_induktivnyi_nakopitel_housing -->|материал| material_stal_st3
    часть_induktivnyi_nakopitel_coil -->|материал| material_ti_6al_4v
    часть_induktivnyi_nakopitel_switch -->|материал| material_ti_6al_4v
    часть_induktivnyi_nakopitel_core -->|материал| material_ti_6al_4v
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot -->|материал| material_al_6061_t6
    часть_termoelektricheskii_postoyannyi_magnit_clamping -->|материал| material_ti_6al_4v
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold -->|материал| material_al_6061_t6
    часть_termoelektricheskii_postoyannyi_magnit_teg_modules -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_fuel -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_coolant -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_moderator -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_heat_exchanger -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_vessel -->|материал| material_ti_6al_4v
    часть_mikroreaktor_deleniya_shielding -->|материал| material_ti_6al_4v
    часть_lt_sofc_seal -->|материал| material_ti_6al_4v
    часть_lt_sofc_interconnect -->|материал| material_ti_6al_4v
    часть_lt_sofc_manifold -->|материал| material_ss_aisi_304
    часть_reversivnye_pelte_peltier_couples -->|материал| material_ti_6al_4v
    часть_reversivnye_pelte_electrodes -->|материал| material_ti_6al_4v
    часть_reversivnye_pelte_ceramic_top -->|материал| material_ti_6al_4v
    часть_reversivnye_pelte_solder -->|материал| material_ti_6al_4v
    часть_betavoltaiki_terminal -->|материал| material_ti_6al_4v
    часть_betavoltaiki_isotope -->|материал| material_ti_6al_4v
    часть_betavoltaiki_case -->|материал| material_ti_6al_4v
    часть_betavoltaiki_semiconductor -->|материал| material_ti_6al_4v
    часть_zeno_power_am_241_housing -->|материал| material_al_6061_t6
    часть_zeno_power_am_241_shielding -->|материал| material_ti_6al_4v
    часть_ni_63_betavoltaik_4h_sic_isotope -->|материал| material_ti_6al_4v
    часть_ni_63_betavoltaik_4h_sic_case -->|материал| material_ti_6al_4v
    часть_ni_63_betavoltaik_4h_sic_sic_diode -->|материал| material_ti_6al_4v
    часть_ni_63_betavoltaik_4h_sic_substrate -->|материал| material_ti_6al_4v
    часть_nasa_asc_e_srsc_power_piston -->|материал| material_ti_6al_4v
    часть_nasa_asc_e_srsc_alternator -->|материал| material_ti_6al_4v
    часть_nasa_asc_e_srsc_cooler -->|материал| material_al_6061_t6
    часть_nasa_asc_e_srsc_displacer_piston -->|материал| material_ti_6al_4v
    часть_nasa_asc_e_srsc_regenerator -->|материал| material_ss_aisi_304
    часть_4h_sic_betavoltaik_sic_diode -->|материал| material_ti_6al_4v
    часть_4h_sic_betavoltaik_isotope -->|материал| material_ti_6al_4v
    часть_4h_sic_betavoltaik_case -->|материал| material_ti_6al_4v
    часть_4h_sic_betavoltaik_substrate -->|материал| material_ti_6al_4v
    часть_alyuminievo_vozdushnye_toplivnye_elementy_housing -->|материал| material_al_6061_t6
    часть_tpv_lenty_reflector -->|материал| material_al_6061_t6
    часть_tpv_lenty_pv_cells -->|материал| material_ti_6al_4v
    часть_tpv_lenty_emitter_ribbon -->|материал| material_ti_6al_4v
    часть_tpv_lenty_cooling -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Ti-6Al-4V` | 106 |
| `Al 6061-T6` | 20 |
| `Inconel 718` | 6 |
| `Bi₂Te₃` | 5 |
| `Сталь Ст3` | 5 |
| `SS AISI 304` | 5 |
| `NdFeB` | 4 |
| `Inconel 625` | 3 |
| `Эпоксид Epon 828 + TETA` | 3 |
| `ScT?` | 2 |
| `Am-241` | 2 |
| `углеродная сажа (токопроводящий наполнитель) + PTFE 20% (связующее), опционально катализатор MnO₂; токосъёмник — никелевая сетка` | 2 |
| `Pu-238 (плутоний-238)` | 2 |
| `Pt` | 2 |
| `Графен-аэрогель` | 2 |
