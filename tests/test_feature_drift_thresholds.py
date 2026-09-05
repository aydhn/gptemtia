import pytest
from advanced_feature_quality_drift.feature_drift_thresholds import (
    build_feature_drift_threshold_registry,
    get_default_drift_thresholds,
)


def test_feature_drift_thresholds():
    thresholds = get_default_drift_thresholds()
    assert "distribution_mean_shift" in thresholds
    assert thresholds["distribution_mean_shift"]["warning"] == 0.50
    assert thresholds["distribution_mean_shift"]["critical"] == 1.00

    df, summary = build_feature_drift_threshold_registry()
    assert not df.empty
    assert summary["auto_drop_allowed"] is False
    assert summary["auto_fix_allowed"] is False
    assert summary["non_signal"] is True
