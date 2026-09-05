import pytest
from advanced_feature_quality_drift.feature_drift_metric_registry import (
    build_feature_drift_metric_registry,
    list_supported_drift_metrics,
)


def test_feature_drift_metric_registry():
    metrics = list_supported_drift_metrics()
    expected = [
        "distribution_mean_shift",
        "distribution_std_shift",
        "quantile_shift",
        "missingness_shift",
        "zero_variance_new_flag",
        "stability_score",
        "rolling_mean_stability",
        "rolling_std_stability",
        "population_shift_placeholder",
        "factor_family_drift_placeholder",
    ]
    for m in expected:
        assert m in metrics

    df, summary = build_feature_drift_metric_registry()
    assert not df.empty
    assert summary["total_drift_metrics"] == len(expected)
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
