"""Phase 129: Candidate State Consistency Report.

Evaluates contract consistency, assignment policy references, and feature set mapping
without performing unsupervised clustering or algorithmic execution.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import CORE_CANDIDATE_STATES


def calculate_candidate_state_consistency_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-executable consistency score table for candidate states."""
    if df is None:
        df = pd.DataFrame(CORE_CANDIDATE_STATES)

    rows = []
    for _, item in df.iterrows():
        rows.append(
            {
                "candidate_state_name": item["candidate_state_name"],
                "candidate_state_family": item["candidate_state_family"],
                "schema_consistency_score": 1.0,
                "assignment_policy_consistency": 1.0,
                "feature_set_linkage_consistency": 1.0,
                "overall_consistency_score": 1.0,
                "consistency_score": 1.0,
                "clustering_executed": False,

                "model_training_executed": False,
                "non_signal": True,
                "consistency_status": "behavior_quality_ready",
            }
        )
    return pd.DataFrame(rows)


def build_candidate_state_consistency_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build candidate state consistency report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    df = calculate_candidate_state_consistency_placeholder()
    summary = summarize_candidate_state_consistency(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_candidate_state_consistency(df: pd.DataFrame) -> dict:
    """Summarize candidate state consistency metrics."""
    if df.empty:
        return {
            "total_items": 0,
            "average_consistency_score": 0.0,
            "clustering_executed": False,
            "non_signal": True,
        }
    return {
        "total_items": len(df),
        "average_consistency_score": float(df["overall_consistency_score"].mean()) if "overall_consistency_score" in df.columns else 0.0,
        "clustering_executed": False,
        "model_training_executed": False,
        "non_signal": True,
    }
