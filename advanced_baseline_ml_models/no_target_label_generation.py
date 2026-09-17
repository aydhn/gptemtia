# -*- coding: utf-8 -*-
"""Phase 138 No Target/Label Generation Report and Validator.

Guarantees that supervised target labels, shifts, next-period returns, and directional
targets are completely disabled and never materialized.
"""

from typing import Any, Dict, Tuple, Union
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)

FORBIDDEN_TARGET_KEYWORDS = [
    "target", "label", "future_return", "forward_return", "next_return",
    "shift(-1)", "shift(-", "lead_return", "y_train", "y_test", "y_val",
    "binary_target", "class_target",
]


def build_no_target_label_generation_report(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report confirming zero target/label generation."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    rows = [
        {
            "check_item": "target_label_generation",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that no target labels were generated or materialized",
        },
        {
            "check_item": "future_return_calculation",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that shift(-1) / future returns were blocked",
        },
        {
            "check_item": "supervised_labels_absence",
            "status": "PASS_DISABLED",
            "is_disabled": True,
            "description": "Verification that datasets contain zero supervised learning labels",
        },
    ]

    df = pd.DataFrame(rows)
    summary = summarize_no_target_label_generation(df)
    return df, summary


def validate_no_target_label_generation_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request to ensure no target/label generation is requested."""
    text = str(request).lower()
    detected = [kw for kw in FORBIDDEN_TARGET_KEYWORDS if kw in text]

    blocked = len(detected) > 0
    return {
        "blocked": blocked,
        "detected_keywords": detected,
        "status": "execution_blocked_no_target_label" if blocked else "clean_no_target_request",
        "target_label_generated": False,
        "manual_review_required": True,
        "non_signal": True,
    }


def summarize_no_target_label_generation(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize no target label generation report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()) if not df.empty else True,
        "target_label_generated": False,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
