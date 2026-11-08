---
id: izdelie_vysokotemperaturnyi_sverhprovodyaschii_podshipnik
тип: изделие
категория: машиностроение
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: HTS_подшипник
стандарты: 
  - ISO 15241
исследовательская_группа: boeing_nasa
родитель: null
дочерние_части:
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft
  - часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing
материалы_частей:
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element
    материал: ybco_bulk
    форма: магнитный_подвес_hts_подшипник
    доля_массы: 0.285
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet
    материал: ndfeb
    доля_массы: 0.38
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat
    материал: stainless_steel_316
    доля_массы: 0.38
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft
    материал: titanium_alloy
    доля_массы: 0.095
технологии_частей:
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element
    технология: tverdofaznyi_sintez
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ybco
        роль: обрабатываемый
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet
    технология: vakuumnoe_spekanie
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ndfeb
        роль: обрабатываемый
      - материал: argon
        роль: защитная_атмосфера
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat
    технология: ebw
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ss_316l
        роль: обрабатываемый
  - часть: часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft
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
          max: 50
          nominal: 10
  габариты_mm:
          l: 220
          w: 220
          h: 200
  выработка_энергии_W:
          min: 0
          max: 0
          nominal: 0
  выработка_тепла_W:
          min: 1.05
          max: 3
          nominal: 1.5
наследуемые: {}
дополнительные: 
  T_рабочая_C: -196
  N_критическая_об_мин: 10000
  примечание_тепло_баланс: 'суммарная криогенная нагрузка: статический теплоприток криостата ~1 Вт (излучение на полированных стенках + кондукция опор/трубопроводов, 77 К) + потери YBCO-статора 0.3 Вт (гистерезис/вихревые от неоднородности поля ротора при номинальных об/мин) + собственные ~0.2 Вт (эдди в углепластиковом бандаже, ветровые в вакууме); Σ детей = 1.3 Вт ≤ номинал 1.5 Вт; при 0 об/мин — только теплоприток ~1.05 Вт; при 10000 об/мин — до ~3 Вт (Murakami Physica C 378 (2002) 883: 8.03 Вт при 6000 об/мин для класса 838 Н — масштаб на 10 кг класс)'
  обоснование_габаритов: 'сборочная огибающая: корпус (housing) 180×180×120 мм — внутри криостат 170×170×90 мм и магнитная пара ротор Ø150/статор 30×30×15; в плане 220×220 мм = корпус 180×180 + монтажный фланец с болтами и криогенными магистралями заливки LN2 (по 20 мм на сторону корпуса); по высоте 200 мм = корпус 120 + верхний выступ вала Ø42 мм (вал 42×42×150 мм частично выходит из корпуса для соединения с приводом) + сервисный зазор датчиков положения; V=220×220×200=9 680 000 мм³ ≥ ΣV детей×1.15=8 946 540 мм³ (ΣV детей=7 779 600 мм³ — криостат 2 601 000 + housing 3 888 000 + hts_element 13 500 + magnet 1 012 500 + shaft 264 600), запас +8.2 %; оси: l 220≥180, w 220≥180, h 200≥150'
  источник: Boeing HTS bearing research
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: Высокотемпературный сверхпроводящий подшипник

## Описание

Высокотемпературный сверхпроводящий подшипник (HTS)

Полное наименование (как в CSV): `Высокотемпературный сверхпроводящий подшипник (HTS)`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |
| выработка тепла (номинал) | 1.5 | W | баланс: теплоприток криостата 1.0 + потери YBCO 0.3 + собственные 0.2 |
| выработка тепла (мин/макс) | 1.05 / 3 | W | мин: только теплоприток при 0 об/мин; макс: 10000 об/мин (масштаб Murakami 2002: 8 Вт при 6000 об/мин, класс 838 Н) |
| рабочая температура | −196 (77 K) | °C | LN2-криостат |
| критические обороты | 10000 | об/мин | canon (Boeing HTS bearing research) |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части (уровень 2):

- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element` — массивный YBCO-статор 30×30×15 мм (гистерезисные/вихревые потери 0.3 Вт)
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet` — сегментированный NdFeB-ротор Ø150/Ø90×45 мм (пассивный, 0 Вт)
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat` — вакуумный LN2-криостат 170×170×90 мм (статический теплоприток 1.0 Вт)
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft` — вал (пассивный, 0 Вт)
- `часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing` — корпус (пассивный, 0 Вт)

## Используемые технологии

Технологии обработки частей (frontmatter `технологии_частей`):

