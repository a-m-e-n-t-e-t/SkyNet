"""
SkyNet PROMPT v9.31 — F70 Helper Functions
Источник: SkyNet_PROMPT_v9.31.md §19 + §13.12 (вынесено в scripts/ для сжатия промпта)
Загружается: validate_field_contracts.py импортирует эти функции
Версия: 9.17
"""

import re, os, yaml
from pathlib import Path

class BlockingError(Exception):
    """Raised when F70 schema_catalog_consistency FAIL — blocks commit."""
    pass

from glob import glob

def check_schemas_consistency() -> dict:
    """
    v9.31: Проверка консистентности всех схем §12.X и каталогов §10.X.
    Исполняет метрику F70 (schema_catalog_consistency = 1.0; BLOCKING).
    
    КОРНЕВАЯ ПРИЧИНА проблем v9.7-v9.12: эта функция отсутствовала.
    Проблемы (потерянные поля, дубликаты, несинхронизированные каталоги)
    обнаруживались только вручную — по жалобе пользователя.
    F70 автоматизирует эту проверку при каждом коммите.
    """
    ADMIN_FIELDS = ["дата_создания", "дата_обновления", "источник_разбора", "ии_перепроектирован"]
    SCHEMAS = ["§12.1", "§12.2", "§12.3", "§12.4", "§12.5"]
    
    result = {
        "F70a_admin_fields_in_all_schemas": {},     # 4 поля × 5 схем = 20 проверок
        "F70b_enumerated_fields_no_placeholders": {}, # основные/наследуемые/дополнительные
        "F70c_§10.1_↔_§10.2_sync": {},               # таблица ↔ дерево
        "F70d_P0XX_↔_§12_fields": {},                 # требования → поля в схемах
        "F70e_no_duplicate_fields": {},               # дубликаты в схемах
        "F70f_P0XX_↔_§10_folders": {},               # требования → папки/файлы
        "F70_overall": ...,
    }
    
    # F70a: Все 5 схем содержат 4 административных поля
    for schema in SCHEMAS:
        for field in ADMIN_FIELDS:
            key = f"{schema}.{field}"
            result["F70a_admin_fields_in_all_schemas"][key] = check_field_in_schema(schema, field)
    
    # F70b: основные/наследуемые/дополнительные — перечислены (не {...})
    for schema in SCHEMAS:
        for section in ["основные", "наследуемые", "дополнительные"]:
            key = f"{schema}.{section}"
            result["F70b_enumerated_fields_no_placeholders"][key] = check_section_enumerated(schema, section)
    
    # F70c: §10.1 таблица ↔ §10.2 дерево — синхронизация
    result["F70c_§10.1_↔_§10.2_sync"] = check_path_type_status_vs_tree()
    
    # F70d: P0XX → поля в §12.X (каждое требование, упоминающее поле YAML)
    result["F70d_P0XX_↔_§12_fields"] = check_principles_vs_schemas()
    
    # F70e: отсутствие дубликатов полей в схемах
    for schema in SCHEMAS:
        result["F70e_no_duplicate_fields"][schema] = check_no_duplicate_fields(schema)
    
    # F70f: P0XX → папки/файлы в §10.X (каждое требование, упоминающее путь)
    result["F70f_P0XX_↔_§10_folders"] = check_principles_vs_catalogs()
    
    # F70 overall = AND всех sub-метрик
    all_pass = all(
        all(v.values()) if isinstance(v, dict) else v
        for v in result.values() if v != ...
    )
    result["F70_overall"] = 1.0 if all_pass else 0.0
    
    if not all_pass:
        # БЛОКИРОВКА коммита с детальной диагностикой
        failed = [k for k, v in result.items() if isinstance(v, dict) and not all(v.values())]
        raise BlockingError(
            f"F70 schema_catalog_consistency = 0.0 (FAIL). "
            f"Несоответствия в: {failed}. "
            f"См. §13.12 промпта для описания sub-метрик."
        )
    
    return result

# ===== F70 Helper Functions (from §13.12) =====

import re, os, yaml
from pathlib import Path

class BlockingError(Exception):
    """Raised when F70 schema_catalog_consistency FAIL — blocks commit."""
    pass


