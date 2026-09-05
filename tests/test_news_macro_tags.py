import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_macro_tags import (
    build_news_macro_tag_registry,
    build_default_news_macro_tags,
    summarize_news_macro_tags
)

def test_news_macro_tags():
    profile = get_default_news_provider_profile()
    tags = build_default_news_macro_tags(profile)
    assert len(tags) == 9
    df, summary = build_news_macro_tag_registry(profile)
    assert len(df) == 9
    assert "CENTRAL_BANK" in df["tag_label"].values
    assert summary["total_tags"] == 9
