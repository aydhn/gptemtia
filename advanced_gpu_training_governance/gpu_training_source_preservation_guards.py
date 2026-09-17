# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Source Preservation Guards."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_DESTRUCTIVE_ACTIONS: List[str] = [
    "overwrite",
    "delete",
    "move",
    "destructive_clean",
    "auto_impute",
    "auto_drop",
    "drop_na",
    "truncate_source",
    "wipe_catalog",
]


def build_gpu_training_source_preservation_guard_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build source preservation guard registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    guards = [
        {
            "guard_id": "SRC_GRD_001",
            "guard_name": "source_overwrite_guard",
            "check_type": "filesystem_integrity",
            "enforced": True,
            "non_signal": True,
            "description": "Prevents writing over original DataLake/FeatureStore raw sources.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "SRC_GRD_002",
            "guard_name": "file_deletion_guard",
            "check_type": "filesystem_integrity",
            "enforced": True,
            "non_signal": True,
            "description": "Blocks any rm, unlink, or deletion commands on existing tables.",
            "status": "gpu_governance_ready",
        },
        {
            "guard_id": "SRC_GRD_003",
            "guard_name": "auto_imputation_guard",
            "check_type": "data_integrity",
            "enforced": True,
            "non_signal": True,
            "description": "Blocks silent fillna/imputation that hides data gaps.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(guards)
    summary = summarize_gpu_training_source_preservation_guards(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_training_source_preservation_action(action: str) -> Dict[str, Any]:
    """Validate that an action does not perform destructive source modification."""
    a_lower = action.lower()
    blocked = False
    violating_actions = []

    for forbidden in FORBIDDEN_DESTRUCTIVE_ACTIONS:
        if forbidden in a_lower:
            blocked = True
            violating_actions.append(forbidden)

    return {
        "action": action,
        "is_safe": not blocked,
        "blocked": blocked,
        "violating_actions": violating_actions,
        "non_signal": True,
        "status": "BLOCKED_DESTRUCTIVE" if blocked else "SAFE_OPERATION",
    }


def summarize_gpu_training_source_preservation_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize source preservation guards DataFrame."""
    if df.empty:
        return {"total_guards": 0, "non_signal": True}
    return {
        "total_guards": len(df),
        "all_enforced": bool((df["enforced"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
