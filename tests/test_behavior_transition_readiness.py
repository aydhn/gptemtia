from advanced_market_behavior_diagnostics.behavior_transition_readiness import (
    build_behavior_transition_readiness_report,
    summarize_behavior_transition_readiness,
)


def test_behavior_transition_readiness():
    df, summary = build_behavior_transition_readiness_report()

    assert not df.empty
    assert "readiness_area" in df.columns
    assert summary["all_ready"] is True
    assert summary["phase_130_transition_ready"] is True
    assert summary["non_signal"] is True
