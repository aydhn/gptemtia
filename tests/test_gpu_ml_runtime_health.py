"""Test suite for Phase 136 GPU ML Runtime Health Check."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_health import (
    build_gpu_ml_runtime_health_check,
    HEALTH_COMPONENTS,
)


def test_health_components_list():
    assert len(HEALTH_COMPONENTS) >= 10
    names = [c["name"] for c in HEALTH_COMPONENTS]
    assert "advanced_gpu_ml_runtime" in names
    assert "feature_store" in names
    assert "data_lake" in names


def test_build_gpu_ml_runtime_health_check():
    df, summary = build_gpu_ml_runtime_health_check()
    assert not df.empty
    assert summary["total_components"] >= 10
    assert summary["all_healthy"] is True
    assert summary["non_signal"] is True
