"""Test suite for Phase 136 Regime Metadata ML Input Contracts."""

import pytest
from advanced_gpu_ml_runtime.regime_metadata_ml_input_contracts import (
    build_regime_metadata_ml_input_contract_registry,
)


def test_build_regime_metadata_ml_input_contracts():
    df, summary = build_regime_metadata_ml_input_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] == 10
    assert summary["all_non_signal"] is True
    assert summary["all_source_preserved"] is True
    assert summary["training_blocked"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
