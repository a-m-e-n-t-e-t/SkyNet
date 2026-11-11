---
id: izdelie_pezoelektricheskii_gromkogovoritel
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
- часть_pezoelektricheskii_gromkogovoritel_core
- часть_pezoelektricheskii_gromkogovoritel_housing
- часть_pezoelektricheskii_gromkogovoritel_connectors
- часть_pezoelektricheskii_gromkogovoritel_mounting
материалы_частей:
- часть: часть_pezoelektricheskii_gromkogovoritel_core
  материал: latun_c36000
  форма: пруток_автоматный_ASTM_B16
  доля_массы: 0.45
- часть: часть_pezoelektricheskii_gromkogovoritel_housing
  материал: al_6061-t6
  форма: корпуса_электроники
  доля_массы: 0.27
технологии_частей:
- часть: часть_pezoelektricheskii_gromkogovoritel_core
  технология: shtampovka_listovaya
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: latun_c36000
    роль: обрабатываемый
- часть: часть_pezoelektricheskii_gromkogovoritel_housing
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: al_6061-t6
    роль: обрабатываемый
- часть: часть_pezoelektricheskii_gromkogovoritel_connectors
  технология: tokarnaya_obrabotka_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: latun_c36000
    роль: обрабатываемый
- часть: часть_pezoelektricheskii_gromkogovoritel_mounting
  технология: frezervanie_chpu
  доля_использования: 1.0
  материалы_для_процесса:
  - материал: ss_aisi_304
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
    l: 100
    w: 50
    h: 50
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
наследуемые_материалы:
- материал: latun_c36000
  суммарная_доля_массы: 0.45
  источники_частей:
  - часть_pezoelektricheskii_gromkogovoritel_core
  форма: пруток_автоматный_ASTM_B16
- материал: al_6061-t6
  суммарная_доля_массы: 0.27
  источники_частей:
  - часть_pezoelektricheskii_gromkogovoritel_housing
  форма: корпуса_электроники
масштабируемость:
  режим: масштабируемая
  параметры:
  - имя: количество_единиц
    диапазон:
    - 1
    - 1000
    единица: шт
  - имя: масса_единицы
    диапазон:
    - 0.005
    - 0.1
    единица: kg
  - имя: резонансная_частота
    диапазон:
    - 1
    - 20
    единица: kHz
  пределы:
    max_единиц_в_системе: 1000
    min_массы: 0.005
    max_массы: 0.1
    min_частоты: 1
    max_частоты: 20
  закон_масштабирования: 'линейный — масса_системы = N × масса_единицы (без overhead);
    типовая установка: Murata 7BB-35-3L0 (35mm dia, 2.8kHz, 30nF); KSN1090A (33g,
    50W, 450Hz-20kHz)'
  ограничивающие_части:
  - часть_pezoelektricheskii_gromkogovoritel_core (piezo ceramic disc + brass diaphragm
    — критическая точность производства)
  - часть_pezoelektricheskii_gromkogovoritel_housing (al_6061-t6 + anodizing — стандартное
    производство)
источник_url: https://en.wikipedia.org/wiki/Piezoelectric_speaker
источник_дата: '2026-11-11'
---

# Изделие: пьезоэлектрический громкоговоритель

## Описание

пьезоэлектрический громкоговоритель

Полное наименование (как в CSV): `пьезоэлектрический громкоговоритель`

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| подсистема | приводная_система | — | classify_subsystem |
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
    pezoelektricheskii_g["izdelie_pezoelektricheskii_gromkogovoritel"]
    pezoelektricheskii_gromko["часть_pezoelektricheskii_gromkogovoritel_core"]
    pezoelektricheskii_g --> pezoelektricheskii_gromko
    pezoelektricheskii_gromko["часть_pezoelektricheskii_gromkogovoritel_housing"]
    pezoelektricheskii_g --> pezoelektricheskii_gromko
    pezoelektricheskii_gromko["часть_pezoelektricheskii_gromkogovoritel_connectors"]
    pezoelektricheskii_g --> pezoelektricheskii_gromko
    pezoelektricheskii_gromko["часть_pezoelektricheskii_gromkogovoritel_mounting"]
    pezoelektricheskii_g --> pezoelektricheskii_gromko
```
