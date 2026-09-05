import pytest
from advanced_regime_rule_free.regime_rule_free_config import (
    REGIME_RULE_FREE_PROFILES,
    get_regime_rule_free_profile,
    get_default_regime_rule_free_profile,
    list_regime_rule_free_profiles,
    validate_regime_rule_free_profiles,
)


def test_regime_rule_free_config_profiles_exist():
    profiles = list_regime_rule_free_profiles()
    assert len(profiles) >= 3
    assert "balanced_local_regime_rule_free_prep" in profiles
    assert "strict_non_signal_rule_free_safety" in profiles
    assert "dry_run_unsupervised_prep_contract_focus" in profiles


def test_regime_rule_free_config_invariants():
    default_p = get_default_regime_rule_free_profile()
    assert default_p.current_phase == 128
    assert default_p.target_final_phase == 160
    assert default_p.next_phase == 129
    assert default_p.dry_run_default is True
    assert default_p.local_only is True
    assert default_p.non_production is True
    assert default_p.research_only is True
    assert default_p.allow_live_trading is False
    assert default_p.allow_broker_integration is False
    assert default_p.allow_candidate_state_as_signal is False
    assert default_p.allow_pseudo_state_as_signal is False
    assert default_p.allow_clustering_execution is False
    assert default_p.allow_model_training is False
    assert default_p.allow_model_fit is False
    assert default_p.allow_model_predict is False
    assert default_p.allow_unsupervised_execution is False
    assert default_p.allow_dimensionality_reduction_execution is False
    assert default_p.allow_target_label_generation is False
    assert default_p.allow_prediction_generation is False
    assert default_p.allow_source_overwrite is False
    assert default_p.allow_auto_imputation is False
    assert default_p.allow_auto_feature_drop is False


def test_validate_regime_rule_free_profiles():
    validation_results = validate_regime_rule_free_profiles()
    assert all(validation_results.values())


def test_unknown_profile_raises_key_error():
    with pytest.raises(KeyError):
        get_regime_rule_free_profile("non_existent_profile")
