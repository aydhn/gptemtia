"""Tests for Trend Transition Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.trend_transition_diagnostics import (
    build_trend_transition_diagnostics_report,
    summarize_trend_transition_diagnostics,
    TREND_TRANSITION_DATA,
)


def test_build_trend_transition_diagnostics_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_trend_transition_diagnostics_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "trend_regime" in df.columns
    assert "trend_persistence" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_dependencies_satisfied"] is True
    assert summary["all_non_signal"] is True


def test_summarize_trend_transition_diagnostics():
    profile = get_default_regime_transition_profile()
    df, _ = build_trend_transition_diagnostics_report(profile)
    summary = summarize_trend_transition_diagnostics(df)
    assert summary["total_contexts"] == 3
    assert summary["all_non_signal"] is True
