"""Test suite for Phase 137 Advanced ML Dataset Labels."""

import pytest
from advanced_ml_dataset_registry.advanced_ml_dataset_labels import (
    list_advanced_ml_dataset_domain_labels,
    list_advanced_ml_dataset_status_labels,
    list_ml_experiment_permission_labels,
    validate_advanced_ml_dataset_domain_label,
    validate_advanced_ml_dataset_status_label,
    validate_ml_experiment_permission_label,
)


def test_list_labels():
    domains = list_advanced_ml_dataset_domain_labels()
    statuses = list_advanced_ml_dataset_status_labels()
    permissions = list_ml_experiment_permission_labels()

    assert len(domains) >= 35
    assert len(statuses) >= 5
    assert len(permissions) >= 5


def test_validate_domain_labels():
    assert validate_advanced_ml_dataset_domain_label("dataset_contract_domain") is True
    assert validate_advanced_ml_dataset_domain_label("leakage_guard_domain") is True
    assert validate_advanced_ml_dataset_domain_label("invalid_domain_xyz") is False


def test_validate_status_labels():
    assert validate_advanced_ml_dataset_status_label("dataset_contract_ready") is True
    assert validate_advanced_ml_dataset_status_label("dataset_contract_blocked_by_safety") is True
    assert validate_advanced_ml_dataset_status_label("unknown_status") is False


def test_validate_permission_labels():
    assert validate_ml_experiment_permission_label("experiment_training_blocked") is True
    assert validate_ml_experiment_permission_label("experiment_metadata_only_allowed") is True
    assert validate_ml_experiment_permission_label("random_permission") is False
