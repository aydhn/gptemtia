"""Test suite for Phase 136 ML Runtime Findings."""

import pytest
from advanced_gpu_ml_runtime.ml_runtime_findings import (
    build_ml_runtime_findings_registry,
)


def test_build_ml_runtime_findings_registry():
    df, summary = build_ml_runtime_findings_registry()
    assert not df.empty
    assert summary["total_findings"] > 0
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
