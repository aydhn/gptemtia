import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_region_currency_mapping import (
    build_news_region_currency_mapping_registry,
    build_default_news_region_currency_mappings,
    summarize_news_region_currency_mapping
)

def test_news_region_currency_mapping():
    profile = get_default_news_provider_profile()
    df_map = build_default_news_region_currency_mappings(profile)
    assert len(df_map) == 10
    df, summary = build_news_region_currency_mapping_registry(profile)
    assert len(df) == 10
    assert "US" in df["region"].values
    assert "TR" in df["region"].values
    assert summary["total_mappings"] == 10
