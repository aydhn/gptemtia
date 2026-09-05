import pytest
from advanced_feature_quality_drift.feature_quality_metric_registry import (
    build_feature_quality_metric_registry,
    list_supported_quality_metrics,
)


def test_feature_quality_metric_registry():
    metrics = list_supported_quality_metrics()
    expected = [
        "missingness_ratio",
        "infinite_value_ratio",
        "all_nan_flag",
        "zero_variance_flag",
        "duplicate_value_ratio",
        "numeric_sanity_flag",
        "namespace_validity_flag",
        "source_validation_status",
        "manual_review_blocker_count",
    ]
    for m in expected:
        assert m in metrics

    df, summary = build_feature_quality_metric_registry()
    assert not df.empty
    assert summary["total_quality_metrics"] == len(expected)
    assert summary["non_signal"] is True
    assert summary["destructive_action_allowed"] is False
