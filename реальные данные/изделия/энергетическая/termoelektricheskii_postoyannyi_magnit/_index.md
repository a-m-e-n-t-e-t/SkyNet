---
id: izdelie_termoelektricheskii_postoyannyi_magnit
тип: изделие
категория: энергетика
уровень_иерархии: верхний
уровень_номер: 1
подсистема: энергетическая
подтип: термоэлектрический_генератор
стандарты: 
  - ASTM E1289
исследовательская_группа: ii_vi_marlow
родитель: null
дочерние_части:
  - часть_termoelektricheskii_postoyannyi_magnit_teg_modules
  - часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot
  - часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold
  - часть_termoelektricheskii_postoyannyi_magnit_clamping
  - часть_termoelektricheskii_postoyannyi_magnit_insulation
материалы_частей:
  - часть: часть_termoelektricheskii_postoyannyi_magnit_teg_modules
    материал: bi2te3
    доля_массы: 0.36
  - часть: часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot
    материал: copper
    доля_массы: 0.19
  - часть: часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold
    материал: aluminum
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
          min: 0.1
          max: 5
          nominal: 0.5
  габариты_mm:
          l: 50
          w: 50
          h: 5
  выработка_энергии_W:
          min: 0.01
          max: 10
          nominal: 1
  выработка_тепла_W:
          min: 0.01
          max: 10
          nominal: 1
наследуемые: {}
дополнительные: 
  T_рабочая_C: 250
  КПД_процентов: 8
  источник: II-VI Marlow TEG
дата_создания: 2026-11-03
дата_обновления: 2026-11-03
источник: user_input
источник_разбора: пользовательский ввод
---
# Изделие: термоэлектрический постоянный магнит

## Описание

термоэлектрический постоянный магнит

Полное наименование (как в CSV): `термоэлектрический постоянный магнит`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | энергетическая | — | classify_subsystem |
| категория | прочее | — | — |

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

---


## Декомпозиция

```mermaid
graph TD
    termoelektricheskii_["izdelie_termoelektricheskii_postoyannyi_magnit"]
    termoelektricheskii_posto["часть_termoelektricheskii_postoyannyi_magnit_teg_modules"]
    termoelektricheskii_ --> termoelektricheskii_posto
    termoelektricheskii_posto["часть_termoelektricheskii_postoyannyi_magnit_heat_sink_hot"]
    termoelektricheskii_ --> termoelektricheskii_posto
    termoelektricheskii_posto["часть_termoelektricheskii_postoyannyi_magnit_heat_sink_cold"]
    termoelektricheskii_ --> termoelektricheskii_posto
    termoelektricheskii_posto["часть_termoelektricheskii_postoyannyi_magnit_clamping"]
    termoelektricheskii_ --> termoelektricheskii_posto
    termoelektricheskii_posto["часть_termoelektricheskii_postoyannyi_magnit_insulation"]
    termoelektricheskii_ --> termoelektricheskii_posto
```
