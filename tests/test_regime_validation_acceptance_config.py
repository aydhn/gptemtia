"""Tests for Phase 133 Regime Validation Acceptance Config."""

import pytest
from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    RegimeValidationAcceptanceProfile,
    get_regime_validation_acceptance_profile,
    get_default_regime_validation_acceptance_profile,
    list_regime_validation_acceptance_profiles,
    validate_regime_validation_acceptance_profiles,
    PROFILES,
)


def test_config_profiles_invariants():
    assert validate_regime_validation_acceptance_profiles() is True

    profiles = list_regime_validation_acceptance_profiles()
    assert len(profiles) >= 3

    for p in profiles:
        assert p.current_phase == 133
        assert p.target_final_phase == 160
        assert p.next_phase == 134
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert p.dry_run_default is True
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_acceptance_as_signal is False
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
        assert p.allow_model_deployment is False
        assert p.allow_production_deployment is False
        assert p.allow_web_scraping is False
        assert p.allow_credential_output is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_destructive_cleaning is False
        assert p.allow_file_deletion is False
        assert p.allow_overwrite is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_get_profile():
    default_p = get_default_regime_validation_acceptance_profile()
    assert default_p.profile_name == "balanced_local_regime_validation_acceptance"

    strict_p = get_regime_validation_acceptance_profile("strict_no_lookahead_metadata_only_acceptance")
    assert strict_p.min_acceptance_score == 0.60

    with pytest.raises(ValueError):
        get_regime_validation_acceptance_profile("non_existent_profile")