- `hts_element` → `tverdofaznyi_sintez` — порошковый керамический маршрут YBCO: оксидные/карбонатные прекурсоры (Y₂O₃ + BaCO₃ + CuO) → кальцинирование → прессование → спекание; финальная форма массивного статора — однодоменный TSMG-блок (top-seeded melt growth — подтверждено веб-поиском: IAEA «Development of superconductor bulk for superconductor bearing», ResearchGate «Reliable fabrication of single grain bulk YBCO»)
- `magnet` → `vakuumnoe_spekanie` — промышленный маршрут sintered NdFeB: порошковая металлургия, вакуумное спекание зелёных прессовок при 1000–1100 °C (типично 1050–1080 °C) — подтверждено веб-поиском (radialmagnet.com, ccmagnetics.com, US9643249B2); защитная атмосфера — аргон
- `cryostat` → `ebw` — электронно-лучевая сварка в вакууме герметичных швов корпуса криостата из нержавеющей стали (316L — сварочный вариант 316 с низким углеродом для стойкости к межкристаллитной коррозии швов)
- `shaft` → `frezervanie_chpu` — ЧПУ-обработка вала из проката титанового сплава Ti-6Al-4V (посадочные поверхности под магнитный узел и привод)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Ротор (NdFeB-кольцо + вал) левитирует над массивными YBCO-блоками (эффект Мейснера + пиннинг потока, field-cooled режим): механический контакт отсутствует, сухое трение равно нулю. Тепловой баланс изделия — суммарная криогенная нагрузка, снимаемая криоохладителем/испарением LN2: (1) статический теплоприток в криостат ~1 Вт — излучение на полированных стенках + кондукция через опоры и заливные трубопроводы (вакуум 5×10⁻³ Торр устраняет конвекцию); (2) вращательные потери в YBCO-статоре ~0.3 Вт при номинальных оборотах — гистерезисные и вихревые потери от неоднородности поля сегментированного ротора (доминирующий механизм вращательных потерь HTS-подшипников — Deng 2015; при 6000 об/мин для класса 838 Н измерено 8.03 Вт — Murakami 2002); (3) собственные потери ~0.2 Вт (эдди в углепластиковом бандаже ротора, ветровые в вакууме — пренебрежимо малы). Сверхпроводник омических потерь не имеет (DC-режим пиннинга) — поэтому потери статора на порядки ниже обычных магнитных подшипников, а основную долю нагрузки даёт криостат.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Murakami A. et al., «Fabrication and evaluation of superconducting bearing» / Proc. of SMB, Physica C 378–381 (2002) 883 — вращательные потери SMB 8.03 Вт при 6000 об/мин (нагрузка 838 Н), главный механизм — неоднородность магнитного поля — https://ui.adsabs.harvard.edu/abs/2002PhyC..378..883M (обращение 2026-11-08)
- Deng Z. et al. (2015), «Effect of anisotropic magnetization on the rotational loss in YBCO bulk» — эдди-потери от неоднородного поля — один из главных механизмов вращательных потерь HTS-подшипника (обращение 2026-11-08)
- Werfel F.N. et al., «Application Advances in HTS Bearing Technology» — инкапсулированные HTS-подшипники: вакуумный криостат, отсечка излучения и газовой кондукции при 77 К — https://www.magneticbearings.org/app/uploads/publications/ismb7/ismb7_submission_101.pdf (обращение 2026-11-08, веб-поиск)
- IAEA INIS, «Development of superconductor bulk for superconductor bearing» — TSMG-процесс изготовления монодоменных YBCO bulk для подшипников — https://inis.iaea.org/records/xnkvy-ahn13 (обращение 2026-11-08, веб-поиск)
- «How Neodymium Magnets Are Made» (radialmagnet.com) + «Preparation process of sintered NdFeB magnets» (ccmagnetics.com) — вакуумное спекание NdFeB при 1000–1100 °C (типично 1050–1080 °C); US Patent 9643249B2 — вакуумная спекательная печь для NdFeB (обращение 2026-11-08, веб-поиск)
- Johnson B.R. et al. (2017), «A Large-Diameter Hollow-Shaft Cryogenic Motor Based on a Superconducting Magnetic Bearing» — bulk YBCO-диски статора (25×13 мм, 60 Н/диск) в криостате с NdFeB-ротором — https://arxiv.org/html/1706.05963v3 (обращение 2026-11-08, веб-поиск)

---


## Декомпозиция

```mermaid
graph TD
    vysokotemperaturnyi_["izdelie_vysokotemperaturnyi_sverhprovodyaschii_podshipnik"]
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_hts_element"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_magnet"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_cryostat"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_shaft"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
    vysokotemperaturnyi_sverh["часть_vysokotemperaturnyi_sverhprovodyaschii_podshipnik_housing"]
    vysokotemperaturnyi_ --> vysokotemperaturnyi_sverh
```
