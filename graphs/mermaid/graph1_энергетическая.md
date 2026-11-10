# Граф 1 — подсистема «энергетическая»

```mermaid
graph LR
    izdelie_mptm[микро_ТЭЦ]
    izdelie_tpv_lenty[TPV_ленточный]
    izdelie_zeno_power_am_241[радиоизотопный_генератор_Am241]
    izdelie_svobodnoporshnevoi_stirling[свободнопоршневой_Стирлинг]
    izdelie_tpv[термофотоэлектрический_гене…]
    izdelie_mmrtg[радиоизотопный_генератор]
    izdelie_4h_sic_betavoltaik[бета_вольтаик_SiC]
    izdelie_marx_generator[импульсный_генератор_Маркса]
    izdelie_betavoltaiki[бетавольтаик]
    izdelie_perovskite_tandem[фотоэлектрический_модуль]
    izdelie_mikroreaktor_deleniya[микро_реактор_деления]
    izdelie_lt_sofc[твердооксидный_топливный_эл…]
    izdelie_3d_sic_mikropillarnyi_tritii_betavoltaik[бета_вольтаик_3D_SiC]
    izdelie_tverdooksidnyi_toplivnyi_element[твердооксидный_топливный_эл…]
    izdelie_alyuminievo_vozdushnye_toplivnye_elementy[алюминиево-воздушный_ТЭ]
    izdelie_ni_63_betavoltaik_4h_sic[бета_вольтаик_SiC]
    izdelie_termoelektricheskii_postoyannyi_magnit[термоэлектрический_генератор]
    izdelie_vodorodnye_toplivnye_elementy[водородный_топливный_элемент]
    izdelie_nasa_asc_e_srsc[Стирлинг_конвертер]
    izdelie_asrg[радиоизотопный_генератор_Ст…]
    часть_mptm_generator[генератор]
    часть_mptm_controls[электроника_управления]
    часть_mptm_housing[корпус]
    часть_mptm_engine[двигатель]
    часть_mptm_heat_exchanger[теплообменник]
    часть_tpv_lenty_reflector[рефлектор]
    часть_tpv_lenty_cooling[охлаждение]
    часть_tpv_lenty_emitter_ribbon[излучающая_лента]
    часть_tpv_lenty_pv_cells[PV_ячейки]
    часть_zeno_power_am_241_thermocouples[термопары]
    часть_zeno_power_am_241_housing[корпус]
    часть_zeno_power_am_241_shielding[экранирование]
    часть_zeno_power_am_241_isotope[Am-241_источник]
    часть_svobodnoporshnevoi_stirling_alternator[генератор]
    часть_svobodnoporshnevoi_stirling_heater[нагреватель]
    часть_svobodnoporshnevoi_stirling_regenerator[регенератор]
    часть_svobodnoporshnevoi_stirling_cooler[охладитель]
    часть_svobodnoporshnevoi_stirling_gas_spring[газовая_пружина]
    часть_svobodnoporshnevoi_stirling_piston[поршень]
    часть_tpv_emitter[излучатель]
    часть_tpv_cooling[охлаждение]
    часть_tpv_housing[корпус]
    часть_tpv_heat_source[источник_тепла]
    часть_tpv_pv_cell[PV_ячейка]
    часть_tpv_filter[оптический_фильтр]
    часть_mmrtg_housing[корпус]
    часть_mmrtg_cold_side[холодный_узел]
    часть_mmrtg_isotope[Pu-238_источник]
    часть_mmrtg_connector[разъём]
    часть_mmrtg_thermal_insulation[изоляция]
    часть_mmrtg_hot_side[горячий_узел]
    часть_mmrtg_thermocouples[термопары]
    часть_4h_sic_betavoltaik_case[корпус]
    часть_4h_sic_betavoltaik_sic_diode[SiC_pn_диод]
    часть_4h_sic_betavoltaik_substrate[SiC_подложка]
    часть_4h_sic_betavoltaik_isotope[Ni-63_источник]
    часть_4h_sic_betavoltaik_encapsulant[инкапсулянт]
    часть_marx_generator_insulator[изоляторы_SF6]
    часть_marx_generator_resistors[зарядные_резисторы]
    часть_marx_generator_spark_gaps[искровые_промежутки]
    часть_marx_generator_housing[корпус]
    часть_marx_generator_capacitors[конденсаторы]
    часть_marx_generator_output_terminal[выходной_вывод]
    часть_betavoltaiki_semiconductor[SiC_преобразователь]
    часть_betavoltaiki_encapsulant[инкапсулянт]
    часть_betavoltaiki_terminal[вывод]
    часть_betavoltaiki_case[корпус_титан]
    часть_betavoltaiki_isotope[Ni-63_источник]
    часть_perovskite_tandem_front_glass[переднее_стекло]
    часть_perovskite_tandem_frame[рама_алюминий]
    часть_perovskite_tandem_backsheet[подложка]
    часть_perovskite_tandem_cells[Si_ячейки]
    часть_perovskite_tandem_encapsulant[инкапсулянт_EVA]
    часть_perovskite_tandem_junction_box[распредкоробка]
    часть_mikroreaktor_deleniya_moderator[замедлитель]
    часть_mikroreaktor_deleniya_heat_exchanger[теплообменник]
    часть_mikroreaktor_deleniya_vessel[корпус_реактора]
    часть_mikroreaktor_deleniya_control_rods[стержни_управления]
    часть_mikroreaktor_deleniya_fuel[U-235_топливо]
    часть_mikroreaktor_deleniya_coolant[охладитель]
    часть_mikroreaktor_deleniya_shielding[экранирование]
    часть_lt_sofc_interconnect[интерконнект]
    часть_lt_sofc_seal[герметизация]
    часть_lt_sofc_cathode[катод_LSM]
    часть_lt_sofc_electrolyte[YSZ_электролит]
    часть_lt_sofc_manifold[коллектор_газа]
    часть_lt_sofc_anode[анод_Ni_Cermet]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_isotope[H-3_тритий]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_substrate[SiC_подложка]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_case[корпус]
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_micropillars[3D_SiC_микропилляры]
    часть_tverdooksidnyi_toplivnyi_element_interconnect[интерконнект]
    часть_tverdooksidnyi_toplivnyi_element_seal[герметизация]
    часть_tverdooksidnyi_toplivnyi_element_anode[анод_Ni_Cermet]
    часть_tverdooksidnyi_toplivnyi_element_cathode[катод_LSM]
    часть_tverdooksidnyi_toplivnyi_element_electrolyte[YSZ_электролит]
    часть_tverdooksidnyi_toplivnyi_element_manifold[коллектор_газа]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_air_electrode[газодиффузионный_электрод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_separator[сепаратор]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_housing[корпус]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_cathode[воздушный_катод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_anode[Al_анод]
    часть_alyuminievo_vozdushnye_toplivnye_elementy_electrolyte[щелочной_электролит]
    часть_ni_63_betavoltaik_4h_sic_sic_diode[SiC_pn_диод]
    часть_ni_63_betavoltaik_4h_sic_encapsulant[инкапсулянт]
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot[горячий_радиатор]
    часть_termoelektricheskii_postoyannyi_magnit_clamping[прижимные_болты]
    часть_termoelektricheskii_postoyannyi_magnit_teg_modules[ТЕГ_модули]
    часть_termoelektricheskii_postoyannyi_magnit_insulation[изоляция]
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold[холодный_радиатор]
    часть_vodorodnye_toplivnye_elementy_catalyst_anode[Pt_анод]
    часть_vodorodnye_toplivnye_elementy_bipolar_plate[биполярная_пластина]
    часть_vodorodnye_toplivnye_elementy_catalyst_cathode[Pt_катод]
    часть_vodorodnye_toplivnye_elementy_end_plate[торцевая_пластина]
    часть_vodorodnye_toplivnye_elementy_gdl_anode[GDL_анод]
    часть_vodorodnye_toplivnye_elementy_gdl_cathode[GDL_катод]
    часть_vodorodnye_toplivnye_elementy_gasket[уплотнение]
    часть_vodorodnye_toplivnye_elementy_membrane[PEM_мембрана]
    часть_nasa_asc_e_srsc_regenerator[регенератор]
    часть_nasa_asc_e_srsc_cooler[охладитель]
    часть_nasa_asc_e_srsc_displacer_piston[поршень_вытеснитель]
    часть_nasa_asc_e_srsc_alternator[линейный_генератор]
    часть_nasa_asc_e_srsc_heater_head[нагреватель]
    часть_nasa_asc_e_srsc_power_piston[рабочий_поршень]
    часть_asrg_piston[поршень]
    часть_asrg_cooler[охладитель]
    часть_asrg_alternator[генератор_тока]
    часть_asrg_housing[корпус]
    часть_asrg_regenerator[регенератор]
    часть_asrg_heater_head[нагреватель_голова]
    часть_asrg_isotope[Pu-238_источник]
    izdelie_asrg_v28_ии[радиоизотопный_генератор_Ст…]
    часть_asrg_v28_ии_piston[компонент_РИТЭГ_Стирлинг]
    часть_asrg_v28_ии_isotope[компонент_РИТЭГ_Стирлинг]
    часть_asrg_v28_ии_regenerator[компонент_РИТЭГ_Стирлинг]
    часть_asrg_v28_ии_alternator[компонент_РИТЭГ_Стирлинг]
    часть_asrg_v28_ии_heater_head[компонент_РИТЭГ_Стирлинг]
    часть_asrg_v28_ии_housing[компонент_РИТЭГ_Стирлинг]
    часть_t600_топливная_ячейка[fuel_cell]
    часть_t_x_топливная_ячейка_1[plasma_cell]
    часть_t800_топливная_ячейка_1[hydrogen_fuel_cell]
    часть_hk_aerial_двигатель_левый[nuclear_vtol_engine]
    часть_hk_tank_двигатель[nuclear_engine]
    часть_hk_tank_боеприпасы[plasma_ammo]
    часть_t850_топливная_ячейка_1[hydrogen_fuel_cell_v2]
    часть_marcus_человеческое_сердце[biological_heart]
    часть_marcus_сердце_гибрид[hybrid_heart]
    часть_marcus_топливная_ячейка[fuel_cell]
    часть_cameron_топливная_ячейка_1[fuel_cell_small]
    часть_cameron_топливная_ячейка_2[fuel_cell_small]
    material_al_6061_t6[Al основа; Si 0.4–0.8 …]
    material_aluminum[Al ≥ 99.5 % (основа); …]
    material_copper[Cu ≥99.9% (электролити…]
    material_ti_6al_4v[Ti-6Al-4V (Grade 5, UN…]
    material_stal_st3[Ст3сп/Ст3пс (ГОСТ 380-…]
    izdelie_mptm -->|материал| material_copper
    izdelie_tpv_lenty -->|материал| material_al_6061_t6
    izdelie_svobodnoporshnevoi_stirling -->|материал| material_al_6061_t6
    izdelie_mmrtg -->|материал| material_aluminum
    izdelie_4h_sic_betavoltaik -->|материал| material_ti_6al_4v
    izdelie_marx_generator -->|материал| material_aluminum
    izdelie_termoelektricheskii_postoyannyi_magnit -->|материал| material_copper
    izdelie_termoelektricheskii_postoyannyi_magnit -->|материал| material_aluminum
    izdelie_vodorodnye_toplivnye_elementy -->|материал| material_aluminum
    izdelie_nasa_asc_e_srsc -->|материал| material_copper
    izdelie_nasa_asc_e_srsc -->|материал| material_al_6061_t6
    izdelie_asrg -->|материал| material_copper
    часть_mptm_generator -->|материал| material_copper
    часть_mptm_controls -->|материал| material_al_6061_t6
    часть_mptm_housing -->|материал| material_al_6061_t6
    часть_tpv_lenty_reflector -->|материал| material_al_6061_t6
    часть_tpv_lenty_cooling -->|материал| material_copper
    часть_zeno_power_am_241_housing -->|материал| material_al_6061_t6
    часть_svobodnoporshnevoi_stirling_piston -->|материал| material_al_6061_t6
    часть_tpv_cooling -->|материал| material_al_6061_t6
    часть_tpv_housing -->|материал| material_ti_6al_4v
    часть_mmrtg_housing -->|материал| material_al_6061_t6
    часть_mmrtg_connector -->|материал| material_al_6061_t6
    часть_4h_sic_betavoltaik_case -->|материал| material_ti_6al_4v
    часть_marx_generator_housing -->|материал| material_stal_st3
    часть_marx_generator_output_terminal -->|материал| material_copper
    часть_betavoltaiki_case -->|материал| material_ti_6al_4v
    часть_3d_sic_mikropillarnyi_tritii_betavoltaik_case -->|материал| material_ti_6al_4v
    часть_alyuminievo_vozdushnye_toplivnye_elementy_housing -->|материал| material_al_6061_t6
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot -->|материал| material_al_6061_t6
    часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold -->|материал| material_al_6061_t6
    часть_vodorodnye_toplivnye_elementy_end_plate -->|материал| material_ti_6al_4v
    часть_nasa_asc_e_srsc_cooler -->|материал| material_al_6061_t6
    часть_nasa_asc_e_srsc_alternator -->|материал| material_copper
    часть_asrg_cooler -->|материал| material_al_6061_t6
    часть_asrg_housing -->|материал| material_al_6061_t6
    izdelie_asrg_v28_ии -->|материал| material_al_6061_t6
    часть_asrg_v28_ии_housing -->|материал| material_al_6061_t6
    часть_t600_топливная_ячейка -->|материал| material_ti_6al_4v
    часть_t_x_топливная_ячейка_1 -->|материал| material_ti_6al_4v
    часть_t850_топливная_ячейка_1 -->|материал| material_ti_6al_4v
    часть_marcus_сердце_гибрид -->|материал| material_ti_6al_4v
    часть_marcus_топливная_ячейка -->|материал| material_ti_6al_4v
    часть_cameron_топливная_ячейка_1 -->|материал| material_ti_6al_4v
    часть_cameron_топливная_ячейка_2 -->|материал| material_ti_6al_4v
```

