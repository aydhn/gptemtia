import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_commodity_tags import (
    build_news_commodity_tag_registry,
    build_default_news_commodity_tags,
    summarize_news_commodity_tags
)

def test_news_commodity_tags():
    profile = get_default_news_provider_profile()
    tags = build_default_news_commodity_tags(profile)
    assert len(tags) == 9
    df, summary = build_news_commodity_tag_registry(profile)
    assert len(df) == 9
    assert "GOLD" in df["tag_label"].values
    assert "CRUDE_OIL" in df["tag_label"].values
    assert summary["total_tags"] == 9
