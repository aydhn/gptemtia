import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_safety_boundary import (
    build_news_safety_boundary,
    build_news_no_go_conditions,
    build_news_safe_go_conditions,
    summarize_news_safety_boundary
)

def test_news_safety_boundary():
    profile = get_default_news_provider_profile()
    nogos = build_news_no_go_conditions(profile)
    assert len(nogos) >= 25
    assert "web scraping" in nogos["rule"].values
    assert "news page scraping" in nogos["rule"].values
    assert "full article download" in nogos["rule"].values

    safegos = build_news_safe_go_conditions(profile)
    assert len(safegos) >= 15

    df, summary = build_news_safety_boundary(profile)
    assert len(df) >= 40
    assert summary["no_go_rules_count"] >= 25
