---
id: material_pe_pp
тип: материал
класс: полимер
химический_состав: '(—C₂H₄—)ₙ PE / (—CH₂—CH(CH₃)—)ₙ PP — микропористые полиолефиновые сепараторные мембраны (монослой PP: Celgard 2400/2500; трёхслой PP/PE/PP: Celgard 2325)'
кристаллическая_структура: 'полукристаллический (PE — орторомбическая элементарная ячейка, изотактический PP — моноклинная α-фаза)'
вариант_структуры: layered_microporous_membrane
оптимальная_структура:
  структура: layered_microporous_membrane
  обоснование_выбора: 'Трёхслойная микропористая плёнка PP/PE/PP (Celgard 2325): внутренний PE-слой даёт shutdown при плавлении ~130–135 °C (поры закрываются — защита от теплового разгона), наружные PP-слои сохраняют механическую целостность (melt integrity) до 165 °C и окислительную стойкость к заряженному катоду — сочетание безопасности и целостности'
  применение_по_умолчанию: сепаратор_li_ion
  источник_обоснования: web_search
варианты_по_применению:
  трижды_pp_pe_pp_celgard_2325:
    описание: 'Трёхслойная микропористая мембрана PP/PE/PP (Celgard 2325), 25 мкм: внутренний PE-слой — shutdown при ~130–135 °C, наружные PP-слои — melt integrity до 165 °C и окислительная стойкость к заряженному катоду.'
    свойства: 'пористость 39 %; Gurley 645 s (JIS); прочность MD 1900 кгс/см² (≈186 МПа, typ), TD 150 кгс/см²; puncture 450 gf; термоусадка MD 3.0 % @90 °C/1ч; shutdown PE-слоя ~130 °C.'
    применение: 'сепараторы Li-ion аккумуляторов с требованием теплового shutdown (защита от теплового разгона при перезаряде/перегреве).'
    источник_url: https://www.canrud.com/knowledge/lab-equipment/celgard-2325-vs-2400-vs-2500-separator-comparison-197
  монослой_pp_celgard_2400:
    описание: 'Монослойная микропористая PP-мембрана (Celgard 2400), 25 мкм: нет shutdown — остаётся пористой до плавления PP ~165 °C (melt integrity), высокая окислительная стойкость.'
    свойства: 'пористость 41 %; Gurley 620 s (JIS); прочность MD 1420 кгс/см² (≈139 МПа, typ), TD 140 кгс/см²; puncture 450 gf; термоусадка MD 2.3 % @90 °C/1ч; поры 0.043×0.039 мкм.'
    применение: 'первичные Li-SOCl₂ элементы и системы, где shutdown не нужен (нет перезаряда/теплового разгона), но нужна окислительная стойкость.'
    источник_url: https://labcorematerials.com/resources/celgard-2325-vs-2400-separator-comparison
  монослой_pp_высокопористый_celgard_2500:
    описание: 'Монослойная PP-мембрана повышенной пористости (Celgard 2500), 25 мкм: пористость 55 % — сниженное ионное сопротивление и лучшая смачиваемость против 2400 при том же отсутствии shutdown.'
    свойства: 'пористость 55 %; Gurley 200 s (JIS); прочность MD 1170 кгс/см² (≈115 МПа, typ), TD 130 кгс/см²; puncture 325 gf; термоусадка MD 1.1 % @90 °C/1ч.'
    применение: 'Li-ion элементы с приоритетом энергетической плотности и низкого внутреннего сопротивления (power cells).'
    источник_url: https://www.canrud.com/knowledge/lab-equipment/celgard-2325-vs-2400-vs-2500-separator-comparison-197
сравнение_структур:
  монослой_pp:
    описание: 'Монослойная микропористая PP-мембрана (Celgard 2400: пористость 41 %, Gurley 620 s; 2500: 55 %, Gurley 200 s) — сухой процесс (растяжение).'
    свойства: 'нет shutdown — пориста до плавления PP ~165 °C; прочность MD 115–139 МПа; термоусадка MD ≤2.3 % @90 °C/1ч; в Li-SOCl₂ shutdown не нужен, а melt integrity 165 °C даёт запас против рабочего окна −55…+85 °C.'
    применение: 'первичные элементы (Li-SOCl₂), Li-ion с внешней тепловой защитой.'
    источник_url: https://www.canrud.com/knowledge/lab-equipment/celgard-2325-vs-2400-vs-2500-separator-comparison-197
  монослой_pe:
    описание: 'Монослойная PE-мембрана (мокрый процесс, тип Celgard 2730) — shutdown при плавлении PE ~130–135 °C.'
    свойства: 'плохая смачиваемость и низкая термостабильность против PP (C.T. Love 2011; Membrane Journal — усадка почти полная к 200 °C); дешевле; при нагреве в Li-ion shutdown компенсируется трижды-структурой PP/PE/PP.'
    применение: 'массовые Li-ion элементы потребительского класса — shutdown без затрат на трижды-структуру.'
    источник_url: https://www.researchgate.net/publication/305472165_In-depth_correlation_of_separator_pore_structure_and_electrochemical_performance_in_lithium-ion_batteries
  керамическое_покрытие:
    описание: 'PP/PE-мембрана с керамическим покрытием (Al₂O₃/AlOOH, 2–4 мкм на сторону) — гибрид полимер/керамика.'
    свойства: 'улучшенные смачиваемость и термостабильность; добавка 28–45 % к электрическому сопротивлению против чистого PP (сравнительное исследование покрытий); shutdown сохраняется.'
    применение: 'Li-ion с повышенными требованиями к безопасности (EV, стационарные накопители).'
    источник_url: https://www.researchgate.net/publication/317768544_A_comparative_study_on_polypropylene_separators_coated_with_different_inorganic_materials_for_lithium-ion_batteries
