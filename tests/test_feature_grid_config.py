import pytest
from advanced_feature_grid.feature_grid_config import (
    FeatureGridProfile,
    get_feature_grid_profile,
    list_feature_grid_profiles,
    validate_feature_grid_profiles,
    get_default_feature_grid_profile,
    FeatureGridConfigError,
)


def test_feature_grid_config_profiles():
    profiles = list_feature_grid_profiles()
    assert len(profiles) >= 3

    for p in profiles:
        assert p.current_phase == 118
        assert p.target_final_phase == 160
        assert p.next_phase == 119
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert p.dry_run_default is True
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_feature_grid_as_signal is False
        assert p.allow_directional_claim is False
        assert p.allow_strategy_generation is False
        assert p.allow_backtest_execution is False
        assert p.allow_optimizer_execution is False
        assert p.allow_target_label_generation is False
        assert p.allow_prediction_generation is False
        assert p.allow_web_scraping is False
        assert p.allow_credential_output is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_destructive_cleaning is False

    validate_feature_grid_profiles()


def test_feature_grid_default_profile():
    p = get_default_feature_grid_profile()
    assert p.name == "balanced_local_multi_window_feature_grid"
    assert p.enabled is True


def test_feature_grid_unknown_profile():
    with pytest.raises(FeatureGridConfigError):
        get_feature_grid_profile("non_existent_profile_xyz")
