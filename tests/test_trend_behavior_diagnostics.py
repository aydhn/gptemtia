from advanced_market_behavior_diagnostics.trend_behavior_diagnostics import (
    build_trend_behavior_diagnostics_report,
    summarize_trend_behavior_diagnostics,
)


def test_trend_behavior_diagnostics():
    df, summary = build_trend_behavior_diagnostics_report()

    assert not df.empty
    assert "context_name" in df.columns
    assert summary["all_ready"] is True
    assert summary["dependencies_passed"] is True
    assert summary["non_signal"] is True
