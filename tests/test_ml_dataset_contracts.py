"""Test suite for Phase 137 ML Dataset Contracts."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_contracts import (
    build_ml_dataset_contract_registry,
    validate_ml_dataset_contract,
    summarize_ml_dataset_contracts,
)


def test_build_contracts():
    df, summary = build_ml_dataset_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] >= 8
    assert summary["materialization_allowed"] is False
    assert summary["target_label_allowed"] is False
    assert summary["training_allowed"] is False
    assert summary["prediction_allowed"] is False


def test_validate_contract_invalid():
    res = validate_ml_dataset_contract({"contract_name": "c1", "dataset_materialization_allowed": True})
    assert res["valid"] is False
