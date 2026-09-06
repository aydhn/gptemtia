"""Tests for Phase 134 Regime FeatureStore Domain Registry."""

from advanced_regime_featurestore_integration.regime_featurestore_domain_registry import (
    build_regime_featurestore_domain_registry,
    summarize_regime_featurestore_domain_registry,
)


def test_domain_registry_output():
    df, summary = build_regime_featurestore_domain_registry()
    assert not df.empty
    assert len(df) >= 30
    assert (df["non_signal"] == True).all()
    assert summary["current_phase"] == 134

    s_res = summarize_regime_featurestore_domain_registry(df)
    assert s_res["total_domains"] == len(df)
    assert s_res["all_non_signal"] is True
