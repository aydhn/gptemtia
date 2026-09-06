"""Test suite for Phase 136 Accelerator Backend Registry."""

import pytest
from advanced_gpu_ml_runtime.accelerator_backend_registry import (
    build_accelerator_backend_registry,
)


def test_build_accelerator_backend_registry():
    df, summary = build_accelerator_backend_registry()
    assert not df.empty
    assert summary["total_backends"] >= 5
    assert summary["available_backends"] >= 1
    assert summary["non_signal"] is True
