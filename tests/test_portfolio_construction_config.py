# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Construction Configuration."""

import pytest
from advanced_portfolio_construction.portfolio_construction_config import (
    PortfolioConstructionProfile,
    get_portfolio_construction_profile,
    get_default_portfolio_construction_profile,
    list_portfolio_construction_profiles,
    validate_portfolio_construction_profiles,
    PORTFOLIO_CONSTRUCTION_PROFILES,
)


def test_default_portfolio_construction_profile():
    profile = get_default_portfolio_construction_profile()
    assert profile.profile_name == "balanced_local_portfolio_construction_contracts"
    assert profile.current_phase == 153
    assert profile.target_final_phase == 160
    assert profile.next_phase == 154
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_portfolio_construction is False
    assert profile.allow_position_sizing is False
    assert profile.allow_capital_allocation is False
    assert profile.allow_weight_generation is False
    assert profile.allow_order_generation is False
    assert profile.allow_optimizer_execution is False
    assert profile.allow_metric_calculation is False


def test_list_portfolio_construction_profiles():
    profiles = list_portfolio_construction_profiles(enabled_only=True)
    assert len(profiles) >= 3
    names = [p.profile_name for p in profiles]
    assert "balanced_local_portfolio_construction_contracts" in names
    assert "strict_non_production_portfolio_risk_budget_safety" in names
    assert "dry_run_phase_153_sizing_contracts_focus" in names


def test_get_portfolio_construction_profile_by_name():
    prof = get_portfolio_construction_profile("strict_non_production_portfolio_risk_budget_safety")
    assert prof.min_readiness_score == 0.65
    with pytest.raises(KeyError):
        get_portfolio_construction_profile("non_existent_profile")


def test_validate_portfolio_construction_profiles():
    assert validate_portfolio_construction_profiles() is True


def test_invalid_profile_fails_validation():
    invalid_profile = PortfolioConstructionProfile(
        profile_name="invalid_test_profile",
        description="Invalid profile for testing",
        allow_live_trading=True,
    )
    test_dict = {"invalid": invalid_profile}
    with pytest.raises(ValueError):
        validate_portfolio_construction_profiles(test_dict)
