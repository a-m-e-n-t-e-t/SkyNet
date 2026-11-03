"""SkyNet Validate Field Contracts — F56, F58-F60, F70.

v9.13: расширен check_schemas_consistency() (F70).
v9.31.1: исправлен импорт (from scripts._helpers → from _helpers)
"""
from _helpers import check_schemas_consistency

def validate():
    """F56: cross_layer_consistency, F58-F60, F70."""
    result = check_schemas_consistency()
    return result

if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, indent=2, ensure_ascii=False) if isinstance(result, dict) else result)
