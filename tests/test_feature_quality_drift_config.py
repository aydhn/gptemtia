import pytest
from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
    get_feature_quality_drift_profile,
    list_feature_quality_drift_profiles,
    validate_feature_quality_drift_profiles,
)


def test_feature_quality_drift_config_invariants():
    validate_feature_quality_drift_profiles()
    profile = get_default_feature_quality_drift_profile()

    assert profile.current_phase == 123
    assert profile.target_final_phase == 160
    assert profile.next_phase == 124
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True

    # Safety invariants
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_quality_as_signal is False
    assert profile.allow_drift_as_signal is False
    assert profile.allow_directional_claim is False
    assert profile.allow_strategy_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_target_label_generation is False
    assert profile.allow_prediction_generation is False
    assert profile.allow_official_approval_claim is False
    assert profile.allow_production_ready_claim is False
    assert profile.allow_auto_imputation is False
    assert profile.allow_auto_feature_drop is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_auto_destructive_cleaning is False
    assert profile.allow_web_scraping is False
    assert profile.allow_credential_output is False


def test_feature_quality_drift_profile_lookup():
    profiles = list_feature_quality_drift_profiles()
    assert len(profiles) >= 3

    p1 = get_feature_quality_drift_profile("balanced_local_feature_quality_drift")
    assert p1.name == "balanced_local_feature_quality_drift"

    p2 = get_feature_quality_drift_profile("unknown_profile_fallback")
    assert p2.name == "balanced_local_feature_quality_drift"
