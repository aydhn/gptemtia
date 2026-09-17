# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Resource Policies."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_resource_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build resource policies registry ensuring contract-only execution."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "RES_POL_001",
            "policy_name": "gpu_training_strict_resource_cap_policy",
            "resource_type": "gpu",
            "allowed_mode": "contract_only",
            "dry_run_required": True,
            "local_only": True,
            "non_production": True,
            "real_training_allowed": False,
            "prediction_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "max_runtime_seconds_placeholder": 3600,
            "max_memory_fraction_placeholder": 0.80,
            "manual_review_required": True,
            "description": "Standard GPU resource policy capping runtime to 1h and memory to 80% dry-run placeholder.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "RES_POL_002",
            "policy_name": "cpu_training_resource_fallback_policy",
            "resource_type": "cpu",
            "allowed_mode": "contract_only",
            "dry_run_required": True,
            "local_only": True,
            "non_production": True,
            "real_training_allowed": False,
            "prediction_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "max_runtime_seconds_placeholder": 1800,
            "max_memory_fraction_placeholder": 0.50,
            "manual_review_required": True,
            "description": "CPU fallback policy capping core usage and thread count in dry-run contract mode.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "RES_POL_003",
            "policy_name": "memory_oom_guard_governance_policy",
            "resource_type": "memory",
            "allowed_mode": "contract_only",
            "dry_run_required": True,
            "local_only": True,
            "non_production": True,
            "real_training_allowed": False,
            "prediction_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "max_runtime_seconds_placeholder": 3600,
            "max_memory_fraction_placeholder": 0.75,
            "manual_review_required": True,
            "description": "Strict OOM prevention policy requiring reserved headroom before simulated allocations.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "RES_POL_004",
            "policy_name": "timeout_watchdog_governance_policy",
            "resource_type": "timeout",
            "allowed_mode": "contract_only",
            "dry_run_required": True,
            "local_only": True,
            "non_production": True,
            "real_training_allowed": False,
            "prediction_allowed": False,
            "artifact_persistence_allowed": False,
            "model_registry_write_allowed": False,
            "max_runtime_seconds_placeholder": 300,
            "max_memory_fraction_placeholder": 0.80,
            "manual_review_required": True,
            "description": "Watchdog timeout policy blocking any loop that exceeds simulated duration.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_gpu_training_resource_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_training_resource_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """Validate a single resource policy against Phase 139 limits."""
    violations = []
    if policy.get("allowed_mode") != "contract_only":
        violations.append("allowed_mode must be contract_only")
    if not policy.get("dry_run_required", False):
        violations.append("dry_run_required must be True")
    if policy.get("real_training_allowed", True):
        violations.append("real_training_allowed must be False")
    if policy.get("prediction_allowed", True):
        violations.append("prediction_allowed must be False")
    if policy.get("artifact_persistence_allowed", True):
        violations.append("artifact_persistence_allowed must be False")
    if policy.get("model_registry_write_allowed", True):
        violations.append("model_registry_write_allowed must be False")

    return {
        "policy_name": policy.get("policy_name", "unknown"),
        "is_valid": len(violations) == 0,
        "violations": violations,
        "non_signal": True,
    }


def summarize_gpu_training_resource_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize resource policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_contract_only": bool((df["allowed_mode"] == "contract_only").all()),
        "all_real_training_disabled": bool((df["real_training_allowed"] == False).all()),
        "all_prediction_disabled": bool((df["prediction_allowed"] == False).all()),
        "all_manual_review_required": bool((df["manual_review_required"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
