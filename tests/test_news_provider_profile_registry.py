import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_profile_registry import (
    build_news_metadata_provider_profile_registry,
    build_default_news_provider_profile_items,
    summarize_news_provider_profile_registry
)

def test_news_provider_profile_registry():
    profile = get_default_news_provider_profile()
    items = build_default_news_provider_profile_items(profile)
    assert len(items) >= 3
    df, summary = build_news_metadata_provider_profile_registry(profile)
    assert len(df) >= 3
    assert "total_profiles" in summary
    assert summary["total_profiles"] >= 3
