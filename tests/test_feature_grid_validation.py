import pandas as pd
from advanced_feature_grid.feature_grid_validation import (
    validate_feature_grid_profile_registry,
    validate_window_grid_contracts,
    validate_indicator_parameter_grids,
    validate_no_forbidden_feature_grid_claims,
    build_feature_grid_validation_report,
)
from advanced_feature_grid.feature_grid_config import get_default_feature_grid_profile


def test_feature_grid_validation():
    profile = get_default_feature_grid_profile()

    # Test forbidden claims check
    res_claim = validate_no_forbidden_feature_grid_claims("Burada kesin al sinyali vardır.")
    assert res_claim["valid"] is False
    assert res_claim["has_violations"] is True

    res_clean_claim = validate_no_forbidden_feature_grid_claims("Sadece geriye dönük araştırma feature grid çıktısıdır.")
    assert res_clean_claim["valid"] is True

    # Test validation report build
    dummy_prof = pd.DataFrame([{
        "profile_name": profile.name,
        "current_phase": 118,
        "target_final_phase": 160,
        "next_phase": 119,
        "local_only": True,
        "research_only": True,
    }])
    tables = {"profiles": dummy_prof}
    df_val, sum_val = build_feature_grid_validation_report(tables, profile)
    assert not df_val.empty
    assert sum_val["validation_status"] == "PASS"
    assert sum_val["violations_count"] == 0
