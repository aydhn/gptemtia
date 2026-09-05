"""Phase 129: Candidate State Coverage Report.

Evaluates coverage ratios across candidate state families and market behavior dimensions.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.candidate_state_quality import CORE_CANDIDATE_STATES


def calculate_candidate_state_coverage(
    df: pd.DataFrame, group_field: str = "candidate_state_family"
) -> pd.DataFrame:
    """Calculate coverage counts and ratios grouped by family or domain."""
    if df.empty or group_field not in df.columns:
        return pd.DataFrame()
    grouped = (
        df.groupby(group_field)
        .agg(
            state_count=("candidate_state_name", "count"),
            avg_completeness=("schema_completeness", "mean"),
        )
        .reset_index()
    )
    total = len(df)
    grouped["coverage_ratio"] = grouped["state_count"] / total if total > 0 else 0.0
    grouped["coverage_status"] = grouped["coverage_ratio"].apply(
        lambda x: "behavior_quality_ready" if x >= 0.05 else "behavior_quality_ready_with_warnings"
    )
    grouped["non_signal"] = True
    return grouped


def build_candidate_state_coverage_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build candidate state coverage report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    source_df = pd.DataFrame(CORE_CANDIDATE_STATES)
    df = calculate_candidate_state_coverage(source_df, group_field="candidate_state_family")
    summary = summarize_candidate_state_coverage(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_candidate_state_coverage(df: pd.DataFrame) -> dict:
    """Summarize candidate state coverage metrics."""
    if df.empty:
        return {
            "total_families": 0,
            "all_families_covered": False,
            "non_signal": True,
        }
    return {
        "total_families": len(df),
        "total_candidate_states": int(df["state_count"].sum()) if "state_count" in df.columns else 0,
        "average_family_completeness": float(df["avg_completeness"].mean()) if "avg_completeness" in df.columns else 0.0,
        "all_families_covered": True,
        "non_signal": True,
    }
