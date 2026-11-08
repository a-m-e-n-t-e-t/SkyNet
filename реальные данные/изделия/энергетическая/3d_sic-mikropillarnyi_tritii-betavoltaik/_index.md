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
    доля_массы: 0.19
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_micropillars
    материал: silicon_carbide
    доля_массы: 0.38
  - часть: часть_3d_sic-mikropillarnyi_tritii-betavoltaik_substrate
    материал: silicon_carbide
    доля_массы: 0.297
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
          l: 10
          w: 10
          h: 1
  выработка_энергии_W:
          min: 0.0001
          max: 0.01
          nominal: 0.001
  выработка_тепла_W:
          min: 0.081
          max: 0.162
          nominal: 0.162
наследуемые: {}
дополнительные: 
  изотоп: H-3 (tritium)
  T_жизни_лет: 12.32
  источник: 3D micropillar 4H-SiC tritium research
  тепловыделение_обоснование: 'β-распад трития: 0.5 г × 0.3240 Вт/г (калориметрия Pillinger 1961, Phys. Rev. 121, 232: 0.3240±0.0009 Вт/г) = 0.162 Вт; кросс-чек: 4.8 кКи × 5.7 кэВ (средняя энергия β) = 0.162 Вт; min = номинал/2 — после одного периода полураспада (12.32 лет); всё β-тепло генерируется в тритиевом слое (часть_..._isotope), SiC-части и корпус тепло не вырабатывают (прецедент: 4h-sic_betavoltaik, betavoltaiki)'
дата_создания: 2026-11-03
дата_обновления: 2026-11-08
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

Изделие верхнего уровня. Дочерние части не указаны (требуется декомпозиция).

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
