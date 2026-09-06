"""Test suite for Phase 136 scikit-learn Runtime Capability."""

import pytest
from advanced_gpu_ml_runtime.sklearn_runtime_capability import (
    build_sklearn_runtime_capability_report,
)


def test_build_sklearn_runtime_capability_report():
    df, summary = build_sklearn_runtime_capability_report()
    assert not df.empty
    assert "sklearn_installed" in summary
    assert summary["non_signal"] is True
