"""Tests for Phase 132 News Metadata Regime Entities (Metadata-Only)."""

from advanced_macro_event_news_regime.news_metadata_regime_entities import (
    build_news_metadata_regime_entity_registry,
    summarize_news_metadata_regime_entities,
)


def test_build_news_metadata_regime_entities():
    df, summary = build_news_metadata_regime_entity_registry()
    assert not df.empty
    assert len(df) >= 8
    assert "entity_type" in df.columns
    assert "news_topic_tag" in df["entity_type"].values
    assert "news_asset_tag" in df["entity_type"].values
    assert "news_macro_tag" in df["entity_type"].values
    assert "news_event_reference" in df["entity_type"].values

    # Invariants
    assert not df["contains_full_article_text"].any()
    assert not df["contains_article_body"].any()
    assert not df["contains_raw_content"].any()
    assert not df["contains_scraped_html"].any()
    assert not df["contains_embedding"].any()
    assert not df["contains_vector"].any()
    assert not df["sentiment_model_output"].any()
    assert summary["all_non_signal"] is True


def test_summarize_news_metadata_regime_entities():
    df, _ = build_news_metadata_regime_entity_registry()
    summary = summarize_news_metadata_regime_entities(df)
    assert summary["total_news_metadata_entities"] >= 8
    assert summary["zero_article_text"] is True
    assert summary["zero_sentiment"] is True
    assert summary["all_non_signal"] is True
