"""Tests for State Persistence Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_persistence_diagnostics import (
    build_state_persistence_diagnostics_report,
    calculate_state_persistence_placeholder,
    summarize_state_persistence_diagnostics,
)


def test_build_state_persistence_diagnostics_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_persistence_diagnostics_report(profile)

    assert not df.empty
    assert len(df) == 6
    assert "candidate_state" in df.columns
    assert "persistence_score" in df.columns
    assert (df["non_signal"] == True).all()


    assert summary["total_analyzed_states"] == 6
    assert summary["all_non_signal"] is True
    assert summary["contains_prediction"] is False


def test_summarize_state_persistence_diagnostics():
    df = calculate_state_persistence_placeholder()
    summary = summarize_state_persistence_diagnostics(df)
    assert summary["total_analyzed_states"] == 6
    assert summary["all_non_signal"] is True
