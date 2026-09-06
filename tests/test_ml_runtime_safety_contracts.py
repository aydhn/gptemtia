"""Test suite for Phase 136 ML Runtime Safety Contracts."""

import pytest
from advanced_gpu_ml_runtime.ml_runtime_safety_contracts import (
    build_ml_runtime_safety_contract_registry,
    SAFETY_CONTRACTS,
)


def test_safety_contracts_definitions():
    assert len(SAFETY_CONTRACTS) == 12
    ids = [c["contract_id"] for c in SAFETY_CONTRACTS]
    assert "no_live_trading_contract" in ids
    assert "no_model_training_contract" in ids


def test_build_ml_runtime_safety_contract_registry():
    df, summary = build_ml_runtime_safety_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] == 12
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
