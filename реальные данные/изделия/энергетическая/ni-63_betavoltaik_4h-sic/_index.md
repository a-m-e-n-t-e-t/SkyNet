---
id: izdelie_ni-63_betavoltaik_4h-sic
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: бета_вольтаик_SiC
стандарты: 
  - ISO 2919
исследовательская_группа: widetronix
родитель: null
дочерние_части:
  - часть_ni-63_betavoltaik_4h-sic_isotope
  - часть_ni-63_betavoltaik_4h-sic_sic_diode
  - часть_ni-63_betavoltaik_4h-sic_substrate
  - часть_ni-63_betavoltaik_4h-sic_encapsulant
  - часть_ni-63_betavoltaik_4h-sic_case
материалы_частей:
  - часть: часть_ni-63_betavoltaik_4h-sic_isotope
    материал: ni63_metal
    доля_массы: 0.2375
  - часть: часть_ni-63_betavoltaik_4h-sic_sic_diode
    материал: silicon_carbide
    доля_массы: 0.475
  - часть: часть_ni-63_betavoltaik_4h-sic_substrate
    материал: silicon_carbide
    доля_массы: 0.198
  - часть: часть_ni-63_betavoltaik_4h-sic_encapsulant
    материал: epoxy
    доля_массы: 0.095
  - часть: часть_ni-63_betavoltaik_4h-sic_case
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
          min: 0.005
          max: 0.05
          nominal: 0.01
  габариты_mm:
          l: 20
          w: 20
          h: 2
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
  изотоп: Ni-63
  T_жизни_лет: 100
  источник: Widetronix 4H-SiC betavoltaic
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Ni-63 бетавольтаик 4H-SiC

## Описание

Ni-63 бетавольтаик 4H-SiC

Полное наименование (как в CSV): `Ni-63 бетавольтаик 4H-SiC`

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
    ni-63_betavoltaik_4h["izdelie_ni-63_betavoltaik_4h-sic"]
    ni-63_betavoltaik_4h-sic_["часть_ni-63_betavoltaik_4h-sic_isotope"]
    ni-63_betavoltaik_4h --> ni-63_betavoltaik_4h-sic_
    ni-63_betavoltaik_4h-sic_["часть_ni-63_betavoltaik_4h-sic_sic_diode"]
    ni-63_betavoltaik_4h --> ni-63_betavoltaik_4h-sic_
    ni-63_betavoltaik_4h-sic_["часть_ni-63_betavoltaik_4h-sic_substrate"]
    ni-63_betavoltaik_4h --> ni-63_betavoltaik_4h-sic_
    ni-63_betavoltaik_4h-sic_["часть_ni-63_betavoltaik_4h-sic_encapsulant"]
    ni-63_betavoltaik_4h --> ni-63_betavoltaik_4h-sic_
    ni-63_betavoltaik_4h-sic_["часть_ni-63_betavoltaik_4h-sic_case"]
    ni-63_betavoltaik_4h --> ni-63_betavoltaik_4h-sic_
```
