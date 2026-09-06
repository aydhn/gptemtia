"""Tests for Phase 134 Regime FeatureStore Profile Registry."""

from advanced_regime_featurestore_integration.regime_featurestore_profile_registry import (
    build_regime_featurestore_profile_registry,
    summarize_regime_featurestore_profile_registry,
)


def test_profile_registry_output():
    df, summary = build_regime_featurestore_profile_registry()
    assert not df.empty
    assert len(df) >= 3
    assert (df["non_signal"] == True).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert summary["current_phase"] == 134
    assert summary["next_phase"] == 135

    s_res = summarize_regime_featurestore_profile_registry(df)
    assert s_res["total_profiles"] == len(df)
    assert s_res["all_non_signal"] is True
