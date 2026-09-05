"""Tests for Regime Transition Profile Registry."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_profile_registry import (
    build_regime_transition_profile_registry,
)


def test_build_regime_transition_profile_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_profile_registry(profile)

    assert not df.empty
    assert len(df) >= 3
    assert "profile_name" in df.columns
    assert "current_phase" in df.columns
    assert (df["current_phase"] == 130).all()
    assert (df["target_final_phase"] == 160).all()
    assert (df["next_phase"] == 131).all()
    assert (df["non_signal"] == True).all()

    assert summary["total_profiles"] >= 3
    assert summary["all_local_only"] is True
    assert summary["zero_trading_allowed"] is True
    assert summary["zero_clustering_allowed"] is True
