"""Test suite for Phase 137 Artifact Disabled Contracts."""

import pytest
from advanced_ml_dataset_registry.ml_artifact_disabled_contracts import (
    build_ml_artifact_disabled_contract_registry,
    validate_artifact_disabled_request,
    summarize_artifact_disabled_contracts,
)


def test_build_artifact_disabled_contracts():
    df, summary = build_ml_artifact_disabled_contract_registry()
    assert not df.empty
    assert summary["all_enforced"] is True
    assert summary["artifact_persistence_blocked"] is True
    assert summary["model_registry_write_blocked"] is True
    assert summary["dataset_materialization_blocked"] is True


def test_validate_artifact_disabled():
    clean = validate_artifact_disabled_request("read markdown report")
    assert clean["valid"] is True

    dirty_save = validate_artifact_disabled_request("save_model weights to registry")
    assert dirty_save["valid"] is False
    assert dirty_save["blocked"] is True
