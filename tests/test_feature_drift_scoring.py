"""Tests for advanced_feature_quality_drift.feature_drift_scoring."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_drift_scoring import (
    calculate_feature_drift_score,
    build_feature_drift_score_report,
)
from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
)


def test_calculate_feature_drift_score():
    score_full = calculate_feature_drift_score(1.0, 1.0, 1.0, 1.0)
    assert score_full == 1.0

    score_zero = calculate_feature_drift_score(0.0, 0.0, 0.0, 0.0)
    assert score_zero == 0.0

    score_mid = calculate_feature_drift_score(0.8, 0.7, 0.6, 0.9)
    assert 0.0 <= score_mid <= 1.0
    # Expected: 0.8*0.3 + 0.7*0.3 + 0.6*0.2 + 0.9*0.2 = 0.24 + 0.21 + 0.12 + 0.18 = 0.75
    assert abs(score_mid - 0.75) < 1e-3


def test_build_feature_drift_score_report_default():
    df, summary = build_feature_drift_score_report()
    assert not df.empty
    assert len(df) == 5
    assert set(df["dimension"]) == {
        "overall_stability",
        "mean_stability",
        "std_stability",
        "quantile_stability",
        "rolling_stability",
    }
    assert summary["overall_drift_score"] == 1.0
    assert summary["drift_status"] == "diagnostic_pass"
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124


def test_build_feature_drift_score_report_with_tables():
    drift_df = pd.DataFrame([
        {"severity": "drift_critical"},
        {"severity": "drift_medium"},
    ])
    roll_df = pd.DataFrame([
        {"stability_score": 0.45},
        {"stability_score": 0.55},
    ])
    tables = {
        "distribution_drift": drift_df,
        "rolling_stability": roll_df,
    }
    df, summary = build_feature_drift_score_report(diagnostic_tables=tables)
    assert summary["overall_drift_score"] < 1.0
    assert summary["non_signal"] is True
