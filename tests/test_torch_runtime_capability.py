"""Test suite for Phase 136 PyTorch Runtime Capability."""

import pytest
from advanced_gpu_ml_runtime.torch_runtime_capability import (
    build_torch_runtime_capability_report,
)


def test_build_torch_runtime_capability_report():
    df, summary = build_torch_runtime_capability_report()
    assert not df.empty
    assert "torch_installed" in summary
    assert summary["non_signal"] is True
