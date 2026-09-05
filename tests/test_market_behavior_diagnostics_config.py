import pytest
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES,
    get_market_behavior_diagnostics_profile,
    get_default_market_behavior_diagnostics_profile,
    list_market_behavior_diagnostics_profiles,
    validate_market_behavior_diagnostics_profiles,
)


def test_market_behavior_diagnostics_config_profiles_exist():
    profiles = list_market_behavior_diagnostics_profiles()
    assert len(profiles) >= 3
    assert "balanced_local_market_behavior_diagnostics" in profiles
    assert "strict_non_signal_behavior_quality_safety" in profiles
    assert "dry_run_behavior_diagnostics_focus" in profiles


def test_market_behavior_diagnostics_config_invariants():
    default_p = get_default_market_behavior_diagnostics_profile()
    assert default_p.current_phase == 129
    assert default_p.target_final_phase == 160
    assert default_p.next_phase == 130
    assert default_p.dry_run_default is True
    assert default_p.local_only is True
    assert default_p.non_production is True
    assert default_p.research_only is True
    assert default_p.allow_live_trading is False
    assert default_p.allow_broker_integration is False
    assert default_p.allow_quality_as_signal is False
    assert default_p.allow_behavior_as_signal is False
    assert default_p.allow_candidate_state_as_signal is False
    assert default_p.allow_clustering_execution is False
    assert default_p.allow_model_training is False
    assert default_p.allow_model_fit is False
    assert default_p.allow_model_predict is False
    assert default_p.allow_unsupervised_execution is False
    assert default_p.allow_target_label_generation is False
    assert default_p.allow_prediction_generation is False
    assert default_p.allow_source_overwrite is False
    assert default_p.allow_auto_imputation is False
    assert default_p.allow_auto_feature_drop is False


def test_validate_market_behavior_diagnostics_profiles():
    assert validate_market_behavior_diagnostics_profiles() is True



def test_unknown_profile_raises_key_error():
    with pytest.raises(KeyError):
        get_market_behavior_diagnostics_profile("non_existent_profile")
