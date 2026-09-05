import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_registry import (
    build_news_provider_registry,
    build_default_news_provider_registry,
    summarize_news_provider_registry
)

def test_news_provider_registry():
    profile = get_default_news_provider_profile()
    reg = build_default_news_provider_registry(profile)
    assert len(reg.list_providers()) == 6
    assert "news_dry_run_fixture_provider" in reg.list_providers()

    df, summary = build_news_provider_registry(profile)
    assert len(df) == 6
    assert summary["total_providers"] == 6
