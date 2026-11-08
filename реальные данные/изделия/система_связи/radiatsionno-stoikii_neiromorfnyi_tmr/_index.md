---
id: izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
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
  - часть_radiatsionno-stoikii_neiromorfnyi_tmr_core
  - часть_radiatsionno-stoikii_neiromorfnyi_tmr_housing
  - часть_radiatsionno-stoikii_neiromorfnyi_tmr_connectors
  - часть_radiatsionno-stoikii_neiromorfnyi_tmr_mounting
материалы_частей:
  - часть: часть_radiatsionno-stoikii_neiromorfnyi_tmr_core
    материал: si
    доля_массы: 0.45
  - часть: часть_radiatsionno-stoikii_neiromorfnyi_tmr_housing
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
          nominal: 1.5
наследуемые: {}
дополнительные:
  цена_usd: null
  тепловой_баланс_обоснование: вычислительный модуль не генерирует энергию — вся электрическая мощность переходит в тепло (КПД вычислений ≈ 0); системный номинал 1.5 Вт = ядро-процессор нейроморфного класса ~1 Вт (Intel Loihi 2 — измеренно 1.55 Вт при 103.94 GOP/s/W, arXiv 2408.16096) + интерфейсная логика и DC-DC конвертеры платы модуля ~0.5 Вт; класс-прецедент радиационно-стойких бортовых вычислителей GR740 LEON4FT — менее 3 Вт (core typical); Σ детей = 1.0 ≤ 1.5 — баланс сходится с запасом ×1.5
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: радиационно-стойкий нейроморфный TMR

## Описание

Радиационно-стойкий нейроморфный вычислительный модуль — спайковый нейропроцессор с тройной модульной избыточностью (TMR — triple modular redundancy) для защиты от одиночных событийных эффектов (SEU) космической радиации. Ядро — керамический CCGA-корпус 42×42 мм класса радиационно-стойких чипов (прецедент Xilinx XQR Virtex-5QV CCGA1137 42.5×42.5 мм), размещён в алюминиевой оболочке с Micro-D жгутом и стальной рамкой-экраном MTJ-синапсов.

Полное наименование (как в CSV): `радиационно-стойкий нейроморфный TMR`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | система_связи | — | classify_subsystem |
| категория | электроника | — | синхронизировано с YAML |
| масса | 0.1 (0.005–5) | kg | номинал изделия (ядро 20 г + корпус 18 г + жгут 80 г + рамка 25 г + плата) |
| габариты (Д×Ш×В) | 50×30×5 | mm | канон изделия |
| выработка тепла | 1.5 (0.01–5) | W | системный тепловой поток — класс Loihi 2 (Intel brief, arXiv 2408.16096) + GR740 LEON4FT (rad-hard класс < 3 Вт) |
| выработка энергии | 0 | W | canon |

## Состав

Изделие верхнего уровня, 4 дочерних части:

- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_core` — радиационно-стойкий нейроморфный вычислитель (TMR, CCGA 42×42×5, 20 г, ~1 Вт — единственный источник тепла)
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_housing` — алюминиевый корпус-оболочка с ЭМИ-экранированием (49×49×8, 18 г, пассивная)
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_connectors` — Micro-D жгут 79 контактов (MIL-DTL-83513, 80 г, пассивный)
- `часть_radiatsionno-stoikii_neiromorfnyi_tmr_mounting` — стальная рамка-экран с пружинным контактом (32×32×8, 25 г, пассивная)

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Спайковая нейроморфная обработка данных — входной поток кодируется асинхронными спайками, MTJ-синапсы ядра выполняют событийные вычисления с энергопотреблением ~1 Вт (класс Loihi 2). Тройная модульная избыточность (TMR): три идентичных вычислительных канала внутри кристалла работают параллельно, мажоритарный элемент отбрасывает канал, поражённый SEU-ошибкой космической радиации — сбой маскируется без прерывания вычислений. Алюминиевая оболочка экранирует ЭМИ и отводит тепло ядра к плате; стальная рамка прижимает крышку магнитного экрана (поля >10 Э сбивают TMR-состояния синапсов); Micro-D жгут выносит шины троированных каналов, питание и телеметрию.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Intel Neuromorphic Computing Loihi 2 brief — «Loihi consumes far less than 1 watt of power» (класс мощности нейроморфных процессоров): https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf (проверено 2026-11-08)
- Analyzing Energy Consumption of Loihi 2 (arXiv 2408.16096) — потребление 1.55 Вт при 103.94 GOP/s/W: https://arxiv.org/html/2408.16096v1 (проверено 2026-11-08)
- Frontgrade Gaisler GR740 Quad-core LEON4FT — радиационно-стойкий бортовой процессор, «very low power, < 3 W (core typical)» — класс-прецедент мощности радиационно-стойких вычислителей: https://www.gaisler.com/products/gr740 (проверено 2026-11-08)

---


## Декомпозиция

```mermaid
graph TD
    radiatsionno-stoikii["izdelie_radiatsionno-stoikii_neiromorfnyi_tmr"]
    radiatsionno-stoikii_neir["часть_radiatsionno-stoikii_neiromorfnyi_tmr_core"]
    radiatsionno-stoikii --> radiatsionno-stoikii_neir
    radiatsionno-stoikii_neir["часть_radiatsionno-stoikii_neiromorfnyi_tmr_housing"]
    radiatsionno-stoikii --> radiatsionno-stoikii_neir
    radiatsionno-stoikii_neir["часть_radiatsionno-stoikii_neiromorfnyi_tmr_connectors"]
    radiatsionno-stoikii --> radiatsionno-stoikii_neir
    radiatsionno-stoikii_neir["часть_radiatsionno-stoikii_neiromorfnyi_tmr_mounting"]
    radiatsionno-stoikii --> radiatsionno-stoikii_neir
```
