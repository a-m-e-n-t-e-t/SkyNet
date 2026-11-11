---
id: izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov
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
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors
- часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting
материалы_частей:
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
  материал: copper
  форма: шины_и_заземление
  доля_массы: 0.45
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing
  материал: aluminum
  форма: корпуса_электроники
  доля_массы: 0.27
технологии_частей:
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
  технология: volochenie
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: copper
    роль: обрабатываемый
- часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing
  технология: shtampovka_listovaya
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: aluminum
    роль: обрабатываемый
наследуемые_материалы:
- материал: copper
  суммарная_доля_массы: 0.9
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
  форма: шины_и_заземление
- материал: copper
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
  форма: теплосъём_и_экранирование
- материал: tedlar_pet
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
  форма: tpt_классическая_двусторонняя
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing
  форма: крепёж_и_монтажные_плиты
масштабируемость:
  режим: масштабируемая
  параметры:
  - масса_kg
  - выработка_тепла_W
  пределы:
    min:
      масса_kg: 0.05
      выработка_тепла_W: 0.1
    max:
      масса_kg: 50
      выработка_тепла_W: 50
  закон_масштабирования:
    масса: '≈ линейный от длины жгута и числа токопроводящих проводов оплётки (Smart
      Braid: жгут 250×180×45 масштабируется по числу ветвей без изменения шага плетения)'
    выработка_тепла: 'P = I²R по меди ветвей: при параллельных ветвях R ∝ 1/n, номинальный
      нагрев 0.6 Вт на ветку сохраняется; верх 50 Вт — предел по допустимому току
      изоляции'
  ограничивающие_части:
  - часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core
    причина: омический нагрев токопроводящих проводов и допустимый ток изоляции ограничивают
      максимум выработки_тепла_W
  - часть: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing
    причина: габарит кожуха 288×207×52 задаёт конверт жгута и максимальную массу/длину
      ветвей
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
    l: 350
    w: 230
    h: 85
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
источник_url: https://en.wikipedia.org/wiki/Shielded_cable
источник_дата: '2026-11-11'
---





# Изделие: оплётку из токопроводящих изолированных проводов

## Описание

«Smart Braid» — упрочняющая оплётка пневматической мышцы Маккиббена, сплетённая из токопроводящих изолированных проводов, образующих соленоидоподобную цепь: при сокращении мышцы меняется геометрия оплётки и её индуктивность, что даёт встроенное измерение сокращения и силы без отдельных датчиков (Felt, Hunter, Remy — IEEE Trans. Robotics 2017). В канонической декомпозиции изделие представлено сборкой «жгут токопроводящих изолированных проводов в защитном кожухе»: ядро-жгут (силовые и сигнальные ветки, экранирующая оплётка, защитная обмотка) в жёстком кожухе с разъёмной панелью и монтажными кронштейнами. Габаритный конверт изделия 350×230×85 мм — сборка вокруг кожуха ядра 288×207×52 (часть_..._housing, припуск ~15 % к ядру 250×180×45): торцевая разъёмная панель с разъёмами 37.1×37.1×38 (часть_..._connectors) добавляет ~50 мм по длине (288+50=338≤350); монтажные кронштейны 45×18×18 (часть_..._mounting) по бокам — ширина 207+18+зазор=230; кабельные вводы и сервисная петля жгута сверху — высота 85. Проверка упаковки: V(конверт)=350×230×85=6 842 500 мм³ ≥ Σ V(детей)=5 191 916 мм³ × 1.15 = 5 970 703 мм³ (коэффициент 1.32); по осям 350≥288, 230≥207, 85≥52.

Полное наименование (как в CSV): `оплётку из токопроводящих изолированных проводов — «Smart Braid»`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | classify_subsystem |
| категория | машиностроение | — | canon |
| габариты (конверт изделия) | 350×230×85 | мм | сборка: кожух ядра 288×207×52 + разъёмная панель ~50 мм + кронштейны и вводы (дети) |
| принцип «Smart Braid» | соленоидная оплётка из проводящих изолированных проводов, индуктивность ↦ сокращение/сила | — | Felt, Hunter, Remy, IEEE Trans. Robotics 2017 (PubMed 28503062) |
| измерение | встроенное (без датчиков): по изменению индуктивности | — | Felt et al. 2017 |

## Состав

Изделие верхнего уровня (уровень 1, подсистема приводная_система). Дочерние части уровня 2: часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core (жгут 250×180×45, декомпозирован на 4 ветки уровня 3: силовые провода, сигнальные провода, экранирующая оплётка, защитная обмотка), часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing (кожух 288×207×52), часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors (разъёмы 37.1×37.1×38), часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting (кронштейны 45×18×18).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Как «Smart Braid» (Felt et al.): оплётка сплетена из токопроводящих изолированных проводов так, что пересекающиеся витки образуют соленоидоподобную цепь; сокращение мышцы меняет шаг и диаметр плетения, а с ними — индуктивность и взаимные ёмкости цепи, измеряемые снаружи: само усиление становится датчиком сокращения и силы. Как жгут в исполнении сборки: ядро распределяет питание (силовые ветки, омический нагрев ~0.6 Вт) и сигнальные цепи обратной связи, экранирующая оплётка защищает от ЭМИ, кожух с разъёмной панелью обеспечивает механическую защиту и подключение, кронштейны — монтаж в приводной системе.

## Источники

- Felt W., Hunter M., Remy C.D. Contraction Sensing with Smart Braid McKibben Muscles (IEEE Trans. Robotics 2017; оплётка McKibben-мышцы из токопроводящих изолированных проводов, соленоидная индуктивная сенсорика) — https://pubmed.ncbi.nlm.nih.gov/28503062/ (обращение 2026-11-08)
- Smart braid: Air muscles that measure force and contraction (Felt, Remy) — https://www.semanticscholar.org/paper/591606c18a4344dec7d9f1e773b75300f324f0ee (обращение 2026-11-08)
- CSV: `начальные данные_final.csv` (пользовательский ввод)

---


## Декомпозиция

```mermaid
graph TD
    opletku_iz_tokoprovo["izdelie_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov"]
    opletku_iz_tokoprovodyasc["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core"]
    opletku_iz_tokoprovo --> opletku_iz_tokoprovodyasc
    opletku_iz_tokoprovodyasc["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_housing"]
    opletku_iz_tokoprovo --> opletku_iz_tokoprovodyasc
    opletku_iz_tokoprovodyasc["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_connectors"]
    opletku_iz_tokoprovo --> opletku_iz_tokoprovodyasc
    opletku_iz_tokoprovodyasc["часть_opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_mounting"]
    opletku_iz_tokoprovo --> opletku_iz_tokoprovodyasc
```