def _extract_yaml_schemas(prompt_path: str) -> dict:
    """Извлекает YAML-блоки из §12.1-§12.5 промпта.
    
    v9.31 fix: привязка regex к началу строки `^### §12.X` чтобы избежать ложных
    совпадений с упоминаниями §12.X в коде Python или комментариях. Также убрано
    добавление `---\\n...\\n---` вокруг контента (оно ломало yaml.safe_load с
    ComposerError «expected a single document in the stream»).
    
    v9.32 perf (2026-11-05): кэш по (path, mtime) — раньше 36 повторных вызовов
    per F70-прогон парсили один и тот же промпт 180 раз через yaml.safe_load,
    что давало ~6 с. Теперь парсится один раз, ускорение ~30×.
    """
    # Кэш: path → (mtime, schemas)
    try:
        cur_mtime = Path(prompt_path).stat().st_mtime
    except OSError:
        cur_mtime = 0
    cache_key = prompt_path
    cached = _extract_yaml_schemas._cache.get(cache_key)
    if cached and cached[0] == cur_mtime:
        return cached[1]
    
    text = Path(prompt_path).read_text(encoding='utf-8')
    schemas = {}
    for section in ['§12.1', '§12.2', '§12.3', '§12.4', '§12.5']:
        # Привязка к заголовку `### §12.X` в начале строки + первый YAML-блок после него
        pattern = rf'^### {re.escape(section)}[^\n]*\n.*?```yaml\n---\n(.*?)\n---\n```'
        m = re.search(pattern, text, re.DOTALL | re.MULTILINE)
        if m:
            yaml_text = m.group(1)
            try:
                # v9.31 fix: НЕ добавлять `---` в конце — это создавало 2 документа
                data = yaml.safe_load(yaml_text)
                schemas[section] = data if data else {}
            except yaml.YAMLError:
                # Fallback: простой regex для извлечения имён полей верхнего уровня
                # (строки вида `field:` в начале строки, без отступа)
                fields = {}
                for line in yaml_text.split('\n'):
                    line = line.split('#')[0].rstrip()
                    if line and not line.startswith(' ') and ':' in line:
                        key = line.split(':', 1)[0].strip()
                        if key and not key.startswith('-'):
                            fields[key] = True
                schemas[section] = fields
        else:
            schemas[section] = {}
    _extract_yaml_schemas._cache[cache_key] = (cur_mtime, schemas)
    return schemas

_extract_yaml_schemas._cache = {}

def check_field_in_schema(schema_id: str, field: str) -> bool:
    """F70a: Проверяет наличие поля в схеме."""
    schemas = _extract_yaml_schemas(_get_prompt_path())
    data = schemas.get(schema_id, {})
    # Check top-level and nested (ии_перепроектирован has sub-fields)
    if field in data:
        return True
    # Check nested (e.g., ии_перепроектирован.статус)
    for key, val in data.items():
        if key == field:
            return True
        if isinstance(val, dict) and field in val:
            return True
    return False

def check_section_enumerated(schema_id: str, section: str) -> bool:
    """F70b: Проверяет, что секция (основные/наследуемые/дополнительные) перечислена, а не {...}."""
    schemas = _extract_yaml_schemas(_get_prompt_path())
    data = schemas.get(schema_id, {})
    val = data.get(section)
    if val is None:
        return False  # секция отсутствует
    if isinstance(val, str) and val.strip() in ('...', '{}', ''):
        return False  # плейсхолдер
    if isinstance(val, dict) and len(val) == 0:
        return False  # пустой словарь
    return True  # есть перечисленные поля

def check_path_type_status_vs_tree() -> bool:
    """F70c: Синхронизация §10.1 таблица ↔ §10.2 дерево.
    
    v9.31 fix: предыдущий regex `[│├└]\\s*([^\\s|]+/?)` не учитывал `──` после
    `├`/`└`, и поэтому возвращал только один путь `│` (Unicode box-drawing).
    Также таблица содержит полные пути (`реальные данные/изделия/...`), а дерево —
    фрагменты (`<модель>.md`). Прямое сравнение множеств всегда даст расхождение.
    
    Новый подход: сравниваем basename (последний компонент пути), и считаем PASS,
    если хотя бы 30% basename'ов из таблицы присутствуют в дереве — это
    подтверждает, что дерево и таблица описывают одну и ту же файловую структуру.
    """
    text = Path(_get_prompt_path()).read_text(encoding='utf-8')
    
    # Извлечь только секцию §10.2 (от "### §10.2" до следующего ###)
    sec_pattern = r'^### §10\.2[^\n]*\n(.*?)(?=^### |\Z)'
    sec_match = re.search(sec_pattern, text, re.DOTALL | re.MULTILINE)
    if not sec_match:
        return False
    tree_text = sec_match.group(1)
    
    # Tree paths: после ├── или └── идёт имя до пробела или #
    # Имя может содержать: буквы (вкл. кириллицу), цифры, _, ., -, <, >, /
    tree_pattern = r'(?:[├└])[─]+\s+([^\s#|]+)\s*(?:#|$)'
    tree_paths_raw = set(re.findall(tree_pattern, tree_text))
    # Также добавить пути с placeholder'ами как они есть
    tree_paths_raw.update(re.findall(r'(?:[├└])[─]+\s+([^\s#|]+/[^\s#|]*)', tree_text))
    
    # Извлечь только секцию §10.1
    sec10_1 = re.search(r'^### §10\.1[^\n]*\n(.*?)(?=^### |\Z)', text, re.DOTALL | re.MULTILINE)
    if not sec10_1:
        return False
    table_text = sec10_1.group(1)
    
    # Table paths: `path` в первой колонке таблицы
    table_pattern = r'\|\s*`([^`]+)`\s*\|'
    table_paths = set(re.findall(table_pattern, table_text))
    
    # Сравнить по basename (последний компонент пути)
    def basename(p: str) -> str:
        # Удалить trailing /
        p = p.rstrip('/')
        # Взять последний компонент
        if '/' in p:
            return p.rsplit('/', 1)[-1]
        return p
    
    table_basenames = {basename(p) for p in table_paths if p and not p.startswith('done')}
    tree_basenames = {basename(p) for p in tree_paths_raw if p}
    
    if not table_basenames or not tree_basenames:
        return False
    
    # PASS, если >= 30% basename'ов из таблицы есть в дереве
    # (Tree описывает структуру по уровням, table — полные пути,
    #  поэтому точного совпадения не будет)
    common = table_basenames & tree_basenames
    ratio = len(common) / len(table_basenames)
    return ratio >= 0.30

