// SkyNet — единый источник normalizeViolationKey + extractFileId + determineComplexity
// для verify_decomposition.yml и cron_run.sh.
//
// Оба шага workflow (Create issues + Auto-close stale) require() этот модуль.
// История: в v9.34 функция была скопирована в два места, auto-close копия
// не получила F26-ветку → каждый F26 issue ложно закрывался как stale через
// час после создания и никогда не пересоздавался (dedup учитывает closed).
// Одна копия = класс copy-rot багов устранён.
//
// v9.57: добавлена extractFileId() — извлечение file_id из violation
//        для гибридной группировки (один issue на файл, supplement в существующий).
//
// v9.58: добавлена determineComplexity() — присвоение метки сложности
//        (complexity:quick|medium|complex) на основе содержимого violations.
//        Используется:
//          - в workflow при создании issue (label в запросе create)
//          - в cron_run.sh для complexity-aware stale-detection (порог 30/45/60 мин)
//          - в логике приоритизации (quick берутся раньше complex)
'use strict';

function normalizeViolationKey(metric, violation) {
  if (metric === 'F25' || violation.startsWith('Дубликат:')) {
    const m = violation.match(/с габаритами\s+([^:]+?)\s*:/);
    if (m) return `${metric}:${m[1].trim()}`;
    const idx = violation.indexOf(': [');
    return `${metric}:${idx > 0 ? violation.substring(0, idx) : violation}`;
  }
  if (metric === 'F26') {
    // "Родитель izdelie_XXX: подтип 'YYY' имеет N файлов..."
    const m = violation.match(/Родитель\s+(\S+?):\s*подтип\s+'([^']+)'/);
    if (m) return `${metric}:${m[1]}:${m[2]}`;
    const colonIdx = violation.indexOf(':');
    return `${metric}:${colonIdx > 0 ? violation.substring(0, colonIdx).trim() : violation.substring(0, 80)}`;
  }
  const colonIdx = violation.indexOf(':');
  const fileId = colonIdx > 0 ? violation.substring(0, colonIdx).trim() : violation.substring(0, 80);
  return `${metric}:${fileId}`;
}

// v9.57: extractFileId — извлечь file_id из violation для группировки.
// В отличие от normalizeViolationKey (который даёт metric:file_id),
// extractFileId возвращает ТОЛЬКО file_id (без метрики).
// Одинаковые file_id → группируются в один issue.
//   [A-url] izdelie_loop_heat_pipe: источник=web_search...  →  izdelie_loop_heat_pipe
//   izdelie_SkyNet-T800: ...                                  →  izdelie_SkyNet-T800
//   Родитель izdelie_X: подтип 'Y' имеет N файлов...          →  izdelie_X__subtype_Y
//   с габаритами 100×50×50: ...                               →  100×50×50
function extractFileId(metric, violation) {
  // Strip leading [..] markers like [A-url], [A-форма], [B-форма], etc.
  const v = violation.replace(/^\[[^\]]*\]\s*/, '');
  if (metric === 'F25' || v.startsWith('Дубликат:')) {
    const m = v.match(/с габаритами\s+([^:]+?)\s*:/);
    if (m) return m[1].trim();
    const idx = v.indexOf(': [');
    return idx > 0 ? v.substring(0, idx) : v.substring(0, 80);
  }
  if (metric === 'F26') {
    // F26 группируем по родитель+подтип (один issue на каждый подтип-дубликат)
    const m = v.match(/Родитель\s+(\S+?):\s*подтип\s+'([^']+)'/);
    if (m) return `${m[1]}__subtype_${m[2]}`;
    const colonIdx = v.indexOf(':');
    return colonIdx > 0 ? v.substring(0, colonIdx).trim() : v.substring(0, 80);
  }
  const colonIdx = v.indexOf(':');
  return colonIdx > 0 ? v.substring(0, colonIdx).trim() : v.substring(0, 80);
}

