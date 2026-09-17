# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Model Drift Configuration."""

import pytest
from advanced_model_drift_monitoring.model_drift_config import (
    PROFILES,
    ModelDriftProfile,
    get_default_model_drift_profile,
    get_model_drift_profile,
    list_model_drift_profiles,
    validate_model_drift_profiles,
)


def test_model_drift_profile_defaults():
    profile = ModelDriftProfile()
    assert profile.current_phase == 142
    assert profile.target_final_phase == 160
    assert profile.next_phase == 143
    assert profile.dry_run_default is True
    assert profile.local_only is True
    assert profile.allow_live_trading is False
    assert profile.allow_drift_metric_calculation is False
    assert profile.allow_alerting is False
    assert profile.allow_retraining_trigger is False
    assert profile.allow_model_action is False


def test_list_and_get_profiles():
    profiles = list_model_drift_profiles()
    assert "balanced_local_model_drift_contracts" in profiles
    assert "strict_non_executing_drift_monitoring_safety" in profiles
    assert "dry_run_drift_linkage_governance_focus" in profiles

    default_prof = get_default_model_drift_profile()
    assert default_prof.name == "balanced_local_model_drift_contracts"

    prof = get_model_drift_profile("strict_non_executing_drift_monitoring_safety")
    assert prof.name == "strict_non_executing_drift_monitoring_safety"
    assert prof.profile_name == "strict_non_executing_drift_monitoring_safety"
    assert prof.display_name == "Strict Non Executing Drift Monitoring Safety"


def test_validate_all_profiles():
    assert validate_model_drift_profiles() is True
