---
id: SkyNet-T100Wheeled
тип: модель_SkyNet
класс: наземный_колёсный
категория: наземный_HK
тип_модели: наземный_колёсный
источник_происхождения: игра
функции: ["патруль", "разведка"]
канон_источник: Terminator: Resistance (2019)
произведения: ["work_046"]
производитель: Скайнет
статус_реальности: canon
подтип_модели: стандартный
многослойная_броня:
  слои:
    - номер: 1
      материал: b4c  # B₄C
      толщина_мм: {min: 2, target: 10}
    - номер: 2
      материал: ti6al4v  # Ti-6Al-4V
      толщина_мм: {min: 2, target: 10}
    - номер: 3
      материал: uhmwpe_dyneema  # UHMWPE
      толщина_мм: {min: 2, target: 10}
  тип_брони: наземный_колёсный
  соответствует_типу_модели: true  # F74, max_mass_percent: 40, min_layers: 3
доступность: фантастический
expected_subsystems: ["вычислительная", "энергетическая", "каркас", "сенсоры", "приводная_система", "система_связи", "навигация", "система_питания", "система_передвижения"]
relations:
  successor_of: null
  variation_of: null
  hybrid_of: []
  paradigm_shift_from: null
реализация_промышленная: 
  - izdelie_tverdooksidnyi_toplivnyi_element
  - izdelie_nasa_asc-e_srsc
  - izdelie_superkondensatory
  - izdelie_SkyNet-HKAerial
  - izdelie_SkyNet-Rev9
  - izdelie_SkyNet-Cameron
  - izdelie_metalinza
  - izdelie_mwir_nbn_640
  - izdelie_lidar_robosense_ac1
  - izdelie_hasel
  - izdelie_povorotnoe_uplotnenie
  - izdelie_elektroflyuidnye_volokna_mit
  - izdelie_radiatsionno-stoikii_neiromorfnyi_tmr
  - izdelie_razryvnye_mufty_iso_16028
  - izdelie_flat-face_couplings_iso_16028
реализация_ии: []
источник: web_search
источник_url: https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/TerminatorResistance
источник_разбора: канон
ии_перепроектирован:
  статус: false
  верификация: []
---
# v9.31: структурные поля §12.4.1-§12.4.X — добавлены как placeholder
# Реальные значения будут заполнены через web_search для каждой модели.
требования_выживаемости: 
  эми_защита: industrial
  термобарьер:
          рабочий_диапазон_C:
                      min: -40
                      target: 60
маскировка_инфильтратора: n/a (patrol)
тактико_технические_характеристики: 
  мобильность:
          скорость_км_ч:
                      min: 80
                      target: 200
  вооружение: плазма-пушки на винглетах
защита_от_собственной_радиации: n/a
кибербезопасность: 
  аппаратные_меры:
          HSM: true
          secure_boot: true
          TPM: true
          anti_tamper: zeroization
  iff: SkyNet IFF v3.1 (transponder 1090 MHz + crypto)
  шифрование: AES-256 + SkyNet proprietary
  skynet_protocol: Hive (collective consciousness) или Rogue (autonomous)
эмс_внутренняя: ECM + radar
компоновка_изделий: мотоциклетный форм-фактор
трассировка_соединителей: []
программное_обеспечение: 'Neural Net CPU + SkyNet OS (Hive mode по умолчанию, Rogue для автономных)'
единая_эми_стратегия: SkyNet patrol protocol
единая_герметичность: IP65
сертификация_модели_целого: 
  тест_skyet: phase_5 (F70 metrics PASS)
  канон_верификация: 'источник_разбора=канон'
журнал_экземпляра: SkyNet patrol unit registry
утилизация_после_120_лет: 'T-800: 120 лет на 1 топливной ячейке (canon); после истощения — замена ячеек или разборка на запчасти'
экипаж_оператор: 0
промышленная_база: Skynet automated factory (Cyberdyne Systems / CRS)
alice_specs: ALICE sync protocol v9.31 (SkyNet hive-mind)
original_improved: canon
дата_создания: 2026-11-03
дата_обновления: 2026-11-06
---
# SkyNet-T100Wheeled

## Описание

T-100 (колёсный) — лёгкий разведывательный дрон; 4 колеса; вооружение лёгкое.

