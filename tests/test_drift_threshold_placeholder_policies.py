# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Drift Threshold Placeholders."""

import pytest
from advanced_model_drift_monitoring.drift_threshold_placeholder_policies import (
    build_drift_threshold_placeholders,
    validate_drift_threshold_placeholder,
    validate_drift_threshold_request,
)


def test_drift_threshold_placeholders():
    thresholds = build_drift_threshold_placeholders()
    assert len(thresholds) == 6
    for t in thresholds:
        val = validate_drift_threshold_placeholder(t)
        assert val["valid"] is True
        assert t.execution_enabled is False


def test_validate_threshold_request_safety():
    # Safe request
    res = validate_drift_threshold_request({"threshold_id": "thresh_psi_standard_feature", "threshold_type": "psi"})
    assert res["valid"] is True

    # Attempt live execution should be rejected
    res_unsafe = validate_drift_threshold_request({"trigger_retraining": True})
    assert res_unsafe["valid"] is False
