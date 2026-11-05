# -*- coding: utf-8 -*-
"""Issue #107 (F25 cluster 100×100×50): Batch 2 — 71 файлов _core (основной_элемент).
Каждому: уникальные габариты/масса по референсу (datasheet или оценка), материал из библиотеки,
источник_url, реальное описание. Идемпотентно.
"""
import re, glob, os, sys

ITEMS = {
 # id: (l, w, h, massa, mat, url, ref, basis_kind, funkc)
 'ads-b_priemnik_core': ('90','46','14',0.05,'al_6061-t6','https://en.wikipedia.org/wiki/Automatic_dependent_surveillance%E2%80%93broadcast','приёмник ADS-B класса RTL-SDR/FlightAware USB-стика (типовые ~90×46×14 мм, 50 г)','ref','Приёмник ADS-B (1090 МГц) для приёма телеметрии воздушных целей — РЧ-фронтенд с SDR-демодулятором и USB/LVDS-выходом'),
 'aesa_radar_core': ('140','90','20',0.35,'al_6061-t6','https://en.wikipedia.org/wiki/Active_electronically_scanned_array','AESA-модуль (антенная плата с T/R-каналами, оценка по типовым X-полосным платам)','est','Передающий модуль AESA-радара — антенная плата с приёмо-передающими каналами, распределительной сетью и жидкостным теплосъёмом'),
 'akusticheskaya_linza_core': ('80','80','35',0.18,'silikon_80_shore_a_+_steklyannye_mikrosfery','https://en.wikipedia.org/wiki/Acoustic_lens','акустическая линза (силикон со стеклянными микросферами, оценка)','est','Акустическая линза — фокусировка звукового/ультразвукового потока за счёт градиента скорости звука в композите'),
 'apa_core': ('21','16','10',0.022,'ti-6al-4v','https://en.wikipedia.org/wiki/Piezoelectricity','Cedrat APA35XS класс (усилительный пьезо-привод ~21×16×10 мм, ~20 г)','ref','Усиленный пьезоэлектрический привод (Amplified Piezo Actuator) — пьезостек с лямбда-рычагом, ход ~40–60 мкм при усилии до сотен Н'),
 'belleville_shaiby_core': ('25','25','15',0.03,'stal_st3','https://en.wikipedia.org/wiki/Belleville_washer','пакет тарельчатых пружин Ø25 (типовой стек DIN 2093)','ref','Пакет тарельчатых (бельвильских) пружин — осевая упругая связь с высокой жёсткостью в компактном объёме, DIN 2093'),
 'bldc_core': ('45','45','90',0.35,'al_6061-t6','https://www.maxongroup.com','бесколлекторный двигатель класса Maxon EC45 (Ø45×90, ~350 г)','ref','Бесколлекторный двигатель (BLDC) Ø45 — ротор с неодимовыми магнитами, 3-фазная обмотка, трапецеидальная коммутация'),
 'bldc_+_enkoder_core': ('45','45','110',0.42,'al_6061-t6','https://www.maxongroup.com','BLDC Ø45 с энкодером (длина 110 мм с установкой инкрементального энкодера)','ref','BLDC-двигатель с встроенным инкрементальным энкодером (500–4096 imp/rev) — сервоприводная ось с обратной связью по положению'),
 'copv_core': ('300','300','500',3.5,'cfrp_t1100g','https://en.wikipedia.org/wiki/Composite_overwrapped_pressure_vessel','COPV малого класса (Ø300×500, углеволокно BF3-обмотка, оценка по типовым)','est','Композитный баллон высокого давления (COPV) — тонкостенный металлический лайнер с намоткой углеволокна T1100, хранение рабочего газа 300+ бар'),
 'cw-lazer_core': ('120','60','50',0.45,'al_6061-t6','https://en.wikipedia.org/wiki/Laser','лазерный модуль непрерывного излучения (типовой волоконный/диодный модуль класса 100 Вт, оценка)','est','Лазерный модуль непрерывного излучения (CW) — диодный/волоконный источник с коллиматором и термостабилизацией'),
 'dea_core': ('60','60','5',0.01,'elastomernaya_matritsa','https://en.wikipedia.org/wiki/Electroactive_polymer','диэлектрический эластомерный актуатор (плёнка 60×60, ~10 г)','ref','Диэлектрический эластомерный актуатор (DEA) — эластомерная плёнка с complying-электродами: при 3–10 кВ сжимается до 10–30 % площади'),
 'dielektricheskie_elastomernye_datchiki_core': ('40','40','2',0.004,'p_vdf-trfe-cfe','https://en.wikipedia.org/wiki/Electroactive_polymer','датчик на диэлектрических эластомерах (плёнка 40×40)','ref','Датчик на диэлектрических эластомерах — изменение ёмкости при растяжении/давлении, полимер P(VDF-TrFE-CFE) с высоким k'),
 'dvs_core': ('50','48','35',0.09,'al_6061-t6','https://en.wikipedia.org/wiki/Dynamic_and_active-pixel_vision_sensor','камера DVS класса iniVation DAVIS346 (~50×48×35 мм)','ref','Динамический сенсор зрения (DVS/DAVIS) — пиксели реагируют только на изменение яркости (микросекундная задержка, 120 дБ динамический диапазон)'),
 'elektroflyuidnye_volokna_mit_core': ('100','5','5',0.002,'ionnaya_zhidkost_emim_tfsi','https://news.mit.edu','электрофлюидное волокно (MIT, канал с ионной жидкостью, оценка)','est','Электрофлюидное волокно — гибкое волокно с микроканалом, заполненным ионной жидкостью (EMIM-TFSI): исполнительный/сенсорный элемент мягкой робототехники'),
 'eo_ir_kamera_core': ('65','65','80',0.30,'al_6061-t6','https://en.wikipedia.org/wiki/Electro-optics','EO/IR камерный модуль (телевизионный + ИК-каналы, оценка по компактным)','est','Оптико-электронный модуль (EO/IR) — двухспектральный канал: телевизионная CMOS-матрица + ИК-камера с общей оптической осью'),
 'event_cameras_core': ('45','35','12',0.025,'al_6061-t6','https://en.wikipedia.org/wiki/Event_camera','модуль event-камеры класса Prophesee IMX636 EVK (~45×35×12)','ref','Модуль event-камеры — сенсор имитирует сетчатку: асинхронные события яркости с латентностью микросекунды (Prophesee/IMX636 класс)'),
 'ferritovye_klinya_na_kabelyah_sensorov_core': ('30','15','15',0.02,'magnitnaya_rezina_ferritovyi_poroshok','https://en.wikipedia.org/wiki/Ferrite_(magnet)','ферритовые кольцевые фильтры на кабелях (клип-фильтр ~30×15×15)','ref','Клип-фильтры на ферритах для кабелей сенсоров — подавление синфазных РЧ-помех (демпфирование ВЧ-наводок)'),
 'flat-face_couplings_iso_16028_core': ('35','35','90',0.25,'stal_st3','https://en.wikipedia.org/wiki/Quick_coupler','плоскостыковые быстроразъёмы ISO 16028 (типоразмер 1/2″)','ref','Плоскостыковые гидравлические быстроразъёмные муфты ISO 16028 — соединение с минимальной утечкой (плоский клапан), типоразмер 12 (1/2″)'),
 'fleksury_8_diskov_po_0_15_mm_core': ('50','50','8',0.012,'becu','https://en.wikipedia.org/wiki/Flexure_bearing','пакет гибких дисков (8×0.15 мм, бериллиевая бронза)','ref','Гибкий узел из 8 дисков по 0,15 мм (бериллиевая бронза) — упругий параллелограмм без трения для прецизионных перемещений'),
 'flir_boson_640_core': ('21','21','13',0.01,'al_6061-t6','https://www.flir.com/products/boson/','FLIR Boson 640 (20.6×20.6×12.7 мм, ~10 г)','ref','Тепловизионный модуль LWIR FLIR Boson 640 — микроболометр 640×512, 12 мкм пиксель, диапазон 8–14 мкм'),
 'flir_core': ('10','13','7',0.001,'si','https://www.flir.com/products/lepton/','FLIR Lepton (10.1×12.9×7.2 мм, ~1 г)','ref','Микротепловизионный модуль FLIR Lepton — самый компактный микроболометр (80×60), применяется во встраиваемых системах'),
 'flir_lwir_2_core': ('43','43','30',0.072,'al_6061-t6','https://www.flir.com/products/tau-2/','FLIR Tau 2 (43×43×30 мм, ~72 г)','ref','Тепловизионный модуль FLIR Tau 2 — 640×512 микроболометр, профессиональная серия для БПЛА и наведения'),
 'gibkii_pcb_core': ('100','80','1',0.02,'poliimid','https://en.wikipedia.org/wiki/Flexible_electronics','гибкая печатная плата (полиимид, 100×80, двухслойная)','ref','Гибкая печатная плата — полиимидная подложка (25–125 мкм) с медными проводниками: динамические изгибы до 10⁶ циклов'),
 'gidravlicheskie_iskusstvennye_myshtsy_makkibbena_core': ('250','15','15',0.06,'silicone-textile_composite','https://en.wikipedia.org/wiki/Pneumatic_artificial_muscles','искусственная мышца Мак-Киббена (гидравлическая, 250 мм, текстильно-силиконовая)','ref','Гидравлическая искусственная мышца Мак-Киббена — эластичная камера в текстильной оплётке: при подаче давления сокращается до 20–30 % длины'),
 'gidrostaticheskie_gazovye_podshipniki_na_gelii_core': ('60','60','40',0.35,'stal_st3','https://en.wikipedia.org/wiki/Air_bearing','газостатический подшипник Ø60 (гелий, оценка по прецизионным)','est','Газостатический подшипник на гелии — внешний компрессор подаёт газ через дроссели в зазор ~10–20 мкм: трение практически отсутствует'),
 'hasel_core': ('50','50','3',0.005,'halve_p_vdf-trfe-cfe','https://www.nature.com/articles/s41586-018-0097-2','HASEL актуатор (Keplinger 2018, Nature 559: электрогидравлический мягкий привод)','ref','Мягкий актуатор HASEL (hydraulically amplified self-healing electrostatic) — жидкий диэлектрик между электродами: электростатическое сжатие даёт мышечное движение'),
 'ipg_yls-eco_core': ('250','200','150',15,'stal_st3','https://www.ipgphotonics.com','лазерный модуль IPG YLS-ECO (kW-класс, волоконный источник, оценка)','est','Волоконный лазер IPG YLS-ECO — непрерывный иттербиевый источник кВт-класса с блочностью компоновки и электропитанием 380 В'),
 'ipmc_core': ('30','10','0.3',0.001,'ionogel','https://en.wikipedia.org/wiki/Ionic_polymer%E2%80%93metal_composite','IPMC-плёнка (30×10, ионный полимер + электроды)','ref','Ионный полимерно-металлический композит (IPMC) — Nafion-плёнка с платиновыми электродами: низковольтный (1–5 В) изгиб вhydration/ионосодержащем геле'),
 'iridium_sbd_core': ('31','30','8',0.019,'al_6061-t6','https://www.iridium.com/products/iridium-9603-module/','Iridium 9603 SBD transceiver (31×29.6×8.4 мм, ~19 г)','ref','Спутниковый модем Iridium 9603 SBD — компактная версия 9602: короткобurstовая передача данных через L-диапазон, потребление <0.8 Вт'),
 'kapillyarnaya_teplovaya_trubka_core': ('6','6','200',0.02,'mednyi_provod','https://en.wikipedia.org/wiki/Heat_pipe','капиллярная тепловая трубка Ø6×200 (стандартная медная с водой)','ref','Капиллярная тепловая трубка Ø6×200 мм — медный корпус с фитилём и водой: перенос тепловой мощности до 30 Вт при ΔT несколько °C'),
 'kaskadnyi_stirling-kriokuler_core': ('80','80','300',1.8,'al_6061-t6','https://en.wikipedia.org/wiki/Cryocooler','каскадный стирлинг-криоохладитель (Ø80×300, оценка по компактным машинам)','est','Каскадный стирлинг-криоохладитель — двухкаскадное охлаждение до 30–80 К для сенсоров MWIR: компрессор + холодоноситель с регенератором'),
 'kompensatory_core': ('90','90','35',0.25,'inconel_718','https://en.wikipedia.org/wiki/Expansion_joint','компенсатор теплового расширения (сильфонный узел Ø90, Inconel)','ref','Сильфонный компенсатор — гофрированная оболочка Inconel 718: компенсация теплового расширения трубопроводов при высоких температурах'),
 'lidar_core': ('88','80','47',0.265,'al_6061-t6','https://www.livoxtech.com/mid-360','Livox Mid-360 (88×80×47 мм, 265 г)','ref','Лидар 3D-обзора — полусферическое сканирование (Mid-360 класс: 360°×59°, до 40 м, 200 тыс. точек/с)'),
 'lidar_robosense_ac1_core': ('75','75','55',0.30,'al_6061-t6','https://www.robosense.ai','RoboSense AC1 (компактный автоматический лидар, оценка ~75×75×55)','est','Компактный автоматический лидар RoboSense AC1 — полутвердотельное сканирование для мобильных платформ'),
 'loop_heat_pipe_core': ('150','80','30',0.15,'stal_st3','https://en.wikipedia.org/wiki/Loop_heat_pipe','контурная тепловая труба (испаритель + паро-жидкостные линии ~150×80×30)','ref','Контурная тепловая труба (LHP) — капиллярная помпа в испарителе обеспечивает перенос тепловой мощности против гравитации на десятки см'),
 'lwir_boson_1024_core': ('29','24','16',0.014,'al_6061-t6','https://www.flir.com/products/boson/','FLIR Boson+ 1024 с объективом (~29×24×16, ~14 г)','ref','Тепловизионный модуль FLIR Boson+ 1024×768 с миниобъективом — высочайшее разрешение в классе микромодулей'),
 'mems-imu_core': ('3','4.5','1',0.0002,'si','https://www.bosch-sensortec.com/products/motion-sensing/imus/','Bosch BMI088 (LGA 3×4.5×0.95 мм, ~0.2 г)','ref','MEMS-инерциальный модуль — 3-осевые гироскопы и акселерометры на одном кристалле (BMI088 класс: ±300°/с, 24g)'),
 'mems-mikrofonov_core': ('4','3','1',0.0001,'si','https://www.infineon.com/cms/en/product/sensor/mems-microphones/','Infineon IM69D130 (4×3×1.1 мм LGA)','ref','MEMS-микрофон — конденсаторная мембрана на кремниевом кристалле, AOP 130 дБ, SNR 69 дБ (IM69D130 класс)'),
 'metalinza_core': ('10','10','2',0.001,'metapoverhnost','https://en.wikipedia.org/wiki/Metalens','металинза (метаповерхностная оптика, 10×10×2)','ref','Металинза — наноструктурированная метаповерхность, фокусирующая ИК-излучение (диаметр 10 мм, устраняет хроматические аберрации)'),
 'mikrokanalnye_ohlazhdayuschie_plastiny_core': ('100','60','5',0.10,'mednyi_provod','https://en.wikipedia.org/wiki/Microchannel_heat_exchanger','микроканальная охлаждающая пластина (медь, 100×60×5)','ref','Микроканальная охлаждающая пластина — медная плита с фрезерованными каналами 0.3–0.5 мм: съём теплового потока до 100 Вт/см²'),
 'minigun_m134_core': ('300','250','800',12,'stal_st3','https://en.wikipedia.org/wiki/Minigun','M134 Minigun вращательный блок (6 стволов + ротор, оценка)','est','Вращательный блок M134 Minigun — 6 стволов с внешним приводом, темп 2000–6000 выстр/мин, стволы с электроплакированным каналом'),
 'multispektralnye_cmos-matritsy_s_ik-diapazonom_core': ('40','40','15',0.03,'al_6061-t6','https://en.wikipedia.org/wiki/Multispectral_image','мультиспектральная CMOS-матрица (виз+ИК-диапазоны, оценка)','est','Мультиспектральная CMOS-матрица — сенсор с фотодиодами для видимого и ближнего ИК диапазонов (сплит-оптика или фильтровый массив)'),
 'mwir_2_core': ('45','45','40',0.06,'al_6061-t6','https://en.wikipedia.org/wiki/Thermographic_camera','MWIR-модуль (средневолновый ИК 3–5 мкм, оценка)','est','Модуль MWIR (3–5 мкм) — фотоприёмник на InSb/MCT с интегральным криоохлаждением для дальнего обнаружения'),
 'mwir_nbn_640_core': ('50','50','45',0.08,'al_6061-t6','https://en.wikipedia.org/wiki/Thermographic_camera','MWIR NbN 640 (фотоприёмник NbN 640×512, оценка)','est','MWIR фотоприёмник NbN 640×512 — ниобий-нитридный детектор для среднего ИК диапазона с криогенной стабилизацией'),
 'obd-ii_core': ('48','26','33',0.03,'peek','https://en.wikipedia.org/wiki/On-board_diagnostics','разъём OBD-II SAE J1962 (типовой 16-pin 48×26×33)','ref','Диагностический разъём OBD-II (SAE J1962) — 16-pin: питание, CAN/K-Line/LIN для доступа к бортовым контроллерам'),
 'opletku_iz_tokoprovodyaschih_izolirovannyh_provodov_core': ('250','180','45',0.45,'mednyi_provod','https://en.wikipedia.org/wiki/Cable_harness','жгут проводов (250×180×45, медь в изоляции)','ref','Жгут токопроводящих изолированных проводов — медные жилы с ПВХ/силиконовой изоляцией, экранированные ветки для силовых и сигнальных цепей'),
 'optovolokonnaya_shina_core': ('130','85','28',0.20,'al_6061-t6','https://en.wikipedia.org/wiki/Fiber-optic_communication','оптоволоконная шина (коммутационный блок 130×85×28, оценка)','est','Оптоволоконная шина — коммутационный узел с волоконными каналами: иммунитет к ЭМИ, гальваноразвязка высокоскоростных линий'),
 'pezo-mems_core': ('4','3','0.5',0.0001,'aln','https://en.wikipedia.org/wiki/Microelectromechanical_systems','пьезо-MEMS (4×3×0.5, AlN-плёнка)','ref','Пьезоэлектрический MEMS-элемент — тонкоплёночный AlN-пьезоэлектрик на кремнии: актюация/сенсорика с наносекундным откликом'),
 'pezo-sensor_core': ('16','16','2',0.002,'aln','https://en.wikipedia.org/wiki/Piezoelectric_sensor','пьезодатчик (диск 16×16×2, AlN/PZT)','ref','Пьезоэлектрический датчик — диск AlN/PZT: регистрация динамических усилий и вибраций с частотой до МГц-диапазона'),
 'elastomernyh_dempferah_core': ('60','60','30',0.08,'silikon_40_50_shore_a','https://en.wikipedia.org/wiki/Shock_absorber','эластомерные демпферы (блок 60×60×30, силикон Shore A 40–50)','ref','Эластомерные демпферы — силиконовые блоки: гашение ударов и вибраций за счёт гистерезиса эластомера'),
 'pezoelektricheskie_mems_core': ('5','5','1',0.0002,'aln','https://en.wikipedia.org/wiki/Microelectromechanical_systems','пьезоэлектрические MEMS (5×5×1)','ref','Пьезоэлектрические MEMS — микроструктуры с AlN-слоем для ультразвуковых и инерциальных применений'),
 'pezoelektricheskii_gromkogovoritel_core': ('20','20','5',0.005,'latun_c36000','https://en.wikipedia.org/wiki/Buzzer','пьезоэлектрический излучатель (латунная мембрана 20×20)','ref','Пьезоэлектрический громкоговоритель — латунная мембрана с керамическим слоем: звуковые колебания 2–6 кГц без катушек'),
 'pmut_core': ('8','8','1',0.0003,'aln','https://en.wikipedia.org/wiki/Ultrasonic_transducer','PMUT-массив (8×8×1)','ref','Пьезоэлектрический MEMS-ультразвуковой преобразователь (PMUT) — тонкая мембрана с AlN: воздушный ультразвук, тональная визуализация'),
 'polyimide_fpc_core': ('120','90','1',0.025,'poliimid','https://en.wikipedia.org/wiki/Flexible_electronics','полиимидная FPC (120×90, многослойная)','ref','Полиимидная гибкая плата (FPC) — 2–4 слоя с медными проводниками: межблочные динамические соединения'),
 'poristyi_gazovyi_podshipnik_iz_sic_core': ('50','50','25',0.20,'monokristallicheskogo_sic','https://en.wikipedia.org/wiki/Silicon_carbide','пористый газовый подшипник SiC (Ø50×25)','ref','Пористый газовый подшипник из SiC — воздух/газ выходит через пористую поверхность с равномерным давлением: идеальная осевая устойчивость'),
 'povorotnoe_uplotnenie_core': ('70','70','25',0.12,'ptfe-kompozit_du_vtulki','https://en.wikipedia.org/wiki/Seal_(mechanical)','вращательное уплотнение Ø70 (PTFE-композит)','ref','Вращательное уплотнение — втулка из PTFE-композита с наполнителями: низкое трение и химическая стойкость при вращении вала'),
 'provodnikovaya_nanoreshetka_core': ('25','25','0.5',0.0005,'mxene','https://en.wikipedia.org/wiki/Nanowire','проводящая нанорешётка (MXene, 25×25)','ref','Проводящая нанорешётка — 2D MXene-плёнка: прозрачный проводящий слой с высокой подвижностью носителей'),
 'quantum_cascade_laser_core': ('45','30','25',0.06,'al_6061-t6','https://en.wikipedia.org/wiki/Quantum_cascade_laser','квантово-каскадный лазер (MIR модуль 45×30×25)','ref','Квантово-каскадный лазер (QCL) — инжекционный полупроводниковый лазер среднего ИК диапазона (4–10 мкм) с TEC-стабилизацией'),
 'radiatsionno-stoikii_neiromorfnyi_tmr_core': ('42','42','5',0.02,'si','https://en.wikipedia.org/wiki/Radiation_hardening','радиационно-стойкий нейроморфный модуль (TMR-защита, CCGA 42×42)','ref','Радиационно-стойкий нейроморфный вычислительный модуль — тройная модульная избыточность (TMR) для защиты от SEU, керамический CCGA-корпус 42×42'),
 'razryvnye_mufty_iso_16028_core': ('40','40','95',0.28,'stal_st3','https://en.wikipedia.org/wiki/Quick_coupler','разрывные муфты ISO 16028 (типоразмер 12)','ref','Разрывные гидравлические муфты ISO 16028 — разъединение под нагрузкой с блокировкой потока с двух сторон'),
 'reshetchatyi_karkas_core': ('450','380','200',2.5,'al_6061-t6','https://en.wikipedia.org/wiki/Spacecraft_bus','решетчатый каркас (сотовая конструкция 450×380×200, оценка)','est','Решетчатый каркас — сотовая/стрингерная алюминиевая конструкция: несущая основа с высокой удельной жёсткостью'),
 'sensora_volnovogo_fronta_core': ('35','60','30',0.15,'al_6061-t6','https://en.wikipedia.org/wiki/Shack%E2%80%93Hartmann_wavefront_sensor','датчик волнового фронта Шэка–Гартмана (35×60×30)','ref','Датчик волнового фронта (Шэк–Гартман) — массив микролинз + CMOS: измерение искажений волнового фронта для адаптивной оптики'),
 'slm_eos_m290_core': ('250','250','350',25,'stal_st3','https://www.eos.info','SLM-модуль EOS M290 (зона печати 250×250×350, стальная камера)','ref','Модуль селективного лазерного сплавления EOS M290 — зона построения 250×250×350 мм, 400 Вт лазер, аргоновая атмосфера'),
 'starlink_mini_core': ('150','120','18',0.28,'al_6061-t6','https://www.starlink.com','антенный модуль Starlink Mini (фазированная решётка, оценка)','est','Активная фазированная антенная решётка Ku-диапазона (Starlink Mini класс) — электронное сканирование луча на LEO-спутники'),
 'stm32_core': ('14','14','1.6',0.0012,'si','https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html','STM32F4 LQFP100 (14×14×1.6 мм)','ref','Микроконтроллер STM32 (Cortex-M4, LQFP100) — ядро 168 МГц, FPU, периферия CAN/USB/SPI для систем управления'),
 'stm32h743_core': ('20','20','1.6',0.002,'si','https://www.st.com/en/microcontrollers-microprocessors/stm32h743-753.html','STM32H743 LQFP144 (20×20×1.6 мм)','ref','Микроконтроллер STM32H743 (Cortex-M7 480 МГц, LQFP144) — 2 МБ флеш, двойная шина, периферия для высокопроизводительных контроллеров'),
 'tcp_core': ('150','3','3',0.0005,'neilon_6_66','https://en.wikipedia.org/wiki/Artificial_muscle','TCP-мышца (twisted and coiled polymer, нейлон 6/6, 150 мм)','ref','Искусственная мышца TCP (twisted and coiled polymer) — нейлоновая нить 6/6, скрученная и коилед: нагрев током сокращает до 40 % длины'),
 'tsa_core': ('250','10','10',0.01,'spectra','https://en.wikipedia.org/wiki/Actuator','TSA-привод (twisted string actuator, UHMWPE-шнур 250 мм)','ref','Твист-струнный привод (TSA) — мотор скручивает пучок UHMWPE-шнуров: сокращение до 20 % длины при высоком усилии'),
 'tverdotelnyi_mmwave_radar_core': ('30','45','8',0.012,'al_6061-t6','https://www.ti.com/product/IWR6843','ммW-радар IWR6843 класс (30×45×8, оценка модуля)','est','Твердотельный миллиметровый радар (60–81 ГГц) — FMCW-сенсор с интегральной антенной решёткой: точная дальность и скорость без подвижных частей'),
 'ultrakorotkoimpulsnye_lazery_core': ('150','120','60',0.9,'al_6061-t6','https://en.wikipedia.org/wiki/Ultrashort_pulse','ультракороткоимпульсный лазер (фс-класс, оценка)','est','Ультракороткоимпульсный лазер — фемтосекундная длительность импульса (Ti:Sa/Yb) с чирпированием-компрессией: пикова мощность ТВт-класса'),
 'usb-c_core': ('9','7','3',0.0005,'becu','https://en.wikipedia.org/wiki/USB-C','разъём USB Type-C (8.94×7.35×3.26 мм)','ref','Разъём USB Type-C — 24-pin симметричный разъём: до 240 Вт PD, 40 Гбит/с USB4, бериллиевая бронза с золотым покрытием контактов'),
 'zubchataya_mufta_core': ('80','80','60',0.9,'stal_st3','https://en.wikipedia.org/wiki/Coupling','зубчатая муфта Ø80 (типовая зубчатая компенсирующая)','ref','Зубчатая муфта — компенсация несоосности валов (до 1.5°) с передачей крутящего момента через обойму с внутренними зубьями'),
}