По верифицированным данным веб-поиска (проверено 2026-11-06, TVTropes «Terminator: Resistance (Video Game)» — полный разбор состава врагов, Fandom «Machines» (Terminator Resistance Wiki), Fandom «T-1» и «Moto-Terminator» через web.archive.org): **юнит «T-100» и колесные машины в заявленном канон-источнике файла — Terminator: Resistance (2019) — НЕ появляются**. Полный состав машин игры по верификации: Spider Scout (первый враг, паучий), Silverfish, Armored Spider, Scout Drone и Armored Scout Drone (летающие разведчики), HK-Tank, HK-Aerial, T-800 (варианты T-808 с огнемётом, T-820, T-825/T-825V с двумя винтовками), T-850 Infiltrator (главный антагонист), T-600 (DLC Annihilation Line) — колесных или мотоциклоподобных дронов нет. Обозначение «T-100» существует в каноне лишь в двух контекстах: ① отдельная статья Terminator Wiki «T-100» (содержимое недоступно для проверки: Cloudflare + отсутствие снапшотов web.archive.org); ② режиссёр McG (Terminator Salvation) однократно назвал юнит T-1 «T-100» — Fandom отмечает: «It is unknown if this is merely an error, or the Terminator Salvation version of T-1» (T-1 — гусеничный, а не колесный). Ближайший канонический КОЛЕСНЫЙ юнит Skynet — **Moto-Terminator** (Terminator Salvation, 2009): автоматический мотоцикл-охотник («automated motorcycles, produced by Skynet sometime before 2018, whose main purpose is to hunt down humans»), «fastest land based Terminator» — до 200 миль/ч (~320 км/ч); базы Ducati; красные оптические сенсоры; двойные плазменные эмиттеры (в фильме), по арту — GE M134 Minigun и M1919 Browning; хранятся в ногах Harvester'а и выпускаются для загона бегущих людей; показан патрулирующим дорогу (Джон Коннор захватил и взломал патрульный Moto-Terminator и добрался на нём до Сан-Франциско); арктическая версия Snowminator (Alaskan Wilderness, комикс Salvation: Cold War). Лёгкие разведчики T: Resistance — летающие Scout/Armored Scout Drone и паучьи Spider Scout/Armored Spider. **РАСХОЖДЕНИЕ С ФАЙЛОМ:** ① «T-100 колёсный, 4 колеса, лёгкий разведдрон» не подтверждается ни одним источником — признак программного генерата (как MK-Sub #714/MK-Naval #717); ② канон_источник Terminator: Resistance (2019) ошибочен — юнита там нет; ③ ТТХ (2 оси/4 колеса, 600 кг, 80–200 км/ч, «плазма-пушки на винглетах») источниками не подтверждаются; ④ канонические колёсные аналоги — Moto-Terminator/Snowminator (Salvation); лёгкие разведчики T: Resistance — летающие и паучьи дроны; ⑤ остальное оставлено до реклассификации (F13/F33-таксономия), как для T-500 (#721)/T-200 (#713)/MK-Naval (#717).

## Источник канон

- **Произведение:** Terminator: Resistance (2019)
- **Тип:** игра
- **Каноничность:** canon

## Тактико-технические характеристики

| Параметр | Значение |
|---|---|
| число_осей | 2 |
| масса_кг | 600 |
| производитель | Скайнет |
| класс | наземный_колёсный |
| категория | наземный_HK |
| тип_модели | наземный_колёсный |

## Подсистемы (по типу)

- вычислительная
- энергетическая
- каркас
- сенсоры
- приводная_система
- система_связи
- навигация
- система_питания
- система_передвижения

## Многослойная броня (§11.6)

Минимум слоёв по типу: 3 (§11.6). Макс. доля массы брони: 40%.

1. B₄C (`b4c`)
2. Ti-6Al-4V (`ti6al4v`)
3. UHMWPE (`uhmwpe_dyneema`)

## Произведения, где появляется

- 📚 `work_046` — «Terminator: Resistance» (2019) → [`work_046.md`](../произведения/work_046.md)

## Источники

- Канон: Terminator: Resistance (2019) — опровергается верификацией: в игре нет юнита T-100 и колесных машин
- [Terminator: Resistance (Video Game) — TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/TerminatorResistance) — полный разбор состава врагов игры: Spider Scout (Goomba-первый враг), Silverfish, Armored Spider, Scout/Armored Scout Drone (Airborne Mook), HK-Tank, HK-Aerial, T-800/T-808/T-820/T-825V, T-850 Infiltrator, T-600 (DLC) — колесных и T-100 нет (проверено 2026-11-06)
- [Moto-Terminator | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/Moto-Terminator) — канонический колесный юнит Skynet: автоматический мотоцикл-охотник (Salvation 2009), до 200 mph (~320 км/ч), Ducati, двойные плазменные эмиттеры/GE M134; Harvester-носитель; взломан Коннором; Snowminator (проверено 2026-11-06 через web.archive.org)
- [T-1 | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/T-1) — «The T-1 from Terminator Salvation is once referred as T-100 by McG. It is unknown if this is merely an error, or the Terminator Salvation version of T-1»; T-1 гусеничный, охрана объектов Skynet VLA в 2018 (проверено 2026-11-06, сниппет поиска)
- [T-100 | Terminator Wiki — Fandom](https://terminator.fandom.com/wiki/T-100) — статья существует, содержимое недоступно (Cloudflare; снапшотов web.archive.org нет; проверено 2026-11-06)
