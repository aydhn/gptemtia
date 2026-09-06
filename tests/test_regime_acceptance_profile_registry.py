"""Test suite for Phase 135 Profile Registry."""

from advanced_regime_acceptance.regime_acceptance_profile_registry import (
    build_regime_acceptance_profile_registry,
    summarize_regime_acceptance_profiles,
)


def test_profile_registry_builder():
    df, summary = build_regime_acceptance_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert summary["total_profiles"] >= 3
    assert summary["current_phase"] == 135
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 136
    assert summary["non_signal"] is True

    s2 = summarize_regime_acceptance_profiles(df)
    assert s2["total_profiles"] == len(df)
    assert s2["non_signal"] is True
