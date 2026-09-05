"""Tests for State Transition Continuity Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_transition_continuity import (
    build_state_transition_continuity_report,
    calculate_transition_continuity_placeholder,
    summarize_state_transition_continuity,
)


def test_build_state_transition_continuity_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_transition_continuity_report(profile)

    assert not df.empty
    assert len(df) == 4
    assert "entity_family" in df.columns
    assert "continuity_ratio" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_sequences"] == 4
    assert summary["all_non_signal"] is True
    assert summary["contains_trading_signal"] is False


def test_summarize_state_transition_continuity():
    df = calculate_transition_continuity_placeholder()
    summary = summarize_state_transition_continuity(df)
    assert summary["total_sequences"] == 4
    assert summary["all_non_signal"] is True