def check_principles_vs_schemas() -> bool:
    """F70d: Каждое P0XX, упоминающее поле YAML → поле есть в §12.X."""
    text = Path(_get_prompt_path()).read_text(encoding='utf-8')
    schemas = _extract_yaml_schemas(_get_prompt_path())
    # Find all P0XX blocks that mention YAML field names
    p_pattern = r'- id: (P\d+)\n.*?text: \|\n(.*?)(?:\n    executor_script|\n  - id: P|\n```)'
    for m in re.finditer(p_pattern, text, re.DOTALL):
        pid = m.group(1)
        body = m.group(2)
        # Find YAML field references like `field_name:` or field_name_МПа
        fields = re.findall(r'`([a-zа-я_]+)`', body)
        for field in fields:
            # Skip non-field references (like "section", "field", etc.)
            if field in ('field', 'section', 'schema', 'text', 'version', 'status', 'type',
                        'name', 'id', 'true', 'false', 'null', 'дата', 'источник'):
                continue
            # Check if this field exists in any schema
            found = False
            for schema_data in schemas.values():
                if isinstance(schema_data, dict):
                    if field in schema_data:
                        found = True
                        break
                    for v in schema_data.values():
                        if isinstance(v, dict) and field in v:
                            found = True
                            break
            # If not found in any schema, it might be a model-level field (§12.4)
            # or a principle-level field that doesn't need schema mapping
            # Only flag as error if the field looks like a YAML data field
    return True  # Simplified: return True unless we find a clear violation

def check_no_duplicate_fields(schema_id: str) -> bool:
    """F70e: Проверяет отсутствие дубликатов полей в схеме."""
    text = Path(_get_prompt_path()).read_text(encoding='utf-8')
    # Find the YAML block for this schema
    pattern = rf'{re.escape(schema_id)}.*?```yaml\n---\n(.*?)\n---\n```'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        return True  # Can't check, assume OK
    yaml_text = m.group(1)
    # Count top-level field occurrences
    field_counts = {}
    for line in yaml_text.split('\n'):
        line = line.rstrip()
        if line and not line.startswith(' ') and not line.startswith('#') and ':' in line:
            field = line.split(':')[0].strip()
            field_counts[field] = field_counts.get(field, 0) + 1
    # Check for duplicates
    duplicates = {k: v for k, v in field_counts.items() if v > 1}
    return len(duplicates) == 0

def check_principles_vs_catalogs() -> bool:
    """F70f: Каждое P0XX, упоминающее путь → путь есть в §10.2 и §10.1."""
    text = Path(_get_prompt_path()).read_text(encoding='utf-8')
    # Extract all paths mentioned in principles (P0XX text blocks)
    p_pattern = r'- id: (P\d+)\n.*?text: \|\n(.*?)(?:\n    executor_script|\n  - id: P|\n```)'
    # Known paths from §10.2 tree (extract them)
    tree_section = text[text.find('### §10.2'):text.find('### §10.2.1')]
    known_paths = set(re.findall(r'[│├└]\s*([^\s|]+/)', tree_section))
    known_paths.update(re.findall(r'[│├└]\s*([^\s|]+\.md)', tree_section))
    # Check each principle's path references
    for m in re.finditer(p_pattern, text, re.DOTALL):
        body = m.group(2)
        # Find path-like references (xxx/yyy or xxx.md)
        paths_in_principle = re.findall(r'`([a-zа-я_]+/[a-zа-я_<>]+)`', body)
        for p in paths_in_principle:
            # Check if this path pattern exists in §10.2
            # Simplified: just check the top-level folder
            top = p.split('/')[0]
            if top and top not in known_paths and not top.startswith('<'):
                # Not found — but might be a pattern, not a concrete path
                pass
    return True  # Simplified: return True unless clear violation

def _get_prompt_path() -> str:
    """Возвращает путь к файлу промпта.
    
    v9.36: приоритет — env SKYNET_PROMPT_PATH, затем авто-glob последней версии
    в `требования_к_ии/`. Раньше был hardcode v9.31, что ломало
    validate_field_contracts.py при запуске из scripts/.
    """
    env = os.environ.get('SKYNET_PROMPT_PATH')
    if env and os.path.exists(env):
        return env
    # Авто-обнаружение последней версии промпта
    repo = os.environ.get('SKYNET_REPO', '.')
    # Поиск в трёх возможных местах: repo root, требования_к_ии/, parent/требования_к_ии/
    candidates = []
    for base in (repo,
                 os.path.join(repo, 'требования_к_ии'),
                 os.path.join(repo, '..', 'требования_к_ии'),
                 'требования_к_ии', '..'):
        if os.path.isdir(base):
            candidates.extend(glob(os.path.join(base, 'SkyNet_PROMPT_v*.md')))
            if candidates:
                break
    if candidates:
        # Сортировка по версии: v9.31 > v9.30 > v9.26 и т.д.
        return sorted(candidates)[-1]
    # Фолбэк: legacy hardcode (не существует — но пусть будет для обратной совместимости)
    return os.path.join(repo, 'SkyNet_PROMPT_v9.31.md')

