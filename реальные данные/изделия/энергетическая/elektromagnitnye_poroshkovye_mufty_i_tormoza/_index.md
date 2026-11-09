---
id: izdelie_elektromagnitnye_poroshkovye_mufty_i_tormoza
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: электромагнитная_муфта
стандарты: 
  - DIN VDE 0580
исследовательская_группа: kendrion_mayr
родитель: null
дочерние_части:
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings
  - часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing
материалы_частей:
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil
    материал: copper
    форма: обмотки_электрических_машин
    доля_массы: 0.18
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor
    материал: steel_1045
    форма: валы_и_магнитопроводы_муфт
    доля_массы: 0.285
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator
    материал: steel_1045
    доля_массы: 0.285
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder
    материал: iron_powder
    доля_массы: 0.057
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings
    материал: stainless_steel_440c
    доля_массы: 0.054
технологии_частей:
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil
    технология: spiralnaya_navivka
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: copper
        роль: обрабатываемый
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: steel_1045
        роль: обрабатываемый
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: steel_1045
        роль: обрабатываемый
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder
    технология: karbonilnyi_sintez_poroshka_zheleza
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: iron_powder
        роль: обрабатываемый
  - часть: часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings
    технология: honing_plateau_finish
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: stainless_steel_440c
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
          min: 0.5
          max: 50
          nominal: 5
  габариты_mm:
          l: 150
          w: 220
          h: 220
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1
          max: 100
          nominal: 10
наследуемые: {}
дополнительные: 
  M_ном_Нм: 50
  источник: Kendrion / Mayr electromagnetic clutches
  обоснование_габаритов: 'реальный габаритный бокс муфты 50 Нм класса FL50K (magnetic particle clutch): наружный диаметр D0 = 220 мм, полная длина L0 = 150 мм, вал Ø30 со шпонкой B8, фланец Ø110 M6; ориентация: l = осевая длина 150, w/h = диаметр 220; F15g: (A) V(parent) = 150×220×220 = 7 260 000 мм³ ≥ ΣV(детей)×1.15 = 4 010 850×1.15 = 4 612 478 мм³ (запас ×1.93); (B) оси: 150 ≥ 122 (дети l ≤ 120), 220 ≥ 122, 220 ≥ 162 (housing h = 160); референс kids: housing 120×120×160 — внутренний монтажный объём корпуса в Ø220 габарите'
  источник_url: https://www.scribd.com/doc/317064781/Clutch-Fl50k-Powder-Magnetic-Particle
  источник_url_2: https://www.kendrion.com/en/products/clutches-and-brakes
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: электромагнитные порошковые муфты и тормоза

## Описание

электромагнитные порошковые муфты и тормоза (magnetic particle brake/clutch) — промышленный узел передачи/регулирования момента через магнитопорошковый слой: номинальный момент 50 Нм (24 В, 2 А), DIN VDE 0580. Референсное исполнение — FL50K: наружный диаметр 220 мм, полная длина 150 мм, вал Ø30 мм со шпонкой B8, фланец Ø110 мм M6; корпус цилиндрический с катушкой статора и порошковой полостью. Масса номинал 5 кг (0.5–50 кг диапазон класса).

Полное наименование (как в CSV): `электромагнитные порошковые муфты и тормоза (magnetic particle brake/clutch)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |
| номинальный момент | 50 | N·m | FL50K magnetic particle clutch datasheet (50 Nm, 24 V / 2 A); Kendrion/Mayr класс |
| масса (ном.) | 5 | kg | класс 0.5–50 кг (DIN VDE 0580), муфта 50 Нм |
| габариты (Д×Ш×В) | 150×220×220 | mm | FL50K datasheet: D0 = 220 мм (наружный Ø), L0 = 150 мм (полная длина), вал Ø30/B8 |

(Масса/момент/габариты — реальные данные FL50K; остальные параметры — диапазоны класса по _field_contracts.yaml)

## Состав

Изделие верхнего уровня (уровень 1), 6 частей уровня 2: coil (катушка возбуждения, copper, 0.8 кг), rotor (ротор с валом Ø30, steel_1045, 1.5 кг), stator (статорное кольцо с магнитопроводом, steel_1045, 1.5 кг), powder (магнитопорошковая смесь в рабочем зазоре, iron_powder, 0.3 кг), bearings (подшипниковые опоры вала, stainless_steel_440c, 0.3 кг), housing (корпус с фланцем Ø110 M6 и кабельным вводом, stal_st3, 5 кг оценка).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Магнитопорошковая передача момента: катушка возбуждения создаёт магнитный поток через рабочий зазор, заполненный ферромагнитным порошком (iron powder); в обесточенном состоянии порошок свободен и муфта проскальзывает, при подаче тока частицы выстраиваются по силовым линиям и связывают ротор со статором — момент регулируется плавно пропорционально току катушки (24 В / 2 А → 50 Нм). Применение: натяжение/торможение в перемоточных машинах, плавный пуск, защита от перегрузки; рассеиваемое тепло 10 Вт номинал (1–100 Вт диапазон) отводится корпусом.

## Источники

- FL50K Magnetic Particle Clutch — datasheet (50 Nm, 24 V / 2 A, D0 = 220, L0 = 150, вал Ø30/B8, фланец Ø110 M6): https://www.scribd.com/doc/317064781/Clutch-Fl50k-Powder-Magnetic-Particle (проверено 2026-11-08)
- Kendrion — Clutches and Brakes (электромагнитные муфты/тормоза, DIN VDE 0580): https://www.kendrion.com/en/products/clutches-and-brakes (проверено 2026-11-08)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    elektromagnitnye_por["izdelie_elektromagnitnye_poroshkovye_mufty_i_tormoza"]
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_coil"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_rotor"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_stator"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_powder"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_bearings"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
    elektromagnitnye_poroshko["часть_elektromagnitnye_poroshkovye_mufty_i_tormoza_housing"]
    elektromagnitnye_por --> elektromagnitnye_poroshko
```
