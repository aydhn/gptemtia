"""Tests for Phase 134 Macro / Event / News Regime Store Catalog."""

from advanced_regime_featurestore_integration.macro_event_news_regime_store_catalog import (
    build_macro_event_news_regime_store_catalog,
    summarize_macro_event_news_regime_store_catalog,
)


def test_macro_event_news_regime_store_catalog():
    df, summary = build_macro_event_news_regime_store_catalog()
    assert not df.empty
    assert len(df) == 3
    assert (df["non_signal"] == True).all()
    assert (df["metadata_only_news_accepted"] == True).all()
    assert (df["source_preserved"] == True).all()
    assert summary["source_phase"] == 132

    s_res = summarize_macro_event_news_regime_store_catalog(df)
    assert s_res["total_items"] == 3
    assert s_res["all_metadata_only_news"] is True
    assert s_res["all_non_signal"] is True
