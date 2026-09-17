# -*- coding: utf-8 -*-
"""Unit tests for Phase 140 Ensemble Model Labels."""

from advanced_ensemble_model_registry.ensemble_model_labels import (
    ENSEMBLE_MODEL_DOMAINS,
    ENSEMBLE_MODEL_DOMAIN_LABELS,
    CANDIDATE_MODEL_STATUSES,
    CANDIDATE_MODEL_STATUS_LABELS,
    ENSEMBLE_EXECUTION_LABELS,
    list_ensemble_model_domain_labels,
    list_ensemble_model_status_labels,
    list_candidate_model_status_labels,
    list_ensemble_execution_labels,
    validate_ensemble_domain_label,
    validate_candidate_model_status_label,
    validate_ensemble_execution_label,
)


def test_ensemble_model_domain_labels():
    labels = list_ensemble_model_domain_labels()
    assert len(labels) == len(ENSEMBLE_MODEL_DOMAINS)
    assert "candidate_model_contract_domain" in labels
    assert "ensemble_strategy_contract_domain" in labels
    assert validate_ensemble_domain_label("candidate_model_contract_domain") is True
    assert validate_ensemble_domain_label("invalid_domain_xyz") is False


def test_candidate_status_labels():
    statuses = list_candidate_model_status_labels()
    assert len(statuses) == len(CANDIDATE_MODEL_STATUSES)
    assert "contract_registered" in statuses
    assert validate_candidate_model_status_label("contract_registered") is True
    assert validate_candidate_model_status_label("invalid_status") is False


def test_execution_labels():
    exec_labels = list_ensemble_execution_labels()
    assert len(exec_labels) == len(ENSEMBLE_EXECUTION_LABELS)
    assert "execution_blocked_no_training" in exec_labels
    assert validate_ensemble_execution_label("execution_blocked_no_training") is True
    assert validate_ensemble_execution_label("execution_active") is False
