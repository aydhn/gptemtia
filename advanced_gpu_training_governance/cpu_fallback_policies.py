# -*- coding: utf-8 -*-
"""Phase 139 CPU Fallback Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_cpu_fallback_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build CPU fallback policy registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "CPU_FB_001",
            "policy_name": "auto_cpu_fallback_on_gpu_absence_policy",
            "allow_cpu_fallback": True,
            "fallback_priority": "cpu",
            "max_cpu_threads_placeholder": 4,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Automatically falls back to CPU dry-run contracts if CUDA runtime is absent.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "CPU_FB_002",
            "policy_name": "oom_gpu_to_cpu_evacuation_policy",
            "allow_cpu_fallback": True,
            "fallback_priority": "cpu",
            "max_cpu_threads_placeholder": 2,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Simulated fallback to CPU when GPU memory fraction request exceeds safety budget.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "CPU_FB_003",
            "policy_name": "single_thread_deterministic_cpu_policy",
            "allow_cpu_fallback": True,
            "fallback_priority": "cpu",
            "max_cpu_threads_placeholder": 1,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Single-threaded deterministic fallback policy for strict reproducibility checks.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_cpu_fallback_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_cpu_fallback_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize CPU fallback policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_fallback_allowed": bool((df["allow_cpu_fallback"] == True).all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
