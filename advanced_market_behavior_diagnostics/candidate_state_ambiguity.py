"""Phase 129: Candidate State Ambiguity Report.

Evaluates potential overlap or ambiguity between candidate state definitions
as a purely offline research diagnostic without running unsupervised clustering algorithms.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import CORE_CANDIDATE_STATES


def calculate_candidate_state_ambiguity_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate diagnostic ambiguity score table without executing clustering or distance algorithms."""
    if df is None:
        df = pd.DataFrame(CORE_CANDIDATE_STATES)

    rows = []
    # Baseline expected diagnostic ambiguities (e.g. breakout transition vs continuation)
    for _, item in df.iterrows():
        name = item["candidate_state_name"]
        # Baseline ambiguity diagnostic placeholder: lower is clearer
        ambiguity_score = 0.20 if "transition" in name or "uncertain" in name else 0.10
        rows.append(
            {
                "candidate_state_name": name,
                "candidate_state_family": item["candidate_state_family"],
                "ambiguity_score": ambiguity_score,
                "overlap_risk": "low" if ambiguity_score < 0.25 else "medium",
                "clustering_executed": False,
                "unsupervised_execution": False,
                "non_signal": True,
                "ambiguity_status": "behavior_quality_ready",
            }
        )
    return pd.DataFrame(rows)


def build_candidate_state_ambiguity_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build candidate state ambiguity report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    df = calculate_candidate_state_ambiguity_placeholder()
    summary = summarize_candidate_state_ambiguity(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_candidate_state_ambiguity(df: pd.DataFrame) -> dict:
    """Summarize candidate state ambiguity metrics."""
    if df.empty:
        return {
            "total_states": 0,
            "average_ambiguity_score": 0.0,
            "clustering_executed": False,
            "non_signal": True,
        }
    return {
        "total_states": len(df),
        "average_ambiguity_score": float(df["ambiguity_score"].mean()) if "ambiguity_score" in df.columns else 0.0,
        "high_ambiguity_count": int((df["ambiguity_score"] > 0.50).sum()) if "ambiguity_score" in df.columns else 0,
        "clustering_executed": False,
        "unsupervised_execution": False,
        "non_signal": True,
    }
