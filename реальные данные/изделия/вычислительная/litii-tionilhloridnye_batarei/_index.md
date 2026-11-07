---
id: izdelie_litii-tionilhloridnye_batarei
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: вычислительная
подтип: литий-тионилхлоридная_батарея
стандарты: 
  - IEC 60086
  - UN 3090
исследовательская_группа: saft_tadiran
родитель: null
дочерние_части:
  - часть_litii-tionilhloridnye_batarei_anode
  - часть_litii-tionilhloridnye_batarei_cathode
  - часть_litii-tionilhloridnye_batarei_electrolyte
  - часть_litii-tionilhloridnye_batarei_separator
  - часть_litii-tionilhloridnye_batarei_case
  - часть_litii-tionilhloridnye_batarei_terminal
материалы_частей:
  - часть: часть_litii-tionilhloridnye_batarei_anode
    материал: lithium_metal
    доля_массы: 0.19
  - часть: часть_litii-tionilhloridnye_batarei_cathode
    материал: carbon_black
    доля_массы: 0.18
  - часть: часть_litii-tionilhloridnye_batarei_electrolyte
    материал: socl2
    доля_массы: 0.38
  - часть: часть_litii-tionilhloridnye_batarei_separator
    материал: pp_membrane
    доля_массы: 0.019
  - часть: часть_litii-tionilhloridnye_batarei_case
    материал: stainless_steel_304
    доля_массы: 0.19
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
          max: 1.0
          nominal: 0.3
  габариты_mm:
          l: 50
          w: 25
          h: 25
  выработка_энергии_W:
          min: 0.001
          max: 1
          nominal: 0.1
  выработка_тепла_W:
          min: 0.001
          max: 0.1
          nominal: 0.05
наследуемые: {}
дополнительные: 
  ёмкость_Ач: 19
  V: 3.6
  T_хранения_лет: 20
  источник: Saft LSH20 datasheet
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: web_search
источник_разбора: веб-верификация
источник_url: https://www.evlithium.com/li-socl2-battery/eve-er34615-19000mah-li-thionyl-chloride-d-cell.html
источник_дата: 2026-11-08
---
# Изделие: Литий-тионилхлоридные батареи

## Описание

Литий-тионилхлоридные батареи (Li-SOCl₂)

Полное наименование (как в CSV): `Литий-тионилхлоридные батареи (Li-SOCl₂)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | вычислительная | — | classify_subsystem |
| категория | прочее | — | — |
| референс-элемент | EVE ER34615 (D, bobbin) | — | EVE/evlithium |
| номинальное напряжение | 3.6 | В | EVE ER34615 |
| ёмкость | 19 | Ач | EVE ER34615 |
| макс. непрерывный разряд | 230 | мА | EVE ER34615 |
| макс. импульсный разряд | 300 | мА | EVE ER34615 |
| масса элемента | 100 | г | EVE ER34615 |
| габариты элемента | Ø33.1 × 61.5 | мм | EVE ER34615 |
| выработка тепла (номинал, 230 мА) | 0.05 | Вт | расчёт: (U_хол−U_раб)×I |

Тепловой бюджет (F15b): при максимальном непрерывном разряде 230 мА рабочее напряжение
bobbin-элемента ≈ 3.3–3.4 В против ЭДС 3.6 В (пассивация LiCl + омика) → пере-потенциал
≈ 0.22 В → тепло ≈ 0.05 Вт (6 % отдаваемой мощности 0.78 Вт). Импульс 300 мА: ≈ 0.1 Вт
(максимум диапазона). Холостой ход: ≤ 0.001 Вт (саморазряд ≤ 1 %/год). Проверено 2026-11-08,
источник: https://www.evlithium.com/li-socl2-battery/eve-er34615-19000mah-li-thionyl-chloride-d-cell.html

## Состав

Изделие верхнего уровня (гальванический элемент Li-SOCl2, референс EVE ER34615). Дочерние части:
- часть_litii-tionilhloridnye_batarei_anode — Li-анод (поляризация растворения Li)
- часть_litii-tionilhloridnye_batarei_cathode — bobbin-катод (углерод + PTFE, восстановление SOCl2)
- часть_litii-tionilhloridnye_batarei_electrolyte — электролит SOCl2 + LiAlCl4
- часть_litii-tionilhloridnye_batarei_separator — сепаратор (микропористая мембрана)
- часть_litii-tionilhloridnye_batarei_case — стальной корпус (стенка — проводник тепла)
- часть_litii-tionilhloridnye_batarei_terminal — выводы (контактное сопротивление)

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Литий-тионилхлоридный (Li-SOCl2) bobbin-элемент D-размера: Li-анод, катод из ацетиленовой
сажи с PTFE, жидкий электролит SOCl2 + LiAlCl4. Ток образуется при восстановлении SOCl2
на углеродном катоде и окислении Li на аноде; разрядный продукт LiCl пассивирует анод
(низкий саморазряд ≤ 1 %/год, срок хранения ≥ 10 лет). Энергоплотность — одна из самых
высоких среди первичных элементов (68.4 Вт·ч для ER34615). Рабочие температуры −55…+85 °C.
Источник: EVE ER34615 spec (evlithium.com); https://en.wikipedia.org/wiki/Lithium_battery (проверено 2026-11-08).

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- EVE ER34615 3.6V 19000mAh Li-SOCl2 D-cell spec (230 мА max cont, 300 мА pulse, 100 г, Ø33.1×61.5): https://www.evlithium.com/li-socl2-battery/eve-er34615-19000mah-li-thionyl-chloride-d-cell.html (проверено 2026-11-08)
- Дополнительно: Tenergy/Saft ER34615-класс D bobbin cells (типовые 19 Ач, 3.6 В)

---


## Декомпозиция

```mermaid
graph TD
    litii-tionilhloridny["izdelie_litii-tionilhloridnye_batarei"]
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_anode"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_cathode"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_electrolyte"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_separator"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_case"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
    litii-tionilhloridnye_bat["часть_litii-tionilhloridnye_batarei_terminal"]
    litii-tionilhloridny --> litii-tionilhloridnye_bat
```
