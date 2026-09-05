import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_licensed_provider import (
    NewsLicensedProviderPlaceholder,
    build_news_licensed_provider_placeholder
)

def test_news_licensed_provider():
    profile = get_default_news_provider_profile()
    prov = NewsLicensedProviderPlaceholder()
    assert prov.provider_name == "news_licensed_provider_placeholder"
    df, summary = build_news_licensed_provider_placeholder(profile)
    assert len(df) == 1
    assert summary["status"] == "placeholder_ready"
