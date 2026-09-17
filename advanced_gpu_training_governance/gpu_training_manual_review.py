# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Manual Review Queue."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_manual_review_queue(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manual review queue enforcing non-destructive human inspection."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    items = [
        {
            "item_id": "REV_001",
            "domain": "resource_policy_domain",
            "description": "Verify GPU resource policy constraints and dry-run boundaries.",
            "recommended_action": "inspect GPU resource policy",
            "priority": "HIGH",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_002",
            "domain": "device_selection_policy_domain",
            "description": "Confirm device preference and CPU fallback behaviors.",
            "recommended_action": "inspect device selection policy",
            "priority": "NORMAL",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_003",
            "domain": "memory_budget_policy_domain",
            "description": "Check memory budget fraction limits and system reserve guarantees.",
            "recommended_action": "inspect memory budget policy",
            "priority": "NORMAL",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_004",
            "domain": "timeout_policy_domain",
            "description": "Inspect watchdog timeout boundaries and heartbeat thresholds.",
            "recommended_action": "inspect timeout policy",
            "priority": "NORMAL",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_005",
            "domain": "cpu_fallback_policy_domain",
            "description": "Validate that deterministic CPU fallback functions correctly when GPU is unavailable.",
            "recommended_action": "inspect CPU fallback policy",
            "priority": "NORMAL",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_006",
            "domain": "harness_stub_domain",
            "description": "Ensure harness stubs properly block model fit and return policy-blocked status.",
            "recommended_action": "inspect dry-run harness stubs",
            "priority": "HIGH",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_007",
            "domain": "no_real_training_domain",
            "description": "Review disabled execution reports ensuring zero weight training and zero predictions.",
            "recommended_action": "inspect disabled execution reports",
            "priority": "HIGH",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
        {
            "item_id": "REV_008",
            "domain": "phase_140_handoff_domain",
            "description": "Confirm readiness prerequisites for Phase 140 candidate model registry contracts.",
            "recommended_action": "inspect Phase 140 candidate model registry blockers",
            "priority": "HIGH",
            "manual_review_required": True,
            "non_destructive": True,
            "non_signal": True,
        },
    ]

    df = pd.DataFrame(items)
    summary = summarize_gpu_training_manual_review_queue(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue DataFrame."""
    if df.empty:
        return {"total_review_items": 0, "non_signal": True}
    return {
        "total_review_items": len(df),
        "high_priority_count": int((df["priority"] == "HIGH").sum()) if "priority" in df.columns else 0,
        "all_non_destructive": bool((df["non_destructive"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
