from advanced_market_behavior_diagnostics.candidate_state_stability import (
    build_candidate_state_stability_report,
    summarize_candidate_state_stability,
)


def test_candidate_state_stability():
    df, summary = build_candidate_state_stability_report()

    assert not df.empty
    assert "candidate_state_name" in df.columns
    assert "temporal_stability_score" in df.columns
    assert summary["average_stability_score"] >= 0.80
    assert summary["forward_returns_used"] is False
    assert summary["shift_negative_used"] is False
    assert summary["non_signal"] is True
