"""Test suite for Phase 136 NumPy and Pandas Runtime Capability."""

import pytest
from advanced_gpu_ml_runtime.numpy_pandas_runtime_capability import (
    build_numpy_pandas_runtime_capability_report,
)


def test_build_numpy_pandas_runtime_capability_report():
    df, summary = build_numpy_pandas_runtime_capability_report()
    assert not df.empty
    assert summary["total_packages"] >= 2
    assert summary["all_installed"] is True
    assert summary["non_signal"] is True