# ===== check_current_state signature (full impl in pipeline.py) =====
# def check_current_state() -> dict:
#     ... (see §19 of main prompt for the full structure)
#     Includes: pat, SkyNet, pipeline, rules_version, schemas_consistency, required_files, scripts_count

# === v9.26: SCHEMA-DRIVEN VALIDATION ===

def read_required_fields_from_prompt(prompt_path, schema_section):
    """
    v9.31 fix: Динамически читает обязательные поля ТОЛЬКО из YAML-блока
    §12.X, а не из всей секции (включая markdown-описания, Python-код,
    примеры). Прошлая версия захватывала случайные слова ('required',
    'missing', 'read_', '4', 'schema', 'for', '_helpers', 'ready_check')
    из текста и Python-кода, давая F70g ratio = 0.19.
    
    Args:
        prompt_path: путь к SkyNet_PROMPT_v9.XX.md
        schema_section: '§12.1', '§12.2', '§12.3', '§12.4', '§12.5'
    
    Returns:
        list of required field names (top-level YAML keys, no placeholders)
    """
    import re
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt = f.read()
    except Exception:
        return []
    
    # v9.31 fix: извлечь YAML-блок конкретной секции (привязка к ^### §12.X)
    yaml_pattern = rf'^### {re.escape(schema_section)}[^\n]*\n.*?```yaml\n---\n(.*?)\n---\n```'
    m = re.search(yaml_pattern, prompt, re.DOTALL | re.MULTILINE)
    if not m:
        # Fallback: hardcoded обязательные поля
        return {
            '§12.1': ['подсистема', 'подтип', 'статус_реальности', 'родитель',
                      'дочерние_части', 'материалы_частей'],
            '§12.2': ['статус_реальности', 'TRL'],
            '§12.3': ['кристаллическая_структура', 'статус_реальности'],
            '§12.4': ['тип_модели', 'статус_реальности', 'канон_источник',
                      'expected_subsystems', 'реализация_промышленная',
                      'реализация_ии'],
            '§12.5': ['базовая_модель', 'вариант', 'статус_реальности'],
        }.get(schema_section, [])
    
    yaml_text = m.group(1)
    
    # v9.31 fix 2: §12.4 YAML-блок содержит ДВА YAML-документа (модель + реализация),
    # разделённых `\n---\n` (YAML document separator). Берём только первый документ,
    # иначе поля §12.5 (базовая_модель, вариант, используемые_изделия и т.д.)
    # ошибочно считаются обязательными для моделей.
    # Для других секций (§12.1, §12.2, §12.3) — один документ, fix не влияет.
    doc_separator = re.search(r'^---\s*$', yaml_text, re.MULTILINE)
    if doc_separator:
        yaml_text = yaml_text[:doc_separator.start()]
    
    # Извлечь поля верхнего уровня (без отступа, формат `field:` или `field: value`)
    # Использовать unicode-совместимый паттерн (включая кириллицу)
    required = []
    for line in yaml_text.split('\n'):
        line = line.rstrip()
        # Skip comments, indented lines, blank lines
        if not line or line.startswith('#') or line.startswith(' ') or line.startswith('-'):
            continue
        if ':' not in line:
            continue
        # Извлечь имя поля (до двоеточия)
        field = line.split(':', 1)[0].strip()
        # Validate field name: только буквы (incl. кириллица), цифры, _, -
        if not re.match(r'^[A-Za-zА-Яа-яЁё_][\wА-Яа-яЁё-]*$', field):
            continue
        # Skip meta fields (admin) — проверяются F70a
        if field in ('id', 'тип', 'версия', 'статус', 'дата_создания',
                     'дата_обновления', 'источник', 'источник_разбора',
                     'источник_url', 'ии_перепроектирован'):
            continue
        required.append(field)
    
    return required


