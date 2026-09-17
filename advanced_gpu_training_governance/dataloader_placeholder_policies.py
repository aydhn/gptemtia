# -*- coding: utf-8 -*-
"""Phase 139 Dataloader Placeholder Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_dataloader_placeholder_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataloader placeholder policy registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "DL_POL_001",
            "policy_name": "sequential_time_series_dataloader_placeholder",
            "shuffle_allowed": False,
            "num_workers_placeholder": 0,
            "pin_memory_placeholder": False,
            "reads_real_data": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Chronological sequential iteration placeholder strictly forbidding shuffling to avoid lookahead.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "DL_POL_002",
            "policy_name": "purged_walk_forward_dataloader_placeholder",
            "shuffle_allowed": False,
            "num_workers_placeholder": 0,
            "pin_memory_placeholder": False,
            "reads_real_data": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Purged walk-forward split iteration contract for future cross-validation phases.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "DL_POL_003",
            "policy_name": "zero_copy_in_memory_dataloader_placeholder",
            "shuffle_allowed": False,
            "num_workers_placeholder": 0,
            "pin_memory_placeholder": False,
            "reads_real_data": False,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Zero-copy in-memory placeholder policy enforcing non-disk serialization constraints.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_dataloader_placeholder_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_dataloader_placeholder_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dataloader placeholder policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_reads_real_data_disabled": bool((df["reads_real_data"] == False).all()),
        "all_shuffle_disabled": bool((df["shuffle_allowed"] == False).all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