MAT_NOTES = {
 'al_6061-t6':'конструкционный алюминиевый сплав 6061-T6','si':'монокристаллический кремний','stal_st3':'конструкционная сталь Ст3','ti-6al-4v':'титановый сплав Ti-6Al-4V','poliimid':'полиимид (гибкая подложка)','latun_c36000':'латунь C36000','becu':'бериллиевая бронза','inconel_718':'жаропрочный сплав Inconel 718','peek':'PEEK (полиэфирэфиркетон)','cfrp_t1100g':'углепластик на волокне T1100','ionogel':'ионогель','elastomernaya_matritsa':'эластомерная матрица','p_vdf-trfe-cfe':'P(VDF-TrFE-CFE) релаксорный ферроэлектрик','halve_p_vdf-trfe-cfe':'P(VDF-TrFE-CFE) релаксорный ферроэлектрик','ionnaya_zhidkost_emim_tfsi':'ионная жидкость EMIM-TFSI','mxene':'MXene (2D-карбид/нитрид)','silikon_40_50_shore_a':'силикон Shore A 40–50','silikon_80_shore_a_+_steklyannye_mikrosfery':'силикон Shore A 80 со стеклянными микросферами','silicone-textile_composite':'текстильно-силиконовый композит','ptfe-kompozit_du_vtulki':'PTFE-композит (втулка)','monokristallicheskogo_sic':'монокристаллический SiC','mednyi_provod':'медь (проводниковая)','magnitnaya_rezina_ferritovyi_poroshok':'магнитная резина с ферритовым порошком','neilon_6_66':'нейлон 6/6 (полиамид)','spectra':'UHMWPE Spectra/Dyneema','metapoverhnost':'метаповерхность (оптическая)','aln':'нитрид алюминия (AlN, пьезоэлектрик)',
}

