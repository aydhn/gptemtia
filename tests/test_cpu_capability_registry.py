"""Test suite for Phase 136 CPU Capability Registry."""

import pytest
from advanced_gpu_ml_runtime.cpu_capability_registry import (
    build_cpu_capability_registry,
)


def test_build_cpu_capability_registry():
    df, summary = build_cpu_capability_registry()
    assert not df.empty
    assert summary["total_cpus"] > 0
    assert summary["non_signal"] is True
