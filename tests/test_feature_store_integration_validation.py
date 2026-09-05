import pandas as pd
from advanced_feature_store_integration.feature_store_integration_validation import (
    build_feature_store_integration_validation_report,
    validate_no_forbidden_feature_store_claims,
)
from advanced_feature_store_integration.feature_store_integration_profile_registry import (
    build_feature_store_integration_profile_registry,
)
from advanced_feature_store_integration.feature_store_contract_registry import (
    build_feature_store_contract_registry,
)
from advanced_feature_store_integration.feature_store_schema_registry import (
    build_feature_store_schema_registry,
)
from advanced_feature_store_integration.feature_store_metadata_manifest import (
    build_feature_store_metadata_manifest,
)

def test_validation_report():
    df_p, _ = build_feature_store_integration_profile_registry()
    df_c, _ = build_feature_store_contract_registry()
    df_s, _ = build_feature_store_schema_registry()
    df_m, _ = build_feature_store_metadata_manifest()

    tables = {"profiles": df_p, "contracts": df_c, "schemas": df_s, "manifest": df_m}
    df_val, s_val = build_feature_store_integration_validation_report(tables)
    assert not df_val.empty
    assert s_val["status"] == "VALIDATION_PASS"
    assert s_val["forbidden_claims_detected"] == 0

    assert validate_no_forbidden_feature_store_claims(text="non-signal offline feature store")["is_safe"] is True
    assert validate_no_forbidden_feature_store_claims(text="buy signal prediction")["is_safe"] is False
