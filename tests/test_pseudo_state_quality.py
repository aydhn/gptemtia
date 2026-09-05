from advanced_market_behavior_diagnostics.pseudo_state_quality import (
    build_pseudo_state_quality_report,
    calculate_pseudo_state_quality_summary,
    CORE_PSEUDO_STATES,
)


def test_pseudo_state_quality():
    df, summary = build_pseudo_state_quality_report()

    assert not df.empty
    assert len(df) == len(CORE_PSEUDO_STATES)
    assert "pseudo_state_name" in df.columns
    assert summary["all_non_signal"] is True
    assert summary["all_unsupervised_disallowed"] is True
    assert summary["ready_count"] == len(CORE_PSEUDO_STATES)
