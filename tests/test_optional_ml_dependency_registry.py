"""Test suite for Phase 136 Optional ML Dependency Registry."""

import pytest
from advanced_gpu_ml_runtime.optional_ml_dependency_registry import (
    build_optional_ml_dependency_registry,
)


def test_build_optional_ml_dependency_registry():
    df, summary = build_optional_ml_dependency_registry()
    assert not df.empty
    assert summary["total_optional_packages"] >= 10
    assert summary["non_signal"] is True