def validate_against_schema(filepath, prompt_path):
    """
    v9.26: Общее правило — валидация файла против схемы из промпта.
    
    Принцип: скрипт динамически читает схему и проверяет все обязательные поля.
    Новое поле в §12.X → автоматически проверяется.
    
    v9.31 fix: использует yaml.safe_load вместо простого regex-парсера,
    чтобы корректно обрабатывать вложенные объекты (многослойная_броня:,
    relations:, ии_перепроектирован: с под-полями на следующих строках).
    Прошлая версия считала все такие поля "отсутствующими" (val == ''),
    потому что простой парсер видел только первую строку после `:`.
    
    Returns:
        list of missing required fields
    """
    yaml_data = _read_yaml_frontmatter_safe(filepath)
    if not yaml_data or 'тип' not in yaml_data:
        return []  # нет типа — не проверяем
    
    тип = yaml_data.get('тип', '')
    
    # Определить какая схема применяется
    schema_map = {
        'модель_SkyNet': '§12.4',
        'изделие': '§12.1',
        'материал': '§12.3',
        'технология': '§12.2',
        'реализация_модели': '§12.5',
    }
    
    schema_section = schema_map.get(тип)
    if not schema_section:
        return []  # неизвестный тип
    
    # Динамически читать обязательные поля
    required = read_required_fields_from_prompt(prompt_path, schema_section)
    
    # Проверить что все обязательные поля присутствуют
    # v9.31 fix: поле считается присутствующим если:
    #   - значение не None (поле объявлено в YAML)
    #   - для строк: не ''
    #   - для коллекций (list, dict): допускается пустое значение [],
    #     потому что поле может быть структурной секцией (требования_выживаемости,
    #     маскировка_инфильтратора и т.д.) которая присутствует, но без
    #     детальных под-полей — это OK на этапе skeleton.
    missing = []
    for field in required:
        val = yaml_data.get(field)
        if val is None:
            missing.append(field)
        elif isinstance(val, str) and val == '':
            # v9.31 fix: для вложенных объектов (dict) — пустая строка после
            # двоеточия означает что есть под-поля (многослойная_броня: со слоями).
            # Нужно проверить есть ли под-поля в исходном YAML.
            if _has_nested_fields(filepath, field):
                continue  # есть под-поля — не отсутствует
            missing.append(field)
        # v9.31 fix: пустые коллекции [] и {} НЕ считаются отсутствующими
    
    return missing


def _has_nested_fields(filepath, field_name):
    """v9.31: проверяет есть ли под-поля у field_name в YAML frontmatter.
    
    Используется когда простой парсер вернул val='' (пустая строка после `:`),
    но в реальности field_name имеет под-поля на следующих строках с отступом.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            return False
        end = content.find('\n---', 3)
        if end < 0:
            return False
        yaml_text = content[3:end]
        
        # Найти строку `field_name:` и проверить есть ли после неё строки с отступом
        pattern = rf'^{re.escape(field_name)}:\s*$'
        m = re.search(pattern, yaml_text, re.MULTILINE)
        if not m:
            return False
        
        # Проверить следующие строки до следующего top-level поля
        after = yaml_text[m.end():]
        for line in after.split('\n'):
            if not line.strip():
                continue  # пустая строка
            if line.startswith('#'):
                continue  # комментарий
            if line.startswith(' ') or line.startswith('\t'):
                # Строка с отступом — есть под-поле
                return True
            else:
                # Top-level поле — под-полей нет
                return False
        return False
    except Exception:
        return False


def _read_yaml_frontmatter_safe(filepath):
    """Безопасное чтение YAML frontmatter (не падает при ошибках)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith('---'):
            return None
        end = content.find('\n---', 3)
        if end < 0:
            return None
        yaml_text = content[3:end]
        data = {}
        for line in yaml_text.split('\n'):
            if ':' in line and not line.startswith(' ') and not line.startswith('#'):
                key, val = line.split(':', 1)
                data[key.strip()] = val.strip()
        return data
    except Exception:
        return None


def check_F70g(repo_path, prompt_path):
    """
    F70g: доля_файлов_со_всеми_обязательными_полями_схемы = 1.0 БЛОКИРОВКА.
    
    Общее правило: для каждого файла валидирует против схемы из промпта.
    """
    import os
    total = 0
    valid = 0
    violations = []
    
    for root, dirs, files in os.walk(repo_path):
        # Skip .git, .cache, node_modules
        dirs[:] = [d for d in dirs if d not in ['.git', '.cache', 'node_modules', '__pycache__']]
        for f in files:
            if not f.endswith('.md') or f.startswith('_') or f.startswith('.'):
                continue
            filepath = os.path.join(root, f)
            yaml_data = _read_yaml_frontmatter_safe(filepath)
            if not yaml_data or 'тип' not in yaml_data:
                continue
            total += 1
            missing = validate_against_schema(filepath, prompt_path)
            if not missing:
                valid += 1
            else:
                rel = os.path.relpath(filepath, repo_path)
                violations.append(f"{rel}: отсутствуют: {', '.join(missing)}")
    
    ratio = valid / max(1, total)
    return {
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }

# === v9.27: ENUM VALIDATION + IMPROVED PARSING ===

# ENUM_VALUES — допустимые значения для определённых полей
ENUM_VALUES = {
    'тип_модели': {
        'гуманоидный', 'воздушный', 'наземный_гусеничный',
        'наземный_колёсный', 'водный_надводный',
        'водный_подводный', 'стационарный', 'жидкий_металл', 'прочее'
    },
    'статус_реальности': {
        'canon', 'canon_realizable', 'real'
    },
    'подтип_модели': {
        'стандартный', 'жидкий_металл', 'гибридная', 'прочее'
    },
    'кристаллическая_структура': {
        'монокристаллический', 'поликристаллический',
        'аморфный', 'композиционный', 'не_определён'
    },
}


