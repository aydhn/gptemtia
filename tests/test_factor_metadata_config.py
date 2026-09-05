import pytest
from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
    get_factor_metadata_profile,
    list_factor_metadata_profiles,
    validate_factor_metadata_profiles,
)


def test_factor_metadata_config_defaults():
    profile = get_default_factor_metadata_profile()
    assert profile.name == "balanced_local_factor_metadata"
    assert profile.current_phase == 122
    assert profile.target_final_phase == 160
    assert profile.next_phase == 123
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_factor_as_signal is False
    assert profile.allow_directional_claim is False
    assert profile.allow_strategy_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_target_label_generation is False
    assert profile.allow_prediction_generation is False
    assert profile.allow_sentiment_model_output is False
    assert profile.allow_full_article_usage is False
    assert profile.allow_official_approval_claim is False
    assert profile.allow_production_ready_claim is False
    assert profile.allow_web_scraping is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_auto_destructive_cleaning is False
    assert profile.allow_file_deletion is False
    assert profile.allow_file_move is False
    assert profile.allow_overwrite is False


def test_list_and_get_profiles():
    profiles = list_factor_metadata_profiles()
    assert len(profiles) >= 3
    names = [p.name for p in profiles]
    assert "balanced_local_factor_metadata" in names
    assert "strict_non_signal_factor_metadata" in names
    assert "dry_run_factor_contract_focus" in names

    prof = get_factor_metadata_profile("strict_non_signal_factor_metadata")
    assert prof.name == "strict_non_signal_factor_metadata"


def test_validate_factor_metadata_profiles():
    # Should not raise any ValueError
    validate_factor_metadata_profiles()
