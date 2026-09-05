import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_freshness_requirements import (
    build_news_freshness_staleness_requirement_registry,
    build_default_news_freshness_requirements,
    summarize_news_freshness_requirements
)

def test_news_freshness_requirements():
    profile = get_default_news_provider_profile()
    df_req = build_default_news_freshness_requirements(profile)
    assert len(df_req) >= 3
    df, summary = build_news_freshness_staleness_requirement_registry(profile)
    assert len(df) >= 3
    assert summary["total_requirements"] >= 3