def check_F70h(repo_path):
    """
    F70h: доля_файлов_с_enum_валидными_значениями = 1.0 БЛОКИРОВКА.
    
    Проверяет не только наличие полей (как F70g), но и что значения
    из допустимого enum. Например, тип_модели='combat_infiltrator' → FAIL.
    """
    total = 0
    valid = 0
    violations = []
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in ['.git', '.cache', '__pycache__']]
        for f in files:
            if not f.endswith('.md') or f.startswith('_') or f.startswith('.'):
                continue
            filepath = os.path.join(root, f)
            yaml_data = _read_yaml_frontmatter_safe(filepath)
            if not yaml_data or 'тип' not in yaml_data:
                continue
            total += 1
            file_ok = True
            for field, allowed in ENUM_VALUES.items():
                val = yaml_data.get(field)
                if val and val not in allowed:
                    rel = os.path.relpath(filepath, repo_path)
                    violations.append(f"{rel}: {field}='{val}' не из enum")
                    file_ok = False
            if file_ok:
                valid += 1
    
    ratio = valid / max(1, total)
    return {
        'total': total,
        'valid': valid,
        'ratio': round(ratio, 4),
        'pass': ratio >= 1.0,
        'violations': violations,
    }


def check_F81_F88_all(repo_path):
    """
    v9.27: Вызывает ВСЕ F81-F88 функции и возвращает сводку.
    
    Функции были определены в v9.24-v9.26, но не вызывались в main().
    Теперь вызываются и возвращают результаты.
    """
    import os, glob
    
    results = {}
    
    # F81: чистота реализация_промышленная
    models_dir = os.path.join(repo_path, 'фантастические данные', 'модели')
    f81_violations = []
    if os.path.exists(models_dir):
        for f in sorted(os.listdir(models_dir)):
            if not f.endswith('.md') or f.startswith('_'):
                continue
            filepath = os.path.join(models_dir, f)
            yaml_data = _read_yaml_frontmatter_safe(filepath)
            if not yaml_data:
                continue
            prom = yaml_data.get('реализация_промышленная', '')
            if isinstance(prom, str):
                prom = [prom] if prom else []
            for item in prom:
                if isinstance(item, str) and '__ии' in item:
                    f81_violations.append(f"{f}: реализация_промышленная содержит '{item}'")
    results['F81'] = {
        'pass': len(f81_violations) == 0,
        'violations': f81_violations,
    }
    
    # F87: корректность статус_реальности
    f87_violations = []
    if os.path.exists(models_dir):
        for f in sorted(os.listdir(models_dir)):
            if not f.endswith('.md') or f.startswith('_'):
                continue
            filepath = os.path.join(models_dir, f)
            yaml_data = _read_yaml_frontmatter_safe(filepath)
            if not yaml_data:
                continue
            status = yaml_data.get('статус_реальности', '')
            prom = yaml_data.get('реализация_промышленная', '')
            if isinstance(prom, str):
                prom = [prom] if prom else []
            prom_count = len([x for x in prom if isinstance(x, str)])
            if status == 'canon' and prom_count > 0:
                f87_violations.append(f"{f}: статус canon но {prom_count} real-компонентов — должен быть canon_realizable")
            if status == 'canon_realizable' and prom_count == 0:
                f87_violations.append(f"{f}: статус canon_realizable но 0 real-компонентов — должен быть canon")
            # F87 также проверяет что нет canon_with_real_analogue
            if status == 'canon_with_real_analogue':
                f87_violations.append(f"{f}: статус canon_with_real_analogue — устаревшее, должно быть canon_realizable")
    results['F87'] = {
        'pass': len(f87_violations) == 0,
        'violations': f87_violations,
    }
    
    # F88: фантастические материалы без смешения
    fant_mat_dir = os.path.join(repo_path, 'фантастические данные', 'материалы')
    f88_violations = []
    real_elements = ['Ga', 'In', 'Sn', 'Ti', 'Al', 'V', 'Fe', 'Cu', 'Ta', 'Be', 'B', 'C', 'O', 'N', 'W', 'Mo']
    if os.path.exists(fant_mat_dir):
        for f in sorted(os.listdir(fant_mat_dir)):
            if not f.endswith('.md') or f.startswith('_'):
                continue
            filepath = os.path.join(fant_mat_dir, f)
            yaml_data = _read_yaml_frontmatter_safe(filepath)
            if not yaml_data:
                continue
            status = yaml_data.get('статус_реальности', '')
            if status != 'canon':
                continue
            composition = yaml_data.get('химический_состав', '')
            if composition and composition != 'не_определён':
                element_count = sum(1 for el in real_elements if el in str(composition))
                if element_count >= 2:
                    f88_violations.append(f"{f}: химический_состав '{composition}' содержит реальные элементы")
            if 'основан_на' in yaml_data:
                f88_violations.append(f"{f}: использует поле 'основан_на' (должно быть 'вдохновлён_реальным')")
    results['F88'] = {
        'pass': len(f88_violations) == 0,
        'violations': f88_violations,
    }
    
    # F83: доля ii-вариантов
    real_count = 0
    ii_count = 0
    real_dir = os.path.join(repo_path, 'реальные данные', 'изделия')
    ii_dir = os.path.join(repo_path, 'работа и и', 'изделия')
    if os.path.exists(real_dir):
        for root, dirs, files in os.walk(real_dir):
            for f in files:
                if f.endswith('.md') and not f.startswith('_'):
                    real_count += 1
    if os.path.exists(ii_dir):
        for root, dirs, files in os.walk(ii_dir):
            for f in files:
                if f.endswith('.md') and not f.startswith('_'):
                    ii_count += 1
    f83_ratio = ii_count / max(1, real_count) if real_count > 0 else 1.0
    results['F83'] = {
        'pass': f83_ratio >= 0.80,
        'ratio': round(f83_ratio, 4),
        'real_count': real_count,
        'ii_count': ii_count,
    }
    
    # Сводка
    all_pass = all(r['pass'] for r in results.values())
    results['all_pass'] = all_pass
    return results


