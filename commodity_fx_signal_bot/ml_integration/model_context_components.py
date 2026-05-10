"""
Model Context Components

Computes raw scores from ML context like support, conflict, and leakage.
"""

import pandas as pd
from typing import Tuple, Dict, Union, Optional

from .integration_config import MLIntegrationProfile
from .integration_labels import (
    ML_CONTEXT_SUPPORTIVE,
    ML_CONTEXT_CONFLICTING,
    ML_CONTEXT_NEUTRAL,
    ML_CONTEXT_UNCERTAIN,
    ML_CONTEXT_UNAVAILABLE,
    ML_CONTEXT_QUALITY_FAILED,
    ML_CONTEXT_LEAKAGE_RISK,
    UNKNOWN_ML_CONTEXT,
)


def calculate_ml_context_quality_score(
    ml_row: Union[pd.Series, Dict], profile: MLIntegrationProfile
) -> float:
    """Calculate the quality score of the ML context."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return 0.0

    model_quality = float(ml_row.get("model_quality_score", 0.5))
    dataset_quality = float(ml_row.get("dataset_quality_score", 0.5))
    leakage_risk = float(ml_row.get("leakage_risk_score", 0.0))

    # Base quality is the average of model and dataset quality
    base_quality = (model_quality + dataset_quality) / 2.0

    # Penalize by leakage risk
    quality = max(0.0, base_quality - leakage_risk)
    return float(min(1.0, quality))


def calculate_ml_support_score(
    ml_row: Union[pd.Series, Dict],
    target_directional_bias: str,
    profile: MLIntegrationProfile,
) -> float:
    """Calculate the support score for a specific directional bias."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return 0.0

    prediction = str(ml_row.get("predicted_direction", "flat")).lower()
    confidence = float(ml_row.get("confidence_score", 0.0))

    if confidence < profile.min_confidence_score:
        return 0.0

    if target_directional_bias == "bullish" and prediction == "up":
        return confidence
    elif target_directional_bias == "bearish" and prediction == "down":
        return confidence
    elif target_directional_bias in ["neutral", "no_trade", "watchlist"] and prediction == "flat":
        return confidence

    return 0.0


def calculate_ml_conflict_score(
    ml_row: Union[pd.Series, Dict],
    target_directional_bias: str,
    profile: MLIntegrationProfile,
) -> float:
    """Calculate the conflict score for a specific directional bias."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return 0.0

    prediction = str(ml_row.get("predicted_direction", "flat")).lower()
    confidence = float(ml_row.get("confidence_score", 0.0))

    if confidence < profile.min_confidence_score:
        return 0.0

    if target_directional_bias == "bullish" and prediction == "down":
        return confidence
    elif target_directional_bias == "bearish" and prediction == "up":
        return confidence

    return 0.0


def calculate_ml_uncertainty_penalty(
    ml_row: Union[pd.Series, Dict], profile: MLIntegrationProfile
) -> float:
    """Calculate the uncertainty penalty."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return 0.0

    uncertainty = float(ml_row.get("uncertainty_score", 0.0))
    if uncertainty > profile.max_uncertainty_score:
        # Scale penalty based on how much it exceeds the threshold
        excess = uncertainty - profile.max_uncertainty_score
        max_excess = 1.0 - profile.max_uncertainty_score
        penalty = min(1.0, (excess / max_excess) if max_excess > 0 else 1.0)
        return penalty

    return 0.0


