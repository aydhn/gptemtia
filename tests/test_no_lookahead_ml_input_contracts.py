"""Test suite for Phase 136 No-Lookahead ML Input Contracts."""

import pytest
from advanced_gpu_ml_runtime.no_lookahead_ml_input_contracts import (
    build_no_lookahead_ml_input_contract_registry,
)


def test_build_no_lookahead_ml_input_contracts():
    df, summary = build_no_lookahead_ml_input_contract_registry()
    assert not df.empty
    assert summary["no_lookahead_guaranteed"] is True
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
