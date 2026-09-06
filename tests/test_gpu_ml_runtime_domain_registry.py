"""Test suite for Phase 136 GPU ML Runtime Domain Registry."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_domain_registry import (
    build_gpu_ml_runtime_domain_registry,
)


def test_build_domain_registry():
    df, summary = build_gpu_ml_runtime_domain_registry()
    assert not df.empty
    assert len(df) >= 20
    assert summary["total_domains"] >= 20
    assert summary["non_signal"] is True
    assert summary["status"] == "runtime_ready"
