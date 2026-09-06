"""Tests for Phase 134 Transition Store Catalog."""

from advanced_regime_featurestore_integration.transition_store_catalog import (
    build_transition_store_catalog,
    summarize_transition_store_catalog,
)


def test_transition_store_catalog():
    df, summary = build_transition_store_catalog()
    assert not df.empty
    assert len(df) == 3
    assert (df["non_signal"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert (df["production_ready"] == False).all()
    assert summary["source_phase"] == 130

    s_res = summarize_transition_store_catalog(df)
    assert s_res["total_items"] == 3
    assert s_res["all_non_signal"] is True
