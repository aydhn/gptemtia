# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Health Check."""

import pytest
from advanced_model_drift_monitoring.model_drift_health import run_model_drift_health_check


def test_model_drift_health():
    res = run_model_drift_health_check()
    assert res["phase"] == 142
    assert res["overall_health"] == "HEALTHY"
    assert res["all_passed"] is True
    assert res["total_checks"] >= 4