def calculate_ml_leakage_penalty(
    ml_row: Union[pd.Series, Dict], profile: MLIntegrationProfile
) -> float:
    """Calculate the leakage penalty."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return 0.0

    leakage_risk = float(ml_row.get("leakage_risk_score", 0.0))
    if leakage_risk > profile.max_leakage_risk_score:
        excess = leakage_risk - profile.max_leakage_risk_score
        max_excess = 1.0 - profile.max_leakage_risk_score
        penalty = min(1.0, (excess / max_excess) if max_excess > 0 else 1.0)
        return penalty

    return 0.0


def infer_ml_context_label(
    ml_row: Union[pd.Series, Dict],
    target_directional_bias: str,
    profile: MLIntegrationProfile,
) -> str:
    """Infer the general ML context label based on alignment and quality."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty):
        return ML_CONTEXT_UNAVAILABLE

    quality_score = calculate_ml_context_quality_score(ml_row, profile)
    leakage_risk = float(ml_row.get("leakage_risk_score", 0.0))
    uncertainty = float(ml_row.get("uncertainty_score", 0.0))

    if profile.block_on_high_leakage_risk and leakage_risk > profile.max_leakage_risk_score:
        return ML_CONTEXT_LEAKAGE_RISK

    if profile.block_on_model_quality_fail and quality_score < profile.min_model_quality_score:
        return ML_CONTEXT_QUALITY_FAILED

    if uncertainty > profile.max_uncertainty_score:
        return ML_CONTEXT_UNCERTAIN

    support = calculate_ml_support_score(ml_row, target_directional_bias, profile)
    conflict = calculate_ml_conflict_score(ml_row, target_directional_bias, profile)

    if conflict > 0.0:
        return ML_CONTEXT_CONFLICTING
    elif support > 0.0:
        return ML_CONTEXT_SUPPORTIVE
    else:
        return ML_CONTEXT_NEUTRAL


def build_ml_context_component_frame(
    ml_context_df: pd.DataFrame,
    candidate_df: Optional[pd.DataFrame],
    profile: MLIntegrationProfile,
) -> Tuple[pd.DataFrame, dict]:
    """
    Build a frame of ML context components aligned with the candidate data.
    """
    summary = {"status": "success", "warnings": []}

    if ml_context_df is None or ml_context_df.empty:
        summary["status"] = "unavailable"
        summary["warnings"].append("ML context is unavailable")
        # Return an empty dataframe with expected index but no data
        return pd.DataFrame(), summary

    if candidate_df is None or candidate_df.empty:
        summary["status"] = "unavailable"
        summary["warnings"].append("Candidate DataFrame is unavailable")
        return pd.DataFrame(), summary

    # Use asof to align timestamps (forward fill ML context to candidates)
    # Both must have datetime indices
    if not isinstance(ml_context_df.index, pd.DatetimeIndex) or not isinstance(candidate_df.index, pd.DatetimeIndex):
        summary["status"] = "error"
        summary["warnings"].append("Indices must be DatetimeIndex for alignment")
        return pd.DataFrame(), summary

    ml_context_df = ml_context_df.sort_index()
    candidate_df = candidate_df.sort_index()

    # Simple reindex with forward fill
    aligned_ml = ml_context_df.reindex(candidate_df.index, method="ffill")

    results = []

    for idx, row in candidate_df.iterrows():
        ml_row = aligned_ml.loc[idx] if idx in aligned_ml.index else None

        target_bias = "neutral"
        if "directional_bias" in row:
            target_bias = str(row["directional_bias"]).lower()

        # Check availability
        is_available = ml_row is not None and not pd.isna(ml_row.get("predicted_direction", pd.NA))

        quality_score = calculate_ml_context_quality_score(ml_row, profile) if is_available else 0.0
        passed_quality = quality_score >= profile.min_model_quality_score if is_available else False

        comp_dict = {
            "ml_context_quality_score": quality_score,
            "ml_support_score": calculate_ml_support_score(ml_row, target_bias, profile) if is_available else 0.0,
            "ml_conflict_score": calculate_ml_conflict_score(ml_row, target_bias, profile) if is_available else 0.0,
            "ml_uncertainty_penalty": calculate_ml_uncertainty_penalty(ml_row, profile) if is_available else 0.0,
            "ml_leakage_penalty": calculate_ml_leakage_penalty(ml_row, profile) if is_available else 0.0,
            "ml_context_label": infer_ml_context_label(ml_row, target_bias, profile) if is_available else ML_CONTEXT_UNAVAILABLE,
            "ml_context_available": is_available,
            "ml_context_passed_quality": passed_quality
        }
        results.append(comp_dict)

    result_df = pd.DataFrame(results, index=candidate_df.index)
    return result_df, summary
