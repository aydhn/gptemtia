import pytest
from advanced_feature_engine.feature_engine_config import (
    FeatureEngineProfile,
    get_feature_engine_profile,
    list_feature_engine_profiles,
    validate_feature_engine_profiles,
    get_default_feature_engine_profile,
    ConfigError,
)


def test_feature_engine_config_profiles():
    profiles = list_feature_engine_profiles()
    assert len(profiles) >= 3

    default_p = get_default_feature_engine_profile()
    assert default_p.name == "balanced_local_feature_engine"
    assert default_p.current_phase == 116
    assert default_p.target_final_phase == 160
    assert default_p.next_phase == 117
    assert default_p.dry_run_default is True
    assert default_p.local_only is True
    assert default_p.non_production is True
    assert default_p.research_only is True
    assert default_p.allow_live_trading is False
    assert default_p.allow_broker_integration is False
    assert default_p.allow_feature_as_signal is False
    assert default_p.allow_indicator_directional_claim is False
    assert default_p.allow_strategy_generation is False
    assert default_p.allow_backtest_execution is False
    assert default_p.allow_optimizer_execution is False

    # Validate all profiles without error
    validate_feature_engine_profiles()


def test_feature_engine_config_error():
    with pytest.raises(ConfigError):
        get_feature_engine_profile("non_existent_profile_xyz")
