import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_capability_matcher import (
    build_news_provider_capability_matcher_report,
    match_news_provider_capabilities,
    summarize_news_provider_capability_matcher
)
from advanced_news_metadata.news_provider_capabilities import build_news_provider_capability_registry

def test_news_provider_capability_matcher():
    profile = get_default_news_provider_profile()
    cap_df, _ = build_news_provider_capability_registry(profile)
    matched = match_news_provider_capabilities("news_data_metadata", "central_bank", "US", cap_df)
    assert not matched.empty
    df, summary = build_news_provider_capability_matcher_report(profile)
    assert summary["matched_capabilities_count"] > 0
