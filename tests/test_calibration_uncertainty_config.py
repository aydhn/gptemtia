# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Config."""

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    PROFILES,
    get_calibration_uncertainty_profile,
    list_calibration_uncertainty_profiles,
)


def test_profiles_exist():
    profiles = list_calibration_uncertainty_profiles()
    assert "balanced_local_calibration_uncertainty_contracts" in profiles
    assert "strict_non_executing_calibration_safety" in profiles
    assert "dry_run_uncertainty_governance_focus" in profiles


def test_active_profile_invariants():
    p = get_calibration_uncertainty_profile()
    assert p.current_phase == 141
    assert p.next_phase == 142
    assert p.target_final_phase == 160
    assert p.dry_run_default is True
    assert p.local_only is True
    assert p.allow_live_trading is False
    assert p.allow_broker_integration is False
    assert p.allow_signal_generation is False
    assert p.allow_model_training is False
    assert p.allow_probability_prediction is False
    assert p.allow_calibration_execution is False
    assert p.allow_uncertainty_estimation is False
