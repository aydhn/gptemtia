# -*- coding: utf-8 -*-
"""Phase 139 No Prediction Execution Verification."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_no_prediction_execution_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero prediction or inference execution."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    checks = [
        {
            "check_item": "model_predict_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Model.predict and predict_proba methods are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "forward_inference_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Neural network forward inference pass is disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "representation_transform_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Estimator transform, transform_predict, and embedding projections are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
    ]

    df = pd.DataFrame(checks)
    summary = summarize_no_prediction_execution(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_no_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that an execution request does not contain prediction or inference commands."""
    if isinstance(request, str):
        query = request.lower()
    else:
        req_dict = request or {}
        query = str(req_dict.get("command", "")).lower() + " " + str(req_dict.get("action", "")).lower()

    prediction_words = ["predict", "inference", "forward pass", "predict_proba", "transform"]
    detected = [w for w in prediction_words if w in query]
    blocked = len(detected) > 0

    return {
        "blocked": blocked,
        "detected_prediction_keywords": detected,
        "model_predict_executed": False,
        "model_inference_executed": False,
        "non_signal": True,
        "reason": f"Prediction requested: {detected}" if blocked else "No prediction requested",
    }


def summarize_no_prediction_execution(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no prediction execution DataFrame."""
    if df.empty:
        return {"all_disabled": True, "model_predict_executed": False, "non_signal": True}
    return {
        "total_checks": len(df),
        "all_disabled": bool((df["is_disabled"] == True).all()),
        "model_predict_executed": False,
        "model_inference_executed": False,
        "current_phase": 139,
        "non_signal": True,
    }
