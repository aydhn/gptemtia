# -*- coding: utf-8 -*-
"""Phase 139 Dry-Run Device Selection Report."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_device_selection_policies import (
    dry_run_select_device,
)


def build_dry_run_device_selection_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run device selection report comparing standard simulated requests."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    test_requests = [
        {"request_id": "REQ_DEV_001", "device_preference": "cuda_if_available", "force_cpu": False},
        {"request_id": "REQ_DEV_002", "device_preference": "cpu_only", "force_cpu": True},
        {"request_id": "REQ_DEV_003", "device_preference": "mps_if_available", "force_cpu": False},
    ]

    rows = []
    for req in test_requests:
        res = dry_run_select_device(req)
        rows.append(
            {
                "request_id": req["request_id"],
                "requested_preference": req["device_preference"],
                "selected_device": res["selected_device"],
                "selection_reason": res["selection_reason"],
                "dry_run": True,
                "real_allocation": False,
                "non_signal": True,
                "status": "gpu_governance_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_device_selection(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_dry_run_device_selection(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize device selection report DataFrame."""
    if df.empty:
        return {"total_simulations": 0, "non_signal": True}
    return {
        "total_simulations": len(df),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "all_zero_allocation": bool((df["real_allocation"] == False).all()),
        "current_phase": 139,
        "non_signal": True,
    }
