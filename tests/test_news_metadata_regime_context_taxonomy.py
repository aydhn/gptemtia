"""Tests for Phase 132 News Metadata Regime Context Taxonomy."""

from advanced_macro_event_news_regime.news_metadata_regime_context_taxonomy import (
    build_news_metadata_regime_context_taxonomy_registry,
    summarize_news_metadata_regime_context_taxonomy,
)


def test_build_news_metadata_regime_context_taxonomy():
    df, summary = build_news_metadata_regime_context_taxonomy_registry()
    assert not df.empty
    assert len(df) >= 6
    assert "taxonomy_name" in df.columns
    assert "news_topic_attention_context" in df["taxonomy_name"].values
    assert "news_asset_tag_context" in df["taxonomy_name"].values
    assert "news_macro_tag_context" in df["taxonomy_name"].values
    assert "news_event_linkage_context" in df["taxonomy_name"].values

    assert summary["strictly_metadata_only"] is True
    assert summary["zero_article_text"] is True
    assert summary["zero_sentiment"] is True
    assert summary["all_non_signal"] is True


def test_summarize_news_metadata_context_taxonomy():
    df, _ = build_news_metadata_regime_context_taxonomy_registry()
    summary = summarize_news_metadata_regime_context_taxonomy(df)
    assert summary["total_taxonomies"] >= 6
    assert summary["zero_article_text"] is True
    assert summary["all_non_signal"] is True
