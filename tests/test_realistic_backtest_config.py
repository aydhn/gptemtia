# -*- coding: utf-8 -*-
"""Unit tests for Phase 146: Realistic Backtest Configuration."""

import pytest
from advanced_realistic_backtest.realistic_backtest_config import (
    RealisticBacktestProfile,
    get_default_realistic_backtest_profile,
    get_realistic_backtest_profile,
    list_realistic_backtest_profiles,
    validate_realistic_backtest_profiles,
    PROFILES,
)


def test_default_profile_attributes():
    prof = get_default_realistic_backtest_profile()
    assert prof.profile_name == "balanced_local_realistic_backtest_contracts"
    assert prof.current_phase == 146
    assert prof.target_final_phase == 160
    assert prof.next_phase == 147
    assert prof.dry_run_default is True
    assert prof.local_only is True
    assert prof.non_production is True
    assert prof.research_only is True


def test_negative_safety_invariants_all_profiles():
    for p in list_realistic_backtest_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_signal_generation is False
        assert p.allow_directional_claim is False
        assert p.allow_optimizer_execution is False
        assert p.allow_walk_forward_execution is False
        assert p.allow_benchmark_execution is False
        assert p.allow_stress_test_execution is False
        assert p.allow_monte_carlo_execution is False
        assert p.allow_model_training is False
        assert p.allow_model_predict is False
        assert p.allow_target_label_generation is False
        assert p.allow_performance_claim is False
        assert p.allow_full_article_usage is False
        assert p.allow_article_body_usage is False
        assert p.allow_source_overwrite is False


def test_validate_realistic_backtest_profiles():
    assert validate_realistic_backtest_profiles() is True
    with pytest.raises(KeyError):
        get_realistic_backtest_profile("unknown_profile_xyz")
