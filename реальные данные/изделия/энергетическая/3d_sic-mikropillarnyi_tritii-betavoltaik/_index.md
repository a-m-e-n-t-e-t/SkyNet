---
id: izdelie_3d_sic-mikropillarnyi_tritii-betavoltaik
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: бета_вольтаик_3D_SiC
стандарты: []
исследовательская_группа: university_research
родитель: null
дочерние_части:
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case
материалы_частей:
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
    материал: tritium_gas
    доля_массы: 0.19
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
    материал: silicon_carbide
    доля_массы: 0.38
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
    материал: silicon_carbide
    доля_массы: 0.297
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
          min: 0.001
          max: 0.01
          nominal: 0.003
  габариты_mm:
          l: 10
          w: 10
          h: 1
  выработка_энергии_W:
          min: 0.0001
          max: 0.01
          nominal: 0.001
  выработка_тепла_W:
          min: 0
          max: 0
          nominal: 0
наследуемые: {}
дополнительные: 
  изотоп: H-3 (tritium)
  T_жизни_лет: 12
  источник: 3D micropillar 4H-SiC tritium research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: 3D SiC-микропилларный тритий-бетавольтаик

## Описание

3D SiC-микропилларный тритий-бетавольтаик

Полное наименование (как в CSV): `3D SiC-микропилларный тритий-бетавольтаик`

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
    3d_sic-mikropillarny["izdelie_3d_sic-mikropillarnyi_tritii-betavoltaik"]
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
```
