import pandas as pd
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_validation import (
    validate_technical_indicator_profile_registry,
    validate_technical_indicator_catalog,
    validate_indicator_parameter_contracts,
    validate_indicator_output_schema,
    validate_indicator_computation_rehearsal,
    validate_no_forbidden_indicator_claims,
    build_technical_indicator_validation_report,
)


def test_technical_indicator_validation():
    profile = get_default_technical_indicator_profile()

    prof_df = pd.DataFrame([{"current_phase": 117, "target_final_phase": 160}])
    assert validate_technical_indicator_profile_registry(prof_df, profile)["valid"] is True

    cat_df = pd.DataFrame([{"indicator_name": f"ind_{i}"} for i in range(35)])
    assert validate_technical_indicator_catalog(cat_df, profile)["valid"] is True

    # Claims validation
    assert validate_no_forbidden_indicator_claims(text="Bu basit bir SMA indikatörüdür.")["valid"] is True
    assert validate_no_forbidden_indicator_claims(text="Buradan kesin al tavsiyesi verilir.")["valid"] is False

    val_df, summary = build_technical_indicator_validation_report({}, profile)
    assert not val_df.empty
    assert summary["validation_status"] == "PASS"
