"""Tests for Range Transition Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.range_transition_diagnostics import (
    build_range_transition_diagnostics_report,
    summarize_range_transition_diagnostics,
    RANGE_TRANSITION_DATA,
)


def test_build_range_transition_diagnostics_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_range_transition_diagnostics_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "range_state" in df.columns
    assert "range_stability" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_dependencies_satisfied"] is True
    assert summary["all_non_signal"] is True


def test_summarize_range_transition_diagnostics():
    profile = get_default_regime_transition_profile()
    df, _ = build_range_transition_diagnostics_report(profile)
    summary = summarize_range_transition_diagnostics(df)
    assert summary["total_contexts"] == 3
    assert summary["all_non_signal"] is True
