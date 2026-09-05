"""Tests for State Transition Ambiguity Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_transition_ambiguity import (
    build_state_transition_ambiguity_report,
    calculate_transition_ambiguity_placeholder,
    summarize_state_transition_ambiguity,
)


def test_build_state_transition_ambiguity_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_transition_ambiguity_report(profile)

    assert not df.empty
    assert len(df) == 4
    assert "transition_boundary" in df.columns
    assert "mean_ambiguity_score" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_ambiguity_records"] == 4
    assert summary["all_non_signal"] is True
    assert summary["contains_predictive_score"] is False


def test_summarize_state_transition_ambiguity():
    df = calculate_transition_ambiguity_placeholder()
    summary = summarize_state_transition_ambiguity(df)
    assert summary["total_ambiguity_records"] == 4
    assert summary["all_non_signal"] is True
