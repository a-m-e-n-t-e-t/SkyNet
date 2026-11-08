---
id: izdelie_usb-c
тип: изделие
категория: электроника
уровень_иерархии: верхний
уровень_номер: 1
подсистема: система_связи
подтип: прочее
стандарты: 
  - FCC Part 15
  - ETSI EN 301 489
исследовательская_группа: harris_thales
родитель: null
дочерние_части:
  - часть_usb-c_core
  - часть_usb-c_housing
  - часть_usb-c_connectors
  - часть_usb-c_mounting
материалы_частей:
  - часть: часть_usb-c_core
    материал: becu
    доля_массы: 0.45
  - часть: часть_usb-c_housing
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
          min: 0.005
          max: 5
          nominal: 0.1
  габариты_mm:
          l: 50
          w: 30
          h: 5
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.01
          max: 5
          nominal: 1.2
наследуемые: {}
дополнительные:
  цена_usd: null
  тепловой_баланс_обоснование:
    тип: "родитель = Σ(детей) + собственные потери"
    сумма_детей_Вт: 1.10
    собственные_потери_Вт: 0.10
    итог_номинал_Вт: 1.20
    разложение_детей:
      часть_usb-c_core: 1.00  # USB Type-C receptacle 24-pin, 4×VBUS × 5A × ~20 мОм контакт = 1.0 Вт под PD-нагрузкой
      часть_usb-c_housing: 0.00  # алюминиевый кожух AL 6061 — пассив
      часть_usb-c_connectors: 0.10  # IEC 60320 C14 inlet 10A/250V, ohmic потери при скважности USB-станции
      часть_usb-c_mounting: 0.00  # сталь AISI 304 плита — пассив
    собственные_потери_разложение_Вт:
      PD_контроллер: 0.05  # TI TPS25750/25751 Idle state (datasheet §6.7)
      DC_DC_buck_quiescent: 0.03  # дежурный режим понижающих преобразователей 5/9/15/20 В
      EMI_фильтр: 0.01  # differential-mode choke I²R
      status_LEDs: 0.01  # индикаторы PD/связь
  источник_url: https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
  источник_url_2: https://www.ti.com/product/TPS25750
  источник_url_3: https://www.te.com/en/products/connectors/audio-and-video-connectors/usb-connectors/usb-type-c-connectors.html
  источник_дата: 2026-11-08
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: USB-C

## Описание

USB-C

Полное наименование (как в CSV): `USB-C`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_связи | — | classify_subsystem |
| категория | прочее | — | — |
| выработка_тепла_W (min/nom/max) | 0.01 / 1.2 / 5 | Вт | тепловой баланс: Σ(детей)=1.10 + собств. потери 0.10 (PD-контроллер TI TPS25750 Idle, DC-DC quiescent, EMI, LEDs) — USB-IF Type-C Spec R2.0 §5A, TI TPS25750 §6.7, IEC 60320 C14 10A/250V |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня — USB-C станция/узел связи. Состоит из 4 дочерних частей:

| Часть | Роль | Выработка тепла, Вт | Примечание |
|---|---|---|---|
| `часть_usb-c_core` | Разъём USB Type-C 24-pin (receptacle, PD до 240 Вт) | 1.00 | ohmic нагрев 4×VBUS × 5A × ~20 мОм |
| `часть_usb-c_housing` | Алюминиевый корпус-кожух (AL 6061-T6) | 0.00 | пассив — теплоотвод через корпус |
| `часть_usb-c_connectors` | Сетевой inlet IEC 60320 C14 + кабельный жгут | 0.10 | ohmic потери 10A inlet при скважности USB-станции |
| `часть_usb-c_mounting` | Монтажная пластина AISI 304 (30×15×3 мм) | 0.00 | пассив — теплоотвод в шасси |
| **Итого Σ детей** | — | **1.10** | — |
| Родитель (собств. потери) | PD-контроллер + DC-DC + EMI + LEDs | **0.10** | TPS25750 Idle, DC-DC quiescent |
| **Σ родителя (nominal)** | — | **1.20** | Σ детей + собственные потери |

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

USB-C станция обеспечивает силовую доставку (USB PD 3.1, до 240 Вт) и передачу данных (USB4 40 Гбит/с) через симметричный 24-pin разъём Type-C. Тепловой поток распределён между четырьмя дочерними частями:

1. **Ядро (`часть_usb-c_core`)** — основной теплогенерирующий элемент. Под PD-нагрузкой (5A на 4 контактах VBUS при контактном сопротивлении ~20 мОм) выделяет P = 4 × I²R = 4 × 25 × 0.02 = 2 Вт в пике; усреднённая скважность USB-станции 50% → 1.0 Вт nominal.
2. **Разъёмы (`часть_usb-c_connectors`)** — IEC 60320 C14 inlet (10A/250V) + кабельный жгут. Ohmic потери при типовой нагрузке USB-станции (низкая скважность, 5-10% цикла) → 0.1 Вт average.
3. **Корпус (`часть_usb-c_housing`)** — алюминиевый кожух AL 6061-T6, пассивный элемент. Отводит тепло от ядра к окружающей среде (конвекция + излучение).
4. **Монтаж (`часть_usb-c_mounting`)** — стальная пластина AISI 304, пассивный элемент. Механическое удержание разъёма (20K циклов, USB-IF) + теплоотвод в шасси.

Собственные потери родителя (0.1 Вт): TI TPS25750/25751 PD-контроллер в Idle-режиме (datasheet §6.7 Active/Idle/Sleep states), DC-DC buck quiescent (5/9/15/20 В выходы, 90-95% КПД), EMI-фильтр (differential-mode choke I²R), status LEDs.

Баланс: P(parent) = 1.2 Вт = Σ(детей) 1.1 Вт + собственные потери 0.1 Вт ✓

## Источники

- USB Type-C Cable and Connector Spec R2.0 (USB-IF, Aug 2019) — 5A current rating, PD 3.1 до 240 Вт: https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf
- TE Connectivity USB Type-C Connectors (USB4950 datasheet, 5A VBUS collective): https://www.te.com/en/products/connectors/audio-and-video-connectors/usb-connectors/usb-type-c-connectors.html
- Texas Instruments TPS25750/TPS25751 USB Type-C и PD Controller — §6.7 Power Consumption (Active/Idle/Sleep states): https://www.ti.com/product/TPS25750
- IEC 60320-1 — Appliance couplers (C14 inlet 10A/250V rating)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    usb-c["izdelie_usb-c"]
    usb-c_core["часть_usb-c_core"]
    usb-c --> usb-c_core
    usb-c_housing["часть_usb-c_housing"]
    usb-c --> usb-c_housing
    usb-c_connectors["часть_usb-c_connectors"]
    usb-c --> usb-c_connectors
    usb-c_mounting["часть_usb-c_mounting"]
    usb-c --> usb-c_mounting
```
