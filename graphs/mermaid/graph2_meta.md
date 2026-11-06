# Граф 2 — мета-граф репозитория

```mermaid
graph TB
    script___init___py(("__init__.py"))
    script__helpers_py(("_helpers.py"))
    script__migrate_256_fix_links_py(("_migrate_256_fix_links.py"))
    script__migrate_256_variant_a_py(("_migrate_256_variant_a.py"))
    script__migrate_256_variant_d_py(("_migrate_256_variant_d.py"))
    script__migrate_256_variant_d_fix_links_py(("_migrate_256_variant_d_fix_links.py"))
    script__stubs_py(("_stubs.py"))
    script_capture_dialog_py(("capture_dialog.py"))
    script_check_model_completeness_py(("check_model_completeness.py"))
    script_classify_subsystem_py(("classify_subsystem.py"))
    script_decompose_all_izdeliya_py(("decompose_all_izdeliya.py"))
    script_fix_yaml_corruption_py(("fix_yaml_corruption.py"))
    script_generate_decomposition_py(("generate_decomposition.py"))
    script_generate_graphs_py(("generate_graphs.py"))
    script_generate_wrapper_izdeliya_py(("generate_wrapper_izdeliya.py"))
    script_migrate_aliases_py(("migrate_aliases.py"))
    script_migrate_dedup_materials_py(("migrate_dedup_materials.py"))
    script_migrate_material_form_py(("migrate_material_form.py"))
    script_pipeline_py(("pipeline.py"))
    script_pre-commit-hook_py(("pre-commit-hook.py"))
    script_real_decomposition_py(("real_decomposition.py"))
    script_validate_decomposition_py(("validate_decomposition.py"))
    script_validate_field_contracts_py(("validate_field_contracts.py"))
    script_web_verify_py(("web_verify.py"))
    spec_SkyNet_PROMPT_v9_31_md{{"SkyNet_PROMPT_v9.31.md"}}
    section_§0_1_Что_проверять_(через_GitHub_REST_API_с_PAT)(/"§0.1 Что проверять (через GitHub REST AP"/)
    section_§0_2_Решение_по_результатам_проверки(/"§0.2 Решение по результатам проверки"/)
    section_§0_3_Связь_с_§19(/"§0.3 Связь с §19"/)
    section_§1__ИДЕНТИЧНОСТЬ_И_ИНСТРУМЕНТАРИЙ(/"§1. ИДЕНТИЧНОСТЬ И ИНСТРУМЕНТАРИЙ"/)
    section_§2__САМОДИАГНОСТИКА_(перед_каждой_фазой)(/"§2. САМОДИАГНОСТИКА (перед каждой фазой)"/)
    section_§3__ПРОГНОЗ-ВЕРИФИКАЦИЯ_(перед_каждым_действием)(/"§3. ПРОГНОЗ-ВЕРИФИКАЦИЯ (перед каждым де"/)
    section_§3_1_WebSearch_ДО_создания_файла_(v9_24_НОВОЕ_—_из_аудита_ди(/"§3.1 WebSearch ДО создания файла (v9.24 "/)
    section_§4__АДАПТИВНЫЕ_СТРАТЕГИИ_(plan_A_→_B_→_C)(/"§4. АДАПТИВНЫЕ СТРАТЕГИИ (plan A → B → C"/)
    section_§5__ПРОЗРАЧНОСТЬ_РЕШЕНИЙ_(audit_log)(/"§5. ПРОЗРАЧНОСТЬ РЕШЕНИЙ (audit log)"/)
    section_§6__TELEMETRY_(real-time_метрики)(/"§6. TELEMETRY (real-time метрики)"/)
    section_§7__ЗАЩИТА_ОТ_ПОТЕРИ_КОНТЕКСТА_(checkpoints)(/"§7. ЗАЩИТА ОТ ПОТЕРИ КОНТЕКСТА (checkpoi"/)
    section_§8__КРИТЕРИИ_ВЫХОДА_ИЗ_ЦИКЛОВ(/"§8. КРИТЕРИИ ВЫХОДА ИЗ ЦИКЛОВ"/)
    section_§9__АВТОМАТИЗАЦИЯ_(9_фаз_0-8,_без_пропусков,_с_циклами_до_кр(/"§9. АВТОМАТИЗАЦИЯ (9 фаз 0-8, без пропус"/)
    section_§9_0_ПРОТОКОЛ_ЗАПУСКА_AI-45_(ОБЯЗАТЕЛЬНО)(/"§9.0 ПРОТОКОЛ ЗАПУСКА AI-45 (ОБЯЗАТЕЛЬНО"/)
    section_§9_1_ПАКЕТНАЯ_ОБРАБОТКА_И_УПРАВЛЕНИЕ_КОНТЕКСТОМ(/"§9.1 ПАКЕТНАЯ ОБРАБОТКА И УПРАВЛЕНИЕ КОН"/)
    section_§9_2_РАЗБОР_ТИПА_ЗАПРОСА(/"§9.2 РАЗБОР ТИПА ЗАПРОСА"/)
    section_§9_3_УСЛОВНЫЕ_ЦИКЛЫ_ДЛЯ_CANON(/"§9.3 УСЛОВНЫЕ ЦИКЛЫ ДЛЯ CANON"/)
    section_§9_4_ФОРМАТ_ОТЧЁТА_ПРОВЕРКИ(/"§9.4 ФОРМАТ ОТЧЁТА ПРОВЕРКИ"/)
    section_§10__АРХИТЕКТУРА_`SkyNet`(/"§10. АРХИТЕКТУРА `SkyNet`"/)
    section_§10_1_Правила_консистентности_путь_↔_тип_↔_статус_реальности(/"§10.1 Правила консистентности путь ↔ тип"/)
    section_§10_2_Дерево_папок(/"§10.2 Дерево папок"/)
    section_§10_2_1_Instance_example_—_конкретные_примеры_файлов_(v9_8)(/"§10.2.1 Instance example — конкретные пр"/)
    section_§10_3_Канон__паттерн_vs_конкретное_имя_в_дереве_(P064,_v9_8)(/"§10.3 Канон: паттерн vs конкретное имя в"/)
    section_§10_4_Расширенная_структура_фантастические_данные__(v9_25_НО(/"§10.4 Расширенная структура фантастическ"/)
    section_§11__ИЕРАРХИЯ_ИЗДЕЛИЙ(/"§11. ИЕРАРХИЯ ИЗДЕЛИЙ"/)
    section_§11_0_ТИПЫ_МОДЕЛЕЙ_SKYNET_(v9_22_НОВОЕ_—_7_типов)(/"§11.0 ТИПЫ МОДЕЛЕЙ SKYNET (v9.22 НОВОЕ —"/)
    section_§11_1_13_подсистем_+_1_fallback_(классификация)(/"§11.1 13 подсистем + 1 fallback (классиф"/)
    section_§11_2_Иерархия_изделий_(подсистема_=_классификация,_НЕ_урове(/"§11.2 Иерархия изделий (подсистема = кла"/)
    section_§11_3_7_антипаттернов_(уроки_из_прошлых_реализаций)(/"§11.3 7 антипаттернов (уроки из прошлых "/)
    section_§11_4_Полный_реестр_подтипов_(146_подтипов)(/"§11.4 Полный реестр подтипов (146 подтип"/)
    section_§11_5__Разделение_уровней__паттерн_vs_экземпляр(/"§11.5. Разделение уровней: паттерн vs эк"/)
    section_§11_6_МНОГОСЛОЙНАЯ_БРОНЯ_(v9_22_НОВОЕ_—_5_слоёв)(/"§11.6 МНОГОСЛОЙНАЯ БРОНЯ (v9.22 НОВОЕ — "/)
    section_§9_5_Авто-отчёт_после_batch_(v9_24_НОВОЕ_—_из_аудита_диалога(/"§9.5 Авто-отчёт после batch (v9.24 НОВОЕ"/)
    section_§9_6_Запрет_эвристик_без_явного_правила_(v9_24_НОВОЕ_—_из_ау(/"§9.6 Запрет эвристик без явного правила "/)
    section_§9_7_Прозрачная_остановка_(v9_24_НОВОЕ_—_из_аудита_диалога)(/"§9.7 Прозрачная остановка (v9.24 НОВОЕ —"/)
    section_§9_8_Issues_как_очередь_задач_(v9_30_НОВОЕ_—_полная_интеграц(/"§9.8 Issues как очередь задач (v9.30 НОВ"/)
    section_§9_9_Авто-создание_Issues_при_FAIL_(v9_30_НОВОЕ)(/"§9.9 Авто-создание Issues при FAIL (v9.3"/)
    section_§12__YAML-СХЕМЫ_ФАЙЛОВ(/"§12. YAML-СХЕМЫ ФАЙЛОВ"/)
    section_§12_1_Схема_файла_изделия_(`_index_md`_или_`<часть>_md`)(/"§12.1 Схема файла изделия (`_index.md` и"/)
    section_§12_2_Схема_файла_технологии(/"§12.2 Схема файла технологии"/)
    section_§12_3_Схема_файла_материала(/"§12.3 Схема файла материала"/)
    section_§12_3a_Правила_для_фантастических_материалов_(v9_25_НОВОЕ)(/"§12.3a Правила для фантастических матери"/)
    section_§12_4_Схема_файла_модели_Skynet(/"§12.4 Схема файла модели Skynet"/)
    section_§12_5_Схема_файла_реализации_модели(/"§12.5 Схема файла реализации модели"/)
    section_§13__МЕТРИКИ_(ПОЛНЫЙ_РЕЕСТР_—_118_уникальных,_v9_10)(/"§13. МЕТРИКИ (ПОЛНЫЙ РЕЕСТР — 118 уникал"/)
    section_§13_1_Базовые_проверки_v2_1_(10_штук)(/"§13.1 Базовые проверки v2.1 (10 штук)"/)
    section_§13_2_Метрики_аудита_v3_0_(23_штуки)(/"§13.2 Метрики аудита v3.0 (23 штуки)"/)
    section_§13_3_Дополнительные_метрики_v2_0_v2_1_(18_штук)(/"§13.3 Дополнительные метрики v2.0/v2.1 ("/)
    section_§13_4_Метрики_v4_0_(5_штук)(/"§13.4 Метрики v4.0 (5 штук)"/)
    section_§13_5_Метрики_v7_2-v9_0_(48_метрик)_+_канон_canon-exempt_(DR(/"§13.5 Метрики v7.2-v9.0 (48 метрик) + ка"/)
    section_§13_13_Метрики_v9_22_F71-F75_(типизация_моделей_+_многослойн(/"§13.13 Метрики v9.22 F71-F75 (типизация "/)
    section_§13_14_Метрики_v9_23_F79-F80_(тип-специфичный_subset_подсист(/"§13.14 Метрики v9.23 F79-F80 (тип-специф"/)
    section_§13_15_Метрики_v9_24_F81-F87_(аудиты_реализации,_диалога,_ca(/"§13.15 Метрики v9.24 F81-F87 (аудиты реа"/)
    section_§13_16_Метрика_v9_25_F88_(фантастические_материалы_без_смеше(/"§13.16 Метрика v9.25 F88 (фантастические"/)
    section_§13_17_Метрика_v9_26_F70g_(schema-driven_validation)(/"§13.17 Метрика v9.26 F70g (schema-driven"/)
    section_§13_18_Метрика_v9_27_F70h_(enum_validation)(/"§13.18 Метрика v9.27 F70h (enum validati"/)
    section_§13_19_Метрика_v9_28_F70i_(enforcement)(/"§13.19 Метрика v9.28 F70i (enforcement)"/)
    section_§13_20_Метрики_v9_29_F70j_+_F90_(decisions_log_+_маскировка_(/"§13.20 Метрики v9.29 F70j + F90 (decisio"/)
    section_§13_21_Метрика_v9_30_F89_(Issues_integration)(/"§13.21 Метрика v9.30 F89 (Issues integra"/)
    section_§13_6_Резюме_реестра_(v9_16__сжато)(/"§13.6 Резюме реестра (v9.16: сжато)"/)
    section_§13_7_Метрики_v9_1_(5_новых_—_F51-F55)(/"§13.7 Метрики v9.1 (5 новых — F51-F55)"/)
    section_§13_8_Метрики_v9_3_F56-F61_(перенесено_из_§30_в_v9_9)(/"§13.8 Метрики v9.3 F56-F61 (перенесено и"/)
    section_§13_8a_Метрика_F61_—_TRL_доступность_(перенесено_из_§32_6_в_(/"§13.8a Метрика F61 — TRL доступность (пе"/)
    section_§13_9_Метрика_F62_—_кристаллическая_структура_по_применению_(/"§13.9 Метрика F62 — кристаллическая стру"/)
    section_§13_10_Метрика_F63_—_паттерн_vs_instance_в_дереве_(перенесен(/"§13.10 Метрика F63 — паттерн vs instance"/)
    section_§13_11_Метрики_v9_10_F64-F69_(вдохновлено_v5_0)(/"§13.11 Метрики v9.10 F64-F69 (вдохновлен"/)
    section_§13_12_Метрика_v9_13_F70_—_schema_catalog_consistency_(НОВАЯ(/"§13.12 Метрика v9.13 F70 — schema_catalo"/)
    section_§14__ОПЕРАЦИОННЫЕ_ПАТТЕРНЫ(/"§14. ОПЕРАЦИОННЫЕ ПАТТЕРНЫ"/)
    section_§14_0_Сводная_таблица_13_паттернов_(с_принципами_и_метриками(/"§14.0 Сводная таблица 13 паттернов (с пр"/)
    section_§14_1_PATTERN_1__matrix_of_operational_modes(/"§14.1 PATTERN 1: matrix_of_operational_m"/)
    section_§14_2_PATTERN_2__criticality_to_redundancy(/"§14.2 PATTERN 2: criticality_to_redundan"/)
    section_§14_3_PATTERN_3__degradation_hierarchy(/"§14.3 PATTERN 3: degradation_hierarchy"/)
    section_§14_4_PATTERN_4__distributed_architecture_failover(/"§14.4 PATTERN 4: distributed_architectur"/)
    section_§14_5_PATTERN_5__secure_boot_chain_(RUNTIME-поведение,_не_ар(/"§14.5 PATTERN 5: secure_boot_chain (RUNT"/)
    section_§14_6_PATTERN_6__behavioral_models(/"§14.6 PATTERN 6: behavioral_models"/)
    section_§14_7_PATTERN_7__interaction_vectors(/"§14.7 PATTERN 7: interaction_vectors"/)
    section_§14_8_PATTERN_8__self_repair_system_4_components(/"§14.8 PATTERN 8: self_repair_system_4_co"/)
    section_§14_9_PATTERN_9__signature_management_(МЕТА-ПРИНЦИП_бюджета,(/"§14.9 PATTERN 9: signature_management (М"/)
    section_§14_10_PATTERN_10__power_gating(/"§14.10 PATTERN 10: power_gating"/)
    section_§14_11_PATTERN_11__combined_actions_chains(/"§14.11 PATTERN 11: combined_actions_chai"/)
    section_§14_12_PATTERN_12__defense_in_depth_(МЕТА-ПРИНЦИП_эшелонов,_(/"§14.12 PATTERN 12: defense_in_depth (МЕТ"/)
    section_§14_13_PATTERN_13__target_identification_5tuple(/"§14.13 PATTERN 13: target_identification"/)
    section_§15__ПРИНЦИПЫ_(YAML-формат,_с_полем_version)_—_71_принцип,_v(/"§15. ПРИНЦИПЫ (YAML-формат, с полем vers"/)
    section_§15a__КОНВЕНЦИИ_(имена_файлов,_коммиты,_ссылки)(/"§15a. КОНВЕНЦИИ (имена файлов, коммиты, "/)
    section_§15a_1_Имена_файлов_и_папок(/"§15a.1 Имена файлов и папок"/)
    section_§15a_2_Коммит-сообщения_(Localized_Conventional_Commits_—_Ru(/"§15a.2 Коммит-сообщения (Localized Conve"/)
    section_§15a_3_Внутренние_ссылки(/"§15a.3 Внутренние ссылки"/)
    section_§16__ОБРАБОТКА_ОШИБОК_(с_адаптивными_стратегиями,_v9_15__кон(/"§16. ОБРАБОТКА ОШИБОК (с адаптивными стр"/)
    section_§17__ПОЭТАПНЫЙ_ПЛАН_РАБОТЫ(/"§17. ПОЭТАПНЫЙ ПЛАН РАБОТЫ"/)
    section_§18__ФИНАЛЬНЫЕ_ТРЕБОВАНИЯ(/"§18. ФИНАЛЬНЫЕ ТРЕБОВАНИЯ"/)
    section_§18_2_Требования_v9_22_(154-157)_—_типизация_+_многослойная_(/"§18.2 Требования v9.22 (154-157) — типиз"/)
    section_§18_3_Требование_v9_23_(158)_—_тип-специфичная_полнота_подси(/"§18.3 Требование v9.23 (158) — тип-специ"/)
    section_§18_4_Требования_v9_24_(159-161)_—_аудиты_v9_17(/"§18.4 Требования v9.24 (159-161) — аудит"/)
    section_§18_5_Требование_v9_25_(162)_—_разделение_фантастических_мат(/"§18.5 Требование v9.25 (162) — разделени"/)
    section_§18_6_Требование_v9_26_(163)_—_schema-driven_validation(/"§18.6 Требование v9.26 (163) — schema-dr"/)
    section_§18_7_Требование_v9_27_(164)_—_enum_validation(/"§18.7 Требование v9.27 (164) — enum vali"/)
    section_§18_8_Требование_v9_28_(165)_—_enforcement(/"§18.8 Требование v9.28 (165) — enforceme"/)
    section_§18_9_Требования_v9_29_(166-167)_—__decisions_log_+_гибридна(/"§18.9 Требования v9.29 (166-167) — _deci"/)
    section_§18_10_Требование_v9_30_(168)_—_Issues_как_основа_процесса(/"§18.10 Требование v9.30 (168) — Issues к"/)
    section_§18_1_Требования_v9_1-v9_13_(111-153)_—_см__§15_для_полных_т(/"§18.1 Требования v9.1-v9.13 (111-153) — "/)
    section_§19__ТЕКУЩЕЕ_СОСТОЯНИЕ_ГОТОВНОСТИ(/"§19. ТЕКУЩЕЕ СОСТОЯНИЕ ГОТОВНОСТИ"/)
    section_§20__FIELD_CONTRACTS_—_ЯВНЫЙ_КОНТРАКТ_ПОЛЕЙ(/"§20. FIELD_CONTRACTS — ЯВНЫЙ КОНТРАКТ ПО"/)
    section_§20_1_Принцип(/"§20.1 Принцип"/)
    section_§20_2_Bidirectional_integrity_((см__§20_2))(/"§20.2 Bidirectional integrity ((см. §20."/)
    section_§20_3_Tier_классификация(/"§20.3 Tier классификация"/)
    section_§20_4_KNOWLEDGE_BASE_—_MAT_KB___TEC_KB(/"§20.4 KNOWLEDGE BASE — MAT_KB / TEC_KB"/)
    section_§21__CROSS-LAYER_CONSISTENCY(/"§21. CROSS-LAYER CONSISTENCY"/)
    section_§21_1_Принцип(/"§21.1 Принцип"/)
    section_§21_2_Примеры_конфликтов_(детектируемые_F56)(/"§21.2 Примеры конфликтов (детектируемые "/)
    section_§21_3_Метрика_F56(/"§21.3 Метрика F56"/)
    section_§22__PROVENANCE_&_ANTI-SIMULATION(/"§22. PROVENANCE & ANTI-SIMULATION"/)
    section_§22_1_Принцип(/"§22.1 Принцип"/)
    section_§22_2_Допустимые_значения_`*_source`(/"§22.2 Допустимые значения `*_source`"/)
    section_§22_3_Метрика_F57(/"§22.3 Метрика F57"/)
    section_§22_4_Пример(/"§22.4 Пример"/)
    section_§23__COMPUTE-BEFORE-WEB(/"§23. COMPUTE-BEFORE-WEB"/)
    section_§23_1_Принцип(/"§23.1 Принцип"/)
    section_§23_2_Стратегия_вычисления_по_типу_поля(/"§23.2 Стратегия вычисления по типу поля"/)
    section_§23_3_Порядок_заполнения(/"§23.3 Порядок заполнения"/)
    section_§23_4_Метрика_F58(/"§23.4 Метрика F58"/)
    section_§23_5_Изменение_§9_Фаза_3_5(/"§23.5 Изменение §9 Фаза 3.5"/)
    section_§23_6_МЕТРИКИ_УЛУЧШЕНИЯ(/"§23.6 МЕТРИКИ УЛУЧШЕНИЯ"/)
    section_§24__REGISTRY_COMPLETION_100%(/"§24. REGISTRY COMPLETION 100%"/)
    section_§24_1_Принцип(/"§24.1 Принцип"/)
    section_§24_2_Запрещённые_placeholder'ы(/"§24.2 Запрещённые placeholder'ы"/)
    section_§24_3_Стратегия_заполнения(/"§24.3 Стратегия заполнения"/)
    section_§24_4_Метрика_F59(/"§24.4 Метрика F59"/)
    section_§25__ARCHIVE_CONTRACT_+_IMMUTABLE_COVERAGE(/"§25. ARCHIVE CONTRACT + IMMUTABLE COVERA"/)
    section_§25_1_Archive_contract_(строгий_JSON-контракт_вывода)(/"§25.1 Archive contract (строгий JSON-кон"/)
    section_§25_2_Immutable_coverage_script(/"§25.2 Immutable coverage script"/)
    section_§25_3_Метрика_F60(/"§25.3 Метрика F60"/)
    section_§26__THRESHOLD_PROGRESSION(/"§26. THRESHOLD PROGRESSION"/)
    section_§26_1_Адаптивные_пороги(/"§26.1 Адаптивные пороги"/)
    section_§26_2_Regression_detection_((см__§26_2_regression))(/"§26.2 Regression detection ((см. §26.2 r"/)
    section_§27__17_TABLE_TYPES_+_PARSE_TARGET_ROUTING(/"§27. 17 TABLE TYPES + PARSE_TARGET_ROUTI"/)
    section_§27_1_Типы_таблиц(/"§27.1 Типы таблиц"/)
    section_§27_2_Parse_target_routing(/"§27.2 Parse target routing"/)
    section_§28__DEPRECATION_POLICY_+_CONSOLIDATION_MAP(/"§28. DEPRECATION POLICY + CONSOLIDATION "/)
    section_§28_1_Deprecation_policy(/"§28.1 Deprecation policy"/)
    section_§28_2_Consolidation_map(/"§28.2 Consolidation map"/)
    section_§32__ШКАЛА_ДОСТУПНОСТИ_TRL_(v9_9__P061_+_F61_перенесены_в_§1(/"§32. ШКАЛА ДОСТУПНОСТИ TRL (v9.9: P061 +"/)
    section_§32_1_7_уровней_доступности(/"§32.1 7 уровней доступности"/)
    section_§32_2_Поле_YAML(/"§32.2 Поле YAML"/)
    section_§32_3_Применение_к_материалам(/"§32.3 Применение к материалам"/)
    section_§32_4_Применение_к_технологиям(/"§32.4 Применение к технологиям"/)
    section_§32_5_Применение_к_изделиям(/"§32.5 Применение к изделиям"/)
    catalog_scripts__CATALOG_md[["scripts/_CATALOG.md"]]
    readme_README_md(("README.md"('[', ']')
    concept_гипотезы_CHANGELOG_md(("CHANGELOG.md"('[', ']')
    concept_гипотезы_INDEX_md(("INDEX.md"('[', ']')
    concept_улучшения_CHANGELOG_md(("CHANGELOG.md"('[', ']')
    concept_улучшения_INDEX_md(("INDEX.md"('[', ']')
    concept_требования_к_ии__examples_md(("_examples.md"('[', ']')
    concept_требования_к_ии__алгоритм_обработки_сообщения_md(("_алгоритм_обработки_сообщения.md"('[', ']')
    concept_требования_к_ии__классификация_подсистем_md(("_классификация_подсистем.md"('[', ']')
    concept_требования_к_ии__критерии_оптимизации_md(("_критерии_оптимизации.md"('[', ']')
    concept_требования_к_ии__паттерны_md(("_паттерны.md"('[', ']')
    concept_требования_к_ии__правила_извлечения_md(("_правила_извлечения.md"('[', ']')
    concept_требования_к_ии__принципы_md(("_принципы.md"('[', ']')
    concept_требования_к_ии__реестр_произведений_md(("_реестр_произведений.md"('[', ']')
    concept_требования_к_ии__требования_к_ии_варианту_md(("_требования_к_ии_варианту.md"('[', ']')
    concept_требования_к_ии__требования_к_промышленному_варианту_md(("_требования_к_промышленному_варианту.md"('[', ']')
    concept_требования_к_ии__шаблоны_изделий_md(("_шаблоны_изделий.md"('[', ']')
    concept_требования_к_ии__шаблоны_подсистем_md(("_шаблоны_подсистем.md"('[', ']')
    concept_диалог_CHANGELOG_md(("CHANGELOG.md"('[', ']')
    script_decompose_all_izdeliya_py -.->|imports| script_validate_decomposition_py
    script_decompose_all_izdeliya_py -.->|imports| script__helpers_py
    script_fix_yaml_corruption_py -.->|imports| script_migrate_aliases_py
    script_generate_decomposition_py -.->|imports| script_validate_decomposition_py
    script_generate_decomposition_py -.->|imports| script__helpers_py
    script_generate_wrapper_izdeliya_py -.->|imports| script_validate_decomposition_py
    script_generate_wrapper_izdeliya_py -.->|imports| script__helpers_py
    script_generate_wrapper_izdeliya_py -.->|imports| script_generate_decomposition_py
    script_migrate_dedup_materials_py -.->|imports| script_validate_decomposition_py
    script_pipeline_py -.->|imports| script__helpers_py
    script_pre-commit-hook_py -.->|imports| script_validate_decomposition_py
    script_pre-commit-hook_py -.->|imports| script__helpers_py
    script_real_decomposition_py -.->|imports| script_validate_decomposition_py
    script_real_decomposition_py -.->|imports| script__helpers_py
    script_validate_field_contracts_py -.->|imports| script__helpers_py
    script_web_verify_py -.->|imports| script_validate_decomposition_py
    script_web_verify_py -.->|imports| script__helpers_py
    section_§0_1_Что_проверять_(через_GitHub_REST_API_с_PAT) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§0_2_Решение_по_результатам_проверки -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§0_3_Связь_с_§19 -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§1__ИДЕНТИЧНОСТЬ_И_ИНСТРУМЕНТАРИЙ -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§2__САМОДИАГНОСТИКА_(перед_каждой_фазой) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§3__ПРОГНОЗ-ВЕРИФИКАЦИЯ_(перед_каждым_действием) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§3_1_WebSearch_ДО_создания_файла_(v9_24_НОВОЕ_—_из_аудита_ди -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§4__АДАПТИВНЫЕ_СТРАТЕГИИ_(plan_A_→_B_→_C) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§5__ПРОЗРАЧНОСТЬ_РЕШЕНИЙ_(audit_log) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§6__TELEMETRY_(real-time_метрики) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§7__ЗАЩИТА_ОТ_ПОТЕРИ_КОНТЕКСТА_(checkpoints) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§8__КРИТЕРИИ_ВЫХОДА_ИЗ_ЦИКЛОВ -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9__АВТОМАТИЗАЦИЯ_(9_фаз_0-8,_без_пропусков,_с_циклами_до_кр -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_0_ПРОТОКОЛ_ЗАПУСКА_AI-45_(ОБЯЗАТЕЛЬНО) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_1_ПАКЕТНАЯ_ОБРАБОТКА_И_УПРАВЛЕНИЕ_КОНТЕКСТОМ -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_2_РАЗБОР_ТИПА_ЗАПРОСА -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_3_УСЛОВНЫЕ_ЦИКЛЫ_ДЛЯ_CANON -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_4_ФОРМАТ_ОТЧЁТА_ПРОВЕРКИ -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10__АРХИТЕКТУРА_`SkyNet` -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10_1_Правила_консистентности_путь_↔_тип_↔_статус_реальности -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10_2_Дерево_папок -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10_2_1_Instance_example_—_конкретные_примеры_файлов_(v9_8) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10_3_Канон__паттерн_vs_конкретное_имя_в_дереве_(P064,_v9_8) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§10_4_Расширенная_структура_фантастические_данные__(v9_25_НО -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11__ИЕРАРХИЯ_ИЗДЕЛИЙ -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_0_ТИПЫ_МОДЕЛЕЙ_SKYNET_(v9_22_НОВОЕ_—_7_типов) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_1_13_подсистем_+_1_fallback_(классификация) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_2_Иерархия_изделий_(подсистема_=_классификация,_НЕ_урове -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_3_7_антипаттернов_(уроки_из_прошлых_реализаций) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_4_Полный_реестр_подтипов_(146_подтипов) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_5__Разделение_уровней__паттерн_vs_экземпляр -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§11_6_МНОГОСЛОЙНАЯ_БРОНЯ_(v9_22_НОВОЕ_—_5_слоёв) -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
    section_§9_5_Авто-отчёт_после_batch_(v9_24_НОВОЕ_—_из_аудита_диалога -.->|part_of| spec_SkyNet_PROMPT_v9_31_md
```

_Узлов: 190, рёбер: 218 (показано топ-50)._

| Тип узла | Количество |
|---|---:|
| spec_section | 146 |
| script | 24 |
| concept_doc | 17 |
| catalog | 1 |
| readme | 1 |
| spec | 1 |
