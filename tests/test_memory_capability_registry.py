"""Test suite for Phase 136 Memory Capability Registry."""

import pytest
from advanced_gpu_ml_runtime.memory_capability_registry import (
    build_memory_capability_registry,
)


def test_build_memory_capability_registry():
    df, summary = build_memory_capability_registry()
    assert not df.empty
    assert summary["total_records"] > 0
    assert summary["total_ram_gb"] > 0
    assert summary["non_signal"] is True
