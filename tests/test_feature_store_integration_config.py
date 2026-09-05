import pytest
from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_feature_store_integration_profile,
    list_feature_store_integration_profiles,
    validate_feature_store_integration_profiles,
    get_default_feature_store_integration_profile,
)

def test_feature_store_integration_config_invariants():
    validate_feature_store_integration_profiles()
    default_prof = get_default_feature_store_integration_profile()
    assert default_prof.current_phase == 124
    assert default_prof.target_final_phase == 160
    assert default_prof.next_phase == 125
    assert default_prof.dry_run_default is True
    assert default_prof.local_only is True
    assert default_prof.non_production is True
    assert default_prof.research_only is True
    assert default_prof.allow_live_trading is False
    assert default_prof.allow_broker_integration is False
    assert default_prof.allow_store_as_signal is False
    assert default_prof.allow_directional_claim is False
    assert default_prof.allow_strategy_generation is False
    assert default_prof.allow_backtest_execution is False
    assert default_prof.allow_optimizer_execution is False
    assert default_prof.allow_model_training is False
    assert default_prof.allow_target_label_generation is False
    assert default_prof.allow_prediction_generation is False
    assert default_prof.allow_official_approval_claim is False
    assert default_prof.allow_production_ready_claim is False
    assert default_prof.allow_broker_ready_claim is False
    assert default_prof.allow_auto_imputation is False
    assert default_prof.allow_auto_feature_drop is False
    assert default_prof.allow_source_overwrite is False
    assert default_prof.allow_web_scraping is False

def test_get_and_list_profiles():
    profiles = list_feature_store_integration_profiles()
    assert len(profiles) >= 3
    p = get_feature_store_integration_profile("strict_non_signal_feature_store_safety")
    assert p.name == "strict_non_signal_feature_store_safety"
    with pytest.raises(KeyError):
        get_feature_store_integration_profile("non_existent_profile")
