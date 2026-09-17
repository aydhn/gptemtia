# -*- coding: utf-8 -*-
"""Phase 139 Batch Size Placeholder Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_batch_size_placeholder_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build batch size placeholder policy registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "BAT_POL_001",
            "policy_name": "small_batch_placeholder_policy",
            "placeholder_batch_size": 16,
            "min_batch_size": 8,
            "max_batch_size": 32,
            "execution_allowed": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Small batch size configuration contract for low memory environments.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "BAT_POL_002",
            "policy_name": "standard_batch_placeholder_policy",
            "placeholder_batch_size": 32,
            "min_batch_size": 16,
            "max_batch_size": 64,
            "execution_allowed": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Standard batch size configuration contract for baseline tabular/sequence architectures.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "BAT_POL_003",
            "policy_name": "large_batch_placeholder_policy",
            "placeholder_batch_size": 64,
            "min_batch_size": 32,
            "max_batch_size": 128,
            "execution_allowed": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Large batch placeholder contract with gradient accumulation placeholder metadata.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_batch_size_placeholder_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_batch_size_placeholder_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize batch size placeholder policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_execution_disabled": bool((df["execution_allowed"] == False).all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
