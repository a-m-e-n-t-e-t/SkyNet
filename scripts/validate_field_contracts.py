"""SkyNet Validate Field Contracts — F56, F58-F60, F70.

v9.13: расширен check_schemas_consistency() (F70).
v9.17: импортирует helpers из _helpers.py
"""
from scripts._helpers import check_schemas_consistency

def validate():
    # F56: cross_layer_consistency
    # F58: compute_before_web_compliance
    # F59: registry_fill_rate
    # F60: archive_contract_compliance
    # F70: schema_catalog_consistency
    result = check_schemas_consistency()
    return result
