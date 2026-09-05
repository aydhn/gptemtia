"""Tests for Macro Event Transition Context."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.macro_event_transition_context import (
    build_macro_event_transition_context_report,
    summarize_macro_event_transition_context,
    MACRO_EVENT_TRANSITION_DATA,
)


def test_build_macro_event_transition_context_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_macro_event_transition_context_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "event_window_context" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_source_preserved"] is True
    assert summary["all_non_signal"] is True


def test_summarize_macro_event_transition_context():
    profile = get_default_regime_transition_profile()
    df, _ = build_macro_event_transition_context_report(profile)
    summary = summarize_macro_event_transition_context(df)
    assert summary["total_contexts"] == 3
    assert summary["all_source_preserved"] is True
