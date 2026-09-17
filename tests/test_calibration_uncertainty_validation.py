# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Validation."""

from advanced_calibration_uncertainty.calibration_uncertainty_validation import (
    build_calibration_uncertainty_validation_report,
)


def test_calibration_uncertainty_validation():
    df, summary = build_calibration_uncertainty_validation_report()
    assert summary["validation_status"] == "VALID"
    assert summary["passed_checks"] == summary["total_checks"]
    assert summary["forbidden_claims_clean"] is True
