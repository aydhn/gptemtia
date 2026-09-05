from advanced_market_behavior_diagnostics.candidate_state_coverage import (
    build_candidate_state_coverage_report,
    summarize_candidate_state_coverage,
)


def test_candidate_state_coverage():
    df, summary = build_candidate_state_coverage_report()

    assert not df.empty
    assert "candidate_state_family" in df.columns
    assert "state_count" in df.columns
    assert summary["all_families_covered"] is True
    assert summary["non_signal"] is True
    assert summary["total_candidate_states"] == 10
