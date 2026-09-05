import pytest
from advanced_news_metadata.news_provider_config import get_default_news_provider_profile
from advanced_news_metadata.news_provider_preference_resolver import (
    build_news_provider_preference_resolver_report,
    resolve_news_provider_preferences_from_config_profiles,
    summarize_news_provider_preference_resolver
)

def test_news_provider_preference_resolver():
    profile = get_default_news_provider_profile()
    df_pref = resolve_news_provider_preferences_from_config_profiles(profile)
    assert len(df_pref) >= 10
    df, summary = build_news_provider_preference_resolver_report(profile)
    assert len(df) >= 10
    assert summary["total_preferences"] >= 10
