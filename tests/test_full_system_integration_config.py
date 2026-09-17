# -*- coding: utf-8 -*-
"""Unit tests for Phase 158 Full System Integration Configuration."""

import pytest
from advanced_full_system_integration.full_system_integration_config import (
    FullSystemIntegrationProfile,
    get_full_system_integration_profile,
    get_default_full_system_integration_profile,
    list_full_system_integration_profiles,
    validate_full_system_integration_profiles,
    PROFILES,
)


def test_default_profile():
    profile = get_default_full_system_integration_profile()
    assert profile.profile_name == "balanced_local_full_system_integration_contracts"
    assert profile.current_phase == 158
    assert profile.target_final_phase == 160
    assert profile.next_phase == 159
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_order_generation is False
    assert profile.allow_production_deployment is False
    assert profile.allow_model_training is False
    assert profile.allow_model_predict is False
    assert profile.allow_backtest_execution is False
    assert profile.allow_portfolio_execution is False
    assert profile.allow_risk_execution is False
    assert profile.allow_scenario_execution is False
    assert profile.allow_investment_advice is False
    assert profile.allow_web_scraping is False
    assert profile.allow_credential_output is False
    assert profile.allow_source_overwrite is False
    assert profile.allow_model_registry_write is False
    assert profile.allow_artifact_persistence is False


def test_list_and_get_profile():
    profiles = list_full_system_integration_profiles()
    assert len(profiles) >= 3
    p = get_full_system_integration_profile("strict_non_production_system_integration_safety")
    assert p.profile_name == "strict_non_production_system_integration_safety"

    with pytest.raises(KeyError):
        get_full_system_integration_profile("non_existent_profile_phase_158")


def test_validate_profiles():
    assert validate_full_system_integration_profiles() is True
