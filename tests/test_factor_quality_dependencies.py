import pytest
from advanced_factor_metadata.factor_quality_dependencies import (
    build_factor_quality_dependency_registry,
    summarize_factor_quality_dependencies,
)


def test_build_factor_quality_dependency_registry():
    df, summary = build_factor_quality_dependency_registry()
    assert not df.empty
    assert summary["total_quality_dependencies"] >= 6
    assert summary["drift_relevant_count"] >= 5
    assert summary["non_signal"] is True

    metric_ids = list(df["quality_metric_id"])
    assert "qual_dep_missingness_threshold" in metric_ids
    assert "qual_dep_infinite_values" in metric_ids
    assert "qual_dep_duplicate_features" in metric_ids
    assert "qual_dep_drift_diagnostics_readiness" in metric_ids

    stats = summarize_factor_quality_dependencies(df)
    assert stats["total_metrics"] == len(df)
    assert stats["non_signal"] is True
