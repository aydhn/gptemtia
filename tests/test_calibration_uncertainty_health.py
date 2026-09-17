# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Health."""

from advanced_calibration_uncertainty.calibration_uncertainty_health import (
    build_calibration_uncertainty_health_check,
    summarize_calibration_uncertainty_health,
)


def test_calibration_uncertainty_health():
    df, summary = build_calibration_uncertainty_health_check()
    assert summary["status"] == "HEALTHY"
    assert summary["all_passed"] is True
    assert summary["non_signal"] is True
