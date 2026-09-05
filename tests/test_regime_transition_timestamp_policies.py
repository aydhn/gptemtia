"""Tests for Regime Transition Timestamp Policies."""

from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_timestamp_policies import (
    build_regime_transition_timestamp_policy_registry,
    summarize_transition_timestamp_policies,
    TIMESTAMP_POLICIES,
)


def test_build_regime_transition_timestamp_policy_registry():
    profile = get_default_regime_transition_profile()
    df, summary = build_regime_transition_timestamp_policy_registry(profile)

    assert not df.empty
    assert len(df) == 4
    assert "policy_id" in df.columns
    assert (df["strictly_backward_looking"] == True).all()

    assert summary["total_policies"] == 4
    assert summary["all_strictly_backward_looking"] is True


def test_summarize_transition_timestamp_policies():
    profile = get_default_regime_transition_profile()
    df, _ = build_regime_transition_timestamp_policy_registry(profile)
    summary = summarize_transition_timestamp_policies(df)
    assert summary["total_policies"] == 4
    assert summary["all_strictly_backward_looking"] is True
