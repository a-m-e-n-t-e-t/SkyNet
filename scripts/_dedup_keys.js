// SkyNet — единый источник normalizeViolationKey для verify_decomposition.yml.
// Оба шага (Create issues + Auto-close stale) require() этот модуль.
// История: в v9.34 функция была скопирована в два места, auto-close копия
// не получила F26-ветку → каждый F26 issue ложно закрывался как stale через
// час после создания и никогда не пересоздавался (dedup учитывает closed).
// Одна копия = класс copy-rot багов устранён.
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

// Legacy-fallback: метрика для старых issues без [F2x] в заголовке.
// v9.42: диапазон расширен до F28 (альтернативные формы материалов).
// v9.44: добавлены F31/F32 (дедупликация id/алиасов, семантические дубли).
// v9.53: добавлена F27b (битые ссылки на материалы — файл отсутствует в
//        каталоге материалы/; mirror F27 для случая, когда F27 не видит
//        ссылку, потому что файла нет).
// v9.32: добавлена F-scal (опциональное поле масштабируемость, P087 §12.6)
//        и F-ai-lineage (предок+улучшения+real_check для версия: ии-улучшенная, §12.7).
function legacyMetricFromTitle(title, violation) {
  const metricMatch = (title || '').match(/\[(F2[2-9](?:[a-z])?|F3[0-2]|F-scal|F-ai-lineage|F-fant-children)\]/);
  return metricMatch ? metricMatch[1] : (violation.startsWith('Родитель') ? 'F26' : 'F25');
}

module.exports = { normalizeViolationKey, legacyMetricFromTitle };
