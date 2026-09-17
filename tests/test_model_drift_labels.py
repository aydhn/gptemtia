# -*- coding: utf-8 -*-
"""Unit tests for Phase 142 Labels and Domain Registries."""

import pytest
from advanced_model_drift_monitoring.model_drift_labels import (
    MODEL_DRIFT_DOMAIN_LABELS,
    MODEL_DRIFT_EXECUTION_LABELS,
    MODEL_DRIFT_STATUS_LABELS,
    is_valid_drift_domain_label,
    is_valid_drift_execution_label,
    is_valid_drift_status_label,
)


def test_label_membership():
    assert len(MODEL_DRIFT_DOMAIN_LABELS) >= 50
    assert "candidate_model_drift_monitoring_contract" in MODEL_DRIFT_DOMAIN_LABELS
    assert "ensemble_drift_monitoring_contract" in MODEL_DRIFT_DOMAIN_LABELS
    assert "feature_drift_linkage" in MODEL_DRIFT_DOMAIN_LABELS
    assert "regime_drift_linkage" in MODEL_DRIFT_DOMAIN_LABELS

    assert is_valid_drift_domain_label("candidate_model_drift_monitoring_contract") is True
    assert is_valid_drift_domain_label("invalid_nonexistent_label") is False


def test_status_and_execution_labels():
    assert "active" in MODEL_DRIFT_STATUS_LABELS
    assert "placeholder" in MODEL_DRIFT_STATUS_LABELS
    assert is_valid_drift_status_label("active") is True

    assert "drift_calculation_disabled" in MODEL_DRIFT_EXECUTION_LABELS
    assert "drift_alerting_disabled" in MODEL_DRIFT_EXECUTION_LABELS
    assert is_valid_drift_execution_label("drift_calculation_disabled") is True
