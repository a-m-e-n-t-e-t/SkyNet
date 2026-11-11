---
id: material_liquid_metal_polyalloy
тип: материал
класс: композит
химический_состав: 'жидкометаллический сплав галлия (Galinstan — 68.5% Ga, 21.5% In, 10% Sn, ρ=6.44 g/cm³) + нанесённый слоем 50-100 мкм на эластомерную полимерную подложку (silicone elastomer, Shore A 20-50); каталитически стабилизирован оксидной плёнкой Ga₂O₃ (3-5 нм) для смачиваемости и адгезии (IEEE Sensors 2023, Scientific Reports)'
кристаллическая_структура: 'аморфный жидкий металл (T_плав = -19 °C для Galinstan) + аморфный эластомер; слоистый композит: жидкий металл + эластичная матрица'
вариант_структуры: liquid_metal_elastomer_laminate
оптимальная_структура:
  структура: 'Galinstan (68.5% Ga, 21.5% In, 10% Sn) слоем 50-100 мкм на silicone-elastomer подложке; формирование оксидной плёнки Ga₂O₃ для адгезии'
  обоснование_выбора: 'Galinstan (ρ=6.44 g/cm³, IEEE Sensors 2023) — реальный жидкометаллический сплав при комнатной температуре, заменяет ртуть в термометрах и тактильных датчиках; в сочетании с эластомером даёт "mimetic" свойства: эластичность + электропроводимость + способность менять форму при механическом воздействии; IEEE Sensors 2023 — soft robotics applications'
  применение_по_умолчанию: эластомерная_оболочка_для_инфильтрации
  источник_обоснования: web_search
варианты_по_применению:
  эластомерная_оболочка_для_инфильтрации:
    марка: 'Galinstan + silicone-elastomer matrix (Shore A 20-50, MDPI Materials 2024) — 50-100 мкм покрытие; адаптировано из IEEE Sensors 2023 (soft robotics, stretchable electronics)'
    примечание: 'обеспечивает эластичность кожи + электропроводимость для сенсоров; НЕ обеспечивает полный шейпшифтинг (canon-декларация)'
  stretchable_электроника_и_сенсоры:
    марка: 'Galinstan microchannels (50-200 мкм) в PDMS-матрице (Sylgard 184); IEEE Sensors 2023 standard для эпидермальной электроники'
    примечание: 'применяется в soft-robotics и носимой электронике; деформация до 200% без потери проводимости'
  замена_ртути_в_термометрах_и_преобразователях:
    марка: 'Galinstan (Geratherm Medical, ASTM E2251) — стандарт для безопасных термометров'
    примечание: 'нетоксичная замена ртути; T_плав -19 °C, T_кип 1300 °C'
сравнение_структур:
  - 'Galinstan vs ртуть: Galinstan в 11x менее токсичен, T_плав ниже (-19 vs -38.8 °C), но в 1.5x менее плотный (6.44 vs 13.53 g/cm³)'
  - 'Galinstan+silicone vs Ga+Cu: галлий-медь интерметаллиды хрупкие (CuGa₂), в отличие от эластичной Galinstan+silicone комбинации'
  - 'Galinstan+silicone vs eGaIn (75.5% Ga, 24.5% In): eGaIn лучше для микро-электроники (ω=3.6×10⁶ S/m), Galinstan лучше для био-совместимости'
исследовательская_группа: 'IEEE Sensors Journal 23(11):11234-11245 (2023, Liu — Galinstan-embedded liquid metal elastomer composites); Scientific Reports 9:12473 (Li 2019, stretchable liquid metal electronics); MDPI Materials 17(6):1439 (Chan 2024, knitted powernet fabric + silicone); Geratherm Medical (Galinstan thermometer); ASTM E2251 (liquid-in-glass thermometers)'
стандарты:
  - ASTM E2251 (жидкостные термометры)
  - ISO 10993 (биосовместимость)
  - IEEE 2700-2018 (сенсоры)
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://ieeexplore.ieee.org/document/10071031
источник_дата: 2026-11-11
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_g_cm3:
    min: 6.40
    max: 6.50
  температурный_диапазон_C:
    min: -19
    max: 1300
  электропроводность_MS_m:
    min: 3.0
    max: 3.8
  вязкость_mPa_s:
    min: 2.0
    max: 2.4
наследуемые: {}
дополнительные: {}
дата_создания: 2026-11-11
дата_обновления: 2026-11-11
---
## Описание

Liquid metal polyalloy — слоистый композит из жидкометаллического сплава Galinstan (68.5% Ga, 21.5% In, 10% Sn, ρ=6.44 g/cm³) на эластомерной полимерной подложке (silicone elastomer, Shore A 20-50). Galinstan — нетоксичная замена ртути (T_плав -19 °C, T_кип 1300 °C, IEEE Sensors 2023).

В сочетании с эластомером даёт уникальные "mimetic" свойства: эластичность (деформация до 200% без потери электропроводимости), способность менять форму при механическом воздействии, биосовместимость (ISO 10993). Применяется в soft-robotics, stretchable электронике, носимых сенсорах (IEEE Sensors 2023) и протезных покрытиях.

В каноне Terminator (T-1000, T-X) — "mimetic polyalloy" описан как самостоятельный шейпшифтинговый материал. В реальности полный шейпшифтинг не реализован; current state-of-art ограничен эластомерными композитами с проводящими жидкометаллическими каналами.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| тип узла | материал | — | canon |


## Источники

- IEEE Sensors Journal 23(11):11234-11245 (Liu 2023 — liquid metal elastomer composites)
- Scientific Reports 9:12473 (Li 2019 — stretchable liquid metal electronics)
- MDPI Materials 17(6):1439 (Chan 2024 — knitted powernet fabric + silicone)
- Geratherm Medical — Galinstan thermometer manufacturer
- ASTM E2251 — liquid-in-glass thermometers
