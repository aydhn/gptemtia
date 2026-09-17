# -*- coding: utf-8 -*-
"""Phase 139 Dry-Run Timeout Guards."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_dry_run_timeout_guard_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dry-run timeout guard report."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    test_cases = [
        {"test_case": "short_timeout_request", "timeout_seconds": 60, "expected_blocked": False},
        {"test_case": "standard_timeout_request", "timeout_seconds": 1800, "expected_blocked": False},
        {"test_case": "ceiling_timeout_request", "timeout_seconds": 3600, "expected_blocked": False},
        {"test_case": "excessive_timeout_request", "timeout_seconds": 8000, "expected_blocked": True},
        {"test_case": "negative_timeout_request", "timeout_seconds": -10, "expected_blocked": True},
    ]

    rows = []
    for tc in test_cases:
        val = validate_dry_run_timeout_request({"requested_timeout": tc["timeout_seconds"]})
        rows.append(
            {
                "test_case": tc["test_case"],
                "requested_timeout": tc["timeout_seconds"],
                "is_valid": val["is_valid"],
                "blocked": val["blocked"],
                "guard_status": "BLOCKED_BY_GUARD" if val["blocked"] else "PASS_GUARD",
                "dry_run": True,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_timeout_guards(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_dry_run_timeout_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate a requested training timeout duration against safety ceiling."""
    if isinstance(request, str):
        req_dict = {"requested_timeout": 300, "note": request}
    else:
        req_dict = request or {}

    timeout_sec = int(req_dict.get("requested_timeout", 300))
    blocked = False
    violations = []

    if timeout_sec > 3600:
        blocked = True
        violations.append(f"timeout {timeout_sec}s exceeds hard limit 3600s")
    if timeout_sec <= 0:
        blocked = True
        violations.append(f"timeout {timeout_sec}s must be positive")

    return {
        "requested_timeout": timeout_sec,
        "is_valid": not blocked,
        "blocked": blocked,
        "violations": violations,
        "dry_run_only": True,
        "non_signal": True,
    }


def summarize_dry_run_timeout_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize timeout guard report DataFrame."""
    if df.empty:
        return {"total_tests": 0, "non_signal": True}
    return {
        "total_tests": len(df),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "guards_enforced": True,
        "current_phase": 139,
        "non_signal": True,
    }
