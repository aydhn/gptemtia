"""Test suite for Phase 136 GPU Capability Registry."""

import pytest
from advanced_gpu_ml_runtime.gpu_capability_registry import (
    build_gpu_capability_registry,
)


def test_build_gpu_capability_registry():
    df, summary = build_gpu_capability_registry()
    assert not df.empty
    assert "cuda_available" in summary
    assert "cuda_gpu_detected" in summary
    assert summary["non_signal"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
