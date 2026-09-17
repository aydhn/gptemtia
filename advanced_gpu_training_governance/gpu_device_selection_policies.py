# -*- coding: utf-8 -*-
"""Phase 139 GPU Device Selection Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_device_selection_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build device selection policies registry without hardware allocation."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "DEV_SEL_001",
            "policy_name": "cuda_preferred_with_cpu_fallback_policy",
            "device_preference": "cuda_if_available",
            "fallback_allowed": True,
            "allow_real_cuda_initialization": False,
            "dry_run_mode": True,
            "non_signal": True,
            "description": "Selects CUDA if supported in environment, otherwise safely defaults to CPU dry-run.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "DEV_SEL_002",
            "policy_name": "strict_cpu_deterministic_selection_policy",
            "device_preference": "cpu_only",
            "fallback_allowed": False,
            "allow_real_cuda_initialization": False,
            "dry_run_mode": True,
            "non_signal": True,
            "description": "Deterministic CPU selection for isolated local testing without accelerator dependencies.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "DEV_SEL_003",
            "policy_name": "mps_apple_silicon_placeholder_policy",
            "device_preference": "mps_if_available",
            "fallback_allowed": True,
            "allow_real_cuda_initialization": False,
            "dry_run_mode": True,
            "non_signal": True,
            "description": "Placeholder policy for Apple Silicon MPS environments with mandatory CPU fallback.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_gpu_device_selection_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def dry_run_select_device(request: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Simulate device selection in dry-run mode without real tensor/hardware initialization."""
    req = request or {}
    preference = req.get("device_preference", "cuda_if_available")
    force_cpu = req.get("force_cpu", False)

    # Check environment without allocating
    try:
        import torch
        cuda_available = bool(torch.cuda.is_available())
    except ImportError:
        cuda_available = False

    if force_cpu or not cuda_available:
        selected_device = "cpu"
        selection_reason = "would_fallback_cpu" if preference != "cpu_only" else "cpu_requested"
    else:
        selected_device = "cuda:0"
        selection_reason = "would_use_cuda_if_available"

    return {
        "requested_preference": preference,
        "selected_device": selected_device,
        "selection_reason": selection_reason,
        "device_selection_dry_run": True,
        "real_allocation_executed": False,
        "real_training_executed": False,
        "model_fit_executed": False,
        "model_predict_executed": False,
        "non_signal": True,
        "status": "gpu_governance_ready",
    }


def summarize_gpu_device_selection_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize device selection policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_dry_run": bool((df["dry_run_mode"] == True).all()),
        "all_cuda_init_disabled": bool((df["allow_real_cuda_initialization"] == False).all()),
        "current_phase": 139,
        "non_signal": True,
    }
