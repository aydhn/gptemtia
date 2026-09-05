"""Tests for Regime Transition Thresholds."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_thresholds import (
    build_regime_transition_threshold_registry,
    summarize_regime_transition_thresholds,
    TRANSITION_THRESHOLDS,
)


def test_build_regime_transition_threshold_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_threshold_registry(profile)

    assert not df.empty
    assert len(df) == 8
    assert "threshold_key" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_thresholds"] == 8
    assert summary["all_non_signal"] is True


def test_summarize_regime_transition_thresholds():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_transition_threshold_registry(profile)
    summary = summarize_regime_transition_thresholds(df)
    assert summary["total_thresholds"] == 8
    assert summary["all_non_signal"] is True
