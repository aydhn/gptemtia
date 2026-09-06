"""Test suite for Phase 136 GPU ML Runtime Pipeline."""

import pytest
from advanced_gpu_ml_runtime.gpu_ml_runtime_pipeline import GpuMlRuntimePipeline
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile


def test_gpu_ml_runtime_pipeline_execution():
    profile = get_default_gpu_ml_runtime_profile()
    pipeline = GpuMlRuntimePipeline(profile=profile)
    status_df, summary = pipeline.run(save=False)

    assert not status_df.empty
    assert summary["current_phase"] == 136
    assert summary["next_phase"] == 137
    assert summary["target_final_phase"] == 160
    assert summary["status"] == "READY"
    assert summary["non_signal"] is True
    assert summary["validation_passed"] is True
    assert summary["handoff_ready"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
