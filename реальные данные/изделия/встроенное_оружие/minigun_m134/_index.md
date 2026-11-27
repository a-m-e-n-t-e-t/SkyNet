---
id: izdelie_minigun_m134
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: встроенное_оружие
подтип: прочее
стандарты: 
  - MIL-STD-810
исследовательская_группа: general_dynamics
родитель: null
дочерние_части:
  - часть_minigun_m134_core
  - часть_minigun_m134_housing
  - часть_minigun_m134_connectors
  - часть_minigun_m134_mounting
материалы_частей:
  - часть: часть_minigun_m134_core
    материал: stal_st3
    форма: строительные_конструкции_и_крепёж
    доля_массы: 0.45
  - часть: часть_minigun_m134_housing
    материал: ti-6al-4v
    форма: планер_и_космические_изделия
    доля_массы: 0.27
технологии_частей:
  - часть: часть_minigun_m134_core
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: stal_st3
        роль: обрабатываемый
  - часть: часть_minigun_m134_housing
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ti-6al-4v
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
          min: 1
          max: 100
          nominal: 20
  габариты_mm:
          l: 801.6
          w: 304.8
          h: 241.3
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 10
          max: 1000
          nominal: 100
масштабируемость:
  # v9.62 (#1046, P087 §12.6): M134 — дискретный ряд конфигураций
  # (6 стволов 7.62×51 мм, длина стволов 22"/28"/36", темп 2000–6000 выстр/мин,
  # электрический/гидравлический привод). Масса и тепловыделение меняются
  # квантованно с конфигурацией, непрерывного масштабирования нет.
  # Источник: Wikipedia M134 Minigun («steel housing and rotor», #827);
  # пределы — из блока основные (min/max).
  режим: квантуемая
  параметры: [масса_kg, выработка_тепла_W]
  пределы:
    min: {масса_kg: 1, выработка_тепла_W: 10}
    max: {масса_kg: 100, выработка_тепла_W: 1000}
  закон_масштабирования:
    масса: ступенчатый_по_конфигурациям
    тепловыделение: пропорционально_темпу_стрельбы
  ограничивающие_части: [часть_minigun_m134_core, часть_minigun_m134_connectors]
наследуемые: {}
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: web_search
источник_разбора: веб-верификация
источник_url: https://en.wikipedia.org/wiki/M134_Minigun
источник_дата: 2026-11-07
---
# Изделие: Minigun M134

## Описание

Minigun M134

Полное наименование (как в CSV): `Minigun M134`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | встроенное_оружие | — | classify_subsystem |
| категория | прочее | — | — |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

## Используемые технологии

- [`frezervanie_chpu`](../../../технологии/frezervanie_chpu.md) — ЧПУ-фрезерование: обработка деталей core (Ст3, крепёж и элементы блока) и корпуса housing (Ti-6Al-4V, 5-осевое фрезерование — стандарт авиационного производства титановых корпусов/кронштейнов, Carr Machine: «structural brackets, housings, fittings… in Ti-6Al-4V with 5-axis milling»; режимы для Ti: carbide-инструмент, низкие скорости резания ~150–200 SFM, высоконапорная СОЖ — ptsmake)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- [Wikipedia: M134 Minigun — 7.62×51mm NATO, 6 стволов, 2000–6000 выстр/мин](https://en.wikipedia.org/wiki/M134_Minigun)
- [Seaforces.org: M134 Mk.44 GAU-17A — вес 39/19 кг, длина 31.56 in, ствол 558.8 мм](https://www.seaforces.org/wpnsys/SURFACE/M134-minigun.htm)
- [Carr Machine & Tool: Ti-6Al-4V CNC Machining — 5-axis milling housings/brackets/fittings](https://carrmachine.com/materials/ti-6al-4v-machining) (обращение 2026-11-08)
- [PTSMake: How to Effectively Machine Titanium Grade 5 (Ti-6Al-4V) — carbide tool, 150–200 SFM, high-pressure coolant](https://www.ptsmake.com/how-to-effectively-machine-titanium-grade-5-ti-6al-4v) (обращение 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    minigun_m134["izdelie_minigun_m134"]
    minigun_m134_core["часть_minigun_m134_core"]
    minigun_m134 --> minigun_m134_core
    minigun_m134_housing["часть_minigun_m134_housing"]
    minigun_m134 --> minigun_m134_housing
    minigun_m134_connectors["часть_minigun_m134_connectors"]
    minigun_m134 --> minigun_m134_connectors
    minigun_m134_mounting["часть_minigun_m134_mounting"]
    minigun_m134 --> minigun_m134_mounting
```

### Верификация габаритов (web_search 2026-11-07)

M134 Minigun: **длина 801.6 мм** (31.56 in), ширина 304.8 мм (12.0 in), высота 241.3 мм (9.5 in), масса 39 кг / 19 кг lightweight, длина ствола 558.8 мм (22 in) — Wikipedia M134 / General Dynamics spec.
