"""Tests for Fusion Feature Validation Rules."""

import pandas as pd
from advanced_feature_fusion.fusion_feature_validation_rules import (
    get_fusion_feature_validation_rules,
    run_all_fusion_feature_validation_rules,
    get_validation_rules_summary,
)


def test_rules_registry():
    rules = get_fusion_feature_validation_rules()
    assert len(rules) >= 3
    summary = get_validation_rules_summary()
    assert summary["rule_count"] == len(rules)
    assert summary["zero_signal_mandate"] is True


def test_run_validation_rules_clean():
    times = pd.date_range("2025-01-01 10:00:00", periods=5, freq="1h", tz="UTC")
    clean_df = pd.DataFrame({
        "timestamp": times,
        "feature_val": [1.0, 2.0, 3.0, 4.0, 5.0],
        "is_active_flag": [1, 0, 1, 0, 1],
    })
    findings = run_all_fusion_feature_validation_rules(clean_df)
    assert len(findings) == 0


def test_run_validation_rules_violations():
    # Contains forbidden term 'prediction_score'
    bad_df = pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01 10:00:00", periods=3, freq="1h", tz="UTC"),
        "prediction_score": [0.8, 0.9, 0.7],
    })
    findings = run_all_fusion_feature_validation_rules(bad_df)
    assert len(findings) > 0
    assert any(f.severity == "CRITICAL" for f in findings)
