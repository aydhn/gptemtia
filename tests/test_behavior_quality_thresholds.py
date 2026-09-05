from advanced_market_behavior_diagnostics.behavior_quality_thresholds import (
    build_behavior_quality_threshold_registry,
    summarize_behavior_quality_thresholds,
    CORE_BEHAVIOR_QUALITY_THRESHOLDS,
)


def test_behavior_quality_thresholds():
    df, summary = build_behavior_quality_threshold_registry()

    assert not df.empty
    assert len(df) == len(CORE_BEHAVIOR_QUALITY_THRESHOLDS)
    assert "threshold_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["total_thresholds"] == len(CORE_BEHAVIOR_QUALITY_THRESHOLDS)
    assert "coverage_warning_below" in summary["threshold_names"]

