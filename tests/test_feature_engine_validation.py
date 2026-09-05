import pandas as pd
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_profile_registry import build_feature_engine_profile_registry
from advanced_feature_engine.feature_input_contracts import build_feature_input_contract_registry
from advanced_feature_engine.feature_schema_registry import build_feature_schema_registry
from advanced_feature_engine.factor_schema_registry import build_factor_schema_registry
from advanced_feature_engine.indicator_catalog_registry import build_indicator_catalog_registry
from advanced_feature_engine.feature_engine_validation import (
    validate_no_forbidden_feature_claims,
    build_feature_engine_validation_report,
)


def test_feature_engine_validation():
    profile = get_default_feature_engine_profile()

    # Test forbidden claims validator
    assert validate_no_forbidden_feature_claims(text="normal feature calculation")["valid"] is True
    assert validate_no_forbidden_feature_claims(text="kesin al ve buy signal")["valid"] is False
    assert validate_no_forbidden_feature_claims(df=pd.DataFrame({"signal": [1]}))["valid"] is False

    # Test full validation report
    prof_df, _ = build_feature_engine_profile_registry(profile)
    ic_df, _ = build_feature_input_contract_registry(profile)
    fs_df, _ = build_feature_schema_registry(profile)
    fact_df, _ = build_factor_schema_registry(profile)
    ind_df, _ = build_indicator_catalog_registry(profile)

    tables = {
        "profiles": prof_df,
        "input_contracts": ic_df,
        "feature_schemas": fs_df,
        "factor_schemas": fact_df,
        "indicator_catalogs": ind_df,
    }

    report_df, summary = build_feature_engine_validation_report(tables, profile)

    assert summary["validation_status"] == "VALID"
    assert summary["forbidden_claims_found"] is False
    assert summary["non_signal"] is True
