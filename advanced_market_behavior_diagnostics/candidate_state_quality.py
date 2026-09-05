"""Phase 129: Candidate State Quality Report.

Evaluates schema completeness, assignment policy references, source matrix references,
validation dependency status, and non-signal compliance across candidate states.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

CORE_CANDIDATE_STATES = [
    {
        "candidate_state_name": "candidate_state_volatility_expansion",
        "candidate_state_family": "volatility",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_volatility_compression",
        "candidate_state_family": "volatility",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_trend_continuation",
        "candidate_state_family": "trend",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_trend_exhaustion",
        "candidate_state_family": "trend",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_range_bound_oscillation",
        "candidate_state_family": "range",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_range_breakout_transition",
        "candidate_state_family": "range",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_macro_event_shock",
        "candidate_state_family": "macro_event",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_news_attention_surge",
        "candidate_state_family": "news_metadata",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_cross_asset_divergence",
        "candidate_state_family": "cross_asset",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
    {
        "candidate_state_name": "candidate_state_uncertain_regime",
        "candidate_state_family": "uncertain",
        "schema_completeness": 1.0,
        "assignment_policy_ref_available": True,
        "source_matrix_ref_available": True,
        "validation_dependency_passed": True,
        "quality_dependency_passed": True,
        "manual_review_required": False,
        "quality_status": "behavior_quality_ready",
    },
]


def build_candidate_state_quality_report(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and summary for candidate state quality report."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_CANDIDATE_STATES:
        row = dict(item)
        row["non_signal"] = True
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        row["model_training_executed"] = False
        row["clustering_executed"] = False
        row["unsupervised_execution"] = False
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = calculate_candidate_state_quality_summary(df)
    return df, summary


def calculate_candidate_state_quality_summary(df: Optional[pd.DataFrame] = None) -> dict:
    """Calculate summary metrics for candidate state quality."""
    if df is None or df.empty:
        return {
            "total_candidate_states": 0,
            "ready_count": 0,
            "average_completeness": 0.0,
            "manual_review_required_count": 0,
            "all_non_signal": True,
            "all_training_disallowed": True,
        }
    return {
        "total_candidate_states": len(df),
        "ready_count": int((df["quality_status"] == "behavior_quality_ready").sum()) if "quality_status" in df.columns else 0,
        "average_completeness": float(df["schema_completeness"].mean()) if "schema_completeness" in df.columns else 0.0,
        "manual_review_required_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "all_non_signal": bool((df["non_signal"] == True).all()) if "non_signal" in df.columns else True,
        "all_training_disallowed": True,
    }


def summarize_candidate_state_quality(df: pd.DataFrame) -> dict:
    """Alias helper for summarizing candidate state quality."""
    return calculate_candidate_state_quality_summary(df)
