# -*- coding: utf-8 -*-
"""Phase 141: Uncertainty Forbidden Column Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)

FORBIDDEN_COLUMNS_UNCERTAINTY = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "probability",
    "predict_proba",
    "confidence",
    "confidence_score",
    "calibrated_probability",
    "uncertainty",
    "prediction_interval",
    "confidence_interval",
    "quantile",
    "conformal_set",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_uncertainty_forbidden_column_policy_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for uncertainty forbidden column policies."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for col in FORBIDDEN_COLUMNS_UNCERTAINTY:
        rows.append(
            {
                "forbidden_column": col,
                "reason": "Violates non-signal, zero-target, or data boundary policies.",
                "action": "STRICT_EXCLUDE",
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_uncertainty_forbidden_column_policies(df)
    return df, summary


def validate_uncertainty_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that provided column list contains zero forbidden columns."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        if c_lower in FORBIDDEN_COLUMNS_UNCERTAINTY or any(f == c_lower for f in FORBIDDEN_COLUMNS_UNCERTAINTY):
            violations.append(col)

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "FORBIDDEN_COLUMNS_DETECTED",
        "non_signal": True,
    }


def summarize_uncertainty_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize uncertainty forbidden column policies DataFrame."""
    return {
        "total_forbidden_columns": len(df),
        "columns": df["forbidden_column"].tolist() if not df.empty else [],
        "all_excluded": bool((df["action"] == "STRICT_EXCLUDE").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }
