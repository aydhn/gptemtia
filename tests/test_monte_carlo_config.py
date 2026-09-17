# -*- coding: utf-8 -*-
"""Phase 149 Unit Tests: Monte Carlo Configuration and Profiles."""

import pytest
from advanced_monte_carlo_robustness.monte_carlo_config import (
    MonteCarloProfile,
    get_monte_carlo_profile,
    list_monte_carlo_profiles,
    validate_monte_carlo_profiles,
    get_default_monte_carlo_profile,
    PROFILES,
)


def test_default_monte_carlo_profile():
    profile = get_default_monte_carlo_profile()
    assert profile.profile_name == "balanced_local_monte_carlo_robustness_contracts"
    assert profile.current_phase == 149
    assert profile.target_final_phase == 160
    assert profile.next_phase == 150
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_real_order is False
    assert profile.allow_investment_advice is False
    assert profile.allow_signal_generation is False
    assert profile.allow_monte_carlo_execution is False
    assert profile.allow_bootstrap_execution is False
    assert profile.allow_resampling_execution is False
    assert profile.allow_parameter_optimization is False
    assert profile.allow_parameter_sweep_execution is False
    assert profile.allow_metric_calculation is False


def test_list_and_get_monte_carlo_profiles():
    profiles = list_monte_carlo_profiles()
    assert len(profiles) >= 3
    for prof in profiles:
        assert prof.current_phase == 149
        assert prof.allow_live_trading is False
        assert prof.allow_monte_carlo_execution is False


def test_validate_monte_carlo_profiles():
    assert validate_monte_carlo_profiles() is True
    assert len(PROFILES) >= 3


def test_invalid_profile_lookup():
    with pytest.raises(KeyError):
        get_monte_carlo_profile("non_existent_profile_xyz")

