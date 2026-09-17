"""Test suite for Phase 137 Feature Snapshot Contracts."""

import pytest
from advanced_ml_dataset_registry.ml_dataset_feature_snapshot_contracts import (
    build_ml_dataset_feature_snapshot_contract_registry,
    validate_feature_snapshot_contract,
    summarize_feature_snapshot_contracts,
)


def test_build_feature_snapshot_contracts():
    df, summary = build_ml_dataset_feature_snapshot_contract_registry()
    assert not df.empty
    assert summary["total_snapshot_contracts"] >= 5
    assert summary["non_signal"] is True


def test_validate_snapshot_contract():
    v_clean = validate_feature_snapshot_contract({"materialized": False, "production_ready": False})
    assert v_clean["valid"] is True

    v_bad = validate_feature_snapshot_contract({"materialized": True, "production_ready": True})
    assert v_bad["valid"] is False
