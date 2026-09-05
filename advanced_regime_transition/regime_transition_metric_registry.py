"""Phase 130: Regime Transition Metric Registry.

Catalog of transition diagnostics metrics, rate placeholders, ambiguity,
continuity, and readiness indicators.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

TRANSITION_METRIC_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "metric_name": "transition_frequency_placeholder",
        "metric_family": "transition_frequency",
        "description": "Rate of state transitions per unit time in sequence history",
        "formula_placeholder": "count(transitions) / total_valid_intervals",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "transition_count_placeholder",
        "metric_family": "transition_frequency",
        "description": "Total integer count of state changes observed in sequence",
        "formula_placeholder": "sum(state_t != state_{t-1})",
        "expected_range": "[0, inf)",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "transition_rate_placeholder",
        "metric_family": "transition_rate",
        "description": "Normalized ratio of transition occurrences over sequence length",
        "formula_placeholder": "transition_count / sequence_length",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "state_switch_ratio_placeholder",
        "metric_family": "transition_rate",
        "description": "Frequency ratio of switching out of a specific candidate regime",
        "formula_placeholder": "exits_from_state_k / total_observations_in_state_k",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "transition_ambiguity_score_placeholder",
        "metric_family": "transition_ambiguity",
        "description": "Diagnostic metric measuring boundary uncertainty during transition points",
        "formula_placeholder": "1.0 - abs(prob_candidate_1 - prob_candidate_2)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "transition_continuity_score_placeholder",
        "metric_family": "transition_continuity",
        "description": "Continuity ratio measuring lack of missing timestamps during sequence",
        "formula_placeholder": "observed_timestamp_count / expected_timestamp_count",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "transition_readiness_score",
        "metric_family": "transition_readiness",
        "description": "Readiness indicator evaluating if candidate sequence is sufficiently clean for transition analysis",
        "formula_placeholder": "mean(coverage, consistency, 1 - ambiguity)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "timestamp_continuity_score",
        "metric_family": "timestamp_policy",
        "description": "Integrity score verifying monotonic chronological order without negative time deltas",
        "formula_placeholder": "count(delta_t > 0) / count(delta_t)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "manual_review_blocker_count",
        "metric_family": "governance",
        "description": "Count of open blockers requiring manual analyst inspection",
        "formula_placeholder": "sum(review_items_blocking)",
        "expected_range": "[0, inf)",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
]


def build_regime_transition_metric_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition metric registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(TRANSITION_METRIC_DEFINITIONS)
    summary = summarize_regime_transition_metrics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_transition_metrics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime transition metrics."""
    return {
        "total_metrics": len(df),
        "metric_names": df["metric_name"].tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_requires_no_lookahead": bool(df["requires_no_lookahead"].all()) if not df.empty else True,
    }
