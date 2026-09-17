"""Test suite for Phase 137 ML Experiment Permissions."""

import pytest
from advanced_ml_dataset_registry.ml_experiment_permissions import (
    build_ml_experiment_permission_registry,
    validate_ml_experiment_permission_request,
    summarize_ml_experiment_permissions,
)


def test_build_experiment_permissions():
    df, summary = build_ml_experiment_permission_registry()
    assert not df.empty
    assert summary["total_permissions"] >= 8
    assert summary["training_blocked"] is True


def test_validate_permission_requests():
    v_clean = validate_ml_experiment_permission_request("create experiment metadata reference")
    assert v_clean["valid"] is True

    v_train = validate_ml_experiment_permission_request("train model with gradient boosting")
    assert v_train["valid"] is False

    v_mat = validate_ml_experiment_permission_request("materialize parquet dataset")
    assert v_mat["valid"] is False