// v9.58: determineComplexity — классифицировать violations по сложности.
// Возвращает: 'quick' | 'medium' | 'complex'
//
// Эвристика:
//   complex — есть сложная метрика (требует web_search + новый файл)
//             ИЛИ ≥8 violations (большие кластеры)
//   medium  — есть medium-метрика (требует web_search + правки)
//             ИЛИ ≥2 violations
//   quick   — 1 нарушение, простая правка (без web_search)
//
// Метрики по сложности:
//   complex:  F27b (создать материал), F27c (создать технологию),
//             F-ai-lineage (предок + улучшения + real_check),
//             F-fant-children (создать sub-части модели)
//   medium:   F27 (свойства материала + web_search), F27d (создать материал для процесса),
//             F27e (технологии_частей + web_search), F27f (материалы_для_процесса + web_search),
//             F27g (дедупликация + web_search), F28 (альтернативные формы),
//             F15g/F15b/F15d/F15h (физбаланс — может потребовать datasheet),
//             F22 (источник_url), F29 (форма материала + datasheet),
//             F-scal (блок масштабируемости + datasheet), F34 (декомпозиция)
//   quick:    F25/F26 (дубликаты — без web_search), F31 (дедуп — без web_search),
//             F33 (классификация — без web_search)
const COMPLEX_METRICS = new Set(['F27b', 'F27c', 'F-ai-lineage', 'F-fant-children']);
const MEDIUM_METRICS = new Set([
  'F27', 'F27d', 'F27e', 'F27f', 'F27g', 'F28',
  'F15g', 'F15b', 'F15d', 'F15h',
  'F22', 'F29', 'F-scal', 'F34'
]);
const QUICK_METRICS = new Set(['F25', 'F26', 'F31', 'F33']);

function determineComplexity(viols) {
  if (!viols || viols.length === 0) return 'quick';
  const metrics = new Set(viols.map(v => v.metric));
  const n = viols.length;

  const hasComplex = [...metrics].some(m => COMPLEX_METRICS.has(m));
  const hasMedium = [...metrics].some(m => MEDIUM_METRICS.has(m));
  const hasQuick = [...metrics].some(m => QUICK_METRICS.has(m));

  // complex: ≥8 violations ИЛИ есть complex-метрика
  if (hasComplex || n >= 8) return 'complex';
  // medium: ≥2 violations ИЛИ есть medium-метрика
  if (n >= 2 || hasMedium) return 'medium';
  // quick: 1 нарушение, simple-метрика (или без явной complex/medium)
  return 'quick';
}

// v9.58: complexityToThreshold — порог stale для метки сложности.
// Используется в cron_run.sh для complexity-aware stale-detection.
//   quick   → 30 мин (default)
//   medium  → 45 мин (требует больше времени на web_search)
//   complex → 60 мин (большие кластеры, создание файлов)
const COMPLEXITY_STALE_THRESHOLD_MIN = {
  'quick': 30,
  'medium': 45,
  'complex': 60,
};

function complexityToThreshold(complexityLabel) {
  // Accepts 'complexity:quick', 'complexity:medium', 'complexity:complex' OR just 'quick'/'medium'/'complex'
  const c = complexityLabel.replace(/^complexity:/, '').toLowerCase();
  return COMPLEXITY_STALE_THRESHOLD_MIN[c] || 30;
}

// v9.58: complexityToExpectedMinutes — ожидаемое время цикла.
// Используется для time-budget picking.
const COMPLEXITY_EXPECTED_MIN = {
  'quick': 5,
  'medium': 15,
  'complex': 30,
};

function complexityToExpectedMinutes(complexityLabel) {
  const c = complexityLabel.replace(/^complexity:/, '').toLowerCase();
  return COMPLEXITY_EXPECTED_MIN[c] || 10;
}

// Legacy-fallback: метрика для старых issues без [F2x] в заголовке.
// v9.42: диапазон расширен до F28 (альтернативные формы материалов).
// v9.44: добавлены F31/F32 (дедупликация id/алиасов, семантические дубли).
// v9.53: добавлена F27b (битые ссылки на материалы — файл отсутствует в
//        каталоге материалы/; mirror F27 для случая, когда F27 не видит
//        ссылку, потому что файла нет).
// v9.32: добавлена F-scal (опциональное поле масштабируемость, P087 §12.6)
//        и F-ai-lineage (предок+улучшения+real_check для версия: ии-улучшенная, §12.7).
// v9.34: добавлена F-fant-children (ссылки модели → изделия).
// v9.35: regex синхронизирован с scripts/_metrics.py::get_legacy_regex_pattern()
//        через integrity-чек в pre-commit-hook.py. При рассинхроне — warning.
function legacyMetricFromTitle(title, violation) {
  const metricMatch = (title || '').match(/\[(F2[2-9](?:[a-z])?|F3[0-2]|F-scal|F-ai-lineage|F-fant-children)\]/);
  return metricMatch ? metricMatch[1] : (violation.startsWith('Родитель') ? 'F26' : 'F25');
}

module.exports = {
  normalizeViolationKey,
  legacyMetricFromTitle,
  extractFileId,
  determineComplexity,
  complexityToThreshold,
  complexityToExpectedMinutes,
  COMPLEX_METRICS,
  MEDIUM_METRICS,
  QUICK_METRICS,
  COMPLEXITY_STALE_THRESHOLD_MIN,
  COMPLEXITY_EXPECTED_MIN,
};
