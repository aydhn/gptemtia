"""Test suite for Phase 136 CUDA Availability Report."""

import pytest
from advanced_gpu_ml_runtime.cuda_availability import (
    build_cuda_availability_report,
)


def test_build_cuda_availability_report():
    df, summary = build_cuda_availability_report()
    assert not df.empty
    assert "cuda_available" in summary
    assert summary["non_signal"] is True
