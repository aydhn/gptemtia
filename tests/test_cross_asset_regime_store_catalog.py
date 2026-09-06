"""Tests for Phase 134 Cross-Asset Regime Store Catalog."""

from advanced_regime_featurestore_integration.cross_asset_regime_store_catalog import (
    build_cross_asset_regime_store_catalog,
    summarize_cross_asset_regime_store_catalog,
)


def test_cross_asset_regime_store_catalog():
    df, summary = build_cross_asset_regime_store_catalog()
    assert not df.empty
    assert len(df) == 3
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert (df["production_ready"] == False).all()
    assert summary["source_phase"] == 131

    s_res = summarize_cross_asset_regime_store_catalog(df)
    assert s_res["total_items"] == 3
    assert s_res["all_non_signal"] is True
