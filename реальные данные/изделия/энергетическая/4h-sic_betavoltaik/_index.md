---
id: izdelie_4h-sic_betavoltaik
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
  - часть_4h-sic_betavoltaik_isotope
  - часть_4h-sic_betavoltaik_sic_diode
  - часть_4h-sic_betavoltaik_substrate
  - часть_4h-sic_betavoltaik_encapsulant
  - часть_4h-sic_betavoltaik_case
материалы_частей:
  - часть: часть_4h-sic_betavoltaik_isotope
    материал: ni63_metal
    доля_массы: 0.2375
  - часть: часть_4h-sic_betavoltaik_sic_diode
    материал: silicon_carbide
    доля_массы: 0.475
  - часть: часть_4h-sic_betavoltaik_substrate
    материал: silicon_carbide
    доля_массы: 0.198
  - часть: часть_4h-sic_betavoltaik_encapsulant
    материал: epoxy
    доля_массы: 0.095
  - часть: часть_4h-sic_betavoltaik_case
    материал: ti-6al-4v
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
  источник: 4H-SiC betavoltaic research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: 4H-SiC бетавольтаик

## Описание

4H-SiC бетавольтаик

Полное наименование (как в CSV): `4H-SiC бетавольтаик`

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
    4h-sic_betavoltaik["izdelie_4h-sic_betavoltaik"]
    4h-sic_betavoltaik_isotop["часть_4h-sic_betavoltaik_isotope"]
    4h-sic_betavoltaik --> 4h-sic_betavoltaik_isotop
    4h-sic_betavoltaik_sic_di["часть_4h-sic_betavoltaik_sic_diode"]
    4h-sic_betavoltaik --> 4h-sic_betavoltaik_sic_di
    4h-sic_betavoltaik_substr["часть_4h-sic_betavoltaik_substrate"]
    4h-sic_betavoltaik --> 4h-sic_betavoltaik_substr
    4h-sic_betavoltaik_encaps["часть_4h-sic_betavoltaik_encapsulant"]
    4h-sic_betavoltaik --> 4h-sic_betavoltaik_encaps
    4h-sic_betavoltaik_case["часть_4h-sic_betavoltaik_case"]
    4h-sic_betavoltaik --> 4h-sic_betavoltaik_case
```
