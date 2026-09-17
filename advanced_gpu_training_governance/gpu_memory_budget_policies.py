# -*- coding: utf-8 -*-
"""Phase 139 GPU Memory Budget Policies."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_memory_budget_policy_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build memory budget policies registry."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    policies = [
        {
            "policy_id": "MEM_POL_001",
            "policy_name": "conservative_gpu_memory_budget_policy",
            "max_memory_fraction": 0.70,
            "reserved_system_mb": 2048,
            "enable_memory_guard": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Conservative cap keeping 30% VRAM free and reserving 2GB for OS/system processes.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "MEM_POL_002",
            "policy_name": "standard_gpu_memory_budget_policy",
            "max_memory_fraction": 0.80,
            "reserved_system_mb": 1536,
            "enable_memory_guard": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "Standard 80% VRAM ceiling with pre-allocation safety guard.",
            "status": "gpu_governance_ready",
        },
        {
            "policy_id": "MEM_POL_003",
            "policy_name": "strict_low_memory_footprint_policy",
            "max_memory_fraction": 0.50,
            "reserved_system_mb": 4096,
            "enable_memory_guard": True,
            "dry_run_only": True,
            "non_signal": True,
            "description": "High safety memory budget for shared workstation environments.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(policies)
    summary = summarize_gpu_memory_budget_policies(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_gpu_memory_budget_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate a requested memory fraction or budget against governance caps."""
    if isinstance(request, str):
        req_dict = {"requested_fraction": 0.80, "note": request}
    else:
        req_dict = request or {}

    fraction = float(req_dict.get("requested_fraction", 0.80))
    blocked = False
    violations = []

    if fraction > 0.85:
        blocked = True
        violations.append(f"requested fraction {fraction} exceeds hard limit 0.85")
    if fraction <= 0.0:
        blocked = True
        violations.append(f"requested fraction {fraction} must be > 0.0")

    return {
        "requested_fraction": fraction,
        "is_valid": not blocked,
        "blocked": blocked,
        "violations": violations,
        "dry_run_only": True,
        "real_memory_allocated": False,
        "non_signal": True,
    }


def summarize_gpu_memory_budget_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize memory budget policies DataFrame."""
    if df.empty:
        return {"total_policies": 0, "non_signal": True}
    return {
        "total_policies": len(df),
        "all_dry_run": bool((df["dry_run_only"] == True).all()),
        "max_fraction_limit": float(df["max_memory_fraction"].max()) if "max_memory_fraction" in df.columns else 0.80,
        "current_phase": 139,
        "non_signal": True,
    }
