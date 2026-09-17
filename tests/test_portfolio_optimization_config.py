# -*- coding: utf-8 -*-
"""Unit tests for Phase 154 Portfolio Optimization Configuration."""

import pytest
from advanced_portfolio_optimization.portfolio_optimization_config import (
    PortfolioOptimizationProfile,
    get_portfolio_optimization_profile,
    get_default_portfolio_optimization_profile,
    list_portfolio_optimization_profiles,
    validate_portfolio_optimization_profiles,
    PORTFOLIO_OPTIMIZATION_PROFILES,
)


def test_default_portfolio_optimization_profile():
    profile = get_default_portfolio_optimization_profile()
    assert profile.profile_name == "balanced_local_portfolio_optimization_contracts"
    assert profile.current_phase == 154
    assert profile.target_final_phase == 160
    assert profile.next_phase == 155
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_portfolio_optimization is False
    assert profile.allow_weight_generation is False
    assert profile.allow_capital_allocation is False
    assert profile.allow_rebalance_generation is False
    assert profile.allow_order_generation is False
    assert profile.allow_solver_execution is False
    assert profile.allow_metric_calculation is False


def test_list_portfolio_optimization_profiles():
    profiles = list_portfolio_optimization_profiles(enabled_only=True)
    assert len(profiles) >= 3
    names = [p.profile_name for p in profiles]
    assert "balanced_local_portfolio_optimization_contracts" in names
    assert "strict_non_production_portfolio_optimization_safety" in names
    assert "dry_run_phase_154_allocation_constraints_focus" in names


def test_get_portfolio_optimization_profile_by_name():
    prof = get_portfolio_optimization_profile("strict_non_production_portfolio_optimization_safety")
    assert prof.min_readiness_score == 0.65
    with pytest.raises(KeyError):
        get_portfolio_optimization_profile("non_existent_profile")


def test_validate_portfolio_optimization_profiles():
    assert validate_portfolio_optimization_profiles() is True


def test_invalid_profile_fails_validation():
    invalid_profile = PortfolioOptimizationProfile(
        profile_name="invalid_test_profile",
        description="Invalid profile for testing",
        current_phase=154,
        next_phase=155,
        target_final_phase=160,
        allow_live_trading=True,  # VIOLATION
    )
    with pytest.raises(ValueError):
        invalid_profile.validate()
