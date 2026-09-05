import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_impact_requirements import (
    build_news_impact_placeholder_requirement_registry,
    build_default_news_impact_requirements,
    summarize_news_impact_requirements
)

def test_news_impact_requirements():
    profile = get_default_news_provider_profile()
    df_req = build_default_news_impact_requirements(profile)
    assert len(df_req) >= 5
    df, summary = build_news_impact_placeholder_requirement_registry(profile)
    assert len(df) >= 5
    assert summary["total_requirements"] >= 5
