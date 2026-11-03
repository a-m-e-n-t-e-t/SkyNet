---
id: izdelie_memristornye_matritsy
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: memristor_массив
стандарты: []
исследовательская_группа: hp_labs
родитель: null
дочерние_части:
  - часть_memristornye_matritsy_crossbar
  - часть_memristornye_matritsy_word_drivers
  - часть_memristornye_matritsy_bit_sense
  - часть_memristornye_matritsy_adc
  - часть_memristornye_matritsy_controller
материалы_частей:
  - часть: часть_memristornye_matritsy_crossbar
    материал: tio2_memristor
    доля_массы: 0.28
  - часть: часть_memristornye_matritsy_word_drivers
    материал: silicon_wafer
    доля_массы: 0.18
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
          min: 0.005
          max: 0.05
          nominal: 0.01
  габариты_mm:
          l: 12
          w: 12
          h: 1
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.05
          max: 0.5
          nominal: 0.2
наследуемые: {}
дополнительные: 
  технология: memristor crossbar
  источник: HP Labs research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: мемристорные матрицы

## Описание

мемристорные матрицы (RRAM)

Полное наименование (как в CSV): `мемристорные матрицы (RRAM)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    memristornye_matrits["izdelie_memristornye_matritsy"]
    memristornye_matritsy_cro["часть_memristornye_matritsy_crossbar"]
    memristornye_matrits --> memristornye_matritsy_cro
    memristornye_matritsy_wor["часть_memristornye_matritsy_word_drivers"]
    memristornye_matrits --> memristornye_matritsy_wor
    memristornye_matritsy_bit["часть_memristornye_matritsy_bit_sense"]
    memristornye_matrits --> memristornye_matritsy_bit
    memristornye_matritsy_adc["часть_memristornye_matritsy_adc"]
    memristornye_matrits --> memristornye_matritsy_adc
    memristornye_matritsy_con["часть_memristornye_matritsy_controller"]
    memristornye_matrits --> memristornye_matritsy_con
```
