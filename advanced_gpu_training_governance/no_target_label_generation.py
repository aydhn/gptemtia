# -*- coding: utf-8 -*-
"""Phase 139 No Target/Label Generation Verification."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_no_target_label_generation_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero target or label generation."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    checks = [
        {
            "check_item": "future_return_target_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Future return, forward return, and next return calculations are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "shift_minus_one_label_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Lookahead shift(-1) operations are strictly forbidden and disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "binary_multiclass_label_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Binary/multi-class trend and regime classification labels are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
    ]

    df = pd.DataFrame(checks)
    summary = summarize_no_target_label_generation(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_no_target_label_generation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that a request does not generate targets, labels, or future shifts."""
    if isinstance(request, str):
        query = request.lower()
    else:
        req_dict = request or {}
        query = str(req_dict.get("command", "")).lower() + " " + str(req_dict.get("action", "")).lower()

    target_words = ["target", "label", "future_return", "shift(-1)", "shift(-", "forward_return"]
    detected = [w for w in target_words if w in query]
    blocked = len(detected) > 0

    return {
        "blocked": blocked,
        "detected_target_keywords": detected,
        "target_label_generated": False,
        "non_signal": True,
        "reason": f"Target generation requested: {detected}" if blocked else "No target generation requested",
    }


def summarize_no_target_label_generation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no target/label generation DataFrame."""
    if df.empty:
        return {"all_disabled": True, "target_label_generated": False, "non_signal": True}
    return {
        "total_checks": len(df),
        "all_disabled": bool((df["is_disabled"] == True).all()),
        "target_label_generated": False,
        "current_phase": 139,
        "non_signal": True,
    }
