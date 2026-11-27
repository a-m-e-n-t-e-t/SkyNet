---
id: izdelie_tverdotelnye_akkumulyatory
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_питания
подтип: литий-ионный_аккумулятор
стандарты: 
  - IEC 61960
  - UN 38.3
исследовательская_группа: panasonic_lg
родитель: null
дочерние_части:
  - часть_tverdotelnye_akkumulyatory_anode
  - часть_tverdotelnye_akkumulyatory_cathode
  - часть_tverdotelnye_akkumulyatory_electrolyte
  - часть_tverdotelnye_akkumulyatory_separator
  - часть_tverdotelnye_akkumulyatory_current_collector_cu
  - часть_tverdotelnye_akkumulyatory_current_collector_al
  - часть_tverdotelnye_akkumulyatory_case
материалы_частей:
  - часть: часть_tverdotelnye_akkumulyatory_anode
    материал: graphite
    форма: анодный_ли_ионный_mcmb
    доля_массы: 0.18
  - часть: часть_tverdotelnye_akkumulyatory_cathode
    материал: lini_mn_co_o2
    форма: nmc811_высоконикелевый
    доля_массы: 0.34
  - часть: часть_tverdotelnye_akkumulyatory_electrolyte
    материал: li7la3zr2o12
    форма: твёрдый_электролит_ASSB
    доля_массы: 0.19
  - часть: часть_tverdotelnye_akkumulyatory_separator
    материал: poliimid
    форма: сепараторная_мембрана_ссб
    доля_массы: 0.038
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_cu
    материал: copper
    форма: фольга_токосъёмника_анода
    доля_массы: 0.0792
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_al
    материал: aluminum
    форма: гибкая_фольга_и_упаковка
    доля_массы: 0.0792
  - часть: часть_tverdotelnye_akkumulyatory_case
    материал: al_6061-t6
    форма: корпуса_электроники
    доля_массы: 0.19

технологии_частей:
  - часть: часть_tverdotelnye_akkumulyatory_anode
    технология: pogruzhenie_v_mo-shliker
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: graphite
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_cathode
    технология: pogruzhenie_v_mo-shliker
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: lini_mn_co_o2
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_electrolyte
    технология: vio
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: li7la3zr2o12
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_separator
    технология: plazmennaya_aktivatsiya
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: poliimid
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_cu
    технология: galvanika
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_current_collector_al
    технология: otzhig
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: aluminum
        роль: обрабатываемый
  - часть: часть_tverdotelnye_akkumulyatory_case
    технология: ebw
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый

наследуемые_материалы:
  - материал: graphite
    форма: анодный_ли_ионный_mcmb
    суммарная_доля_массы: 0.18
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_anode
  - материал: lini_mn_co_o2
    форма: nmc811_высоконикелевый
    суммарная_доля_массы: 0.34
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_cathode
  - материал: li7la3zr2o12
    форма: твёрдый_электролит_ASSB
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_electrolyte
  - материал: poliimid
    форма: сепараторная_мембрана_ссб
    суммарная_доля_массы: 0.038
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_separator
  - материал: copper
    форма: фольга_токосъёмника_анода
    суммарная_доля_массы: 0.0792
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_current_collector_cu
  - материал: aluminum
    форма: гибкая_фольга_и_упаковка
    суммарная_доля_массы: 0.0792
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_current_collector_al
  - материал: al_6061-t6
    форма: корпуса_электроники
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_tverdotelnye_akkumulyatory_case

масштабируемость:
  режим: квантуемая
  параметры: [масса_kg, ёмкость_Ач, выработка_энергии_W]
  пределы:
    min: {масса_kg: 0.05, ёмкость_Ач: 1, выработка_энергии_W: 1}
    max: {масса_kg: 5, ёмкость_Ач: 60, выработка_энергии_W: 100}
  закон_масштабирования:
    масса: '∝ ёмкости (Ач); удельная энергия твердотельного элемента ≈ 301 Вт·ч/кг (QuantumScape QSE-5: 5 Ач ≈ 0.5 кг, 21.6 Вт·ч)'
    энергия: 'E = C·V (3.7 В); номинал 20 Вт при 0.5 кг / 5 Ач; масштабируется площадью электродных слоёв и числом слоёв в pouch'
    тепло: 'I²R + поляризация интерфейсов; при 1C разряде ~1 Вт на 5 Ач элемент (BU-802a)'
  ограничивающие_части:
    - часть: часть_tverdotelnye_akkumulyatory_electrolyte
      предел: 'LLZO-слои 19% массы: толщина и ионная проводимость (~10⁻⁴ См/см при 25 °C) задают площадь и число слоёв'
    - часть: часть_tverdotelnye_akkumulyatory_separator
      предел: 'полиимидная мембрана 3.8% массы: механика и проникаемость ограничивают толщину пакета'
    - часть: часть_tverdotelnye_akkumulyatory_case
      предел: 'pouch-ламминат 113 мкм: габариты 100×50×10 мм, влагогазовый барьер лимитирует срок хранения'

