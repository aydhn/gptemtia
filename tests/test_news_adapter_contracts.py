import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_adapter_contracts import (
    build_news_adapter_contract,
    build_default_news_adapter_contract_items,
    summarize_news_adapter_contract
)

def test_news_adapter_contracts():
    profile = get_default_news_provider_profile()
    items = build_default_news_adapter_contract_items(profile)
    assert len(items) == 21
    df, summary = build_news_adapter_contract(profile)
    assert len(df) == 21
    assert summary["total_contracts"] == 21
