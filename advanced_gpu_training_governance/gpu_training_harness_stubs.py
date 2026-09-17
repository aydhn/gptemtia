# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Harness Stubs."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_harness_stub_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of GPU training harness stubs."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    stubs = [
        {
            "stub_id": "HARN_STUB_001",
            "stub_name": "default_dry_run_harness_stub",
            "dry_run": True,
            "resource_policy_validated": True,
            "device_selection_dry_run": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "target_label_generated": False,
            "artifact_persisted": False,
            "model_registry_written": False,
            "blocked_by_policy": True,
            "blocked_reason": "Phase 139 strict dry-run resource governance boundary",
            "manual_review_required": True,
            "status": "execution_blocked_no_real_training",
        },
        {
            "stub_id": "HARN_STUB_002",
            "stub_name": "strict_safety_harness_stub",
            "dry_run": True,
            "resource_policy_validated": True,
            "device_selection_dry_run": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "target_label_generated": False,
            "artifact_persisted": False,
            "model_registry_written": False,
            "blocked_by_policy": True,
            "blocked_reason": "Absolute zero-training enforcement policy",
            "manual_review_required": True,
            "status": "execution_blocked_no_real_training",
        },
        {
            "stub_id": "HARN_STUB_003",
            "stub_name": "pre_phase_140_harness_stub",
            "dry_run": True,
            "resource_policy_validated": True,
            "device_selection_dry_run": True,
            "real_training_executed": False,
            "model_fit_executed": False,
            "model_predict_executed": False,
            "target_label_generated": False,
            "artifact_persisted": False,
            "model_registry_written": False,
            "blocked_by_policy": True,
            "blocked_reason": "Ensemble candidate model registry contracts pending Phase 140",
            "manual_review_required": True,
            "status": "execution_blocked_no_real_training",
        },
    ]

    df = pd.DataFrame(stubs)
    summary = summarize_gpu_training_harness_stubs(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def gpu_training_harness_stub(request: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute dry-run harness stub without training, prediction, or artifact creation."""
    req = request or {}
    model_family = req.get("model_family", "unknown_family")
    device_pref = req.get("device_preference", "cuda_if_available")

    return {
        "dry_run": True,
        "resource_policy_validated": True,
        "device_selection_dry_run": True,
        "target_device": "cuda:0" if device_pref != "cpu_only" else "cpu",
        "model_family": model_family,
        "real_training_executed": False,
        "model_fit_executed": False,
        "model_predict_executed": False,
        "model_inference_executed": False,
        "model_transform_executed": False,
        "target_label_generated": False,
        "dataset_materialized": False,
        "feature_snapshot_materialized": False,
        "artifact_persisted": False,
        "model_registry_written": False,
        "optimizer_step_executed": False,
        "backward_pass_executed": False,
        "blocked_by_policy": True,
        "blocked_reason": "Execution permanently blocked by Phase 139 GPU training governance policy",
        "manual_review_required": True,
        "non_signal": True,
        "status": "execution_blocked_no_real_training",
    }


def summarize_gpu_training_harness_stubs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize harness stubs DataFrame."""
    if df.empty:
        return {"total_stubs": 0, "non_signal": True}
    return {
        "total_stubs": len(df),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "all_real_training_disabled": bool((df["real_training_executed"] == False).all()),
        "all_model_fit_disabled": bool((df["model_fit_executed"] == False).all()),
        "all_model_predict_disabled": bool((df["model_predict_executed"] == False).all()),
        "all_blocked_by_policy": bool((df["blocked_by_policy"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
