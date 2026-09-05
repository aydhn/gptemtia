import pytest
from advanced_feature_quality_drift.feature_quality_thresholds import (
    build_feature_quality_threshold_registry,
    get_default_quality_thresholds,
)


def test_feature_quality_thresholds():
    thresholds = get_default_quality_thresholds()
    assert "missingness_ratio" in thresholds
    assert thresholds["missingness_ratio"]["warning"] == 0.25
    assert thresholds["missingness_ratio"]["critical"] == 0.50

    df, summary = build_feature_quality_threshold_registry()
    assert not df.empty
    assert summary["auto_drop_allowed"] is False
    assert summary["auto_fix_allowed"] is False
    assert summary["non_signal"] is True

    for _, row in df.iterrows():
        assert row["auto_drop_allowed"] is False
        assert row["auto_fix_allowed"] is False
