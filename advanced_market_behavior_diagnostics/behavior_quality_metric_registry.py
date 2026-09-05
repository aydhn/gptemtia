"""Phase 129: Behavior Quality Metric Registry.

Registers and evaluates quality metrics for candidate states, pseudo-states,
regime families, and manual review blockers.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)

CORE_BEHAVIOR_QUALITY_METRICS = [
    {
        "metric_name": "candidate_state_coverage_ratio",
        "domain": "candidate_state_coverage_domain",
        "description": "Ratio of required candidate state families covered in the contract registry.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": True,
        "default_value": 1.0,
    },
    {
        "metric_name": "candidate_state_missingness_ratio",
        "domain": "candidate_state_missingness_domain",
        "description": "Ratio of missing attributes or unresolved references in candidate state schemas.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "lower_is_better",
        "is_blocking": False,
        "default_value": 0.0,
    },
    {
        "metric_name": "candidate_state_consistency_score",
        "domain": "candidate_state_consistency_domain",
        "description": "Schema and assignment contract cross-referencing consistency score.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": False,
        "default_value": 1.0,
    },
    {
        "metric_name": "candidate_state_ambiguity_score",
        "domain": "candidate_state_ambiguity_domain",
        "description": "Diagnostic metric quantifying candidate state overlap or boundary ambiguity.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "lower_is_better",
        "is_blocking": False,
        "default_value": 0.15,
    },
    {
        "metric_name": "candidate_state_stability_score",
        "domain": "candidate_state_stability_domain",
        "description": "Baseline temporal persistence and stability assessment score across candidate states.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": False,
        "default_value": 0.85,
    },
    {
        "metric_name": "pseudo_state_schema_completeness",
        "domain": "pseudo_state_quality_domain",
        "description": "Completeness score of pseudo-state definitions and non-signal constraints.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": True,
        "default_value": 1.0,
    },
    {
        "metric_name": "regime_family_coverage_ratio",
        "domain": "regime_family_coverage_domain",
        "description": "Proportion of recognized regime families provided with active diagnostics.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": True,
        "default_value": 1.0,
    },
    {
        "metric_name": "regime_family_consistency_score",
        "domain": "regime_family_consistency_domain",
        "description": "Consistency score between underlying factors, contexts, and regime family definitions.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": False,
        "default_value": 0.95,
    },
    {
        "metric_name": "behavior_context_availability",
        "domain": "market_behavior_diagnostics_domain",
        "description": "Availability of market behavior contexts across volatility, trend, range, macro, and news.",
        "value_type": "float",
        "min_value": 0.0,
        "max_value": 1.0,
        "target_direction": "higher_is_better",
        "is_blocking": True,
        "default_value": 1.0,
    },
    {
        "metric_name": "manual_review_blocker_count",
        "domain": "manual_review_domain",
        "description": "Total count of active blocking items requiring human review before Phase 130.",
        "value_type": "int",
        "min_value": 0.0,
        "max_value": 1000.0,
        "target_direction": "lower_is_better",
        "is_blocking": True,
        "default_value": 0.0,
    },
]


def build_behavior_quality_metric_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and summary for all behavior quality metrics."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for item in CORE_BEHAVIOR_QUALITY_METRICS:
        row = dict(item)
        row["non_signal"] = True
        row["current_phase"] = profile.current_phase
        row["target_final_phase"] = profile.target_final_phase
        row["next_phase"] = profile.next_phase
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_behavior_quality_metrics(df)
    return df, summary


def summarize_behavior_quality_metrics(df: pd.DataFrame) -> dict:
    """Summarize behavior quality metric inventory."""
    return {
        "total_metrics": len(df),
        "blocking_metrics_count": int(df["is_blocking"].sum()) if not df.empty and "is_blocking" in df.columns else 0,
        "all_non_signal": True,
        "metric_names": df["metric_name"].tolist() if not df.empty and "metric_name" in df.columns else [],
    }
