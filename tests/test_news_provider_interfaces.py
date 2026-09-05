import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_interfaces import (
    BaseNewsMetadataProvider,
    build_news_provider_interface_contract,
    summarize_news_provider_interface_contract
)

def test_news_provider_interfaces():
    profile = get_default_news_provider_profile()
    df, summary = build_news_provider_interface_contract(profile)
    assert len(df) == 5
    assert summary["total_methods"] == 5
    assert "fetch_news_metadata" in df["method_name"].values
