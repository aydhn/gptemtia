# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Harness Interfaces."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_gpu_training_harness_interface_registry(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build interface contracts defining simulation, guards, and safety verification."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    interfaces = [
        {
            "interface_name": "validate_resource_policy",
            "interface_type": "pre_execution_check",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Validates that resource limits and execution mode conform to contract_only rules.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "validate_device_policy",
            "interface_type": "hardware_check",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Verifies target device preferences and ensures CPU fallback rules are configured.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "validate_memory_policy",
            "interface_type": "memory_guard",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Ensures requested memory budget does not exceed maximum VRAM threshold.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "validate_timeout_policy",
            "interface_type": "watchdog_guard",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Enforces upper duration limit and watchdog heartbeat contracts.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "validate_input_guards",
            "interface_type": "input_guard",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Checks for absence of lookahead columns, raw news text, and destructive actions.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "simulate_harness_without_training",
            "interface_type": "dry_run_simulation",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Executes full dry-run harness pipeline without training, fit, or inference calls.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "return_blocked_execution_status",
            "interface_type": "safety_block",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Returns deterministic blocked execution status when training or prediction is requested.",
            "status": "gpu_governance_ready",
        },
        {
            "interface_name": "build_resource_audit_placeholder",
            "interface_type": "audit_placeholder",
            "enforces_dry_run": True,
            "real_training_allowed": False,
            "description": "Constructs structured audit record capturing simulated hardware and memory metrics.",
            "status": "gpu_governance_ready",
        },
    ]

    df = pd.DataFrame(interfaces)
    summary = summarize_gpu_training_harness_interfaces(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_harness_interfaces(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize GPU training harness interfaces DataFrame."""
    if df.empty:
        return {"total_interfaces": 0, "non_signal": True}
    return {
        "total_interfaces": len(df),
        "all_enforces_dry_run": bool((df["enforces_dry_run"] == True).all()),
        "all_real_training_disabled": bool((df["real_training_allowed"] == False).all()),
        "current_phase": 139,
        "non_signal": True,
    }
