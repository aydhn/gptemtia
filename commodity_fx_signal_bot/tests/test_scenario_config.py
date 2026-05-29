import pytest
from scenarios.scenario_config import (
    ScenarioProfile, get_scenario_profile, get_default_scenario_profile,
    list_scenario_profiles, validate_scenario_profiles, ConfigError
)

def test_validate_scenario_profiles():
    validate_scenario_profiles()

def test_get_default_scenario_profile():
    profile = get_default_scenario_profile()
    assert profile.name == "balanced_offline_scenarios"
    assert profile.max_symbols > 0
    assert profile.max_rows_per_symbol > 0
    assert profile.use_synthetic_data_only is True
    assert profile.allow_real_market_download is False
    assert profile.allow_live_commands is False
    assert profile.allow_broker_commands is False
    assert profile.allow_deploy_commands is False
    assert profile.allow_background_daemons is False

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_scenario_profile("non_existent_profile")
