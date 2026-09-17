"""Test suite for Phase 137 Prediction Disabled Contracts."""

import pytest
from advanced_ml_dataset_registry.ml_prediction_disabled_contracts import (
    build_ml_prediction_disabled_contract_registry,
    validate_prediction_disabled_request,
    summarize_prediction_disabled_contracts,
)


def test_build_prediction_disabled_contracts():
    df, summary = build_ml_prediction_disabled_contract_registry()
    assert not df.empty
    assert summary["all_enforced"] is True
    assert summary["prediction_blocked"] is True
    assert summary["inference_blocked"] is True
    assert summary["signal_generation_blocked"] is True


def test_validate_prediction_disabled():
    clean = validate_prediction_disabled_request("review regime schema")
    assert clean["valid"] is True

    dirty_predict = validate_prediction_disabled_request("predict tomorrow return")
    assert dirty_predict["valid"] is False
    assert dirty_predict["blocked"] is True
