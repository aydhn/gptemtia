import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_deduplication_requirements import (
    build_news_deduplication_requirement_registry,
    build_default_news_deduplication_requirements,
    summarize_news_deduplication_requirements
)

def test_news_deduplication_requirements():
    profile = get_default_news_provider_profile()
    df_req = build_default_news_deduplication_requirements(profile)
    assert len(df_req) >= 2
    df, summary = build_news_deduplication_requirement_registry(profile)
    assert len(df) >= 2
    assert summary["total_requirements"] >= 2
