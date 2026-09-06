"""Tests for Phase 134 Regime FeatureStore Entities."""

from advanced_regime_featurestore_integration.regime_featurestore_entities import (
    build_regime_featurestore_entity_registry,
    summarize_regime_featurestore_entities,
)


def test_entities_registry():
    df, summary = build_regime_featurestore_entity_registry()
    assert not df.empty
    assert len(df) >= 8
    assert (df["non_signal"] == True).all()
    assert (df["production_ready"] == False).all()

    s_res = summarize_regime_featurestore_entities(df)
    assert s_res["total_entities"] == len(df)
    assert s_res["all_non_signal"] is True
