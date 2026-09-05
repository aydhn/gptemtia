from advanced_regime_foundation.regime_foundation_config import (
    RegimeFoundationProfile,
    get_regime_foundation_profile,
    list_regime_foundation_profiles,
    validate_regime_foundation_profiles,
    get_default_regime_foundation_profile,
)


def test_regime_foundation_config_defaults():
    profile = get_default_regime_foundation_profile()
    assert profile.current_phase == 126
    assert profile.target_final_phase == 160
    assert profile.next_phase == 127
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_regime_as_signal is False
    assert profile.allow_directional_claim is False
    assert profile.allow_strategy_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_clustering_execution is False
    assert profile.allow_target_label_generation is False
    assert profile.allow_prediction_generation is False
    assert profile.allow_official_approval_claim is False
    assert profile.allow_production_ready_claim is False
    assert profile.allow_broker_ready_claim is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_auto_destructive_cleaning is False
    assert profile.allow_file_deletion is False
    assert profile.allow_overwrite is False
    assert profile.allow_auto_imputation is False
    assert profile.allow_auto_feature_drop is False


def test_regime_foundation_profile_validation():
    assert validate_regime_foundation_profiles() is True
    profiles = list_regime_foundation_profiles()
    assert len(profiles) >= 3
    prof = get_regime_foundation_profile("strict_non_signal_regime_safety")
    assert prof.min_readiness_score == 0.60
