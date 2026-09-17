# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Validation Dependencies."""

import pytest
from advanced_model_drift_monitoring.drift_validation_dependencies import check_drift_validation_dependencies


def test_drift_validation_dependencies():
    res = check_drift_validation_dependencies()
    assert res["status"] == "satisfied"
    assert res["all_satisfied"] is True
    assert res["total_checks"] == 2
