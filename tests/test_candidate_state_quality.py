from advanced_market_behavior_diagnostics.candidate_state_quality import (
    build_candidate_state_quality_report,
    calculate_candidate_state_quality_summary,
    CORE_CANDIDATE_STATES,
)


def test_candidate_state_quality():
    df, summary = build_candidate_state_quality_report()

    assert not df.empty
    assert len(df) == len(CORE_CANDIDATE_STATES)
    assert "candidate_state_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_training_disallowed"] is True
    assert summary["ready_count"] == len(CORE_CANDIDATE_STATES)
    assert summary["average_completeness"] == 1.0
