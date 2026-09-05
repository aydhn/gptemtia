from advanced_market_behavior_diagnostics.behavior_stability_readiness import (
    build_behavior_stability_readiness_report,
    summarize_behavior_stability_readiness,
)


def test_behavior_stability_readiness():
    df, summary = build_behavior_stability_readiness_report()

    assert not df.empty
    assert "readiness_area" in df.columns
    assert summary["all_ready"] is True
    assert summary["phase_130_stability_ready"] is True
    assert summary["non_signal"] is True
