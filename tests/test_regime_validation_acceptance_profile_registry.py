"""Tests for Regime Validation Acceptance Profile Registry."""

from advanced_regime_validation_acceptance.regime_validation_acceptance_profile_registry import (
    build_regime_validation_acceptance_profile_registry,
    summarize_regime_validation_acceptance_profiles,
)


def test_profile_registry():
    df, summary = build_regime_validation_acceptance_profile_registry()
    assert not df.empty
    assert summary["total_profiles"] == len(df)
    assert summary["current_phase"] == 133
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 134
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True

    s_df = summarize_regime_validation_acceptance_profiles(df)
    assert s_df["total_profiles"] == len(df)
    assert s_df["active_profiles"] == 1
