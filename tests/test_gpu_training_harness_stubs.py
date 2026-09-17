"""Test suite for Phase 139 GPU Training Harness Stubs."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_harness_stubs import (
    build_gpu_training_harness_stub_registry,
    gpu_training_harness_stub,
    summarize_gpu_training_harness_stubs,
)


def test_build_gpu_training_harness_stub_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_training_harness_stub_registry(profile)

    assert len(df) == 3
    assert summary["total_stubs"] == 3
    assert summary["all_dry_run"] is True
    assert summary["all_real_training_disabled"] is True
    assert summary["all_model_fit_disabled"] is True
    assert summary["all_model_predict_disabled"] is True
    assert summary["all_blocked_by_policy"] is True
    assert summary["non_signal"] is True


def test_gpu_training_harness_stub():
    res = gpu_training_harness_stub({"model_family": "gradient_boosting", "device_preference": "cuda_if_available"})
    assert res["dry_run"] is True
    assert res["real_training_executed"] is False
    assert res["model_fit_executed"] is False
    assert res["model_predict_executed"] is False
    assert res["model_inference_executed"] is False
    assert res["model_transform_executed"] is False
    assert res["target_label_generated"] is False
    assert res["dataset_materialized"] is False
    assert res["feature_snapshot_materialized"] is False
    assert res["artifact_persisted"] is False
    assert res["model_registry_written"] is False
    assert res["optimizer_step_executed"] is False
    assert res["backward_pass_executed"] is False
    assert res["blocked_by_policy"] is True
    assert res["non_signal"] is True
    assert res["status"] == "execution_blocked_no_real_training"