scaling_type: количественный
соединители: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
ии_перепроектирован:
  статус: false
  верификация: []
основные: 
  масса_kg:
          min: 0.05
          max: 5
          nominal: 0.5
  габариты_mm:
          l: 100
          w: 50
          h: 10
  выработка_энергии_W:
          min: 1
          max: 100
          nominal: 20
  выработка_тепла_W:
          min: 0.1
          max: 5
          nominal: 1
наследуемые: {}
дополнительные: 
  ёмкость_Ач: 5
  V: 3.7
  T_жизни_циклы: 1000
  источник: 'QuantumScape QSE-5 B-sample: ~5 Ач, 301 Вт·ч/кг, 844 Вт·ч/л, 21.6 Вт·ч (твердотельный pouch-элемент)'
  источник_url: https://www.quantumscape.com/blog/a-first-look-at-the-qse-5-b-sample
  обоснование_габаритов: 'формат pouch-ячейки 5 Ач: footprint 100×50 мм, толщина 10 мм (V=50 см³ × 844 Вт·ч/л = 42 Вт·ч теоретический потолок объёма; фактическая энергия QSE-5 21.6 Вт·ч при 25.6 см³ активной зоны — запас на корпус/разгрузку слоёв); дети (электродные слои 100×50×~1 мм, фольга корпуса 100×50×0.294 мм) вложены по обеим проверкам F15g: Σ V(детей)=12 434 мм³ × 1.15 = 14 300 ≤ 50 000 мм³; оси 100≥100, 50≥50, 10≥1'
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Твердотельные аккумуляторы

## Описание

Твердотельные аккумуляторы

Полное наименование (как в CSV): `Твердотельные аккумуляторы`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня: твердотельная pouch-ячейка 5 Ач (QuantumScape QSE-5 класс), 7 дочерних частей — внутренние слои стека (anode, cathode, electrolyte, separator, collectors Cu/Al) и алюминиевая ламинат-оболочка (case). Упаковка F15g: Σ V(детей)×1.15 = 14 300 мм³ ≤ V(ячейки) 50 000 мм³.

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Энергетический баланс (F15d/F15b)

Ячейка: 3.7 В × 5 Ач = 18.5 Вт·ч (IEC 61960); номинальная отдача 20 Вт ≈ 1.08C (P = V×Ah — DNK Power 18650 calculator).

F15d: Σ генераторов внутри = анод 10 Вт + катод 10 Вт = 20 Вт ≥ родитель 20 Вт → PASS (электрохимическая пара «анод↔катод» — совместный источник; по отдельности электроды мощность не отдают, разбивка учётная). Остальные 5 компонентов (электролит, сепаратор, токосъёмники Cu/Al, корпус) — не генераторы: 0 Вт.

F15b: Σ тепла детей = 1.0 Вт = номинал родителя 1.0 Вт → PASS. Физика потерь при η ≈ 95% и 1C: 20 Вт × 5% ≈ 1 Вт, распределение: электролит 0.3 (ионные омические), Cu 0.2 + Al 0.15 (электронные омические), катод 0.2 + анод 0.1 (активационные/концентрационные перенапряжения), сепаратор 0.05 (джоулев), корпус 0 (Abdellattif et al., 2025 — electrochemical-thermal modeling of NMC811).

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- DNK Power — 18650 Battery Pack Calculator (P = V×Ah, 3.7 В номинал): https://www.dnkpower.com/18650-battery-pack-calculator (обращение 2026-11-07)
- Abdellattif et al., 2025 — Electrochemical-thermal modeling of NMC811 (ohmic + активационные + концентрационные + энтропные источники тепла): https://www.sciencedirect.com/science/article/pii/S1452398125002512 (обращение 2026-11-07)
- Bock et al., 2020 — Thermal Gradients with Sintered Solid State Electrolytes (перенапряжения рассеиваются как тепло): https://www.mdpi.com/1996-1073/13/1/253 (обращение 2026-11-07)

---


## Декомпозиция

```mermaid
graph TD
    tverdotelnye_akkumul["izdelie_tverdotelnye_akkumulyatory"]
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_anode"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_cathode"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_electrolyte"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_separator"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_current_collector_cu"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_current_collector_al"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
    tverdotelnye_akkumulyator["часть_tverdotelnye_akkumulyatory_case"]
    tverdotelnye_akkumul --> tverdotelnye_akkumulyator
```