_Показаны 5 наиболее часто используемых материалов (полный список — в graph1_data.json)._

| Материал | Используется в частях |
|---|---:|
| `Al основа; Si 0.4–0.8 %; Mg 0.8–1.2 %; Cu 0.15–0.40 %; Cr 0.04–0.35 %; Fe ≤0.7 %; Mn ≤0.15 %; Zn ≤0.25 %; Ti ≤0.15 % — сплав 6061 (AlSi1MgCu, UNS A96061), состояние T6` | 19 |
| `Ti-6Al-4V (Grade 5, UNS R56400): Al 5.5–6.75 %, V 3.5–4.5 %, Fe ≤0.30 %, O ≤0.20 %, C ≤0.08 %, N ≤0.05 %, H ≤0.015 %, Y ≤0.005 %, Ti — остальное (ASTM-спецификация, Wikipedia/ASM)` | 13 |
| `нержавеющая сталь 316L (AISI 316L / UNS S31603 / EN 1.4404 X2CrNiMo17-12-2): Fe — остальное; Cr 16.0–18.0 %, Ni 10.0–14.0 %, Mo 2.0–3.0 %, C ≤0.03 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 % (Cleveland-Cliffs, ASTM A240)` | 10 |
| `Ni+Co 50.0–55.0; Cr 17.0–21.0; Fe баланс; Nb+Ta 4.75–5.50; Mo 2.80–3.30; Ti 0.65–1.15; Al 0.35–0.80; Co ≤1.0; C ≤0.08; Mn ≤0.35; Si ≤0.35; Cu ≤0.15; B 0.001–0.006; P ≤0.015; S ≤0.015` | 9 |
| `Cu ≥99.9% (электролитическая медь C11000/ETP)` | 8 |
| `нержавеющая сталь AISI 304 / EN 1.4301 (X5CrNi18-10): Cr 18.0–20.0 %, Ni 8.0–12.0 %, C ≤0.08 %, Mn ≤2.0 %, Si ≤0.75 %, P ≤0.045 %, S ≤0.030 %, N ≤0.10 %, Fe — остальное (Cleveland-Cliffs, ASTM A240)` | 8 |
| `SiC — стехиометрический карбид кремния (50 ат.% Si / 50 ат.% C); монокристалл 4H-SiC, n-легирование азотом (подложки) или высокочистый без легирования` | 8 |
| `Ni баланс; Cr 20.0–23.0; Mo 8.0–10.0; Nb+Ta 3.15–4.15; Fe ≤5.0; Co ≤1.0; C ≤0.10; Mn ≤0.50; Si ≤0.50; Al ≤0.40; Ti ≤0.40; P ≤0.015; S ≤0.015` | 5 |
| `W ≥99.95% (вольфрам, спечённый/кованый; примеси Mo, Fe <0.05%)` | 4 |
| `In(1-x)Ga(x)As(1-y)Sb(y) (InGaAsSb) на подложке GaSb: прямой запрет зоны 0.50–0.55 эВ (λcutoff ≈ 2.3–2.5 мкм), LPE/MBE-эпитаксия` | 4 |
| `Bi₂Te₃ (теллурид висмута; промышленные марки легированы: p-тип — Bi₀.₅Sb₁.₅Te₃ (Sb), n-тип — Bi₂Te₂.₇Se₀.₃ (Se); M = 800.8 г/моль)` | 4 |
| `PuO2 на основе изотопа Pu-238 (диоксид плутония-238): для RTG-топлива изотопная доля Pu-238 > 80 % (остальное Pu-239/Pu-240 и дочерние продукты распада, прежде всего U-234); стехиометрия O/Pu ≈ 2.00` | 4 |
| `Al ≥ 99.5 % (основа); Fe ≤ 0.40 %; Si ≤ 0.25 %; Cu ≤ 0.05 %; Mn ≤ 0.05 %; Mg ≤ 0.05 %; Zn ≤ 0.05–0.07 %; Ti ≤ 0.03–0.05 %; V ≤ 0.05 % — технически чистый алюминий 1050 (UNS A91050, EN AW-1050A)` | 4 |
| `Ni–YSZ кермет: Ni + 8YSZ ((ZrO₂)₀.₉₂(Y₂O₃)₀.₀₈); исходный анодный порошок NiO:YSZ 50:50–65:35 масс.% (Ni 28–55 об.% после восстановления); рабочее состояние — металлический Ni + керамический каркас кубического YSZ + пористость 25–40%` | 4 |
| `LSM-20: (La0.8Sr0.2)MnO3-δ — манганит лантана, легированный 20 мол.% Sr (перовскит ABO3); катодный композит LSM/YSZ — 50 wt% (La0.80Sr0.20)0.95MnO3-X + 50 wt% (Y2O3)0.08(ZrO2)0.92 (8YSZ)` | 4 |
