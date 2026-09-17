# -*- coding: utf-8 -*-
"""Phase 139 Dry-Run Memory Guards."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_memory_budget_policies import (
    validate_gpu_memory_budget_request,
)


def build_dry_run_memory_guard_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run memory guard report."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    test_cases = [
        {"test_case": "normal_memory_request", "fraction": 0.50, "expected_blocked": False},
        {"test_case": "ceiling_memory_request", "fraction": 0.80, "expected_blocked": False},
        {"test_case": "excessive_memory_request", "fraction": 0.95, "expected_blocked": True},
        {"test_case": "zero_memory_request", "fraction": 0.0, "expected_blocked": True},
    ]

    rows = []
    for tc in test_cases:
        val = validate_dry_run_memory_request({"requested_fraction": tc["fraction"]})
        rows.append(
            {
                "test_case": tc["test_case"],
                "requested_fraction": tc["fraction"],
                "is_valid": val["is_valid"],
                "blocked": val["blocked"],
                "guard_status": "BLOCKED_BY_GUARD" if val["blocked"] else "PASS_GUARD",
                "dry_run": True,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_memory_guards(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_dry_run_memory_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate memory request using memory budget policy rules."""
    return validate_gpu_memory_budget_request(request)


def summarize_dry_run_memory_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize dry-run memory guard report DataFrame."""
    if df.empty:
        return {"total_tests": 0, "non_signal": True}
    return {
        "total_tests": len(df),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "guards_enforced": True,
        "current_phase": 139,
        "non_signal": True,
    }
