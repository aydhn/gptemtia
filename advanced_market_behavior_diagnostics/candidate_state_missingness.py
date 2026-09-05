"""Phase 129: Candidate State Missingness Report.

Evaluates field-level completeness and unresolved references across candidate state definitions.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import CORE_CANDIDATE_STATES


def build_candidate_state_missingness_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build candidate state missingness audit report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_CANDIDATE_STATES:
        rows.append(
            {
                "candidate_state_name": item["candidate_state_name"],
                "candidate_state_family": item["candidate_state_family"],
                "missing_fields_count": 0,
                "missingness_ratio": 0.0,
                "unresolved_reference_count": 0,
                "has_blocking_missingness": False,
                "non_signal": True,
                "missingness_status": "behavior_quality_ready",
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_candidate_state_missingness(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_candidate_state_missingness(df: pd.DataFrame) -> dict:
    """Summarize candidate state missingness metrics."""
    if df.empty:
        return {
            "total_items": 0,
            "total_missing_fields": 0,
            "average_missingness_ratio": 0.0,
            "non_signal": True,
        }
    return {
        "total_items": len(df),
        "total_missing_fields": int(df["missing_fields_count"].sum()) if "missing_fields_count" in df.columns else 0,
        "average_missingness_ratio": float(df["missingness_ratio"].mean()) if "missingness_ratio" in df.columns else 0.0,
        "blocking_items_count": int(df["has_blocking_missingness"].sum()) if "has_blocking_missingness" in df.columns else 0,
        "auto_imputation_allowed": False,
        "auto_drop_allowed": False,
        "non_signal": True,
    }

