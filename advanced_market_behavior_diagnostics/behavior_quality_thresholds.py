"""Phase 129: Behavior Quality Thresholds Registry.

Defines operational thresholds for candidate state coverage, missingness,
ambiguity, stability, and manual review triggers.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

CORE_BEHAVIOR_QUALITY_THRESHOLDS = [
    {
        "threshold_name": "coverage_warning_below",
        "metric_name": "candidate_state_coverage_ratio",
        "warning_threshold": 0.50,
        "critical_threshold": 0.25,
        "evaluation_operator": "lt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "coverage_critical_below",
        "metric_name": "candidate_state_coverage_ratio",
        "warning_threshold": 0.40,
        "critical_threshold": 0.25,
        "evaluation_operator": "lt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "ambiguity_warning_above",
        "metric_name": "candidate_state_ambiguity_score",
        "warning_threshold": 0.50,
        "critical_threshold": 0.75,
        "evaluation_operator": "gt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "missingness_warning_above",
        "metric_name": "candidate_state_missingness_ratio",
        "warning_threshold": 0.25,
        "critical_threshold": 0.50,
        "evaluation_operator": "gt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "missingness_critical_above",
        "metric_name": "candidate_state_missingness_ratio",
        "warning_threshold": 0.35,
        "critical_threshold": 0.50,
        "evaluation_operator": "gt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "manual_review_if_insufficient_data",
        "metric_name": "behavior_context_availability",
        "warning_threshold": 0.60,
        "critical_threshold": 0.40,
        "evaluation_operator": "lt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
    {
        "threshold_name": "manual_review_if_schema_placeholder",
        "metric_name": "pseudo_state_schema_completeness",
        "warning_threshold": 0.70,
        "critical_threshold": 0.50,
        "evaluation_operator": "lt",
        "action_on_warning": "record_finding",
        "action_on_critical": "manual_review_required",
    },
]


def build_behavior_quality_threshold_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and summary for all behavior quality thresholds."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_BEHAVIOR_QUALITY_THRESHOLDS:
        row = dict(item)
        row["non_signal"] = True
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_behavior_quality_thresholds(df)
    return df, summary


def summarize_behavior_quality_thresholds(df: pd.DataFrame) -> dict:
    """Summarize behavior quality threshold inventory."""
    return {
        "total_thresholds": len(df),
        "all_non_signal": True,
        "threshold_names": df["threshold_name"].tolist() if not df.empty and "threshold_name" in df.columns else [],
    }
