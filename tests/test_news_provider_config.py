import pytest
from advanced_news_metadata.news_provider_config import (
    NewsProviderProfile,
    get_news_provider_profile,
    list_news_provider_profiles,
    validate_news_provider_profiles,
    get_default_news_provider_profile
)

def test_news_provider_config_profiles():
    profiles = list_news_provider_profiles()
    assert len(profiles) >= 3
    profile_names = [p.name for p in profiles]
    assert "balanced_no_scraping_news_metadata_provider" in profile_names
    assert "strict_news_metadata_safety" in profile_names
    assert "news_metadata_dry_run_fixture_focus" in profile_names

def test_default_news_provider_profile():
    p = get_default_news_provider_profile()
    assert p.dry_run is True
    assert p.local_only is True
    assert p.no_scraping is True
    assert p.metadata_only is True
    assert p.current_phase == 111
    assert p.next_phase == 112
    assert p.target_final_phase == 160

def test_validate_news_provider_profiles():
    res = validate_news_provider_profiles()
    assert res["valid"] is True
    assert len(res["errors"]) == 0
