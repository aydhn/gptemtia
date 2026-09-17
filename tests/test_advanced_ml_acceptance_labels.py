# -*- coding: utf-8 -*-
"""Unit tests for Phase 145: Advanced ML Acceptance Labels."""

import pytest
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    list_advanced_ml_acceptance_domain_labels,
    list_advanced_ml_acceptance_status_labels,
    list_advanced_ml_acceptance_boundary_labels,
    validate_advanced_ml_acceptance_domain_label,
    validate_advanced_ml_acceptance_status_label,
    validate_advanced_ml_acceptance_boundary_label,
    ADVANCED_ML_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
    GO_CONTRACT_ONLY,
)


def test_labels_lists():
    domains = list_advanced_ml_acceptance_domain_labels()
    statuses = list_advanced_ml_acceptance_status_labels()
    boundaries = list_advanced_ml_acceptance_boundary_labels()

    assert len(domains) >= 25
    assert len(statuses) >= 6
    assert len(boundaries) >= 8
    assert ADVANCED_ML_ACCEPTANCE_DOMAIN in domains
    assert ACCEPTANCE_READY in statuses
    assert GO_CONTRACT_ONLY in boundaries


def test_label_validations():
    assert validate_advanced_ml_acceptance_domain_label(ADVANCED_ML_ACCEPTANCE_DOMAIN) is True
    assert validate_advanced_ml_acceptance_status_label(ACCEPTANCE_READY) is True
    assert validate_advanced_ml_acceptance_boundary_label(GO_CONTRACT_ONLY) is True

    with pytest.raises(ValueError):
        validate_advanced_ml_acceptance_domain_label("invalid_domain")
    with pytest.raises(ValueError):
        validate_advanced_ml_acceptance_status_label("invalid_status")
    with pytest.raises(ValueError):
        validate_advanced_ml_acceptance_boundary_label("invalid_boundary")
