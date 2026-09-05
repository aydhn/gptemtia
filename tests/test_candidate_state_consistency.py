from advanced_market_behavior_diagnostics.candidate_state_consistency import (
    build_candidate_state_consistency_report,
    summarize_candidate_state_consistency,
)


def test_candidate_state_consistency():
    df, summary = build_candidate_state_consistency_report()

    assert not df.empty
    assert "candidate_state_name" in df.columns
    assert "consistency_score" in df.columns
    assert summary["average_consistency_score"] == 1.0
    assert summary["clustering_executed"] is False
    assert summary["non_signal"] is True
