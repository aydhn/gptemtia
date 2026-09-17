# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Resource Audit Placeholders."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_resource_audit_placeholder_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build resource audit placeholder registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    placeholders = [
        {
            "resource_audit_id_placeholder": "RES_AUDIT_PH_001",
            "device_selection_policy_ref": "DEV_SEL_001",
            "memory_budget_policy_ref": "MEM_POL_001",
            "timeout_policy_ref": "TMO_POL_001",
            "cpu_fallback_policy_ref": "CPU_FB_001",
            "dry_run_only": True,
            "real_training_executed": False,
            "artifact_persisted": False,
            "manual_review_required": True,
            "non_signal": True,
            "status": "gpu_governance_ready",
        },
        {
            "resource_audit_id_placeholder": "RES_AUDIT_PH_002",
            "device_selection_policy_ref": "DEV_SEL_002",
            "memory_budget_policy_ref": "MEM_POL_002",
            "timeout_policy_ref": "TMO_POL_002",
            "cpu_fallback_policy_ref": "CPU_FB_002",
            "dry_run_only": True,
            "real_training_executed": False,
            "artifact_persisted": False,
            "manual_review_required": True,
            "non_signal": True,
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(placeholders)
    summary = summarize_gpu_training_resource_audit_placeholders(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_resource_audit_placeholders(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize resource audit placeholders DataFrame."""
    if df.empty:
        return {"total_placeholders": 0, "non_signal": True}
    return {
        "total_placeholders": len(df),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "all_training_disabled": bool((df["real_training_executed"] == False).all()),
        "all_artifact_disabled": bool((df["artifact_persisted"] == False).all()),
        "current_phase": 139,
        "non_signal": True,
    }
