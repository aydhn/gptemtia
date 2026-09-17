# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Calibration & Uncertainty Dependencies."""

import pytest
from advanced_model_drift_monitoring.drift_calibration_uncertainty_dependencies import check_drift_calibration_uncertainty_dependencies


def test_drift_calibration_uncertainty_dependencies():
    res = check_drift_calibration_uncertainty_dependencies()
    assert res["status"] == "satisfied"
    assert res["all_satisfied"] is True
    assert res["total_checks"] == 2
