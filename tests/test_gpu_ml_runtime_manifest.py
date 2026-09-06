"""Test suite for Phase 136 GPU ML Runtime Manifest."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_manifest import (
    build_gpu_ml_runtime_manifest,
)


def test_build_gpu_ml_runtime_manifest():
    df, summary = build_gpu_ml_runtime_manifest()
    assert not df.empty
    assert summary["current_phase"] == 136
    assert summary["next_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["model_training_executed"] is False
    assert summary["model_predict_executed"] is False
    assert summary["clustering_executed"] is False
    assert summary["artifact_persisted"] is False
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
