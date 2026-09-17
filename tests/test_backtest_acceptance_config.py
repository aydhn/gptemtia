# -*- coding: utf-8 -*-
"""Unit tests for Phase 152 Backtest Acceptance Configuration."""

import pytest
from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
    get_default_backtest_acceptance_profile,
    list_backtest_acceptance_profiles,
    validate_backtest_acceptance_profiles,
    PROFILES,
)


def test_default_profile():
    profile = get_default_backtest_acceptance_profile()
    assert profile.profile_name == "balanced_local_backtest_acceptance_contracts"
    assert profile.current_phase == 152
    assert profile.target_final_phase == 160
    assert profile.next_phase == 153
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_benchmark_execution is False
    assert profile.allow_metric_calculation is False
    assert profile.allow_strategy_approval is False
    assert profile.allow_portfolio_construction is False
    assert profile.allow_position_sizing is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_model_predict is False
    assert profile.allow_web_scraping is False
    assert profile.allow_credential_output is False
    assert profile.allow_source_overwrite is False


def test_list_and_get_profile():
    profiles = list_backtest_acceptance_profiles()
    assert len(profiles) >= 3
    p = get_backtest_acceptance_profile("strict_non_production_backtest_acceptance_safety")
    assert p.profile_name == "strict_non_production_backtest_acceptance_safety"

    with pytest.raises(KeyError):
        get_backtest_acceptance_profile("non_existent_profile")


def test_validate_profiles():
    assert validate_backtest_acceptance_profiles() is True
