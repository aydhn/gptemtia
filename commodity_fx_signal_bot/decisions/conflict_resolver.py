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
