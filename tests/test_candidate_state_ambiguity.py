from advanced_market_behavior_diagnostics.candidate_state_ambiguity import (
    build_candidate_state_ambiguity_report,
    summarize_candidate_state_ambiguity,
)


def test_candidate_state_ambiguity():
    df, summary = build_candidate_state_ambiguity_report()

    assert not df.empty
    assert "candidate_state_name" in df.columns
    assert "ambiguity_score" in df.columns
    assert summary["average_ambiguity_score"] <= 0.20
    assert summary["unsupervised_execution"] is False
    assert summary["non_signal"] is True
