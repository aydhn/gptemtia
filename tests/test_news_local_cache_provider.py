import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_local_cache_provider import (
    NewsLocalCacheProviderPlaceholder,
    build_news_local_cache_provider_placeholder
)

def test_news_local_cache_provider():
    profile = get_default_news_provider_profile()
    prov = NewsLocalCacheProviderPlaceholder()
    assert prov.provider_name == "news_local_cache_provider_placeholder"
    df, summary = build_news_local_cache_provider_placeholder(profile)
    assert len(df) == 1
    assert summary["status"] == "ready"
