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
function legacyMetricFromTitle(title, violation) {
  const metricMatch = (title || '').match(/\[(F2[2-6])\]/);
  return metricMatch ? metricMatch[1] : (violation.startsWith('Родитель') ? 'F26' : 'F25');
}

module.exports = { normalizeViolationKey, legacyMetricFromTitle };
