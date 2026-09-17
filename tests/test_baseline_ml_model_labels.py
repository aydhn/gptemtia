"""Test suite for Phase 138 Baseline ML Model Labels."""

from advanced_baseline_ml_models.baseline_ml_model_labels import (
    BASELINE_ML_MODEL_DOMAIN_LABELS,
    BASELINE_ML_MODEL_STATUS_LABELS,
    BASELINE_EXECUTION_LABELS,
    list_baseline_ml_model_domain_labels,
    list_baseline_ml_model_status_labels,
    list_baseline_execution_labels,
    validate_baseline_ml_model_domain_label,
    validate_baseline_ml_model_status_label,
    validate_baseline_execution_label,
)


def test_baseline_ml_model_domain_labels():
    labels = list_baseline_ml_model_domain_labels()
    assert len(labels) == 37
    assert "model_family_domain" in labels
    assert "model_contract_domain" in labels
    assert "dry_run_harness_contract_domain" in labels
    assert "no_real_training_domain" in labels
    assert validate_baseline_ml_model_domain_label("model_family_domain") is True
    assert validate_baseline_ml_model_domain_label("invalid_domain_xyz") is False


def test_baseline_ml_model_status_labels():
    statuses = list_baseline_ml_model_status_labels()
    assert len(statuses) == 6
    assert "baseline_contract_ready" in statuses
    assert "baseline_contract_placeholder_only" in statuses
    assert validate_baseline_ml_model_status_label("baseline_contract_ready") is True
    assert validate_baseline_ml_model_status_label("invalid_status_xyz") is False


def test_baseline_execution_labels():
    executions = list_baseline_execution_labels()
    assert len(executions) == 6
    assert "execution_blocked_no_real_training" in executions
    assert "execution_contract_only" in executions
    assert validate_baseline_execution_label("execution_blocked_no_real_training") is True
    assert validate_baseline_execution_label("invalid_exec_xyz") is False
