import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_manual_file_provider import (
    NewsManualFileProviderPlaceholder,
    build_news_manual_file_provider_placeholder
)

def test_news_manual_file_provider():
    profile = get_default_news_provider_profile()
    prov = NewsManualFileProviderPlaceholder()
    assert prov.provider_name == "news_manual_file_provider_placeholder"
    df, summary = build_news_manual_file_provider_placeholder(profile)
    assert len(df) == 1
    assert summary["status"] == "ready"
