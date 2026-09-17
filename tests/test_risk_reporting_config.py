# -*- coding: utf-8 -*-
"""Unit tests for Phase 155 Risk Reporting Configuration."""

import pytest
from advanced_risk_reporting.risk_reporting_config import (
    RiskReportingProfile,
    get_risk_reporting_profile,
    get_default_risk_reporting_profile,
    list_risk_reporting_profiles,
    validate_risk_reporting_profiles,
    RISK_REPORTING_PROFILES,
)


def test_default_risk_reporting_profile():
    profile = get_default_risk_reporting_profile()
    assert profile.profile_name == "balanced_local_risk_reporting_contracts"
    assert profile.current_phase == 155
    assert profile.target_final_phase == 160
    assert profile.next_phase == 156
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_broker_integration is False
    assert profile.allow_signal_generation is False
    assert profile.allow_metric_calculation is False
    assert profile.allow_var_calculation is False
    assert profile.allow_expected_shortfall_calculation is False
    assert profile.allow_exposure_calculation is False
    assert profile.allow_limit_breach_generation is False
    assert profile.allow_alert_generation is False
    assert profile.allow_dashboard_generation is False
    assert profile.allow_portfolio_adjustment is False


def test_list_risk_reporting_profiles():
    profiles = list_risk_reporting_profiles(enabled_only=True)
    assert len(profiles) >= 3
    names = [p.profile_name for p in profiles]
    assert "balanced_local_risk_reporting_contracts" in names
    assert "strict_non_production_risk_reporting_safety" in names
    assert "dry_run_phase_155_risk_reporting_contracts_focus" in names
    assert "dry_run_phase_155_limit_monitoring_focus" in names


def test_validate_risk_reporting_profiles():
    valid = validate_risk_reporting_profiles()
    assert valid is True


def test_get_risk_reporting_profile():
    p = get_risk_reporting_profile("strict_non_production_risk_reporting_safety")
    assert p.profile_name == "strict_non_production_risk_reporting_safety"
    assert p.non_production is True

    with pytest.raises(KeyError):
        get_risk_reporting_profile("non_existent_profile")
