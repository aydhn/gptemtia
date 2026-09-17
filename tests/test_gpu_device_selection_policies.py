"""Test suite for Phase 139 GPU Device Selection Policies."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_device_selection_policies import (
    build_gpu_device_selection_policy_registry,
    dry_run_select_device,
    summarize_gpu_device_selection_policies,
)


def test_build_gpu_device_selection_policy_registry():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_gpu_device_selection_policy_registry(profile)

    assert len(df) == 3
    assert summary["total_policies"] == 3
    assert summary["all_dry_run"] is True
    assert summary["all_cuda_init_disabled"] is True
    assert summary["non_signal"] is True


def test_dry_run_select_device():
    # Test force_cpu
    res = dry_run_select_device({"force_cpu": True})
    assert res["selected_device"] == "cpu"
    assert res["device_selection_dry_run"] is True
    assert res["real_allocation_executed"] is False
    assert res["real_training_executed"] is False
    assert res["model_fit_executed"] is False
    assert res["model_predict_executed"] is False
    assert res["non_signal"] is True

    # Test preference default
    res2 = dry_run_select_device({"device_preference": "cuda_if_available"})
    assert res2["device_selection_dry_run"] is True
    assert res2["real_allocation_executed"] is False
