---
id: izdelie_povorotnoe_uplotnenie
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
- часть_povorotnoe_uplotnenie_core
- часть_povorotnoe_uplotnenie_housing
- часть_povorotnoe_uplotnenie_connectors
- часть_povorotnoe_uplotnenie_mounting
материалы_частей:
- часть: часть_povorotnoe_uplotnenie_core
  материал: ptfe
  форма: уплотнения_и_скользящие_узлы
  доля_массы: 0.45
- часть: часть_povorotnoe_uplotnenie_housing
  материал: al_6061-t6
  форма: корпуса_электроники
  доля_массы: 0.27
технологии_частей:
- часть: часть_povorotnoe_uplotnenie_core
  технология: tokarnaya_obrabotka_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ptfe
    роль: обрабатываемый
- часть: часть_povorotnoe_uplotnenie_housing
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
- часть: часть_povorotnoe_uplotnenie_connectors
  технология: tokarnaya_obrabotka_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_povorotnoe_uplotnenie_mounting
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ss_aisi_304
    роль: обрабатываемый
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
    l: 120
    w: 107.95
    h: 107.95
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
дата_обновления: '2026-11-11'
источник: web_search
источник_разбора: веб-верификация
источник_url: https://advanced-emc.com/when-to-use-a-ptfe-rotary-shaft-seal
источник_дата: '2026-11-11'
наследуемые_материалы:
- материал: ptfe
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_povorotnoe_uplotnenie_core
  форма: уплотнения_и_скользящие_узлы
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_povorotnoe_uplotnenie_housing
  форма: корпуса_электроники
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1000
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.005
    - 0.5
    единица: kg
  - имя: диаметр_вала
    диапазон:
    - 5
    - 100
    единица: mm
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 0.005
    max_массы: 0.5
    min_диаметра: 5
    max_диаметра: 100
  закон_масштабирования: 'линейный — масса_системы = N × масса_единицы; типовая установка:
    PTFE rotary shaft seal (Advanced EMC Technologies, 20-100 mm dia, PTFE lip + spring,
    -200 до +250 °C)'
  ограничивающие_части:
  - часть_povorotnoe_uplotnenie_core (PTFE sealing lip + spring — критическая точность
    производства)
  - часть_povorotnoe_uplotnenie_housing (aluminum housing + anodizing — стандартное
    производство)
---
## Описание

Поворотное уплотнение (rotary union)

Полное наименование (как в CSV): `Поворотное уплотнение (rotary union)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–50 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 120×107.95×107.95 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.1–50 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Поворотное соединение (rotary union) подаёт гидравлическую среду из неподвижной магистрали
во вращающийся узел через 2 независимых канала. Герметичность обеспечивается балансированным
механическим торцевым уплотнением (SiC/SiC, микролапка ≤2 световых полос): давление среды
уравновешивает силу прижима, снижая износ. Корпус (housing) фиксируется против вращения,
ротор с фланцем Ø107.95 мм монтируется на вал машины; присоединение среды — резьбовое
1/4"-18 NPT. Серия ST252 допускает самоустановку (self-aligning) с компенсацией перекоса.
Источник: Deublin ST252 steel-industry brochure; https://www.deublin.com/en/products/2620-000-252 (проверено 2026-11-08).

## Состав

Изделие верхнего уровня (rotary union / поворотное соединение). Дочерние части:
- часть_povorotnoe_uplotnenie_core — уплотнительный узел (механическое торцевое уплотнение, балансированное)
- часть_povorotnoe_uplotnenie_housing — корпус с монтажным фланцем
- часть_povorotnoe_uplotnenie_connectors — резьбовые присоединения среды (1/4"-18 NPT класс)
- часть_povorotnoe_uplotnenie_mounting — фиксация корпуса против вращения

## Используемые технологии

- `tokarnaya_obrabotka_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)
- `tokarnaya_obrabotka_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)


## Используемые материалы

- `ptfe` (форма: уплотнения_и_скользящие_узлы) → [`ptfe`](../../../материалы/ptfe.md)
- `al_6061-t6` (форма: корпуса_электроники) → [`al_6061-t6`](../../../материалы/al_6061-t6.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Deublin 2620-000-252 product page (серия ST252): https://www.deublin.com/en/products/2620-000-252 (проверено 2026-11-08)
- Deublin ST252 brochure: https://www.deublin.com/_Resources/Persistent/5/6/6/8/56683bfe9757615589678c9d6a347919abc3f6fd/SteelBrochure%20-%20ST252%20US_LowRes.pdf

---

## Декомпозиция

```mermaid
graph TD
    izdelie_povorotnoe_uplotnenie["izdelie_povorotnoe_uplotnenie"]
    ______povorotnoe_uplotnenie_core["часть_povorotnoe_uplotnenie_core"]
    izdelie_povorotnoe_uplotnenie --> ______povorotnoe_uplotnenie_core
    ______povorotnoe_uplotnenie_housing["часть_povorotnoe_uplotnenie_housing"]
    izdelie_povorotnoe_uplotnenie --> ______povorotnoe_uplotnenie_housing
    ______povorotnoe_uplotnenie_connectors["часть_povorotnoe_uplotnenie_connectors"]
    izdelie_povorotnoe_uplotnenie --> ______povorotnoe_uplotnenie_connectors
    ______povorotnoe_uplotnenie_mounting["часть_povorotnoe_uplotnenie_mounting"]
    izdelie_povorotnoe_uplotnenie --> ______povorotnoe_uplotnenie_mounting
```
