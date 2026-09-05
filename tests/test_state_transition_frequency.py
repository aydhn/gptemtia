"""Tests for State Transition Frequency Analysis."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_transition_frequency import (
    build_state_transition_frequency_report,
    calculate_transition_frequency_placeholder,
    summarize_state_transition_frequency,
)


def test_build_state_transition_frequency_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_transition_frequency_report(profile)

    assert not df.empty
    assert len(df) == 6
    assert "source_state" in df.columns
    assert "target_state" in df.columns
    assert "transition_count" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_transition_pairs"] == 6
    assert summary["all_non_signal"] is True
    assert summary["contains_predictive_score"] is False


def test_summarize_state_transition_frequency():
    df = calculate_transition_frequency_placeholder()
    summary = summarize_state_transition_frequency(df)
    assert summary["total_transition_pairs"] == 6
    assert summary["all_non_signal"] is True
