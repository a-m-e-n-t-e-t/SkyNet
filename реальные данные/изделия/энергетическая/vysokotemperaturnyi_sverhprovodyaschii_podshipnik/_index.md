---
id: izdelie_vysokotemperaturnyi_sverhprovodyaschii_podshipnik
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: HTS_подшипник
стандарты: 
  - ISO 15241
исследовательская_группа: boeing_nasa
родитель: null
дочерние_части:
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing
материалы_частей:
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element
    материал: ybco_bulk
    доля_массы: 0.285
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet
    материал: ndfeb
    доля_массы: 0.38
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat
    материал: stainless_steel_316
    доля_массы: 0.38
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft
    материал: titanium_alloy
    доля_массы: 0.095
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
          l: 200
          w: 200
          h: 100
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 1
          nominal: 0.1
наследуемые: {}
дополнительные: 
  T_рабочая_C: -196
  N_критическая_об_мин: 10000
  источник: Boeing HTS bearing research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Высокотемпературный сверхпроводящий подшипник

## Описание

Высокотемпературный сверхпроводящий подшипник (HTS)

Полное наименование (как в CSV): `Высокотемпературный сверхпроводящий подшипник (HTS)`

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
    vysokotemperaturnyi_["izdelie_vysokotemperaturnyi_sverhprovodyaschii_podshipnik"]
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
```
