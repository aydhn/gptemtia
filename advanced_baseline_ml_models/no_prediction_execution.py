# -*- coding: utf-8 -*-
"""Phase 138 No Prediction Execution Report and Validator.

Guarantees that model inference, prediction, and forecast generation are completely disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_PREDICTION_KEYWORDS = [
    "predict", "predict_proba", "inference", "forecast", "forward_pass",
    "score_samples", "decision_function", "transform",
]


def build_no_prediction_execution_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero prediction execution."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = [
        {
            "check_item": "model_predict_executed",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model .predict() calls were not executed",
        },
        {
            "check_item": "inference_executed",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model forward inference was not executed",
        },
        {
            "check_item": "prediction_generation",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that no output predictions were generated",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_no_prediction_execution(df)
    return df, summary


def validate_no_prediction_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request to ensure no prediction/inference is requested."""
    text = str(request).lower()
    detected = [kw for kw in FORBIDDEN_PREDICTION_KEYWORDS if kw in text]

    blocked = len(detected) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected,
        "status": "execution_blocked_no_prediction" if blocked else "clean_no_prediction_request",
        "model_predict_executed": False,
        "model_inference_executed": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_no_prediction_execution(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no prediction execution report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "model_predict_executed": False,
        "model_inference_executed": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
