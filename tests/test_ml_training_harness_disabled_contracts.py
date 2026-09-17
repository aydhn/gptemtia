"""Test suite for Phase 137 Training Harness Disabled Contracts."""

import pytest
from advanced_ml_dataset_registry.ml_training_harness_disabled_contracts import (
    build_ml_training_harness_disabled_contract_registry,
    validate_training_harness_disabled_request,
    summarize_training_harness_disabled_contracts,
)


def test_build_training_harness_disabled_contracts():
    df, summary = build_ml_training_harness_disabled_contract_registry()
    assert not df.empty
    assert summary["all_enforced"] is True
    assert summary["model_training_blocked"] is True
    assert summary["optimizer_blocked"] is True
    assert summary["backtest_blocked"] is True


def test_validate_training_disabled():
    clean = validate_training_harness_disabled_request("view contract metadata")
    assert clean["valid"] is True

    dirty_fit = validate_training_harness_disabled_request("call model.fit(x, y)")
    assert dirty_fit["valid"] is False
    assert dirty_fit["blocked"] is True
    assert "fit" in dirty_fit["detected_violations"]
