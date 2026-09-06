"""Tests for Phase 134 Regime Taxonomy Store Catalog."""

from advanced_regime_featurestore_integration.regime_taxonomy_store_catalog import (
    build_regime_taxonomy_store_catalog,
    summarize_regime_taxonomy_store_catalog,
)


def test_taxonomy_store_catalog():
    df, summary = build_regime_taxonomy_store_catalog()
    assert not df.empty
    assert len(df) == 4
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert (df["production_ready"] == False).all()
    assert (df["broker_ready"] == False).all()
    assert summary["source_phase"] == 126

    s_res = summarize_regime_taxonomy_store_catalog(df)
    assert s_res["total_items"] == 4
    assert s_res["all_non_signal"] is True
