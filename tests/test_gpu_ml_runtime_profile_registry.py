"""Test suite for Phase 136 GPU ML Runtime Profile Registry."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_profile_registry import (
    build_gpu_ml_runtime_profile_registry,
)


def test_build_profile_registry():
    df, summary = build_gpu_ml_runtime_profile_registry()
    assert not df.empty
    assert len(df) == 3
    assert summary["total_profiles"] == 3
    assert summary["current_phase"] == 136
    assert summary["next_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["status"] == "runtime_ready"
