# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Safety Boundary."""

from advanced_calibration_uncertainty.calibration_uncertainty_safety_boundary import (
    build_calibration_uncertainty_safety_boundary,
    enforce_calibration_uncertainty_safety_boundary,
    summarize_calibration_uncertainty_safety_boundary,
)


def test_safety_boundary():
    df, summary = build_calibration_uncertainty_safety_boundary()
    assert summary["safety_status"] == "ENFORCED"
    assert summary["no_go_count"] >= 10
    assert summary["safe_go_count"] >= 10

    valid_dict = {
        "phase": 141,
        "non_signal": True,
        "dry_run": True,
        "local_only": True,
        "real_training_executed": False,
        "probability_prediction_executed": False,
    }
    assert enforce_calibration_uncertainty_safety_boundary(valid_dict) is True

    invalid_dict = {"phase": 141, "non_signal": False}
    assert enforce_calibration_uncertainty_safety_boundary(invalid_dict) is False
