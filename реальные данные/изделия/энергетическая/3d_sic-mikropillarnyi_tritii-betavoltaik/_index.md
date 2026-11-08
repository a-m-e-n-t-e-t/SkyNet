---
id: izdelie_3d_sic-mikropillarnyi_tritii-betavoltaik
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: бета_вольтаик_3D_SiC
стандарты: []
исследовательская_группа: university_research
родитель: null
дочерние_части:
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
  - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case
материалы_частей:
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
    материал: sct
    форма: тонкоплёночный_изотопный_слой
    доля_массы: 0.19
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
    материал: monokristallicheskogo_sic
    форма: высокотемпературные_mems_и_сенсоры
    доля_массы: 0.38
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
    материал: monokristallicheskogo_sic
    форма: силовая_электроника
    доля_массы: 0.297
технологии_частей:
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
    технология: dc_magnetron_sputtering
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: sct
        роль: обрабатываемый
      - материал: monokristallicheskogo_sic
        роль: подложка
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
    технология: lazernoe_teksturirovanie_poverhnosti
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: monokristallicheskogo_sic
        роль: обрабатываемый
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
    технология: cmp
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: monokristallicheskogo_sic
        роль: обрабатываемый
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case
    технология: ebw
    доля_использования: 1.0
    материалы_для_процесса:
      - материал: ti-6al-4v
        роль: обрабатываемый
наследуемые_материалы:
  - материал: sct
    суммарная_доля_массы: 0.19
    источники_частей:
      - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
  - материал: monokristallicheskogo_sic
    суммарная_доля_массы: 0.677
    источники_частей:
      - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
      - часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
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
          min: 0.001
          max: 0.01
          nominal: 0.003
  габариты_mm:
          l: 13
          w: 13
          h: 4
  выработка_энергии_W:
          min: 0.0001
          max: 0.01
          nominal: 0.001
  выработка_тепла_W:
          min: 0.081
          max: 0.162
          nominal: 0.162
наследуемые: {}
масштабируемость:
  режим: масштабируемая
  параметры:
    - масса_kg
    - выработка_энергии_W
  пределы:
    min:
      масса_kg: 0.001
      выработка_энергии_W: 0.0001
    max:
      масса_kg: 0.01
      выработка_энергии_W: 0.01
  шаг: {}
  закон_масштабирования:
    масса_kg: 'квантована капсулой: 1 ячейка (капсула 13×13×4 мм огибающая) ≈ 4–5 г BOM (Ti-корпус 2 г + SiC 2 г + ScT₂ 0.5 г); масштабирование — ростом числа ячеек/стеков в корпусе прибора, удельная ~1 г/мВт эл.'
    выработка_энергии_W: 'P_эл = η·P_β: P_β 0.162 Вт (0.5 г трития, 4.8 kCi, Pillinger 1961), КПД-потолок 4H-SiC+тритий 18.6 % (large area, Alam et al. 2016/VT 2017), потолок плотности 85 мВт/см³ для 4H-SiC (OSTI 1548378); номинал 1 мВт (η ~0.6 %, запас на само-поглощение β и деградацию) → 10 мВт (толстый тритий-слой + многорядные пилляры); после 1 T½ (12.32 года) ×0.5'
  ограничивающие_части:
    - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope
      предел: 'слой ScT₂ 10×10×0.2 мм (4.8 kCi): CSDA-пробег β 18.6 кэВ в твёрдом теле ~1–2 мкм — само-поглощение лимитирует полезный поток (только приповерхностный слой); масштабирование мощности — площадью слоя, а не толщиной'
    - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
      предел: 'массив 3D-микростолбиков 4H-SiC 4×4×0.25 мм: площадь p-n перехода на единицу плоскости задаёт сбор β-потока; потолок КПД 18.6 % (Alam et al.), радиационная деградация SiC от β — деградация мощности за 12.32 года ~×2'
    - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case
      предел: 'капсула Ti-6Al-4V 12×12×3.5 мм: тритиевое удержание (ЭЛС-шов, натекание <1×10^-9 Па·м³/с) ограничивает загрузку трития и размеры ячейки; масса корпуса 2 г — нижний квант масштабирования'
дополнительные: 
  изотоп: H-3 (tritium)
  T_жизни_лет: 12.32
  источник: 3D micropillar 4H-SiC tritium research
  тепловыделение_обоснование: 'β-распад трития: 0.5 г × 0.3240 Вт/г (калориметрия Pillinger 1961, Phys. Rev. 121, 232: 0.3240±0.0009 Вт/г) = 0.162 Вт; кросс-чек: 4.8 кКи × 5.7 кэВ (средняя энергия β) = 0.162 Вт; min = номинал/2 — после одного периода полураспада (12.32 лет); всё β-тепло генерируется в тритиевом слое (часть_..._isotope), SiC-части и корпус тепло не вырабатывают (прецедент: 4h-sic_betavoltaik, betavoltaiki)'
дата_создания: 2026-11-03
дата_обновления: 2026-11-09
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: 3D SiC-микропилларный тритий-бетавольтаик

## Описание

3D SiC-микропилларный тритий-бетавольтаик

Полное наименование (как в CSV): `3D SiC-микропилларный тритий-бетавольтаик`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |
| тепловыделение (β-распад трития) | 0.162 Вт (min 0.081 после 1 T½) | Вт | Pillinger 1961, Phys. Rev. 121, 232: 0.3240±0.0009 Вт/г × 0.5 г |

(Параметры требуют уточнения через веб-поиск и вычислений; см. fc_изделие_масса, fc_изделие_стандарты в _field_contracts.yaml)

## Состав

Изделие верхнего уровня. Дочерние части: isotope (ScT₂ слой), micropillars (4H-SiC), substrate (4H-SiC), case (Ti-6Al-4V капсула).

## Используемые технологии

(Ссылки на реальные_данные/технологии/ добавляются после связывания)

## Используемые материалы

(Ссылки на реальные_данные/материалы/ добавляются после связывания)

## Принцип работы

Требует описания на основе инженерного анализа.

## Источники

- CSV: `начальные данные_final.csv` (пользовательский ввод)
- Pillinger, W. L. et al. — «Calorimetric Determination of the Heat Output of Tritium», Physical Review 121, 232 (1961): 0.3240±0.0009 Вт/г — https://link.aps.org/doi/10.1103/PhysRev.121.232 (обращение 2026-11-08)
- OSTI 4120857 (Pillinger, калориметрия трития 0.3240 Вт/г) — https://www.osti.gov/biblio/4120857
- Wikipedia Tritium (удельная активность 9650 Ки/г = 3.57×10¹⁴ Бк/г) — https://en.wikipedia.org/wiki/Tritium

---


## Декомпозиция

```mermaid
graph TD
    3d_sic-mikropillarny["izdelie_3d_sic-mikropillarnyi_tritii-betavoltaik"]
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_isotope"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
    3d_sic-mikropillarnyi_tri["часть_3d_sic-mikropillarnyi_tritii-betavoltaik_case"]
    3d_sic-mikropillarny --> 3d_sic-mikropillarnyi_tri
```
