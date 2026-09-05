from advanced_market_behavior_diagnostics.behavior_quality_metric_registry import (
    build_behavior_quality_metric_registry,
    summarize_behavior_quality_metrics,
    CORE_BEHAVIOR_QUALITY_METRICS,
)


def test_behavior_quality_metric_registry():
    df, summary = build_behavior_quality_metric_registry()

    assert not df.empty
    assert len(df) == len(CORE_BEHAVIOR_QUALITY_METRICS)
    assert "metric_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["total_metrics"] == len(CORE_BEHAVIOR_QUALITY_METRICS)
    assert "candidate_state_coverage_ratio" in summary["metric_names"]

