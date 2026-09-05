import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_metadata import (
    build_news_provider_metadata_registry,
    build_default_news_provider_metadata,
    validate_news_provider_metadata_item,
    summarize_news_provider_metadata
)

def test_news_provider_metadata():
    profile = get_default_news_provider_profile()
    items = build_default_news_provider_metadata(profile)
    assert len(items) == 6
    df, summary = build_news_provider_metadata_registry(profile)
    assert len(df) == 6
    assert summary["total_providers"] == 6

    val = validate_news_provider_metadata_item(items[0], profile)
    assert val["valid"] is True
