"""Phase 130: Regime Stability Metric Registry.

Catalog of stability diagnostics metrics, persistence scores, duration proxies,
and sequence completeness indicators.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

STABILITY_METRIC_DEFINITIONS: List[Dict[str, Any]] = [
    {
        "metric_name": "state_persistence_score_placeholder",
        "metric_family": "state_persistence",
        "description": "Probability proxy that a state persists into the subsequent interval",
        "formula_placeholder": "count(state_{t} == state_{t-1}) / total_transitions",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "average_state_duration_placeholder",
        "metric_family": "state_persistence",
        "description": "Average consecutive intervals spent within a single candidate state run",
        "formula_placeholder": "mean(run_lengths)",
        "expected_range": "[1.0, inf)",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "stability_score_placeholder",
        "metric_family": "stability_score",
        "description": "Overall stability index combining persistence, low ambiguity, and sequence completeness",
        "formula_placeholder": "0.4 * persistence + 0.3 * (1 - ambiguity) + 0.3 * completeness",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "rolling_stability_placeholder",
        "metric_family": "stability_score",
        "description": "Rolling window stability metric tracking regime persistence variance",
        "formula_placeholder": "rolling_mean(persistence, window=W)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "regime_family_stability_placeholder",
        "metric_family": "family_stability",
        "description": "Persistence score measured across entire regime families (volatility, trend, range)",
        "formula_placeholder": "mean(family_member_persistence)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "pseudo_state_stability_placeholder",
        "metric_family": "pseudo_stability",
        "description": "Persistence placeholder for pseudo-state cluster sequences",
        "formula_placeholder": "pseudo_run_length / expected_duration",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "state_sequence_completeness_score",
        "metric_family": "completeness",
        "description": "Ratio of valid non-null state observations in sequence record",
        "formula_placeholder": "count(non_null_states) / total_sequence_length",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
    {
        "metric_name": "source_quality_dependency_score",
        "metric_family": "dependency",
        "description": "Upstream quality score from Phase 123/129 verifying input factor sanity",
        "formula_placeholder": "min(phase_123_quality, phase_129_quality)",
        "expected_range": "[0.0, 1.0]",
        "non_signal": True,
        "source_preserved": True,
        "requires_no_lookahead": True,
    },
]


def build_regime_stability_metric_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build stability metric registry dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(STABILITY_METRIC_DEFINITIONS)
    summary = summarize_regime_stability_metrics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_regime_stability_metrics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime stability metrics."""
    return {
        "total_metrics": len(df),
        "metric_names": df["metric_name"].tolist() if not df.empty else [],
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "all_requires_no_lookahead": bool(df["requires_no_lookahead"].all()) if not df.empty else True,
    }
