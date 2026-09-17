# -*- coding: utf-8 -*-
"""Unit tests for Calibration & Uncertainty Labels."""

from advanced_calibration_uncertainty.calibration_uncertainty_labels import (
    CALIBRATION_UNCERTAINTY_DOMAINS,
    CALIBRATION_UNCERTAINTY_STATUS_LABELS,
    CALIBRATION_UNCERTAINTY_EXECUTION_LABELS,
    list_calibration_uncertainty_domain_labels,
    list_calibration_uncertainty_status_labels,
    list_calibration_uncertainty_execution_labels,
    validate_calibration_uncertainty_domain_label,
    validate_calibration_uncertainty_status_label,
    validate_calibration_uncertainty_execution_label,
)


def test_domain_labels_count():
    assert len(CALIBRATION_UNCERTAINTY_DOMAINS) >= 40
    assert "probability_calibration_contract_domain" in CALIBRATION_UNCERTAINTY_DOMAINS
    assert "uncertainty_estimation_contract_domain" in CALIBRATION_UNCERTAINTY_DOMAINS
    assert validate_calibration_uncertainty_domain_label("probability_calibration_contract_domain") is True


def test_status_and_execution_labels():
    assert "calibration_contract_ready" in CALIBRATION_UNCERTAINTY_STATUS_LABELS
    assert "execution_blocked_no_probability_prediction" in CALIBRATION_UNCERTAINTY_EXECUTION_LABELS
    assert validate_calibration_uncertainty_status_label("calibration_contract_ready") is True
    assert validate_calibration_uncertainty_execution_label("execution_blocked_no_probability_prediction") is True
