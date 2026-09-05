import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_topic_taxonomy import (
    build_news_topic_taxonomy_registry,
    build_default_news_topic_taxonomy,
    summarize_news_topic_taxonomy
)

def test_news_topic_taxonomy():
    profile = get_default_news_provider_profile()
    df_tax = build_default_news_topic_taxonomy(profile)
    assert len(df_tax) >= 12
    df, summary = build_news_topic_taxonomy_registry(profile)
    assert len(df) >= 12
    assert "central_bank" in df["topic_name"].values
    assert summary["total_topics"] >= 12
