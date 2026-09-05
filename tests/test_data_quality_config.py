import pytest
from advanced_data_quality.data_quality_config import (
    DataQualityProfile,
    get_data_quality_profile,
    list_data_quality_profiles,
    validate_data_quality_profiles,
    get_default_data_quality_profile,
    ConfigError
)


def test_data_quality_config_profiles():
    profiles = list_data_quality_profiles()
    assert len(profiles) >= 3
    names = [p.name for p in profiles]
    assert "balanced_local_data_quality" in names
    assert "strict_data_quality_safety" in names
    assert "dry_run_quality_contract_focus" in names


def test_default_data_quality_profile():
    p = get_default_data_quality_profile()
    assert p.name == "balanced_local_data_quality"
    assert p.current_phase == 112
    assert p.target_final_phase == 160
    assert p.next_phase == 113
    assert p.dry_run is True
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False
    assert p.allow_web_scraping is False
    assert p.allow_auto_overwrite_cleaning is False
    assert p.allow_credential_output is False


def test_validate_data_quality_profiles():
    # Calling validate should succeed without raising ConfigError
    validate_data_quality_profiles()


def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_data_quality_profile("non_existent_profile_xyz")
