"""Test suite for Phase 136 GPU ML Runtime Safety Boundary."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_safety_boundary import (
    build_gpu_ml_runtime_safety_boundary,
)


def test_build_gpu_ml_runtime_safety_boundary():
    df, summary = build_gpu_ml_runtime_safety_boundary()
    assert not df.empty
    assert summary["no_go_count"] >= 15
    assert summary["safe_go_count"] >= 8
    assert summary["live_trading_prohibited"] is True
    assert summary["model_training_prohibited"] is True
    assert summary["non_signal"] is True
