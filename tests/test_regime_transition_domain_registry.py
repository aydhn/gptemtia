"""Tests for Regime Transition Domain Registry."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_domain_registry import (
    build_regime_transition_domain_registry,
)


def test_build_regime_transition_domain_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_domain_registry(profile)

    assert not df.empty
    assert len(df) == 28
    assert "domain_key" in df.columns
    assert "domain_name" in df.columns
    assert "current_phase" in df.columns
    assert (df["non_signal"] == True).all()

    assert summary["total_domains"] == 28
    assert summary["all_non_signal"] is True
    assert summary["zero_model_training"] is True