исследовательская_группа: null
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://www.celgard.com/product-data
источник_дата: 2026-11-10
источник_разбора: v9.62 cron F27b #971
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: {min: 895, max: 930, nominal: 910}
  прочность_МПа: {min: 115, max: 186, nominal: 139}
  предел_текучести_МПа: null
  модуль_упругости_ГПа: null
  коэффициент_Пуассона: {min: 0.42, max: 0.46, nominal: 0.44}
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: null
  температура_плавления_C: {min: 135, max: 165, nominal: 135}
  теплопроводность_W_mK: {min: 0.22, max: 0.33, nominal: 0.28}
  теплоёмкость_J_kgK: {min: 1900, max: 2300, nominal: 2000}
  коэффициент_термического_расширения_1_K: {min: 8.0e-05, max: 2.0e-04, nominal: 1.0e-04}
  электропроводность_S_m: {min: 1.0e-16, max: 1.0e-14, nominal: 1.0e-15}
дополнительные:
  рабочая_температура_C: '-40…+135'
  толщина_плёнки_мкм: 25
  пористость_процентов: {min: 39, max: 55, nominal: 41}
  поведение_при_перегреве: 'shutdown PE-слоя ~130–135 °C (поры закрываются); melt integrity PP-слоёв до 165 °C; полная потеря целостности при плавлении PP'
  примечание: 'Полиолефиновый сепаратор — электрический изолятор (ρ ~10¹⁴–10¹⁶ Ом·м) с ионной проницаемостью; смачиваемость электролитом улучшают керамическим покрытием Al₂O₃ или ПВХ-герметизацией'
дата_создания: 2026-11-09
дата_обновления: 2026-11-10
---
## Описание

Микропористые полиолефиновые сепараторные мембраны для литий-ионных и первичных элементов: трёхслойная PP/PE/PP (Celgard 2325) сочетает shutdown внутреннего PE-слоя при ~130–135 °C (поры закрываются — защита от теплового разгона) с melt integrity и окислительной стойкостью наружных PP-слоёв до 165 °C; монослойные PP-мембраны (Celgard 2400 — пористость 41 %, 2500 — 55 %) не дают shutdown, но остаются пористыми до плавления ~165 °C. Толщина 25 мкм, прочность MD 115–186 МПа (ориентированная плёнка, анизотропия MD/TD ~10×), электрический изолятор с ионной проницаемостью; смачиваемость электролитом улучшают керамическим покрытием Al₂O₃.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| тип узла | материал | — | canon |


## Источники

- Celgard — Battery Separator Products & Literature (2400 PP 41 %, 2500 PP 55 %, 2325 PP/PE/PP 39 %, 25 мкм): https://www.celgard.com/product-data
- Celgard 2325 Trilayer Microporous Membrane — Commercial Product Data Sheet (2025-02): https://www.celgard.com/storage/components/2325_com_data_2025-02.pdf
- Celgard 2400 Monolayer Membrane — Commercial Product Data Sheet (2025-02): https://www.celgard.com/storage/components/2400_com_data_2025-02.pdf
- Canrud — Celgard 2325 vs 2400 vs 2500 Separator Comparison (2325: MD 1900 кгс/см², Gurley 645 s, shutdown ~130 °C; 2400: MD 1420, 620 s; 2500: MD 1170, 55 %, 200 s): https://www.canrud.com/knowledge/lab-equipment/celgard-2325-vs-2400-vs-2500-separator-comparison-197
- LabCore — Celgard 2325 vs 2400 (поры 2325 0.209×0.054 мкм, 2400 0.043×0.039 мкм; puncture 5.0/4.5 N; термоусадка <4 % @105 °C/1ч): https://labcorematerials.com/resources/celgard-2325-vs-2400-separator-comparison
- In-depth correlation of separator pore structure and electrochemical performance (ResearchGate — PE: poor wettability/thermal stability): https://www.researchgate.net/publication/305472165_In-depth_correlation_of_separator_pore_structure_and_electrochemical_performance_in_lithium-ion_batteries
- A comparative study on polypropylene separators coated with different inorganic materials (ResearchGate — покрытие +28–45 % сопротивления): https://www.researchgate.net/publication/317768544_A_comparative_study_on_polypropylene_separators_coated_with_different_inorganic_materials_for_lithium-ion_batteries
- PlasticsEurope — Polyolefins (ρ PP 0.895–0.92 г/см³): https://plasticseurope.org/plastics-explained/a-large-family/polyolefins
- Alfa-Chemistry — Plastic Thermal Conductivity Reference Table (PE LD 0.33 / PE HD 0.44 W/m·K): https://www.alfa-chemistry.com/plastics/resources/plastic-thermal-conductivity-reference-table.html
- Patti A. et al. — Thermal Conductivity of Polypropylene-Based Materials (PP 0.11 W/mK @25 °C; IntechOpen 2019): https://www.intechopen.com/chapters/65584

PE/PP многослойный сепаратор (Celgard)
