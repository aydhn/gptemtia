"""Tests for Phase 134 Pseudo-State Store Catalog."""

from advanced_regime_featurestore_integration.pseudo_state_store_catalog import (
    build_pseudo_state_store_catalog,
    summarize_pseudo_state_store_catalog,
)


def test_pseudo_state_store_catalog():
    df, summary = build_pseudo_state_store_catalog()
    assert not df.empty
    assert len(df) == 3
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert (df["production_ready"] == False).all()
    assert summary["source_phase"] == 128

    s_res = summarize_pseudo_state_store_catalog(df)
    assert s_res["total_items"] == 3
    assert s_res["all_non_signal"] is True
