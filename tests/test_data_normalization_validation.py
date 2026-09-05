import pandas as pd
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_validation import (
    validate_no_forbidden_normalization_claims,
    build_data_normalization_validation_report,
)


def test_validation_forbidden_claims():
    res = validate_no_forbidden_normalization_claims(text="Bu bir test metnidir, normal veridir.")
    assert res["passed"] is True
    assert res["violations_count"] == 0

    bad_res = validate_no_forbidden_normalization_claims(text="Bu bir buy signal ve live trading talimatidir.")
    assert bad_res["passed"] is False
    assert bad_res["violations_count"] >= 1


def test_build_validation_report():
    prof = get_default_data_normalization_profile()
    tables = {
        "profile_registry": pd.DataFrame([{"profile_name": "balanced_non_destructive_normalization"}]),
        "domain_registry": pd.DataFrame([{"domain_id": i} for i in range(25)]),
        "rule_registry": pd.DataFrame([{"non_destructive": True}]),
        "canonical_schema_registry": pd.DataFrame([{"schema_name": "s1", "primary_key_fields": ["id"]}]),
        "canonical_field_registry": pd.DataFrame([{"canonical_field_name": "f1", "required": True}]),
        "output_manifest": pd.DataFrame([{"source_preserved": True}]),
        "score_report": pd.DataFrame([{"score": 0.95}]),
    }
    df, summary = build_data_normalization_validation_report(tables, prof)
    assert not df.empty
    assert summary["all_passed"] is True
    assert summary["forbidden_claims_found"] == 0
