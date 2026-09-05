import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_public_dataset_provider import (
    NewsPublicDatasetProviderPlaceholder,
    build_news_public_dataset_provider_placeholder
)

def test_news_public_dataset_provider():
    profile = get_default_news_provider_profile()
    prov = NewsPublicDatasetProviderPlaceholder()
    assert prov.provider_name == "news_public_dataset_provider_placeholder"
    df, summary = build_news_public_dataset_provider_placeholder(profile)
    assert len(df) == 1
    assert summary["status"] == "placeholder_ready"
