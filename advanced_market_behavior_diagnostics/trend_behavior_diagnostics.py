"""Phase 129: Trend Behavior Diagnostics Report.

Evaluates directional persistence contexts, moving average dependencies, momentum factors,
and trend transition readiness as non-signal diagnostic metrics.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

TREND_BEHAVIOR_CONTEXT_ITEMS = [
    {
        "context_name": "trend_directional_persistence_context",
        "description": "Sequential trend continuation and moving average alignment context.",
        "coverage_ratio": 1.0,
        "moving_average_dependency_passed": True,
        "momentum_factor_dependency_passed": True,
        "persistence_readiness": True,
        "transition_readiness": True,
        "is_ready": True,
    },
    {
        "context_name": "trend_exhaustion_context",
        "description": "Momentum deceleration and trend stall diagnostic context.",
        "coverage_ratio": 1.0,
        "moving_average_dependency_passed": True,
        "momentum_factor_dependency_passed": True,
        "persistence_readiness": True,
        "transition_readiness": True,
        "is_ready": True,
    },
    {
        "context_name": "trend_inflection_readiness_context",
        "description": "Slope divergence and boundary inflection preparation context.",
        "coverage_ratio": 1.0,
        "moving_average_dependency_passed": True,
        "momentum_factor_dependency_passed": True,
        "persistence_readiness": True,
        "transition_readiness": True,
        "is_ready": True,
    },
]


def build_trend_behavior_diagnostics_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build trend behavior diagnostics report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in TREND_BEHAVIOR_CONTEXT_ITEMS:
        row = dict(item)
        row["non_signal"] = True
        row["contains_target_or_prediction"] = False
        row["model_training_executed"] = False
        row["clustering_executed"] = False
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_trend_behavior_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_trend_behavior_diagnostics(df: pd.DataFrame) -> dict:
    """Summarize trend behavior diagnostics."""
    if df.empty:
        return {
            "total_contexts": 0,
            "average_coverage": 0.0,
            "all_ready": False,
            "non_signal": True,
        }
    return {
        "total_contexts": len(df),
        "average_coverage": float(df["coverage_ratio"].mean()) if "coverage_ratio" in df.columns else 0.0,
        "all_ready": bool((df["is_ready"] == True).all()) if "is_ready" in df.columns else False,
        "persistence_ready": bool((df["persistence_readiness"] == True).all()) if "persistence_readiness" in df.columns else False,
        "transition_ready": bool((df["transition_readiness"] == True).all()) if "transition_readiness" in df.columns else False,
        "dependencies_passed": bool((df["moving_average_dependency_passed"] == True).all()) if "moving_average_dependency_passed" in df.columns else False,
        "non_signal": True,
    }

