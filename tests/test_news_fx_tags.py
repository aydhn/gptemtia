import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_fx_tags import (
    build_news_fx_tag_registry,
    build_default_news_fx_tags,
    summarize_news_fx_tags
)

def test_news_fx_tags():
    profile = get_default_news_provider_profile()
    tags = build_default_news_fx_tags(profile)
    assert len(tags) == 10
    df, summary = build_news_fx_tag_registry(profile)
    assert len(df) == 10
    assert "USD" in df["tag_label"].values
    assert "TRY" in df["tag_label"].values
    assert summary["total_tags"] == 10
