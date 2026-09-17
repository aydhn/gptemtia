# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Configuration."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
    get_default_advanced_ml_acceptance_profile,
    list_advanced_ml_acceptance_profiles,
    validate_advanced_ml_acceptance_profiles,
    PROFILES,
)


def test_default_profile_attributes():
    prof = get_default_advanced_ml_acceptance_profile()
    assert prof.profile_name == "balanced_local_advanced_ml_acceptance"
    assert prof.current_phase == 145
    assert prof.target_final_phase == 160
    assert prof.next_phase == 146
    assert prof.dry_run_default is True
    assert prof.local_only is True
    assert prof.non_production is True
    assert prof.research_only is True


def test_negative_safety_guards_in_all_profiles():
    for p in list_advanced_ml_acceptance_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_signal_generation is False
        assert p.allow_directional_claim is False
        assert p.allow_strategy_generation is False
        assert p.allow_backtest_execution is False
        assert p.allow_walk_forward_execution is False
        assert p.allow_transaction_cost_calculation is False
        assert p.allow_slippage_calculation is False
        assert p.allow_benchmark_calculation is False
        assert p.allow_optimizer_execution is False
        assert p.allow_dataset_materialization is False
        assert p.allow_feature_snapshot_materialization is False
        assert p.allow_real_model_training is False
        assert p.allow_model_training is False
        assert p.allow_model_fit is False
        assert p.allow_model_predict is False
        assert p.allow_model_inference is False
        assert p.allow_model_transform is False
        assert p.allow_probability_prediction is False
        assert p.allow_calibration_execution is False
        assert p.allow_uncertainty_estimation is False
        assert p.allow_drift_calculation is False
        assert p.allow_explainability_calculation is False
        assert p.allow_feature_attribution_calculation is False
        assert p.allow_model_registry_write is False
        assert p.allow_artifact_persistence is False
        assert p.allow_model_deployment is False
        assert p.allow_production_deployment is False
        assert p.allow_production_approval is False
        assert p.allow_broker_ready_approval is False
        assert p.allow_live_trading_approval is False
        assert p.allow_official_approval_claim is False
        assert p.allow_production_ready_claim is False
        assert p.allow_broker_ready_claim is False
        assert p.allow_release_approval is False
        assert p.allow_real_audit_log is False
        assert p.allow_clustering_execution is False
        assert p.allow_unsupervised_execution is False
        assert p.allow_supervised_execution is False
        assert p.allow_ensemble_execution is False
        assert p.allow_target_label_generation is False
        assert p.allow_prediction_generation is False
        assert p.allow_metric_calculation is False
        assert p.allow_performance_claim is False
        assert p.allow_sentiment_model_output is False
        assert p.allow_full_article_usage is False
        assert p.allow_article_body_usage is False
        assert p.allow_raw_content_usage is False
        assert p.allow_scraped_html_usage is False
        assert p.allow_embedding_generation is False
        assert p.allow_vector_db is False
        assert p.allow_web_scraping is False
        assert p.allow_credential_output is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_destructive_cleaning is False
        assert p.allow_file_deletion is False
        assert p.allow_overwrite is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_validate_advanced_ml_acceptance_profiles():
    assert validate_advanced_ml_acceptance_profiles() is True
    with pytest.raises(KeyError):
        get_advanced_ml_acceptance_profile("non_existent_profile")
