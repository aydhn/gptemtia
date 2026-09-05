"""Tests for Volatility Transition Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.volatility_transition_diagnostics import (
    build_volatility_transition_diagnostics_report,
    summarize_volatility_transition_diagnostics,
    VOLATILITY_TRANSITION_DATA,
)


def test_build_volatility_transition_diagnostics_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_volatility_transition_diagnostics_report(profile)

    assert not df.empty
    assert len(df) == 3
    assert "volatility_regime" in df.columns
    assert "transition_readiness" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_contexts"] == 3
    assert summary["all_dependencies_satisfied"] is True
    assert summary["all_non_signal"] is True


def test_summarize_volatility_transition_diagnostics():
    profile = get_default_regime_transition_profile()
    df, _ = build_volatility_transition_diagnostics_report(profile)
    summary = summarize_volatility_transition_diagnostics(df)
    assert summary["total_contexts"] == 3
    assert summary["all_non_signal"] is True
