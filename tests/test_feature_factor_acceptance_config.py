from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_feature_factor_acceptance_profile,
    list_feature_factor_acceptance_profiles,
    validate_feature_factor_acceptance_profiles,
    get_default_feature_factor_acceptance_profile,
)

def test_feature_factor_acceptance_config_defaults():
    profile = get_default_feature_factor_acceptance_profile()
    assert profile.current_phase == 125
    assert profile.target_final_phase == 160
    assert profile.next_phase == 126
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_acceptance_as_signal is False
    assert profile.allow_directional_claim is False
    assert profile.allow_strategy_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_target_label_generation is False
    assert profile.allow_prediction_generation is False
    assert profile.allow_full_article_usage is False
    assert profile.allow_official_approval_claim is False
    assert profile.allow_production_ready_claim is False
    assert profile.allow_broker_ready_claim is False
    assert profile.allow_model_deployment is False
    assert profile.allow_production_deployment is False
    assert profile.allow_web_scraping is False
    assert profile.allow_credential_output is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_auto_destructive_cleaning is False
    assert profile.allow_file_deletion is False
    assert profile.allow_overwrite is False
    assert profile.allow_auto_imputation is False
    assert profile.allow_auto_feature_drop is False


def test_feature_factor_acceptance_profile_validation():
    assert validate_feature_factor_acceptance_profiles() is True
    profiles = list_feature_factor_acceptance_profiles()
    assert len(profiles) >= 3
    prof = get_feature_factor_acceptance_profile("strict_non_signal_acceptance_safety")
    assert prof.min_score == 0.60
