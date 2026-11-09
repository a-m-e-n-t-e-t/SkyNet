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
    материал: silicone-textile_composite
    доля_массы: 0.45
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
    материал: aluminum
    доля_массы: 0.27
технологии_частей:
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core
    технология: pletenie_opletki
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: uhmwpe
        роль: обрабатываемый
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors
    технология: tokarnaya_obrabotka_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
        роль: обрабатываемый
  - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting
    технология: frezervanie_chpu
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: al_6061-t6
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
          l: 292
          w: 36
          h: 38
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 0.1
          max: 50
          nominal: 5
наследуемые: {}
масштабируемость:
  режим: квантуемая
  параметры: [диаметр_внутренний_mm, длина_активная_mm]
  пределы:
    min: {диаметр_внутренний_mm: 5,  длина_активная_mm: 30}
    max: {диаметр_внутренний_mm: 40, длина_активная_mm: 900}
  шаг:
    диаметр_внутренний_mm: [5, 10, 20, 40]      # ряд Festo Fluidic Muscle DMSP
    длина_активная_mm: null                      # непрерывно по CAD
  закон_масштабирования:
    масса: линейный                              # m ∝ d × l (трубка + оплётка)
    сила: квадратичный                           # F = (π/4)·d²·p·η; Festo: 150/630/1500/6000 N при d=5/10/20/40, p=6 bar
    contraction_pct: постоянный                  # ~20-25 % не зависит от масштаба
  ограничивающие_части:
    - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors
      предел: гидропорт ISO 5599 / G1/8-G1/4 — квантуется под d_шланга → ограничивает расход Q = π·d²/4 × v
    - часть: часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
      предел: внутренний Ø обоймы = Ø мышцы + зазор 1-2 мм
дополнительные:
  цена_usd: null
дата_создания: 2026-11-03
дата_обновления: 2026-11-10
источник: web_search
источник_разбора: веб-верификация
источник_url: https://ftp.festo.com/public/PNEUMATIC/SOFTWARE_SERVICE/DataSheet/EN_GB/534202.pdf
источник_дата: 2026-11-07
---
## Описание

Приводная сборка на основе гидравлической искусственной мышцы Мак-Киббена: эластичная камера в текстильной оплётке (активная длина 250 мм, Ø15 мм) в жёстком защитном кожухе (288 мм) с концевыми цанговыми фитингами и блоком разъёмов/манометрирования. Референс-класс — Fluidic Muscle Festo DMSP/MAS (размер 20: внутренний Ø20 мм, номинальная длина 250 мм, макс. сокращение 25 % номинальной длины, расширение до Ø40 мм при полном ходе). Габариты сборки 292×36×38 мм — конверт «мышца в кожухе + фланец разъёма 38999 (32.9×32.9×36)»; масса 0.05–50 кг, номинал 1 кг (кластерное исполнение из нескольких мышц на общем коллекторе).

Полное наименование (как в CSV): `гидравлические искусственные мышцы МакКиббена`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | canon |
| подтип | прочее | — | canon |
| масса | 0.05–50 (номинал 1) | kg | canon |
| габариты (Д×Ш×В) | 292×36×38 | mm | canon |
| выработка энергии | 0 | W | canon |
| выработка тепла | 0.1–50 | W | canon |
| тип узла | изделие | — | canon |
| уровень_номер | 1 | — | canon |


## Принцип работы

Мышца Мак-Киббена — тянущий пневмо/гидропривод: эластичная внутренняя камера (силикон) в оплётке из высокопрочных волокон (Kevlar). При подаче рабочего давления (гидравлика/пневматика) камера расширяется, оплётка раскрывает угол плетения — мышца сокращается по длине (до 20–25 %) и наращивает тянущее усилие. Одностороннее действие; возврат — внешней пружиной/нагрузкой/антагонистом. Класс Festo DMSP/MAS: номинальная длина до 2250 мм, стандартная длина ≈ 10× внутреннего диаметра, макс. сокращение 25 % номинальной длины.

## Состав

Сборка верхнего уровня, 4 дочерние части:

- `часть_..._core` — гидравлическая мышца Мак-Киббена (камера + оплётка), 250×15×15 мм, 0.06 кг
- `часть_..._housing` — жёсткий защитный кожух с монтажными лапами, 288×18×18 мм, 0.054 кг
- `часть_..._connectors` — блок разъёмов/коллектор 38999 size 23, 32.9×32.9×36 мм, 0.1 кг
- `часть_..._mounting` — концевые цанговые фитинги (2 шт), 28×14×14 мм, 0.02 кг

Упаковка: V(конверта 292×36×38) = 399 456 мм³ ≥ ΣV(детей)×1.15 = 223 119 мм³ ✔

## Используемые технологии

- `pletenie_opletki` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)
- `tokarnaya_obrabotka_chpu` (доля: 1.0)
- `frezervanie_chpu` (доля: 1.0)


## Используемые материалы

- `silicone-textile_composite` → [`silicone-textile_composite`](../../../материалы/silicone-textile_composite.md)
- `aluminum` → [`aluminum`](../../../материалы/aluminum.md)


## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Festo Fluidic Muscle MAS-20 datasheet: https://ftp.festo.com/public/PNEUMATIC/SOFTWARE_SERVICE/DataSheet/EN_GB/534202.pdf
- Festo DMSP/MAS документация (nominal length, 25 % contraction, стандартная длина = 10×Ø): https://ftp.festo.com/public/pneumatic/SOFTWARE_SERVICE/Documentation/2020/US/MAS_ENUS.PDF
- Pneumatic artificial muscles (обзор принципа): https://en.wikipedia.org/wiki/Pneumatic_artificial_muscles

---

## Декомпозиция

```mermaid
graph TD
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena["izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena"]
    ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core"]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena --> ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core
    ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing"]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena --> ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_housing
    ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors"]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena --> ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_connectors
    ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting["часть_gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting"]
    izdelie_gidravlicheskie_iskusstvennye_myshtsy_makkibbena --> ______gidravlicheskie_iskusstvennye_myshtsy_makkibbena_mounting
```
