# -*- coding: utf-8 -*-
"""Unit tests for Phase 148: Stress Testing Configuration."""

import pytest
from advanced_stress_testing.stress_testing_config import (
    StressTestingProfile,
    get_default_stress_testing_profile,
    get_stress_testing_profile,
    list_stress_testing_profiles,
    validate_stress_testing_profiles,
    PROFILES,
)


def test_default_profile_attributes():
    prof = get_default_stress_testing_profile()
    assert prof.profile_name == "balanced_local_stress_testing_contracts"
    assert prof.current_phase == 148
    assert prof.target_final_phase == 160
    assert prof.next_phase == 149
    assert prof.dry_run_default is True
    assert prof.local_only is True
    assert prof.non_production is True
    assert prof.research_only is True


def test_negative_safety_invariants_all_profiles():
    for p in list_stress_testing_profiles():
        assert p.allow_live_trading is False
        assert p.allow_broker_integration is False
        assert p.allow_real_order is False
        assert p.allow_investment_advice is False
        assert p.allow_signal_generation is False
        assert p.allow_directional_claim is False
        assert p.allow_stress_test_execution is False
        assert p.allow_scenario_simulation_execution is False
        assert p.allow_monte_carlo_execution is False
        assert p.allow_optimizer_execution is False
        assert p.allow_metric_calculation is False
        assert p.allow_stress_metric_calculation is False
        assert p.allow_scenario_metric_calculation is False
        assert p.allow_model_training is False
        assert p.allow_model_predict is False
        assert p.allow_target_label_generation is False
        assert p.allow_performance_claim is False
        assert p.allow_full_article_usage is False
        assert p.allow_article_body_usage is False
        assert p.allow_source_overwrite is False
        assert p.allow_auto_imputation is False
        assert p.allow_auto_feature_drop is False


def test_validate_stress_testing_profiles():
    assert validate_stress_testing_profiles() is True
    assert len(PROFILES) >= 3
    with pytest.raises(KeyError):
        get_stress_testing_profile("unknown_profile_phase_148")
