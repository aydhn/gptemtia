import pytest
from advanced_data_normalization.data_normalization_config import (
    get_data_normalization_profile,
    list_data_normalization_profiles,
    validate_data_normalization_profiles,
    get_default_data_normalization_profile,
    ConfigError,
)


def test_default_profile():
    p = get_default_data_normalization_profile()
    assert p.name == "balanced_non_destructive_normalization"
    assert p.current_phase == 113
    assert p.target_final_phase == 160
    assert p.next_phase == 114
    assert p.dry_run_default is True
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False
    assert p.allow_broker_integration is False
    assert p.allow_source_overwrite is False
    assert p.allow_auto_destructive_cleaning is False
    assert p.allow_web_scraping is False
    assert p.allow_full_article_download is False
    assert p.allow_copyrighted_article_copy is False


def test_list_and_validate_profiles():
    profiles = list_data_normalization_profiles()
    assert len(profiles) >= 3
    validate_data_normalization_profiles()


def test_strict_safety_profile():
    p = get_data_normalization_profile("strict_non_destructive_normalization_safety")
    assert p.min_normalization_score == 0.65
    assert p.allow_live_trading is False


def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_data_normalization_profile("non_existent_profile_xyz")