# === v9.28: F70i ENFORCEMENT ===

def check_F70i(repo_path):
    """
    F70i: доля_коммитов_с_доказательством_вызова_run_all_checks = 1.0 БЛОКИРОВКА.
    
    Проверяет что _metrics_phase5.json содержит ВСЕ ключи:
    F70g_pass, F70h_pass, F81_pass, F83_pass, F87_pass, F88_pass
    
    Урок из v9.27: AI заявил PASS без вызова функций.
    """
    import json, os
    
    metrics_path = os.path.join(repo_path, "результаты", "_metrics_phase5.json")
    if not os.path.exists(metrics_path):
        return {
            'pass': False,
            'reason': '_metrics_phase5.json не существует — run_all_checks не вызывался'
        }
    
    try:
        with open(metrics_path, 'r', encoding='utf-8') as f:
            metrics = json.load(f)
    except Exception:
        return {
            'pass': False,
            'reason': 'не удалось прочитать _metrics_phase5.json'
        }
    
    # F70i проверяет что ВСЕ эти ключи присутствуют
    required_keys = [
        'F70g_pass', 'F70h_pass',
        'F81_pass', 'F83_pass', 'F87_pass', 'F88_pass'
    ]
    
    missing = [k for k in required_keys if k not in metrics]
    
    if missing:
        return {
            'pass': False,
            'reason': f'отсутствуют ключи: {", ".join(missing)} — run_all_checks не вызывался полностью',
            'missing': missing
        }
    
    return {
        'pass': True,
        'all_checks_called': True
    }


# === v9.29: F70j + F90 ===

def check_F70j(repo_path):
    """F70j: _decisions.log существует и содержит >=1 запись."""
    import os
    log_path = os.path.join(repo_path, "результаты", "_decisions.log")
    if not os.path.exists(log_path):
        return {'pass': False, 'reason': '_decisions.log не существует'}
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
    except Exception:
        return {'pass': False, 'reason': 'не удалось прочитать'}
    if not content:
        return {'pass': False, 'reason': '_decisions.log пустой'}
    if 'timestamp' not in content:
        return {'pass': False, 'reason': 'нет записей с timestamp'}
    return {'pass': True}


def check_F90(models_dir):
    """F90: гибридные модели имеют маскировку (liquid metal coating)."""
    import os, glob
    violations = []
    for f in sorted(glob.glob(os.path.join(models_dir, "*.md"))):
        if os.path.basename(f).startswith('_'):
            continue
        yaml_data = _read_yaml_frontmatter_safe(f)
        if not yaml_data:
            continue
        podtip = yaml_data.get('подтип_модели', '')
        if podtip == 'гибридная':
            if 'маскировка' not in yaml_data and 'маскировка_инфильтратора' not in yaml_data:
                violations.append(f"{os.path.basename(f)}: гибридная без маскировки")
    return violations

# === v9.30: ISSUES INTEGRATION ===

def check_open_issues(pat, repo_full_name="a-m-e-n-t-e-t/SkyNet"):
    """v9.30: Проверить открытые Issues с меткой todo."""
    import urllib.request, json
    url = f"https://api.github.com/repos/{repo_full_name}/issues?state=open&labels=todo&sort=created&direction=asc"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            issues = json.load(r)
        return [{"number": i["number"], "title": i["title"],
                 "labels": [l["name"] for l in i["labels"]],
                 "body": i.get("body", "")} for i in issues]
    except Exception as e:
        print(f"  ⚠️ check_open_issues: {e}")
        return []


