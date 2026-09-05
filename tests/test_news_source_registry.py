import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_source_registry import (
    build_news_source_registry,
    build_default_news_sources,
    summarize_news_source_registry
)

def test_news_source_registry():
    profile = get_default_news_provider_profile()
    sources = build_default_news_sources(profile)
    assert len(sources) >= 8
    df, summary = build_news_source_registry(profile)
    assert len(df) >= 8
    assert "CENTRAL_BANK_STATEMENTS_PLACEHOLDER" in df["source_name"].values
    assert "LICENSED_NEWSWIRE_PLACEHOLDER" in df["source_name"].values
    assert summary["total_sources"] >= 8
