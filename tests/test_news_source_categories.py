import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_source_categories import (
    build_news_source_category_registry,
    build_default_news_source_categories,
    summarize_news_source_categories
)

def test_news_source_categories():
    profile = get_default_news_provider_profile()
    cats = build_default_news_source_categories(profile)
    assert len(cats) == 10
    df, summary = build_news_source_category_registry(profile)
    assert len(df) == 10
    assert summary["total_categories"] == 10
