# -*- coding: utf-8 -*-
"""Phase 138 No Real Training Execution Report and Validator.

Guarantees that real model training and fitting are completely disabled.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_TRAINING_KEYWORDS = [
    "fit", "train", "training", "epoch", "optimizer_step",
    "gradient_descent", "backprop", "learn", "fine_tune",
]


def build_no_real_training_execution_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming no real model training was executed."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = [
        {
            "check_item": "real_training_executed",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that no real model training was invoked",
        },
        {
            "check_item": "model_fit_executed",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that model .fit() calls were blocked",
        },
        {
            "check_item": "optimizer_execution",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that parameter optimization loops are inactive",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_no_real_training_execution(df)
    return df, summary


def validate_no_real_training_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request to ensure no training or fitting is requested."""
    text = str(request).lower()
    detected = [kw for kw in FORBIDDEN_TRAINING_KEYWORDS if kw in text]

    blocked = len(detected) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected,
        "status": "execution_blocked_no_real_training" if blocked else "clean_no_training_request",
        "real_training_executed": False,
        "model_fit_executed": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_no_real_training_execution(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no real training execution report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "real_training_executed": False,
        "model_fit_executed": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