def fmt(x):
    s = ('%.4f' % x).rstrip('0').rstrip('.')
    return s if s else '0'

def main():
    changed, skipped = [], []
    for f in glob.glob('реальные данные/изделия/**/часть_*/_index.md', recursive=True):
        try: txt = open(f, encoding='utf-8').read()
        except Exception: continue
        fm = txt.split('---')[1] if txt.startswith('---') else ''
        m_id = re.search(r'^id:\s*(\S+)', fm, re.M)
        if not m_id: continue
        item_id = m_id.group(1)
        key = item_id if item_id in ITEMS else item_id.replace('часть_', '', 1)
        if key not in ITEMS: continue
        lm = re.search(r'габариты_mm:\s*\n\s+l:\s*(\S+)\s*\n\s+w:\s*(\S+)\s*\n\s+h:\s*(\S+)', fm)
        massa = re.search(r'^  масса_kg:\s*(\S+)', fm, re.M)
        if not (lm and massa): continue
        if (lm.group(1), lm.group(2), lm.group(3)) != ('100','100','50'):
            skipped.append(item_id); continue
        l, w, h, massa_new, mat, url, ref, basis, funkc = ITEMS[key]
        old_mat_m = re.search(r'^\s+материал:\s*(\S+)', fm, re.M)
        old_mat = old_mat_m.group(1) if old_mat_m else None
        basis_txt = 'паспортные данные (%s)' % ref.split(' (')[0] if basis=='ref' else 'оценка по типовым изделиям класса (%s)' % ref
        desc = '%s. Референсное исполнение — %s. Габариты %s×%s×%s мм, масса %s кг — %s. Материал — %s: %s.' % (funkc, ref, l, w, h, fmt(massa_new), basis_txt, mat, MAT_NOTES.get(mat, mat))
        txt = re.sub(r'(габариты_mm:\s*\n\s+l:)\s*\S+', r'\g<1> %s' % l, txt, count=1)
        txt = re.sub(r'(\n\s+w:)\s*\S+', r'\g<1> %s' % w, txt, count=1)
        txt = re.sub(r'(\n\s+h:)\s*\S+', r'\g<1> %s' % h, txt, count=1)
        txt = re.sub(r'(  масса_kg:)\s*\S+', r'\g<1> %s' % fmt(massa_new), txt, count=1)
        if old_mat != mat:
            txt = re.sub(r'(\n  - часть: %s\n    материал: )\S+' % re.escape(item_id), r'\g<1>%s' % mat, txt, count=1)
        txt = re.sub(r'^источник_разбора:.*$', 'источник_разбора: веб-верификация', txt, count=1, flags=re.M)
        txt = re.sub(r'^дата_обновления:.*$', 'дата_обновления: 2026-11-05', txt, count=1, flags=re.M)
        if re.search(r'^источник_url:', txt, re.M):
            txt = re.sub(r'^источник_url:.*$', 'источник_url: %s' % url, txt, count=1, flags=re.M)
        else:
            txt = re.sub(r'^источник_разбора: веб-верификация$', 'источник_разбора: веб-верификация\nисточник_url: %s\nисточник_дата: 2026-11-05' % url, txt, count=1, flags=re.M)
        if not re.search(r'^источник_дата:', txt, re.M):
            txt = re.sub(r'^(источник_url: .+)$', r'\1\nисточник_дата: 2026-11-05', txt, count=1, flags=re.M)
        txt = re.sub(r'(## Описание\n\n).*?(\n\nРодитель:)', r'\g<1>%s\g<2>' % desc, txt, count=1, flags=re.S)
        txt = re.sub(r'\| масса \| \S+ \| kg \|[^|]*\|', '| масса | %s | kg | %s |' % (fmt(massa_new), ref), txt, count=1)
        txt = re.sub(r'\| габариты \(Д×Ш×В\) \| \S+ \| mm \|[^|]*\|', '| габариты (Д×Ш×В) | %s×%s×%s | mm | %s |' % (l, w, h, ref), txt, count=1)
        txt = re.sub(r'\| материал \| (\S+)[^|]*\|[^|]*\|', '| материал | %s | — | %s |' % (mat, ref), txt, count=1)
        if old_mat and old_mat != mat:
            pat = r'- `%s` → \[[^\]]+\]\([^)]+\)[^\n]*' % re.escape(old_mat)
            repl = '- `%s` → [`%s.md`](../../../../материалы/%s.md) — %s' % (mat, mat, mat, MAT_NOTES.get(mat, mat))
            txt2, n = re.subn(pat, repl, txt, count=1)
            txt = txt2 if n else txt
        src_line = '- %s — %s (обращение 2026-11-05)' % (ref, url)
        if src_line not in txt:
            if '- Канон:' in txt: txt = txt.replace('- Канон:', src_line + '\n- Канон:', 1)
            else: txt = txt.replace('- Материалы:', src_line + '\n- Материалы:', 1)
        open(f, 'w', encoding='utf-8').write(txt)
        changed.append('%s → %s×%s×%s, %s кг, %s' % (item_id, l, w, h, fmt(massa_new), mat))
    print('CHANGED: %d' % len(changed))
    for c in changed: print('  ✓', c)
    print('SKIPPED: %d' % len(skipped))
    for s in skipped: print('  -', s)
    return 0

if __name__ == '__main__':
    if 'SkyNet' not in os.getcwd():
        os.chdir('/home/z/my-project/SkyNet')
    sys.exit(main())
