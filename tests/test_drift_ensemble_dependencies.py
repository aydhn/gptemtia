# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Ensemble Dependencies."""

import pytest
from advanced_model_drift_monitoring.drift_ensemble_dependencies import check_drift_ensemble_dependencies


def test_drift_ensemble_dependencies():
    res = check_drift_ensemble_dependencies()
    assert res["status"] == "satisfied"
    assert res["all_satisfied"] is True
    assert res["total_checks"] == 2
