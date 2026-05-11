"""
Model Strategy Alignment

Measures alignment/conflict between ML context and strategy candidates.
"""

import pandas as pd
from typing import Tuple, Dict, Union, Optional

from .integration_config import MLIntegrationProfile
from .integration_labels import (
    MODEL_ALIGNED_WITH_CANDIDATE,
    MODEL_CONFLICTS_WITH_CANDIDATE,
    MODEL_NEUTRAL_TO_CANDIDATE,
    MODEL_UNCERTAIN_FOR_CANDIDATE,
    MODEL_UNAVAILABLE_FOR_CANDIDATE,
)
from .model_context_components import (
    calculate_ml_support_score,
    calculate_ml_conflict_score,
    calculate_ml_uncertainty_penalty,
)


def calculate_model_strategy_alignment(
    strategy_row: pd.Series,
    ml_row: Union[pd.Series, Dict, None],
    profile: MLIntegrationProfile,
) -> dict:
    """Calculate alignment between a strategy candidate and ML context."""
    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty) or pd.isna(ml_row.get("predicted_direction", pd.NA)):
        return {
            "alignment_label": MODEL_UNAVAILABLE_FOR_CANDIDATE,
            "ml_support_score": 0.0,
            "ml_conflict_score": 0.0,
            "ml_uncertainty_penalty": 0.0,
            "model_strategy_alignment_score": 0.5,
            "warnings": ["ML context is unavailable"],
        }

    candidate_type = str(strategy_row.get("candidate_type", "neutral")).lower()
    strategy_family = str(strategy_row.get("strategy_family", "unknown")).lower()

    # Map candidate type to directional bias
    if "long" in candidate_type:
        target_bias = "bullish"
    elif "short" in candidate_type:
        target_bias = "bearish"
    else:
        target_bias = "neutral"

    prediction = str(ml_row.get("predicted_direction", "flat")).lower()

    # Special rules for strategy families
    if strategy_family == "mean_reversion":
        # For mean reversion, predicted_flat or weak direction can be neutral/supportive
        if prediction == "flat":
            target_bias = "neutral"

    support = calculate_ml_support_score(ml_row, target_bias, profile)
    conflict = calculate_ml_conflict_score(ml_row, target_bias, profile)
    uncertainty_penalty = calculate_ml_uncertainty_penalty(ml_row, profile)

    warnings = []

    if uncertainty_penalty > 0 and profile.allow_uncertain_context_as_neutral:
        label = MODEL_UNCERTAIN_FOR_CANDIDATE
        warnings.append("High uncertainty in ML context (warning for breakout strategies)")
    elif conflict > 0.0:
        label = MODEL_CONFLICTS_WITH_CANDIDATE
        warnings.append("ML prediction conflicts with strategy direction")
    elif support > 0.0:
        label = MODEL_ALIGNED_WITH_CANDIDATE
    else:
        label = MODEL_NEUTRAL_TO_CANDIDATE

    alignment_score = 0.5 + (support * 0.5) - (conflict * 0.5) - (uncertainty_penalty * 0.2)
    alignment_score = max(0.0, min(1.0, alignment_score))

    return {
        "alignment_label": label,
        "ml_support_score": support,
        "ml_conflict_score": conflict,
        "ml_uncertainty_penalty": uncertainty_penalty,
        "model_strategy_alignment_score": alignment_score,
        "warnings": warnings,
    }


def build_model_strategy_alignment_frame(
    strategy_df: pd.DataFrame,
    ml_context_df: pd.DataFrame,
    profile: MLIntegrationProfile,
) -> Tuple[pd.DataFrame, dict]:
    """Build a DataFrame containing strategy alignment metrics."""
    summary = {"status": "success", "warnings": []}

    if strategy_df is None or strategy_df.empty:
        summary["status"] = "unavailable"
        summary["warnings"].append("Strategy DataFrame is empty or None")
        return pd.DataFrame(), summary

    if ml_context_df is None or ml_context_df.empty:
        results = []
        for idx, row in strategy_df.iterrows():
            results.append(calculate_model_strategy_alignment(row, None, profile))
        return pd.DataFrame(results, index=strategy_df.index), {"status": "unavailable", "warnings": ["ML context empty"]}

    # Reindex ML context to match strategy frame
    ml_context_df = ml_context_df.sort_index()
    aligned_ml = ml_context_df.reindex(strategy_df.index, method="ffill")

    results = []
    for idx, row in strategy_df.iterrows():
        ml_row = aligned_ml.loc[idx] if idx in aligned_ml.index else None
        results.append(calculate_model_strategy_alignment(row, ml_row, profile))

    result_df = pd.DataFrame(results, index=strategy_df.index)
    return result_df, summary
