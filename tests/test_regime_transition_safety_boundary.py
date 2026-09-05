"""Tests for Regime Transition Safety Boundary."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_safety_boundary import (
    build_regime_transition_safety_boundary,
    build_regime_transition_no_go_conditions,
    build_regime_transition_safe_go_conditions,
    summarize_regime_transition_safety_boundary,
)


def test_build_regime_transition_safety_boundary():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_safety_boundary(profile)

    assert not df.empty
    assert len(df) == 26
    assert "rule_id" in df.columns
    assert "rule_type" in df.columns
    assert (df["is_active"] == True).all()

    assert summary["safety_status"] == "SECURE"
    assert summary["no_go_count"] == 18
    assert summary["safe_go_count"] == 8
    assert summary["live_trading_prohibited"] is True


def test_summarize_regime_transition_safety_boundary():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_transition_safety_boundary(profile)
    summary = summarize_regime_transition_safety_boundary(df)
    assert summary["safety_status"] == "SECURE"
    assert summary["live_trading_prohibited"] is True
