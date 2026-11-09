---















id: material_socl2_lialcl4_electrolit
тип: материал
класс: неорганическая_жидкость
химический_состав: 'Раствор LiAlCl₄ ~1.5 М в тионилхлориде SOCl₂'
кристаллическая_структура: аморфный
вариант_структуры: liquid_solution
оптимальная_структура:
  структура: аморфный
  обоснование_выбора: "Жидкий электролит-катод первичных Li-SOCl₂ ячеек; SOCl₂ — одновременно растворитель и деполяризатор (веб-верификация Tadiran/Hollingsworth-Vose)"
  применение_по_умолчанию: электролит_первичных_химических_источников
  источник_обоснования: web_search
варианты_по_применению:
  бобинный_высокоёмкостный:
    описание: Bobbin-конструкция (цилиндрическая катодная трубка, слоистый Li-анод) — максимальная удельная энергия среди всех первичных ячеек.
    свойства: до 710 Втч/кг и 1420 Втч/л; саморазряд 0.7-3%/год при комнатной температуре; срок хранения/службы 10-20 лет; НРЦ 3.6 В; токи мкА-единицы мА; характерна пассивация LiCl-плёнки (voltage delay).
    применение: счётчики воды/газа/тепла, датчики IoT, резервное питание памяти, аварийные сигнализаторы — многолетние низкотоковые нагрузки.
    источник_url: https://www.batterypowertips.com/what-is-a-lithium-thionyl-chloride-battery-2
  спиральный_высокотоковый:
    описание: Спирально-навитые (spiral-wound) электроды — увеличенная площадь межфазной границы против bobbin.
    свойства: существенно меньшее внутреннее сопротивление и большие рабочие токи при меньшей удельной энергии и ресурсе; рабочий диапазон -55…+85°C.
    применение: GPS/GSM-трекеры, RTU телеметрия, аварийные маяки, оборудование с пиковыми токами.
    источник_url: https://www.globtek.com/en/battery-packs/lithium-thionyl-chloride-li-socl2-batteries
  высокотемпературный_модифицированный:
    описание: Модифицированный электролит и герметизация для высокотемпературных серий — устойчивость к ускоренной пассивации и росту саморазряда при нагреве.
    свойства: рабочие температуры до +125°C (стандарт -55…+85°C); учёт пассивации при высоких T обязательны при проектировании.
    применение: медицинские приборы с термической стерилизацией до 125°C, downhole нефтегазовое оборудование, автоклавируемые RFID-метки.
    источник_url: https://www.batterypowertips.com/what-is-a-lithium-thionyl-chloride-battery-2
  hlc_гибридный_импульсный:
    описание: Bobbin Li-SOCl₂ ячейка, гибридизированная с гибридным слой-конденсатором (Hybrid Layer Capacitor, HLC) — источник импульсов.
    свойства: бобинная база даёт многолетний ресурс, HLC выдаёт периодические высокие импульсные токи; комбинация снимает ограничение по пиковому току bobbin-элементов.
    применение: двухсторонняя беспроводная связь, smart-metering с передачей данных, устройства с редкими мощными радиопередачами.
    источник_url: https://www.batterypowertips.com/what-is-a-lithium-thionyl-chloride-battery-2
исследовательская_группа: null
стандарты: []
версия: реальная
статус_реальности: real
доступность: промышленный
статус: извлечено
источник: web_search
источник_url: https://tadiranbatteries.de/lithium-thionyl-chloride
источник_дата: 2026-11-05
источник_разбора: веб-верификация
ии_перепроектирован:
  статус: false
  верификация: []
основные:
  плотность_kg_m3: 1630
  прочность_МПа: {min: null, max: null, nominal: null}
  предел_текучести_МПа: {min: null, max: null, nominal: null}
  модуль_упругости_ГПа: null
  коэффициент_Пуассона: null
  ударная_вязкость_Дж_см2: null
  усталостная_прочность_МПа: {min: null, max: null, nominal: null}
  температура_плавления_C: -105
  теплопроводность_W_mK: null
  температура_кипения_C: 74.6
