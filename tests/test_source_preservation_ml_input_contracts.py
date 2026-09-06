"""Test suite for Phase 136 Source Preservation ML Input Contracts."""

import pytest
from advanced_gpu_ml_runtime.source_preservation_ml_input_contracts import (
    build_source_preservation_ml_input_contract_registry,
)


def test_build_source_preservation_ml_input_contracts():
    df, summary = build_source_preservation_ml_input_contract_registry()
    assert not df.empty
    assert summary["source_preservation_guaranteed"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
