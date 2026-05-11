"""
Model Aware Scoring

Adjusts candidate base scores safely using ML context components.
"""

import pandas as pd
from typing import Tuple

from .integration_config import MLIntegrationProfile


def calculate_model_aware_score_adjustment(
    base_score: float,
    ml_support_score: float,
    ml_conflict_score: float,
    ml_uncertainty_penalty: float,
    profile: MLIntegrationProfile,
) -> dict:
    """Safely calculate score adjustment from ML context."""
    if not profile.enable_signal_scoring and not profile.enable_decision_scoring and not profile.enable_strategy_scoring:
        # Research-only mode
        return {
            "ml_adjustment_score": 0.0,
            "model_aware_candidate_score": base_score,
            "ml_adjustment_applied": False,
        }

    # Weight adjustments
    support_adj = ml_support_score * profile.support_weight
    conflict_adj = ml_conflict_score * profile.conflict_penalty_weight
    uncertainty_adj = ml_uncertainty_penalty * profile.uncertainty_penalty_weight

    net_adjustment = support_adj - conflict_adj - uncertainty_adj
    adjusted_score = base_score + net_adjustment

    # Clamp between 0 and 1
    final_score = max(0.0, min(1.0, adjusted_score))

    return {
        "ml_adjustment_score": net_adjustment,
        "model_aware_candidate_score": final_score,
        "ml_adjustment_applied": True,
    }


def _apply_adjustment_to_candidates(
    candidate_df: pd.DataFrame,
    alignment_df: pd.DataFrame,
    profile: MLIntegrationProfile,
    score_column: str,
) -> Tuple[pd.DataFrame, dict]:
    """Internal helper to apply adjustments."""
    summary = {"status": "success", "adjusted_rows": 0, "warnings": []}

    if candidate_df is None or candidate_df.empty:
        return pd.DataFrame(), {"status": "unavailable", "adjusted_rows": 0, "warnings": ["Candidate df empty"]}

    result_df = candidate_df.copy()

    # Preserve original score
    orig_col = f"base_{score_column}_before_ml"
    result_df[orig_col] = result_df[score_column]

    if alignment_df is None or alignment_df.empty:
        summary["warnings"].append("No alignment data, scores unmodified")
        result_df["ml_adjustment_score"] = 0.0
        result_df["model_aware_candidate_score"] = result_df[score_column]
        result_df["ml_adjustment_applied"] = False
        return result_df, summary

    # Assume exact index alignment from previous step
    adjusted_scores = []
    adj_values = []
    applied = []

    for idx, row in result_df.iterrows():
        base_score = float(row.get(score_column, 0.5))

        if idx in alignment_df.index:
            align_row = alignment_df.loc[idx]
            # Handle duplicates if index not unique
            if isinstance(align_row, pd.DataFrame):
                align_row = align_row.iloc[0]

            support = float(align_row.get("ml_support_score", 0.0))
            conflict = float(align_row.get("ml_conflict_score", 0.0))
            uncertainty = float(align_row.get("ml_uncertainty_penalty", 0.0))

            adj = calculate_model_aware_score_adjustment(base_score, support, conflict, uncertainty, profile)
        else:
            adj = {"ml_adjustment_score": 0.0, "model_aware_candidate_score": base_score, "ml_adjustment_applied": False}

        adjusted_scores.append(adj["model_aware_candidate_score"])
        adj_values.append(adj["ml_adjustment_score"])
        applied.append(adj["ml_adjustment_applied"])
        if adj["ml_adjustment_applied"] and adj["ml_adjustment_score"] != 0:
            summary["adjusted_rows"] += 1

    result_df["ml_adjustment_score"] = adj_values
    result_df["model_aware_candidate_score"] = adjusted_scores
    result_df["ml_adjustment_applied"] = applied

    # If confidence_score exists, also adjust it (similarly)
    if "confidence_score" in result_df.columns:
        orig_conf = "base_confidence_score_before_ml"
        result_df[orig_conf] = result_df["confidence_score"]
        conf_scores = []
        for idx, row in result_df.iterrows():
            base_conf = float(row.get("confidence_score", 0.5))
            if idx in alignment_df.index:
                align_row = alignment_df.loc[idx]
                if isinstance(align_row, pd.DataFrame):
                    align_row = align_row.iloc[0]
                support = float(align_row.get("ml_support_score", 0.0))
                conflict = float(align_row.get("ml_conflict_score", 0.0))
                uncertainty = float(align_row.get("ml_uncertainty_penalty", 0.0))
                adj = calculate_model_aware_score_adjustment(base_conf, support, conflict, uncertainty, profile)
                conf_scores.append(adj["model_aware_candidate_score"])
            else:
                conf_scores.append(base_conf)
        result_df["model_aware_confidence_score"] = conf_scores

        # Merge alignment labels into the result for convenience
        if "alignment_label" in alignment_df.columns:
            result_df["ml_alignment_label"] = alignment_df["alignment_label"]

    return result_df, summary


def apply_model_aware_adjustment_to_signal_candidates(
    signal_df: pd.DataFrame, alignment_df: pd.DataFrame, profile: MLIntegrationProfile
) -> Tuple[pd.DataFrame, dict]:
    if not profile.enable_signal_scoring:
        return _apply_adjustment_to_candidates(signal_df, None, profile, "signal_score")
    return _apply_adjustment_to_candidates(signal_df, alignment_df, profile, "signal_score")


def apply_model_aware_adjustment_to_decision_candidates(
    decision_df: pd.DataFrame, alignment_df: pd.DataFrame, profile: MLIntegrationProfile
) -> Tuple[pd.DataFrame, dict]:
    if not profile.enable_decision_scoring:
        return _apply_adjustment_to_candidates(decision_df, None, profile, "decision_score")
    return _apply_adjustment_to_candidates(decision_df, alignment_df, profile, "decision_score")


def apply_model_aware_adjustment_to_strategy_candidates(
    strategy_df: pd.DataFrame, alignment_df: pd.DataFrame, profile: MLIntegrationProfile
) -> Tuple[pd.DataFrame, dict]:
    if not profile.enable_strategy_scoring:
        return _apply_adjustment_to_candidates(strategy_df, None, profile, "strategy_score")
    return _apply_adjustment_to_candidates(strategy_df, alignment_df, profile, "strategy_score")