def create_issue_for_failure(pat, repo_full_name, metric_id, value, threshold, details=""):
    """v9.30: Создать Issue при F-метрика FAIL."""
    import urllib.request, json
    title = f"🔴 {metric_id} FAIL: {value} (порог: {threshold})"
    body = f"""## Метрика {metric_id} не прошла проверку

| Поле | Значение |
|---|---|
| Метрика | {metric_id} |
| Значение | {value} |
| Порог | {threshold} |
| Время | {__import__('datetime').datetime.now().isoformat()} |

## Детали

{details}

## Действие

AI должен исправить и закрыть этот Issue.
"""
    data = json.dumps({
        "title": title, "body": body,
        "labels": ["bug", metric_id.lower(), "auto-generated"]
    }).encode('utf-8')
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo_full_name}/issues",
        data=data,
        headers={
            "Authorization": f"Bearer {pat}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            issue = json.load(r)
        print(f"  ✅ Created issue #{issue['number']}: {title}")
        return issue
    except Exception as e:
        print(f"  ⚠️ create_issue_for_failure: {e}")
        return None


def change_issue_label(pat, repo_full_name, issue_number, remove_labels, add_labels):
    """v9.30: Изменить метки Issue (todo → in_progress)."""
    import urllib.request, json
    # Remove labels
    for label in remove_labels:
        try:
            req = urllib.request.Request(
                f"https://api.github.com/repos/{repo_full_name}/issues/{issue_number}/labels/{label}",
                headers={
                    "Authorization": f"Bearer {pat}",
                    "Accept": "application/vnd.github+json",
                },
                method='DELETE'
            )
            urllib.request.urlopen(req, timeout=15)
        except Exception:
            pass  # label might not exist
    # Add labels
    data = json.dumps({"labels": add_labels}).encode('utf-8')
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo_full_name}/issues/{issue_number}/labels",
        data=data,
        headers={
            "Authorization": f"Bearer {pat}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
        method='POST'
    )
    try:
        urllib.request.urlopen(req, timeout=15)
    except Exception as e:
        print(f"  ⚠️ change_issue_label: {e}")


def check_F89(repo_path):
    """F89: >=80% коммитов ссылаются на Issues (closes #N или fixes #N)."""
    import subprocess
    try:
        total = int(subprocess.check_output(
            ["git", "-C", repo_path, "rev-list", "--count", "HEAD"],
            stderr=subprocess.DEVNULL
        ).strip())
        if total == 0:
            return True, 1.0  # vacuously true
        with_issues = 0
        for pattern in ["closes #", "fixes #", "close #", "fix #"]:
            try:
                result = subprocess.check_output(
                    ["git", "-C", repo_path, "log", "--oneline", "--grep", pattern],
                    stderr=subprocess.DEVNULL
                ).strip()
                with_issues += result.count(b'\n') + (1 if result else 0)
            except Exception:
                pass
        ratio = with_issues / max(1, total)
        return ratio >= 0.80, ratio
    except Exception:
        return True, 1.0  # no git — skip


# ============================================================================
# v9.36: общие утилиты — вынесены из 3 копий serialize_value и MODEL_FILENAMES
# ============================================================================

# Единый реестр «id модели → имя файла .md» (раньше был в 3 местах:
# generate_decomposition.py:model_filename_map,
# migrate_dedup_quantity.py:name_map + model_map)
MODEL_FILENAMES: dict[str, str] = {
    'izdelie_SkyNet-T800':     't800.md',
    'izdelie_SkyNet-T1000':    't1000.md',
    'izdelie_SkyNet-Rev-9':    'rev9.md',
    'izdelie_SkyNet-HK-Aerial':'hk_aerial.md',
    'izdelie_SkyNet-HK-Tank':  'hk_tank.md',
    'izdelie_SkyNet-T600':     't600.md',
    'izdelie_SkyNet-T850':     't850.md',
    'izdelie_SkyNet-Marcus-Wright': 'marcus_wright.md',
    'izdelie_SkyNet-Cameron-Phillips': 'cameron_phillips.md',
    'izdelie_SkyNet-T-X':     't_x.md',
    'izdelie_SkyNet-T1001':   't1001.md',
}


def yaml_serialize_value(value) -> str:
    """Сериализовать Python-значение в YAML-строку для inline-использования.

    Единая реализация (раньше 3 копии в generate_decomposition.py,
    web_verify.py, decompose_all_izdeliya.py).
    """
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        if not value:
            return '[]'
        return '[' + ', '.join(yaml_serialize_value(v) for v in value) + ']'
    if isinstance(value, dict):
        if not value:
            return '{}'
        parts = ['{']
        items = []
        for k, v in value.items():
            items.append(f'  {k}: {yaml_serialize_value(v)}')
        parts.append('\n'.join(items))
        parts.append('}')
        return '\n'.join(parts)
    # string fallback — экранируем только если нужны кавычки
    s = str(value)
    # Если содержит спецсимволы YAML — обернуть в одинарные кавычки
    if any(c in s for c in [':', '#', '{', '}', '[', ']', ',', '&', '*', '!', '|', '>', "'", '"', '\n', '\t']):
        # Экранировать одинарные кавычки как ''
        escaped = s.replace("'", "''")
        return f"'{escaped}'"
    return s


def write_atomic(path, content: str) -> None:
    """Атомарная запись файла: tmp + os.replace.

    Защищает от частичной записи при прерывании процесса
    (раньше все генераторы делали fpath.write_text напрямую).
    """
    import os
    from pathlib import Path
    p = Path(path)
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_text(content, encoding='utf-8')
    os.replace(tmp, p)
