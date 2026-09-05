import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_validation import (
    validate_no_forbidden_data_quality_claims,
    build_data_quality_validation_report,
)


def test_data_quality_validation():
    profile = get_default_data_quality_profile()

    # Forbidden claims check
    clean_res = validate_no_forbidden_data_quality_claims("Bu bir offline testtir.")
    assert clean_res["valid"] is True

    bad_res = validate_no_forbidden_data_quality_claims("Bu sistem kesin live trading sinyali üretir.")
    assert bad_res["valid"] is False
    assert len(bad_res["breaches"]) > 0

    # Validation report with valid dummy data
    tables = {
        "profile_registry": pd.DataFrame([{"profile_name": "p1"}]),
        "domain_registry": pd.DataFrame([{"domain_id": f"d_{i}"} for i in range(25)]),
        "severity_registry": pd.DataFrame([
            {"severity_label": s} for s in ["quality_critical", "quality_high", "quality_medium", "quality_low", "quality_info"]
        ]),
        "rule_registry": pd.DataFrame([{"rule_id": f"r_{i}"} for i in range(20)]),
        "safety_boundary": pd.DataFrame([{"rule": f"sb_{i}"} for i in range(35)]),
    }
    val_df, val_sum = build_data_quality_validation_report(tables, profile)
    assert len(val_df) >= 7
    assert val_sum["valid"] is True
