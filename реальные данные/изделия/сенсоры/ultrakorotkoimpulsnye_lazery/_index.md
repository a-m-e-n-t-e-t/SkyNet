---
id: izdelie_ultrakorotkoimpulsnye_lazery
тип: изделие
категория: оптика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: сенсоры
подтип: прочее
стандарты:
- MIL-STD-810
- IEC 60068
исследовательская_группа: flir_l3
родитель: null
дочерние_части:
- часть_ultrakorotkoimpulsnye_lazery_core
- часть_ultrakorotkoimpulsnye_lazery_housing
- часть_ultrakorotkoimpulsnye_lazery_connectors
- часть_ultrakorotkoimpulsnye_lazery_mounting
материалы_частей:
- часть: часть_ultrakorotkoimpulsnye_lazery_core
  материал: al_6061-t6
  форма: силовые_элементы_конструкций
  доля_массы: 0.45
- часть: часть_ultrakorotkoimpulsnye_lazery_housing
  материал: aluminum
  форма: корпуса_электроники
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
    max: 5
    nominal: 0.5
  габариты_mm:
    l: 800
    w: 400
    h: 200
  выработка_энергии_W:
    min: 0
    max: 0
    nominal: 0
  выработка_тепла_W:
    min: 0.1
    max: 10
    nominal: 2
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
технологии_частей:
- часть: часть_ultrakorotkoimpulsnye_lazery_core
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_ultrakorotkoimpulsnye_lazery_housing
  технология: anodirovanie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: al_6061-t6
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_ultrakorotkoimpulsnye_lazery_core
  форма: силовые_элементы_конструкций
- материал: aluminum
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_ultrakorotkoimpulsnye_lazery_housing
  форма: корпуса_электроники
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 50
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 50.0
    - 300.0
    единица: kg
  - имя: длина_единицы
    диапазон:
    - 680.0
    - 1247.0
    единица: mm
  пределы:
    max_единиц_в_системе: 50
    min_массы: 50.0
    max_массы: 300.0
  закон_масштабирования: 'нелинейный — масса_системы = N × масса_единицы × 1.05 (5%
    overhead на system integration: chiller, power supply, control unit); типовая
    установка: Trumpf TruMicro 5000 (680×289×1060 mm, 200 kg) или Coherent Astrella
    (1247×792×262 mm, 280 kg)'
  ограничивающие_части:
  - часть_ultrakorotkoimpulsnye_lazery_core (Ti:Sa crystal + pump diodes — критическая
    зависимость от Coherent/Trumpf)
  - часть_ultrakorotkoimpulsnye_lazery_housing (aluminum extrusion + anodizing — стандартное
    производство)
источник_url: https://www.trumpf.com/filestorage/TRUMPF_Master/Products/Lasers/02_Brochures/TRUMPF-short-ultrashort-pulsed-laser-brochure-TruMicro-EN.pdf
источник_дата: '2026-11-11'
---

# Изделие: Ультракороткоимпульсные лазеры

## Описание

Ультракороткоимпульсные лазеры (USPL)

Полное наименование (как в CSV): `Ультракороткоимпульсные лазеры (USPL)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | сенсоры | — | classify_subsystem |
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
    ultrakorotkoimpulsny["izdelie_ultrakorotkoimpulsnye_lazery"]
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_core"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_housing"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_connectors"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
    ultrakorotkoimpulsnye_laz["часть_ultrakorotkoimpulsnye_lazery_mounting"]
    ultrakorotkoimpulsny --> ultrakorotkoimpulsnye_laz
```
