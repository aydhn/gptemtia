"""Test suite for Phase 136 FeatureStore ML Input Contracts."""

import pytest
from advanced_gpu_ml_runtime.featurestore_ml_input_contracts import (
    build_featurestore_ml_input_contract_registry,
)


def test_build_featurestore_ml_input_contracts():
    df, summary = build_featurestore_ml_input_contract_registry()
    assert not df.empty
    assert summary["total_contracts"] > 0
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
