import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_official_api_provider import (
    NewsOfficialApiProviderPlaceholder,
    build_news_official_api_provider_placeholder
)

def test_news_official_api_provider():
    profile = get_default_news_provider_profile()
    prov = NewsOfficialApiProviderPlaceholder()
    assert prov.provider_name == "news_official_api_provider_placeholder"
    df, summary = build_news_official_api_provider_placeholder(profile)
    assert len(df) == 1
    assert summary["status"] == "placeholder_ready"
