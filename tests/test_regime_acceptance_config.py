"""Test suite for Phase 135 Regime Acceptance Config."""

import pytest
from advanced_regime_acceptance.regime_acceptance_config import (
    RegimeAcceptanceProfile,
    get_regime_acceptance_profile,
    get_default_regime_acceptance_profile,
    list_regime_acceptance_profiles,
    validate_regime_acceptance_profiles,
    PROFILES,
)


def test_default_profile_properties():
    profile = get_default_regime_acceptance_profile()
    assert profile.profile_name == "balanced_local_regime_acceptance"
    assert profile.current_phase == 135
    assert profile.target_final_phase == 160
    assert profile.next_phase == 136
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True


def test_safety_and_non_signal_flags():
    for p in list_regime_acceptance_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_acceptance_as_signal is False
        assert p.allow_regime_as_signal is False
        assert p.allow_validation_as_signal is False
        assert p.allow_directional_claim is False
        assert p.allow_strategy_generation is False
        assert p.allow_backtest_execution is False
        assert p.allow_optimizer_execution is False
        assert p.allow_model_training is False
        assert p.allow_model_fit is False
        assert p.allow_model_predict is False
        assert p.allow_clustering_execution is False
        assert p.allow_unsupervised_execution is False
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
        assert p.allow_overwrite is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_profile_retrieval_and_validation():
    assert validate_regime_acceptance_profiles() is True
    p1 = get_regime_acceptance_profile("strict_non_signal_regime_block_acceptance")
    assert p1.min_score == 0.60
    with pytest.raises(KeyError):
        get_regime_acceptance_profile("non_existent_profile")
