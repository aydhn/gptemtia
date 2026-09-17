# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Runtime Dependencies."""

import pytest
from advanced_model_drift_monitoring.drift_runtime_dependencies import check_drift_runtime_dependencies


def test_drift_runtime_dependencies():
    res = check_drift_runtime_dependencies()
    assert res["status"] == "satisfied"
    assert res["all_satisfied"] is True
    assert res["total_checks"] == 2
