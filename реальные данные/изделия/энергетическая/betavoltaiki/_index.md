---
id: izdelie_betavoltaiki
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: бетавольтаик
стандарты: 
  - ISO 2919
исследовательская_группа: widetronix
родитель: null
дочерние_части:
  - часть_betavoltaiki_isotope
  - часть_betavoltaiki_semiconductor
  - часть_betavoltaiki_encapsulant
  - часть_betavoltaiki_case
  - часть_betavoltaiki_terminal
материалы_частей:
  - часть: часть_betavoltaiki_isotope
    материал: ni63_metal
    доля_массы: 0.285
  - часть: часть_betavoltaiki_semiconductor
    материал: silicon_carbide
    доля_массы: 0.475
  - часть: часть_betavoltaiki_encapsulant
    материал: epoxy
    доля_массы: 0.095
  - часть: часть_betavoltaiki_case
    материал: titanium_alloy
    доля_массы: 0.285
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
          min: 0.01
          max: 0.1
          nominal: 0.05
  габариты_mm:
          l: 25
          w: 25
          h: 5
  выработка_энергии_W:
          min: 1e-05
          max: 0.001
          nominal: 0.0001
  выработка_тепла_W:
          min: 0
          max: 0
          nominal: 0
наследуемые: {}
дополнительные: 
  изотоп: Ni-63 / H-3
  T_жизни_лет: 50
  источник: Widetronix betavoltaic
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Бетавольтаики

## Описание

Бетавольтаики

Полное наименование (как в CSV): `Бетавольтаики`

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
    betavoltaiki["izdelie_betavoltaiki"]
    betavoltaiki_isotope["часть_betavoltaiki_isotope"]
    betavoltaiki --> betavoltaiki_isotope
    betavoltaiki_semiconducto["часть_betavoltaiki_semiconductor"]
    betavoltaiki --> betavoltaiki_semiconducto
    betavoltaiki_encapsulant["часть_betavoltaiki_encapsulant"]
    betavoltaiki --> betavoltaiki_encapsulant
    betavoltaiki_case["часть_betavoltaiki_case"]
    betavoltaiki --> betavoltaiki_case
    betavoltaiki_terminal["часть_betavoltaiki_terminal"]
    betavoltaiki --> betavoltaiki_terminal
```
