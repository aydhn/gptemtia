import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_domain_registry import (
    build_news_metadata_domain_registry,
    build_default_news_domains,
    summarize_news_domains
)

def test_news_domain_registry():
    profile = get_default_news_provider_profile()
    domains = build_default_news_domains(profile)
    assert len(domains) == 35
    df, summary = build_news_metadata_domain_registry(profile)
    assert len(df) == 35
    assert summary["total_domains"] == 35
