import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_asset_tags import (
    build_news_asset_tag_registry,
    build_default_news_asset_tags,
    summarize_news_asset_tags
)

def test_news_asset_tags():
    profile = get_default_news_provider_profile()
    tags = build_default_news_asset_tags(profile)
    assert len(tags) == 9
    df, summary = build_news_asset_tag_registry(profile)
    assert len(df) == 9
    assert "FX" in df["tag_label"].values
    assert "COMMODITIES" in df["tag_label"].values
    assert summary["total_tags"] == 9
