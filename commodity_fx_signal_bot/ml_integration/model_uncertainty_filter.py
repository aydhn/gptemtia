"""
Model Uncertainty Filter

Detects and reports highly uncertain ML context.
"""

import pandas as pd
from typing import Tuple, Dict, Union, Optional

from .integration_config import MLIntegrationProfile


def detect_high_ml_uncertainty(
    ml_row: Union[pd.Series, Dict, None], profile: MLIntegrationProfile
) -> dict:
    """Detect if ML prediction context has high uncertainty."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty) or pd.isna(ml_row.get("uncertainty_score", pd.NA)):
        return {
            "ml_uncertainty_high": False,
            "ml_uncertainty_filter_label": "unknown",
            "ml_uncertainty_warning": "Missing uncertainty score",
        }

    uncertainty = float(ml_row.get("uncertainty_score", 0.0))
    is_high = uncertainty > profile.max_uncertainty_score

    label = "high_uncertainty" if is_high else "acceptable_uncertainty"
    warning = f"Uncertainty ({uncertainty:.2f}) exceeds threshold ({profile.max_uncertainty_score:.2f})" if is_high else ""

    return {
        "ml_uncertainty_high": is_high,
        "ml_uncertainty_filter_label": label,
        "ml_uncertainty_warning": warning,
    }


def calculate_uncertainty_adjusted_support(
    ml_support_score: float, uncertainty_score: float, profile: MLIntegrationProfile
) -> float:
    """Reduce support score based on uncertainty penalty."""
    if uncertainty_score <= profile.max_uncertainty_score:
        return ml_support_score

    excess = uncertainty_score - profile.max_uncertainty_score
    max_excess = 1.0 - profile.max_uncertainty_score
    penalty_ratio = min(1.0, (excess / max_excess) if max_excess > 0 else 1.0)

    # Uncertainty penalizes the support heavily
    adjusted = ml_support_score * (1.0 - penalty_ratio)
    return max(0.0, adjusted)


def build_ml_uncertainty_filter_frame(
    ml_context_df: pd.DataFrame, profile: MLIntegrationProfile
) -> Tuple[pd.DataFrame, dict]:
    """Build a DataFrame reporting uncertainty for the ML context."""
    summary = {"status": "success", "warnings": [], "high_uncertainty_count": 0}

    if ml_context_df is None or ml_context_df.empty:
        summary["status"] = "unavailable"
        summary["warnings"].append("ML context DataFrame is empty")
        return pd.DataFrame(), summary

    results = []
    high_count = 0

    for idx, row in ml_context_df.iterrows():
        res = detect_high_ml_uncertainty(row, profile)

        # Calculate adjusted support assuming perfect alignment just to show the drop
        support = float(row.get("confidence_score", 0.0))
        uncertainty = float(row.get("uncertainty_score", 0.0))
        res["ml_uncertainty_adjusted_support"] = calculate_uncertainty_adjusted_support(support, uncertainty, profile)

        if res["ml_uncertainty_high"]:
            high_count += 1

        results.append(res)

    summary["high_uncertainty_count"] = high_count
    result_df = pd.DataFrame(results, index=ml_context_df.index)
    return result_df, summary
