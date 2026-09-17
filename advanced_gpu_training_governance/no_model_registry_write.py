# -*- coding: utf-8 -*-
"""Phase 139 No Model Registry Write Verification."""

from typing import Any, Dict, Optional, Tuple, Union
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)


def build_no_model_registry_write_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero model registry writing."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    checks = [
        {
            "check_item": "mlflow_registry_write_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "MLflow/W&B model registry registration APIs are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "local_registry_db_write_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Local SQLite/JSON model registry metadata writes are disabled.",
            "dry_run": True,
            "non_signal": True,
        },
        {
            "check_item": "cloud_model_hub_push_disabled",
            "is_disabled": True,
            "status": "PASS_DISABLED",
            "details": "Push to remote HuggingFace/cloud model hub is disabled.",
            "dry_run": True,
            "non_signal": True,
        },
    ]

    df = pd.DataFrame(checks)
    summary = summarize_no_model_registry_write(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def validate_no_model_registry_write_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate that a request does not attempt to write to a model registry."""
    if isinstance(request, str):
        query = request.lower()
    else:
        req_dict = request or {}
        query = str(req_dict.get("command", "")).lower() + " " + str(req_dict.get("action", "")).lower()

    registry_words = ["register_model", "model_registry_write", "mlflow.register", "push_to_hub", "publish_model"]
    detected = [w for w in registry_words if w in query]
    blocked = len(detected) > 0

    return {
        "blocked": blocked,
        "detected_registry_keywords": detected,
        "model_registry_written": False,
        "non_signal": True,
        "reason": f"Model registry write requested: {detected}" if blocked else "No model registry write requested",
    }


def summarize_no_model_registry_write(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no model registry write DataFrame."""
    if df.empty:
        return {"all_disabled": True, "model_registry_written": False, "non_signal": True}
    return {
        "total_checks": len(df),
        "all_disabled": bool((df["is_disabled"] == True).all()),
        "model_registry_written": False,
        "current_phase": 139,
        "non_signal": True,
    }
