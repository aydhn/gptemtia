import pandas as pd
from typing import Dict, List
from .directional_bias import detect_directional_conflict


def detect_signal_direction_conflict(candidates_df: pd.DataFrame) -> Dict:
    res = detect_directional_conflict(candidates_df)
    return {
        "conflict_score": res["directional_conflict_score"],
        "conflict_reasons": (
            ["High directional conflict in signal candidates"]
            if res["is_directional_conflict"]
            else []
        ),
        "blocking_conflict": res["is_directional_conflict"],
        "warnings": (
            ["Mixed signals detected"] if res["is_directional_conflict"] else []
        ),
    }


def detect_regime_decision_conflict(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> Dict:
    return {
        "conflict_score": 0.0,
        "conflict_reasons": [],
        "blocking_conflict": False,
        "warnings": [],
    }


def detect_mtf_decision_conflict(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> Dict:
    return {
        "conflict_score": 0.0,
        "conflict_reasons": [],
        "blocking_conflict": False,
        "warnings": [],
    }


def detect_macro_decision_conflict(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> Dict:
    return {
        "conflict_score": 0.0,
        "conflict_reasons": [],
        "blocking_conflict": False,
        "warnings": [],
    }


def detect_asset_profile_conflict(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    candidate_type: str,
) -> Dict:
    return {
        "conflict_score": 0.0,
        "conflict_reasons": [],
        "blocking_conflict": False,
        "warnings": [],
    }


def aggregate_decision_conflicts(conflicts: List[Dict]) -> Dict:
    if not conflicts:
        return {
            "conflict_score": 0.0,
            "conflict_reasons": [],
            "blocking_conflict": False,
            "warnings": [],
        }

    scores = [c["conflict_score"] for c in conflicts]
    max_score = max(scores) if scores else 0.0

    reasons = []
    warnings = []
    blocking = False

    for c in conflicts:
        reasons.extend(c.get("conflict_reasons", []))
        warnings.extend(c.get("warnings", []))
        if c.get("blocking_conflict", False):
            blocking = True

    return {
        "conflict_score": max_score,
        "conflict_reasons": list(set(reasons)),
        "blocking_conflict": blocking,
        "warnings": list(set(warnings)),
    }


def detect_ml_decision_conflict(
    context_frames: Dict[str, pd.DataFrame],
    timestamp: pd.Timestamp,
    target_direction: str,
) -> Dict:
    """
    Optionally read ml context to detect high confidence conflicts.
    """
    ml_df = context_frames.get("ml_prediction_context")
    if ml_df is None or ml_df.empty:
        ml_df = context_frames.get("ml_integration_decision")
        if ml_df is None or ml_df.empty:
            return {
                "conflict_score": 0.0,
                "conflict_reasons": [],
                "blocking_conflict": False,
                "warnings": [],
            }

    if timestamp not in ml_df.index:
        past_idx = ml_df.index[ml_df.index <= timestamp]
        if len(past_idx) == 0:
            return {
                "conflict_score": 0.0,
                "conflict_reasons": [],
                "blocking_conflict": False,
                "warnings": [],
            }
        timestamp = past_idx[-1]

    ml_row = ml_df.loc[timestamp]
    if isinstance(ml_row, pd.DataFrame):
        ml_row = ml_row.iloc[0]

    # If already computed by integration layer
    if "conflict_score" in ml_row and "ml_predicted_direction" in ml_row:
        score = float(ml_row["conflict_score"])
        blocking = bool(ml_row.get("blocking_candidate", False))
        warnings = []
        if score > 0.45:  # threshold
            warnings.append(f"ML conflict detected (score: {score:.2f})")
        return {
            "conflict_score": score,
            "conflict_reasons": ["ML prediction conflict"] if score > 0.45 else [],
            "blocking_conflict": blocking,  # Not a live ban, just a block for candidates
            "warnings": warnings,
        }

    # Raw fallback
    prediction = str(ml_row.get("predicted_direction", "flat")).lower()
    confidence = float(ml_row.get("confidence_score", 0.0))

    score = 0.0
    if target_direction == "bullish" and prediction == "down":
        score = confidence
    elif target_direction == "bearish" and prediction == "up":
        score = confidence

    return {
        "conflict_score": score,
        "conflict_reasons": ["High confidence ML prediction conflicts with candidate direction"] if score >= 0.45 else [],
        "blocking_conflict": False,
        "warnings": [f"ML opposite prediction: {prediction}"] if score > 0.0 else [],
    }
