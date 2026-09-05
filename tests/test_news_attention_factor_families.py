import pytest
from advanced_factor_metadata.news_attention_factor_families import (
    build_news_attention_factor_family_registry,
    summarize_news_attention_factor_family,
)


def test_build_news_attention_factor_family_registry():
    df, summary = build_news_attention_factor_family_registry()
    assert not df.empty
    assert summary["total_factors"] >= 4
    assert summary["metadata_only_verified"] is True
    assert summary["non_signal"] is True

    names = list(df["factor_name"])
    assert "factor_news_topic_attention_context" in names
    assert "factor_news_asset_tag_attention_context" in names
    assert "factor_news_macro_tag_attention_context" in names
    assert "factor_news_event_linkage_context" in names
    assert "factor_news_freshness_placeholder_context" in names

    stats = summarize_news_attention_factor_family(df)
    assert stats["total_factors"] == len(df)
    assert stats["metadata_only"] is True
    assert stats["non_signal"] is True
