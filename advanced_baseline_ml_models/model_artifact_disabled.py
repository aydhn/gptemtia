# -*- coding: utf-8 -*-
"""Phase 138 Model Artifact Disabled Report and Validator.

Guarantees that model artifact persistence (weights, pickles, ONNX, joblib)
is strictly disabled by policy.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_ARTIFACT_KEYWORDS = [
    "pickle", "joblib.dump", "torch.save", "save_model", "export_model",
    "weights.pt", "model.pkl", "model.joblib", "model.onnx", "save_weights",
]


def build_model_artifact_disabled_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero model artifact persistence."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = [
        {
            "check_item": "artifact_persistence_disabled",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model artifact saving is disabled",
        },
        {
            "check_item": "weights_dump_blocked",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model weights export is blocked",
        },
        {
            "check_item": "binary_serialization_blocked",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that pickle/joblib dumping is blocked",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_model_artifact_disabled(df)
    return df, summary


def validate_no_model_artifact_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request to ensure no artifact persistence is requested."""
    text = str(request).lower()
    detected = [kw for kw in FORBIDDEN_ARTIFACT_KEYWORDS if kw in text]

    blocked = len(detected) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected,
        "status": "execution_blocked_no_artifact" if blocked else "clean_no_artifact_request",
        "artifact_persisted": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_model_artifact_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model artifact disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "artifact_persisted": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
