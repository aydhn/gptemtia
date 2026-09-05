import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_capabilities import (
    build_news_provider_capability_registry,
    build_default_news_provider_capabilities,
    summarize_news_provider_capabilities
)

def test_news_provider_capabilities():
    profile = get_default_news_provider_profile()
    caps = build_default_news_provider_capabilities(profile)
    assert len(caps) >= 10
    df, summary = build_news_provider_capability_registry(profile)
    assert len(df) >= 10
    assert summary["total_capabilities"] >= 10
    for c in caps:
        assert c.no_scraping_compliant is True
        assert c.metadata_only is True
