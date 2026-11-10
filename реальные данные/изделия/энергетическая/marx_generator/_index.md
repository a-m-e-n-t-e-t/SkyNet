---
id: izdelie_marx_generator
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: импульсный_генератор_Маркса
стандарты: 
  - IEEE C57.12.00
исследовательская_группа: general_electric
родитель: null
дочерние_части:
  - часть_marx_generator_capacitors
  - часть_marx_generator_spark_gaps
  - часть_marx_generator_resistors
  - часть_marx_generator_housing
  - часть_marx_generator_output_terminal
  - часть_marx_generator_insulator
материалы_частей:
  - часть: часть_marx_generator_capacitors
    материал: batio3
    форма: HV_керамика_N4700_класс_I
    доля_массы: 0.2
  - часть: часть_marx_generator_housing
    материал: stal_st3
    форма: строительные_конструкции_и_крепёж
    доля_массы: 0.24
  - часть: часть_marx_generator_spark_gaps
    материал: oksid_alyuminiya
    форма: высоковольтные_изоляторы
    доля_массы: 0.1
  - часть: часть_marx_generator_insulator
    материал: oksid_alyuminiya
    форма: высоковольтные_изоляторы
    доля_массы: 0.037
  - часть: часть_marx_generator_output_terminal
    материал: copper
    форма: шины_и_заземление
    доля_массы: 0.0202
  - часть: часть_marx_generator_resistors
    материал: nichrome
    форма: nikrothal_80_wire_heating
    доля_массы: 0.04
# F29 B-BOM: агрегация (материал, форма) по частям; доли = масса_части/500 кг
# (100→0.2; 120→0.24; 50→0.1; 18.5→0.037; 10.1→0.0202; 20→0.04);
# oksid_alyuminiya объединяет spark_gaps+insulator (0.137)
наследуемые_материалы:
  - материал: batio3
    форма: HV_керамика_N4700_класс_I
    суммарная_доля_массы: 0.2
    источники_частей:
      - часть_marx_generator_capacitors
  - материал: stal_st3
    форма: строительные_конструкции_и_крепёж
    суммарная_доля_массы: 0.24
    источники_частей:
      - часть_marx_generator_housing
  - материал: oksid_alyuminiya
    форма: высоковольтные_изоляторы
    суммарная_доля_массы: 0.137
    источники_частей:
      - часть_marx_generator_spark_gaps
      - часть_marx_generator_insulator
  - материал: copper
    форма: шины_и_заземление
    суммарная_доля_массы: 0.0202
    источники_частей:
      - часть_marx_generator_output_terminal
  - материал: nichrome
    форма: nikrothal_80_wire_heating
    суммарная_доля_массы: 0.04
    источники_частей:
      - часть_marx_generator_resistors
# F27e: технология обработки каждой части (файлы технологии/ существуют — F27c)
технологии_частей:
  - часть: часть_marx_generator_capacitors
    технология: tape_casting
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: batio3
        роль: обрабатываемый
  - часть: часть_marx_generator_housing
    технология: shtampovka_listovaya
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: stal_st3
        роль: обрабатываемый
  - часть: часть_marx_generator_spark_gaps
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: oksid_alyuminiya
        роль: обрабатываемый
  - часть: часть_marx_generator_insulator
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: oksid_alyuminiya
        роль: обрабатываемый
  - часть: часть_marx_generator_output_terminal
    технология: tokarnaya_obrabotka_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_marx_generator_resistors
    технология: volochenie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: nichrome
        роль: обрабатываемый
# F-scal (P087 §12.6): масштабирование Marx — каскады, импульсные параметры
масштабируемость:
  режим: масштабируемая
  параметры: [масса_kg, выработка_тепла_W]
  пределы:
    min: {масса_kg: 50, выработка_тепла_W: 10}
    max: {масса_kg: 5000, выработка_тепла_W: 1000}
  закон_масштабирования:
    масса: '≈ линейный от числа каскадов (125 конденсаторов; масса ∝ N ступеней)'
    импульсные_параметры: 'V_импульс ∝ числу ступеней N; ток I_импульс ограничен коммутацией искровых промежутков (~10 кА)'
  ограничивающие_части:
    - часть: часть_marx_generator_capacitors
      причина: 'дерейтинг 60–70% от 50 кВ (N4700 Class I) задаёт запас по напряжению ступени'
    - часть: часть_marx_generator_spark_gaps
      причина: 'пробивное напряжение и пиковый ток ~10 кА тригатронов ограничивают импульс'
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
          min: 50
          max: 5000
          nominal: 500
  габариты_mm:
          l: 1000
          w: 800
          h: 1650
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 10
          max: 1000
          nominal: 100
наследуемые: {}
дополнительные: 
  V_импульс_kV: 1000
  I_импульс_kA: 100
  источник: Marx generator heritage
дата_создания: 2026-11-03
дата_обновления: 2026-11-10
источник: user_input
источник_разбора: пользовательский ввод
---
## Описание

Marx generator

Полное наименование (как в CSV): `Marx generator`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | canon |
| подтип | импульсный_генератор_Маркса | — | canon |
| масса | 50–5000 (номинал 500) | kg | canon |
| габариты (Д×Ш×В) | 1000×800×1650 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 10–1000 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Требует описания на основе инженерного анализа.

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые материалы

- `batio3` (форма: HV_керамика_N4700_класс_I) → [`batio3`](../../../материалы/batio3.md)
- `tungsten` (форма: электроды_искровых_промежутков) → [`tungsten`](../../../материалы/tungsten.md)
- `aluminum` → [`aluminum`](../../../материалы/aluminum.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_marx_generator["izdelie_marx_generator"]
    ______marx_generator_capacitors["часть_marx_generator_capacitors"]
    izdelie_marx_generator --> ______marx_generator_capacitors
    ______marx_generator_spark_gaps["часть_marx_generator_spark_gaps"]
    izdelie_marx_generator --> ______marx_generator_spark_gaps
    ______marx_generator_resistors["часть_marx_generator_resistors"]
    izdelie_marx_generator --> ______marx_generator_resistors
    ______marx_generator_housing["часть_marx_generator_housing"]
    izdelie_marx_generator --> ______marx_generator_housing
    ______marx_generator_output_terminal["часть_marx_generator_output_terminal"]
    izdelie_marx_generator --> ______marx_generator_output_terminal
    ______marx_generator_insulator["часть_marx_generator_insulator"]
    izdelie_marx_generator --> ______marx_generator_insulator
```
