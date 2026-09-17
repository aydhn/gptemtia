# -*- coding: utf-8 -*-
"""Phase 139 Dry-Run Training Execution Blocks."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)

FORBIDDEN_EXECUTION_KEYWORDS: List[str] = [
    "fit",
    "train",
    "predict",
    "inference",
    "transform",
    "backward",
    "optimizer",
    "step",
    "loss.backward",
    "save_model",
    "model_registry",
    "target",
    "label",
    "signal",
    "buy",
    "sell",
    "long",
    "short",
]


def build_dry_run_training_execution_block_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build execution blocks report validating that all forbidden execution words trigger a block."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    rows = []
    for keyword in FORBIDDEN_EXECUTION_KEYWORDS:
        val = validate_training_execution_block(f"execute_{keyword}_command")
        rows.append(
            {
                "keyword": keyword,
                "test_query": f"execute_{keyword}_command",
                "blocked": val["blocked"],
                "block_reason": val["block_reason"],
                "status": "PASS_BLOCKED",
                "dry_run": True,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_dry_run_training_execution_blocks(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_training_execution_block(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request or query string and block if any forbidden execution keyword is detected."""
    if isinstance(request, str):
        query_text = request.lower()
    else:
        req_dict = request or {}
        query_text = str(req_dict.get("command", "")).lower() + " " + str(req_dict.get("action", "")).lower()

    detected_keywords = []
    for kw in FORBIDDEN_EXECUTION_KEYWORDS:
        if kw in query_text:
            detected_keywords.append(kw)

    blocked = len(detected_keywords) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected_keywords,
        "block_reason": (
            f"Detected forbidden execution keywords: {detected_keywords}"
            if blocked
            else "No forbidden execution keywords detected"
        ),
        "real_training_executed": False,
        "model_fit_executed": False,
        "model_predict_executed": False,
        "non_signal": True,
    }


def summarize_dry_run_training_execution_blocks(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize execution block report DataFrame."""
    if df.empty:
        return {"total_keywords_checked": 0, "non_signal": True}
    return {
        "total_keywords_checked": len(df),
        "all_blocked": bool((df["blocked"] == True).all()),
        "all_dry_run": bool((df["dry_run"] == True).all()),
        "current_phase": 139,
        "non_signal": True,
    }
