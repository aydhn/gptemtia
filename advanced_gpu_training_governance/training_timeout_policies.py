# -*- coding: utf-8 -*-
"""Phase 139 Training Timeout Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_training_timeout_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build timeout policy registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "TMO_POL_001",
            "policy_name": "short_loop_dry_run_timeout_policy",
            "max_timeout_seconds": 300,
            "heartbeat_interval_seconds": 15,
            "terminate_on_timeout": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "5-minute cap for short iteration harness tests.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "TMO_POL_002",
            "policy_name": "standard_epoch_budget_timeout_policy",
            "max_timeout_seconds": 1800,
            "heartbeat_interval_seconds": 60,
            "terminate_on_timeout": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "30-minute cap for multi-split simulated training harnesses.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "TMO_POL_003",
            "policy_name": "ceiling_hard_kill_timeout_policy",
            "max_timeout_seconds": 3600,
            "heartbeat_interval_seconds": 120,
            "terminate_on_timeout": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "1-hour absolute ceiling watchdog enforcing termination of runaway loops.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_training_timeout_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_training_timeout_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a timeout policy against Phase 139 limits."""
    timeout_sec = policy.get("max_timeout_seconds", 3600)
    violations = []
    if timeout_sec > 7200:
        violations.append(f"timeout {timeout_sec} exceeds absolute maximum 7200s")
    if timeout_sec <= 0:
        violations.append(f"timeout {timeout_sec} must be > 0s")
    if not policy.get("terminate_on_timeout", False):
        violations.append("terminate_on_timeout must be True")

    return {
        "policy_name": policy.get("policy_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
        "non_signal": True,
    }


def summarize_training_timeout_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize timeout policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "max_ceiling_seconds": int(df["max_timeout_seconds"].max()) if "max_timeout_seconds" in df.columns else 3600,
        "all_terminate_on_timeout": bool((df["terminate_on_timeout"] == True).all()),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
