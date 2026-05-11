"""
Model Conflict Filter

Detects high confidence conflicts between ML prediction and candidate direction.
"""

import pandas as pd
from typing import Tuple, Dict, Union, Optional
from dataclasses import dataclass, asdict

from .integration_config import MLIntegrationProfile
from .integration_labels import MODEL_UNAVAILABLE_FOR_CANDIDATE, MODEL_CONFLICTS_WITH_CANDIDATE


@dataclass
class MLConflictFilterResult:
    timestamp: str
    source_candidate_id: str
    candidate_layer: str
    candidate_directional_bias: str
    ml_predicted_direction: str
    conflict_score: float
    confidence_score: float
    uncertainty_score: float
    conflict_label: str
    blocking_candidate: bool
    warnings: list[str]


def detect_ml_candidate_conflict(
    candidate_row: pd.Series,
    ml_row: Union[pd.Series, Dict, None],
    profile: MLIntegrationProfile,
    candidate_layer: str,
) -> MLConflictFilterResult:
    """Detect high confidence conflict between ML context and a candidate."""
    timestamp = str(candidate_row.name) if candidate_row.name else "unknown"
    candidate_id = str(candidate_row.get("candidate_id", "unknown"))

    # Extract directional bias depending on layer
    bias = "neutral"
    if candidate_layer == "signal":
        bias = str(candidate_row.get("directional_bias", "neutral")).lower()
    else:
        c_type = str(candidate_row.get("candidate_type", "neutral")).lower()
        if "long" in c_type:
            bias = "bullish"
        elif "short" in c_type:
            bias = "bearish"

    if ml_row is None or (isinstance(ml_row, pd.Series) and ml_row.empty) or pd.isna(ml_row.get("predicted_direction", pd.NA)):
        return MLConflictFilterResult(
            timestamp=timestamp,
            source_candidate_id=candidate_id,
            candidate_layer=candidate_layer,
            candidate_directional_bias=bias,
            ml_predicted_direction="unknown",
            conflict_score=0.0,
            confidence_score=0.0,
            uncertainty_score=0.0,
            conflict_label=MODEL_UNAVAILABLE_FOR_CANDIDATE,
            blocking_candidate=False,
            warnings=["ML context unavailable"],
        )

    prediction = str(ml_row.get("predicted_direction", "flat")).lower()
    confidence = float(ml_row.get("confidence_score", 0.0))
    uncertainty = float(ml_row.get("uncertainty_score", 0.0))
    leakage = float(ml_row.get("leakage_risk_score", 0.0))
    model_quality = float(ml_row.get("model_quality_score", 0.5))

    conflict_score = 0.0
    if bias == "bullish" and prediction == "down":
        conflict_score = confidence
    elif bias == "bearish" and prediction == "up":
        conflict_score = confidence

    warnings = []
    blocking = False
    label = "no_conflict"

    if conflict_score >= profile.min_confidence_score:
        label = MODEL_CONFLICTS_WITH_CANDIDATE
        warnings.append(f"High confidence ({confidence:.2f}) opposite prediction ({prediction})")

        # In conservative profile, bad quality/leakage might make it a blocking warning (still not a live order ban)
        if profile.block_on_high_leakage_risk and leakage > profile.max_leakage_risk_score:
            blocking = True
            warnings.append("High leakage risk associated with conflict")
        if profile.block_on_model_quality_fail and model_quality < profile.min_model_quality_score:
            blocking = True
            warnings.append("Model quality failed during conflict")

    return MLConflictFilterResult(
        timestamp=timestamp,
        source_candidate_id=candidate_id,
        candidate_layer=candidate_layer,
        candidate_directional_bias=bias,
        ml_predicted_direction=prediction,
        conflict_score=conflict_score,
        confidence_score=confidence,
        uncertainty_score=uncertainty,
        conflict_label=label,
        blocking_candidate=blocking,
        warnings=warnings,
    )


def ml_conflict_filter_result_to_dict(result: MLConflictFilterResult) -> dict:
    """Convert dataclass to dict."""
    return asdict(result)


def build_ml_conflict_filter_frame(
    candidate_df: pd.DataFrame,
    ml_context_df: pd.DataFrame,
    profile: MLIntegrationProfile,
    candidate_layer: str,
) -> Tuple[pd.DataFrame, dict]:
    """Build a DataFrame containing conflict filter results for candidates."""
    summary = {"status": "success", "warnings": [], "conflict_count": 0}

    if candidate_df is None or candidate_df.empty:
        summary["status"] = "unavailable"
        summary["warnings"].append(f"{candidate_layer} DataFrame is empty")
        return pd.DataFrame(), summary

    if ml_context_df is None or ml_context_df.empty:
        results = []
        for idx, row in candidate_df.iterrows():
            res = detect_ml_candidate_conflict(row, None, profile, candidate_layer)
            results.append(ml_conflict_filter_result_to_dict(res))
        return pd.DataFrame(results, index=candidate_df.index), {"status": "unavailable", "warnings": ["ML context empty"], "conflict_count": 0}

    # Reindex ML context to match
    ml_context_df = ml_context_df.sort_index()
    aligned_ml = ml_context_df.reindex(candidate_df.index, method="ffill")

    results = []
    conflict_count = 0
    for idx, row in candidate_df.iterrows():
        ml_row = aligned_ml.loc[idx] if idx in aligned_ml.index else None
        res = detect_ml_candidate_conflict(row, ml_row, profile, candidate_layer)
        if res.conflict_score >= profile.min_confidence_score:
            conflict_count += 1
        results.append(ml_conflict_filter_result_to_dict(res))

    summary["conflict_count"] = conflict_count
    result_df = pd.DataFrame(results, index=candidate_df.index)
    return result_df, summary
