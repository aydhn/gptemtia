import pandas as pd
from typing import Dict


def calculate_directional_bias_counts(candidates_df: pd.DataFrame) -> Dict[str, int]:
    if candidates_df is None or candidates_df.empty:
        return {"bullish": 0, "bearish": 0, "neutral": 0, "mixed": 0, "warning": 0}

    counts = {"bullish": 0, "bearish": 0, "neutral": 0, "mixed": 0, "warning": 0}
    if "signal_direction" in candidates_df.columns:
        dir_counts = candidates_df["signal_direction"].value_counts()
        counts["bullish"] = dir_counts.get("bullish", 0)
        counts["bearish"] = dir_counts.get("bearish", 0)
        counts["neutral"] = dir_counts.get("neutral", 0)
    else:
        counts["warning"] = len(candidates_df)

    return counts


def calculate_directional_bias_score(candidates_df: pd.DataFrame) -> Dict[str, float]:
    counts = calculate_directional_bias_counts(candidates_df)
    total = sum(counts.values())
    if total == 0:
        return {
            "bullish_score": 0.0,
            "bearish_score": 0.0,
            "neutral_score": 0.0,
            "mixed_score": 0.0,
            "warning_score": 0.0,
        }

    return {
        "bullish_score": counts["bullish"] / total,
        "bearish_score": counts["bearish"] / total,
        "neutral_score": counts["neutral"] / total,
        "mixed_score": counts["mixed"] / total,
        "warning_score": counts["warning"] / total,
    }


def infer_dominant_direction(candidates_df: pd.DataFrame) -> str:
    scores = calculate_directional_bias_score(candidates_df)
    if scores["warning_score"] > 0:
        return "warning"

    bullish = scores["bullish_score"]
    bearish = scores["bearish_score"]

    if bullish > bearish and bullish > 0.5:
        return "bullish"
    if bearish > bullish and bearish > 0.5:
        return "bearish"

    return "neutral"


def calculate_directional_consensus_score(candidates_df: pd.DataFrame) -> float:
    scores = calculate_directional_bias_score(candidates_df)
    if scores["warning_score"] > 0:
        return 0.0
    return max(scores["bullish_score"], scores["bearish_score"])


def calculate_bullish_bearish_balance(candidates_df: pd.DataFrame) -> float:
    scores = calculate_directional_bias_score(candidates_df)
    if scores["warning_score"] > 0:
        return 0.0
    total = scores["bullish_score"] + scores["bearish_score"]
    if total == 0:
        return 0.0
    return abs(scores["bullish_score"] - scores["bearish_score"]) / total


def detect_directional_conflict(
    candidates_df: pd.DataFrame, conflict_threshold: float = 0.65
) -> Dict:
    consensus = calculate_directional_consensus_score(candidates_df)
    conflict = 1.0 - consensus
    is_conflict = conflict >= conflict_threshold

    return {
        "directional_conflict_score": conflict,
        "is_directional_conflict": is_conflict,
    }
