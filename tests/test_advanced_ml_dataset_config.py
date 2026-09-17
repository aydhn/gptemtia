"""Test suite for Phase 137 Advanced ML Dataset Configuration."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_advanced_ml_dataset_profile,
    get_default_advanced_ml_dataset_profile,
    list_advanced_ml_dataset_profiles,
    validate_advanced_ml_dataset_profiles,
)


def test_default_profile_properties():
    profile = get_default_advanced_ml_dataset_profile()
    assert profile.name == "balanced_local_ml_dataset_contracts"
    assert profile.current_phase == 137
    assert profile.target_final_phase == 160
    assert profile.next_phase == 138
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True


def test_all_profiles_prohibit_live_and_materialization():
    for p in list_advanced_ml_dataset_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_signal_generation is False
        assert p.allow_directional_claim is False
        assert p.allow_dataset_materialization is False
        assert p.allow_feature_snapshot_materialization is False
        assert p.allow_model_training is False
        assert p.allow_model_fit is False
        assert p.allow_model_predict is False
        assert p.allow_model_inference is False
        assert p.allow_model_transform is False
        assert p.allow_clustering_execution is False
        assert p.allow_unsupervised_execution is False
        assert p.allow_ensemble_execution is False
        assert p.allow_calibration_execution is False
        assert p.allow_target_label_generation is False
        assert p.allow_prediction_generation is False
        assert p.allow_sentiment_model_output is False
        assert p.allow_full_article_usage is False
        assert p.allow_article_body_usage is False
        assert p.allow_raw_content_usage is False
        assert p.allow_scraped_html_usage is False
        assert p.allow_embedding_generation is False
        assert p.allow_vector_db is False
        assert p.allow_artifact_persistence is False
        assert p.allow_model_registry_write is False
        assert p.allow_official_approval_claim is False
        assert p.allow_production_ready_claim is False
        assert p.allow_broker_ready_claim is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_destructive_cleaning is False
        assert p.allow_file_deletion is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_validate_advanced_ml_dataset_profiles():
    res = validate_advanced_ml_dataset_profiles()
    assert res["valid"] is True
    assert res["profile_count"] >= 3