дополнительные:
  рабочая_температура_C: '-55…+85'
  удельная_энергия_Втч_кг: 650
  примечание: 'Токсичен, коррозионен; герметичное исполнение обязательно'

сравнение_структур:
  раствор_стандартный_1_5m:
    описание: Базовая форма — ~1.5 М раствор LiAlCl₄ в SOCl₂; SOCl₂ является одновременно растворителем и жидким катодом-деполяризатором (катаодно-растворимая химия).
    свойства: Tпл -105°C, Tкип 74.6°C; плотность ~1630 кг/м3; рабочая температура -55…+85°C; высокая ионная проводимость; продукты разряда — LiCl-пассивация анода (саморазряд <1-3%/год).
    применение: все серийные Li-SOCl₂ ячейки (bobbin/spiral/HLC) от Tadiran, Saft, EEMB, Ultralife.
    источник_url: https://tadiranbatteries.de/lithium-thionyl-chloride
  электролит_с_и2_молекулярным_катализатором:
    описание: Экспериментальная форма состава — добавка молекулярного катализатора I₂ в электролит Li-SOCl₂, перестраивающая химию разряда/заряда.
    свойства: молекулярный катализ I₂ тейлорит механизмы заряд-разряда, превращая первичную систему в мощную перезаряжаемую (ResearchGate 2023); сохраняется высокая плотность энергии.
    применение: перспективные перезаряжаемые высокомощные Li-SOCl₂ системы, R&D первичных элементов с увеличенным ресурсом.
    источник_url: https://www.researchgate.net/publication/374398347_Transforming_a_Primary_Li-SOCl_2_Battery_into_a_High-Power_Rechargeable_System_via_Molecular_Catalysis
---
## Описание

Жидкий неорганический электролит первичных литиевых ячеек Li-SOCl₂: ~1.5 М раствор тетрахлороалюмината лития (LiAlCl₄) в тионилхлориде (SOCl₂). Уникальная химия: SOCl₂ — одновременно растворитель электролита и жидкий катодный деполяризатор (cathode-active solvent), что обеспечивает рекордную удельную энергию до 650 Вт·ч/кг, диапазон −55…+85 °C и срок хранения 10–20 лет. Промышленный стандарт дистанционных датчиков, счётчиков, IoT-меток (референсы: Tadiran, Saft, Eve). Плотность ~1.63 г/см³, t кип SOCl₂ 74.6 °C.

## Технические характеристики

| Параметр | Значение | Единица | Источник |
|---|---|---|---|
| тип узла | материал | — | canon |


## Источники

- [Tadiran: Lithium Thionyl Chloride](https://tadiranbatteries.de/lithium-thionyl-chloride)
- [Hollingsworth & Vose: LiSOCl2 separators](https://www.hollingsworth-vose.com/products/energy-solutions/primary-battery/lithium-thionyl-chloride)
- Battery Power Tips (Tadiran) — what is a Li-SOCl2 battery (bobbin up to 710 Wh/kg and 1420 Wh/l, self-discharge 0.7-3%/yr, modified versions to +125°C, HLC hybrid layer capacitor for pulses): https://www.batterypowertips.com/what-is-a-lithium-thionyl-chloride-battery-2
- GlobTek — Li-SOCl2 battery packs (spiral electrodes for power applications, bobbin for energy, 1/2AA-D formats, 3.6 V): https://www.globtek.com/en/battery-packs/lithium-thionyl-chloride-li-socl2-batteries
- UniRoss guide — bobbin (higher energy density, low continuous drain) vs spiral-wound (lower internal resistance): https://uniross.com/the-complete-guide-to-lithium-thionyl-chloride-li-socl%E2%82%82-batteries
- ResearchGate 2023 — molecular catalyst I2 in Li-SOCl2 electrolyte -> high-power rechargeable system: https://www.researchgate.net/publication/374398347_Transforming_a_Primary_Li-SOCl_2_Battery_into_a_High-Power_Rechargeable_System_via_Molecular_Catalysis
