---
id: izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: приводная_система
подтип: прочее
стандарты: 
  - IEC 60034
  - ISO 1940
исследовательская_группа: maxon_faulhaber
родитель: null
дочерние_части:
  - часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core
  - часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
  - часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors
  - часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting
материалы_частей:
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core
    материал: generic_material
    доля_массы: 0.45
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
    материал: aluminum
    доля_массы: 0.27
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
          max: 50
          nominal: 1
  габариты_mm:
          l: 100
          w: 50
          h: 50
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.1
          max: 50
          nominal: 5
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: гидравлические искусственные мышцы МакКиббена

## Описание

гидравлические искусственные мышцы МакКиббена

Полное наименование (как в CSV): `гидравлические искусственные мышцы МакКиббена`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | classify_subsystem |
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
    gidravlicheskie_isku["izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena"]
    gidravlicheskie_iskusstve["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core"]
    gidravlicheskie_isku --> gidravlicheskie_iskusstve
    gidravlicheskie_iskusstve["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing"]
    gidravlicheskie_isku --> gidravlicheskie_iskusstve
    gidravlicheskie_iskusstve["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors"]
    gidravlicheskie_isku --> gidravlicheskie_iskusstve
    gidravlicheskie_iskusstve["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting"]
    gidravlicheskie_isku --> gidravlicheskie_iskusstve
```
