"""Test suite for Phase 138 Baseline ML Model Configuration."""

import pytest
from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_baseline_ml_model_profile,
    get_default_baseline_ml_model_profile,
    list_baseline_ml_model_profiles,
    validate_baseline_ml_model_profiles,
)


def test_default_profile_properties():
    profile = get_default_baseline_ml_model_profile()
    assert profile.name == "balanced_local_baseline_ml_contracts"
    assert profile.current_phase == 138
    assert profile.target_final_phase == 160
    assert profile.next_phase == 139
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True


def test_all_profiles_prohibit_live_and_real_training():
    for name in list_baseline_ml_model_profiles():
        p = get_baseline_ml_model_profile(name)
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_signal_generation is False
        assert p.allow_directional_claim is False
        assert p.allow_real_model_training is False
        assert p.allow_model_fit is False
        assert p.allow_model_predict is False
        assert p.allow_model_inference is False
        assert p.allow_target_label_generation is False
        assert p.allow_prediction_generation is False
        assert p.allow_artifact_persistence is False
        assert p.allow_model_registry_write is False

        assert p.allow_sentiment_model_output is False
        assert p.allow_full_article_usage is False
        assert p.allow_article_body_usage is False
        assert p.allow_raw_content_usage is False
        assert p.allow_scraped_html_usage is False
        assert p.allow_embedding_generation is False
        assert p.allow_vector_db is False
        assert p.allow_auto_destructive_cleaning is False
        assert p.allow_file_deletion is False
        assert p.allow_source_overwrite is False



def test_list_and_get_profiles():
    names = list_baseline_ml_model_profiles()
    assert len(names) == 3
    assert "balanced_local_baseline_ml_contracts" in names
    assert "strict_no_real_training_baseline_safety" in names
    assert "dry_run_harness_contract_focus" in names

    p1 = get_baseline_ml_model_profile("dry_run_harness_contract_focus")
    assert p1.name == "dry_run_harness_contract_focus"

    # Fallback to default
    p_fallback = get_baseline_ml_model_profile("non_existent_profile_xyz")
    assert p_fallback.name == "balanced_local_baseline_ml_contracts"


def test_validate_profiles():
    assert validate_baseline_ml_model_profiles() is True
