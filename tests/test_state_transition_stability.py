"""Tests for State Transition Stability Diagnostics."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.state_transition_stability import (
    build_state_transition_stability_report,
    calculate_transition_stability_placeholder,
    summarize_state_transition_stability,
)


def test_build_state_transition_stability_report():
    profile = get_default_regime_transition_profile()
    df, summary = build_state_transition_stability_report(profile)

    assert not df.empty
    assert len(df) == 5
    assert "regime_family" in df.columns
    assert "stability_score" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_regimes"] == 5
    assert summary["all_non_signal"] is True
    assert summary["contains_trading_signal"] is False


def test_summarize_state_transition_stability():
    df = calculate_transition_stability_placeholder()
    summary = summarize_state_transition_stability(df)
    assert summary["total_regimes"] == 5
    assert summary["all_non_signal"] is True
