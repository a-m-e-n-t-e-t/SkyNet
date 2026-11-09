---










id: izdelie_provodnikovaya_nanoreshetka
тип: материал
категория: прочее
уровень_иерархии: верхний
уровень_номер: 1
подсистема: прочее
подтип: прочее
стандарты: 
  - ISO 9001
исследовательская_группа: various
родитель: null
дочерние_части:
  - часть_provodnikovaya_nanoreshetka_core
  - часть_provodnikovaya_nanoreshetka_housing
  - часть_provodnikovaya_nanoreshetka_connectors
  - часть_provodnikovaya_nanoreshetka_mounting
материалы_частей:
  - часть: часть_provodnikovaya_nanoreshetka_core
    материал: mxene
    доля_массы: 0.45
  - часть: часть_provodnikovaya_nanoreshetka_housing
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
          min: 0.1
          max: 100
          nominal: 5
  габариты_mm:
          l: 200
          w: 200
          h: 50
  выработка_энергии_W:
          min: 0
          max: 100
          nominal: 0
  выработка_тепла_W:
          min: 0
          max: 100
          nominal: 1
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
## Описание

Проводниковая нанорешётка (Al, шаг 200 нм, высота 500 нм) на сапфировой подложке

Полное наименование (как в CSV): `Проводниковая нанорешётка (Al, шаг 200 нм, высота 500 нм) на сапфировой подложке`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | прочее | — | canon |
| подтип | прочее | — | canon |
| масса | 0.1–100 (номинал 5) | kg | canon |
| габариты (Д×Ш×В) | 200×200×50 | mm | canon |
| выработка энергии | 0–100 | W | canon |
| выработка тепла | 0–100 | W | canon |
| тип узла | материал | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Требует описания на основе инженерного анализа.

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые материалы

- `mxene` → [`mxene`](../материалы/mxene.md)
- `aluminum` → [`aluminum`](../материалы/aluminum.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)

---

## Декомпозиция

```mermaid
graph TD
    izdelie_provodnikovaya_nanoreshetka["izdelie_provodnikovaya_nanoreshetka"]
    ______provodnikovaya_nanoreshetka_core["часть_provodnikovaya_nanoreshetka_core"]
    izdelie_provodnikovaya_nanoreshetka --> ______provodnikovaya_nanoreshetka_core
    ______provodnikovaya_nanoreshetka_housing["часть_provodnikovaya_nanoreshetka_housing"]
    izdelie_provodnikovaya_nanoreshetka --> ______provodnikovaya_nanoreshetka_housing
    ______provodnikovaya_nanoreshetka_connectors["часть_provodnikovaya_nanoreshetka_connectors"]
    izdelie_provodnikovaya_nanoreshetka --> ______provodnikovaya_nanoreshetka_connectors
    ______provodnikovaya_nanoreshetka_mounting["часть_provodnikovaya_nanoreshetka_mounting"]
    izdelie_provodnikovaya_nanoreshetka --> ______provodnikovaya_nanoreshetka_mounting
```
