"""Tests for advanced_feature_quality_drift.feature_quality_scoring."""

import pandas as pd
import pytest

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
)
from advanced_feature_quality_drift.feature_quality_scoring import (
    calculate_feature_quality_score,
    build_feature_quality_score_report,
)


def test_calculate_feature_quality_score():
    score_perfect = calculate_feature_quality_score(1.0, 1.0, 1.0, 1.0, 1.0)
    assert score_perfect == 1.0

    score_zero = calculate_feature_quality_score(0.0, 0.0, 0.0, 0.0, 0.0)
    assert score_zero == 0.0

    score_partial = calculate_feature_quality_score(0.8, 1.0, 0.9, 0.7, 1.0)
    assert 0.0 <= score_partial <= 1.0
    # Expected: 0.8*0.25 + 1.0*0.25 + 0.9*0.20 + 0.7*0.15 + 1.0*0.15 = 0.2 + 0.25 + 0.18 + 0.105 + 0.15 = 0.885
    assert abs(score_partial - 0.885) < 1e-3


def test_build_feature_quality_score_report_default():
    df, summary = build_feature_quality_score_report()
    assert not df.empty
    assert len(df) == 6
    assert set(df["dimension"]) == {
        "overall_quality",
        "missingness",
        "infinite_values",
        "zero_variance",
        "duplicates",
        "namespace",
    }
    assert summary["overall_quality_score"] == 1.0
    assert summary["quality_status"] == "diagnostic_pass"
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["current_phase"] == 123
    assert summary["next_phase"] == 124


def test_build_feature_quality_score_report_with_tables():
    miss_df = pd.DataFrame([{"severity": "quality_critical"}, {"severity": "quality_medium"}])
    inf_df = pd.DataFrame([{"total_inf_count": 5}])
    zv_df = pd.DataFrame([{"zero_variance_flag": True}])
    dup_df = pd.DataFrame([{"severity": "quality_medium"}])
    ns_df = pd.DataFrame([{"has_forbidden_token": False, "is_duplicate": True}])

    tables = {
        "missingness": miss_df,
        "infinite_values": inf_df,
        "zero_variance": zv_df,
        "duplicates": dup_df,
        "namespace": ns_df,
    }

    df, summary = build_feature_quality_score_report(diagnostic_tables=tables)
    assert summary["overall_quality_score"] < 1.0
    assert summary["non_signal"] is True
