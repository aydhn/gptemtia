"""Test suite for Phase 136 GPU ML Runtime Configuration."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import (
    GpuMlRuntimeProfile,
    get_gpu_ml_runtime_profile,
    get_default_gpu_ml_runtime_profile,
    list_gpu_ml_runtime_profiles,
    validate_gpu_ml_runtime_profiles,
    PROFILES,
)


def test_default_profile_properties():
    profile = get_default_gpu_ml_runtime_profile()
    assert profile.profile_name == "balanced_local_gpu_ml_runtime_foundation"
    assert profile.current_phase == 136
    assert profile.target_final_phase == 160
    assert profile.next_phase == 137
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True


def test_all_profiles_prohibit_live_and_models():
    for p in list_gpu_ml_runtime_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_directional_claim is False
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
        assert p.allow_official_approval_claim is False
        assert p.allow_production_ready_claim is False
        assert p.allow_broker_ready_claim is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_destructive_cleaning is False
        assert p.allow_file_deletion is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_profile_retrieval_and_validation():
    p1 = get_gpu_ml_runtime_profile("balanced_local_gpu_ml_runtime_foundation")
    assert p1.profile_name == "balanced_local_gpu_ml_runtime_foundation"

    p2 = get_gpu_ml_runtime_profile("strict_no_training_gpu_runtime_safety")
    assert p2.profile_name == "strict_no_training_gpu_runtime_safety"

    p3 = get_gpu_ml_runtime_profile("dry_run_ml_capability_discovery_focus")
    assert p3.profile_name == "dry_run_ml_capability_discovery_focus"

    assert validate_gpu_ml_runtime_profiles() is True
