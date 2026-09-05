from advanced_market_behavior_diagnostics.candidate_state_missingness import (
    build_candidate_state_missingness_report,
    summarize_candidate_state_missingness,
)


def test_candidate_state_missingness():
    df, summary = build_candidate_state_missingness_report()

    assert not df.empty
    assert "candidate_state_name" in df.columns
    assert "missingness_ratio" in df.columns
    assert summary["average_missingness_ratio"] == 0.0
    assert summary["auto_imputation_allowed"] is False
    assert summary["auto_drop_allowed"] is False
    assert summary["non_signal"] is True
