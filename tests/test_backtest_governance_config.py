# -*- coding: utf-8 -*-
"""Phase 150 Unit Tests: Backtest Governance Configuration and Profiles."""

import pytest
from advanced_backtest_governance.backtest_governance_config import (
    BacktestGovernanceProfile,
    get_backtest_governance_profile,
    list_backtest_governance_profiles,
    validate_backtest_governance_profiles,
    get_default_backtest_governance_profile,
    PROFILES,
)


def test_default_backtest_governance_profile():
    profile = get_default_backtest_governance_profile()
    assert profile.profile_name == "balanced_local_backtest_governance_contracts"
    assert profile.current_phase == 150
    assert profile.target_final_phase == 160
    assert profile.next_phase == 151
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_signal_generation is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_benchmark_execution is False
    assert profile.allow_metric_calculation is False
    assert profile.allow_result_claim is False
    assert profile.allow_performance_claim is False
    assert profile.allow_strategy_approval is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_model_training is False
    assert profile.allow_model_predict is False


def test_list_and_get_backtest_governance_profiles():
    profiles = list_backtest_governance_profiles()
    assert len(profiles) >= 3
    for prof in profiles:
        assert prof.current_phase == 150
        assert prof.allow_live_trading is False
        assert prof.allow_backtest_execution is False


def test_validate_backtest_governance_profiles():
    assert validate_backtest_governance_profiles() is True
    assert len(PROFILES) >= 3


def test_invalid_profile_lookup():
    with pytest.raises(KeyError):
        get_backtest_governance_profile("non_existent_profile_xyz")
