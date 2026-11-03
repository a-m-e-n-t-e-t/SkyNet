---
id: izdelie_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: планетарный_роликовинт
стандарты: 
  - DIN 69051
исследовательская_группа: gsk_rollvis
родитель: null
дочерние_части:
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals
  - часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing
материалы_частей:
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw
    материал: bearing_steel_52100
    доля_массы: 0.38
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers
    материал: bearing_steel_52100
    доля_массы: 0.19
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut
    материал: bearing_steel_52100
    доля_массы: 0.38
  - часть: часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings
    материал: stainless_steel_440c
    доля_массы: 0.09
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
          min: 0.5
          max: 50
          nominal: 5
  габариты_mm:
          l: 300
          w: 80
          h: 80
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 20
наследуемые: {}
дополнительные: 
  M_ном_Нм: 100
  V_линейная_мм_с: 1000
  источник: GSK / Rollvis planetary roller screw
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: планетарные роликовинтовые электроприводы с неодимовыми магнитами

## Описание

планетарные роликовинтовые электроприводы с неодимовыми магнитами

Полное наименование (как в CSV): `планетарные роликовинтовые электроприводы с неодимовыми магнитами`

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
    planetarnye_rolikovi["izdelie_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami"]
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_screw"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_rollers"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_nut"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_bearings"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_seals"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
    planetarnye_rolikovintovy["часть_planetarnye_rolikovintovye_elektroprivody_s_neodimovymi_magnitami_housing"]
    planetarnye_rolikovi --> planetarnye_rolikovintovy
```
