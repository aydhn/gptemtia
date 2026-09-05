import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_sentiment_requirements import (
    build_news_sentiment_placeholder_requirement_registry,
    build_default_news_sentiment_requirements,
    summarize_news_sentiment_requirements
)

def test_news_sentiment_requirements():
    profile = get_default_news_provider_profile()
    df_req = build_default_news_sentiment_requirements(profile)
    assert len(df_req) >= 5
    df, summary = build_news_sentiment_placeholder_requirement_registry(profile)
    assert len(df) >= 5
    assert "positive_placeholder" in summary["allowed_values"]
