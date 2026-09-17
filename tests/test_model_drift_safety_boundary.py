# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Safety Boundary Enforcer."""

import pytest
from advanced_model_drift_monitoring.model_drift_safety_boundary import (
    ModelDriftSafetyViolation,
    assert_drift_safety_boundary,
    verify_drift_safety_status,
)


def test_safety_boundary_status():
    status = verify_drift_safety_status()
    assert status["phase"] == 142
    assert status["boundary_status"] == "SECURE"
    assert status["is_dry_run_enforced"] is True


def test_safety_boundary_assertions():
    # Compliant operation
    assert_drift_safety_boundary("view_drift_contracts", {"contract_only": True})

    # Prohibited operations
    with pytest.raises(ModelDriftSafetyViolation):
        assert_drift_safety_boundary("place_order", {})

    with pytest.raises(ModelDriftSafetyViolation):
        assert_drift_safety_boundary("evaluate", {"execute_calculation": True})

    with pytest.raises(ModelDriftSafetyViolation):
        assert_drift_safety_boundary("evaluate", {"dispatch_alert": True})

    with pytest.raises(ModelDriftSafetyViolation):
        assert_drift_safety_boundary("evaluate", {"auto_retrain_trigger": True})

    with pytest.raises(ModelDriftSafetyViolation):
        assert_drift_safety_boundary("clean_lake", {"destructive_overwrite": True})
