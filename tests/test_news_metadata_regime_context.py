from advanced_regime_foundation.news_metadata_regime_context import (
    build_news_metadata_regime_context_registry,
    summarize_news_metadata_regime_context,
)


def test_news_metadata_regime_context():
    df, summary = build_news_metadata_regime_context_registry()
    assert not df.empty
    assert summary["all_metadata_only"] is True
    assert summary["all_non_signal"] is True

    # Invariant: No full text, no sentiment model output, no embeddings
    assert bool((df["contains_full_text"] == False).all())
    assert bool((df["contains_sentiment_model_output"] == False).all())
    assert bool((df["contains_embeddings"] == False).all())

    ctx_names = list(df["context_name"])
    assert "news_topic_attention_context" in ctx_names
    assert "news_asset_tag_context" in ctx_names
    assert "news_macro_tag_context" in ctx_names
    assert "news_event_linkage_context" in ctx_names
    assert "news_freshness_context_placeholder" in ctx_names

    summ = summarize_news_metadata_regime_context(df)
    assert summ["metadata_only"] is True
    assert summ["non_signal"] is True
