"""Phase 125: Feature Engine Block Acceptance Scoring.

Calculates weighted acceptance scores based on gate evaluations.
Score is purely a structural/contractual readiness metric and NEVER a trading signal
or official production approval.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    FeatureFactorAcceptanceProfile,
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_models import (
    FeatureEngineAcceptanceScore,
)


def classify_acceptance_score(score: float) -> str:
    """Classify the acceptance score into qualitative readiness tiers."""
    if score >= 0.90:
        return "EXCELLENT_READINESS"
    elif score >= 0.75:
        return "STRONG_READINESS"
    elif score >= 0.50:
        return "ACCEPTABLE_WITH_WARNINGS"
    return "NEEDS_IMPROVEMENT"


def calculate_feature_engine_block_acceptance_score(
    gates_df: pd.DataFrame,
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> float:
    """Calculate weighted acceptance score between 0.0 and 1.0."""
    if gates_df.empty:
        return 0.0
    weights = gates_df["score_weight"] if "score_weight" in gates_df.columns else pd.Series(1.0, index=gates_df.index)
    passed = gates_df["passed"].astype(float) if "passed" in gates_df.columns else pd.Series(0.0, index=gates_df.index)
    total_weight = weights.sum()
    if total_weight <= 0:
        return 0.0
    weighted_score = (passed * weights).sum() / total_weight
    return round(float(weighted_score), 4)


def build_feature_engine_block_acceptance_score_report(
    profile: Optional[FeatureFactorAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the acceptance score report DataFrame and summary."""
    active_profile = profile or get_default_feature_factor_acceptance_profile()
    gates_df, _ = build_feature_engine_block_acceptance_gate_registry(active_profile)
    score = calculate_feature_engine_block_acceptance_score(gates_df, active_profile)
    tier = classify_acceptance_score(score)

    total_gates = len(gates_df)
    passed_gates = int(gates_df["passed"].sum())
    failed_gates = total_gates - passed_gates

    item = FeatureEngineAcceptanceScore(
        overall_score=score,
        score_tier=tier,
        total_gates=total_gates,
        passed_gates=passed_gates,
        failed_gates=failed_gates,
        warning_gates=0,
        manual_review_required=failed_gates > 0,
        non_signal=True,
        official_approval=False,
        production_ready=False,
        broker_ready=False,
    )
    df = pd.DataFrame([item.__dict__])

    summary = {
        "overall_score": score,
        "score_tier": tier,
        "meets_profile_minimum": score >= active_profile.min_score,
        "min_required_score": active_profile.min_score,
        "total_gates": total_gates,
        "passed_gates": passed_gates,
        "failed_gates": failed_gates,
        "non_signal": True,
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary


def summarize_acceptance_score(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize acceptance score DataFrame."""
    if df.empty:
        return {"overall_score": 0.0, "score_tier": "UNKNOWN"}
    row = df.iloc[0]
    return {
        "overall_score": row.get("overall_score", 0.0),
        "score_tier": row.get("score_tier", "UNKNOWN"),
        "non_signal": True,
    }
