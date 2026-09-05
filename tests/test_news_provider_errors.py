import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_errors import (
    create_news_provider_error,
    news_provider_error_to_dict,
    build_news_provider_error_schema,
    summarize_news_provider_errors
)

def test_news_provider_errors():
    profile = get_default_news_provider_profile()
    err = create_news_provider_error("prov_1", "blocked_by_no_scraping_boundary", "Scraping blocked", blocked_by_safety=True)
    assert err.blocked_by_safety is True
    assert err.retryable is False

    df, summary = build_news_provider_error_schema(profile)
    assert len(df) >= 10
    assert summary["total_error_types"] >= 10
