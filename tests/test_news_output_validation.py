import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_output_validation import (
    build_news_output_validation_contract,
    build_default_news_output_validation_rules,
    summarize_news_output_validation
)

def test_news_output_validation():
    profile = get_default_news_provider_profile()
    rules = build_default_news_output_validation_rules(profile)
    assert len(rules) >= 7
    df, summary = build_news_output_validation_contract(profile)
    assert len(df) >= 7
    assert summary["total_rules"] >= 7
