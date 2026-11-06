---
id: izdelie_svobodnoporshnevoi_stirling
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: свободнопоршневой_Стирлинг
стандарты: []
исследовательская_группа: sunpower_infinia
родитель: null
дочерние_части:
  - часть_svobodnoporshnevoi_stirling_heater
  - часть_svobodnoporshnevoi_stirling_regenerator
  - часть_svobodnoporshnevoi_stirling_cooler
  - часть_svobodnoporshnevoi_stirling_piston
  - часть_svobodnoporshnevoi_stirling_alternator
  - часть_svobodnoporshnevoi_stirling_gas_spring
материалы_частей:
  - часть: часть_svobodnoporshnevoi_stirling_heater
    материал: inconel_718
    доля_массы: 0.19
  - часть: часть_svobodnoporshnevoi_stirling_piston
    материал: inconel_718
    доля_массы: 0.27
  - часть: часть_svobodnoporshnevoi_stirling_alternator
    материал: copper
    доля_массы: 0.24
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
          min: 1
          max: 50
          nominal: 10
  габариты_mm:
          l: 300
          w: 200
          h: 200
  выработка_энергии_W:
          min: 100
          max: 1000
          nominal: 500
  выработка_тепла_W:
          min: 200
          max: 2000
          nominal: 1000
наследуемые: {}
дополнительные: 
  T_нагрев_C: 650
  КПД_процентов: 30
  источник: Sunpower free-piston Stirling
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Свободнопоршневой Стирлинг

## Описание

Свободнопоршневой Стирлинг (FPSE)

Полное наименование (как в CSV): `Свободнопоршневой Стирлинг (FPSE)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
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
    svobodnoporshnevoi_s["izdelie_svobodnoporshnevoi_stirling"]
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_heater"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_regenerator"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_cooler"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_piston"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_alternator"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
    svobodnoporshnevoi_stirli["часть_svobodnoporshnevoi_stirling_gas_spring"]
    svobodnoporshnevoi_s --> svobodnoporshnevoi_stirli
```
