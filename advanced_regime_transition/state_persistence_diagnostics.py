"""Phase 130: State Persistence Diagnostics.

Provides non-signal diagnostic calculations and reports on candidate state persistence,
average run-lengths, and consecutive interval stability proxies.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

DEFAULT_PERSISTENCE_DATA: List[Dict[str, Any]] = [
    {
        "candidate_state": "volatility_compression",
        "entity_family": "volatility",
        "observed_run_count": 42,
        "average_duration_periods": 6.8,
        "persistence_score": 0.85,
        "exit_frequency": 0.15,
        "stability_category": "stable_persistent",
        "non_signal": True,
    },
    {
        "candidate_state": "volatility_expansion",
        "entity_family": "volatility",
        "observed_run_count": 28,
        "average_duration_periods": 3.4,
        "persistence_score": 0.70,
        "exit_frequency": 0.30,
        "stability_category": "moderate_transient",
        "non_signal": True,
    },
    {
        "candidate_state": "trend_persistent_bullish",
        "entity_family": "trend",
        "observed_run_count": 35,
        "average_duration_periods": 8.2,
        "persistence_score": 0.88,
        "exit_frequency": 0.12,
        "stability_category": "highly_persistent",
        "non_signal": True,
    },
    {
        "candidate_state": "trend_persistent_bearish",
        "entity_family": "trend",
        "observed_run_count": 31,
        "average_duration_periods": 7.5,
        "persistence_score": 0.86,
        "exit_frequency": 0.14,
        "stability_category": "stable_persistent",
        "non_signal": True,
    },
    {
        "candidate_state": "range_bound_consolidation",
        "entity_family": "range",
        "observed_run_count": 55,
        "average_duration_periods": 11.4,
        "persistence_score": 0.91,
        "exit_frequency": 0.09,
        "stability_category": "highly_persistent",
        "non_signal": True,
    },
    {
        "candidate_state": "macro_release_reaction",
        "entity_family": "macro_event",
        "observed_run_count": 18,
        "average_duration_periods": 2.1,
        "persistence_score": 0.52,
        "exit_frequency": 0.48,
        "stability_category": "transient_event",
        "non_signal": True,
    },
]


def calculate_state_persistence_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-signal state persistence placeholder from provided or default data."""
    if df is not None and not df.empty:
        # Immutable copy, never mutate input
        out_df = df.copy()
        if "state" in out_df.columns:
            # Group consecutive runs
            states = out_df["state"]
            is_new_run = states != states.shift(1)
            run_ids = is_new_run.cumsum()
            run_lengths = out_df.groupby(run_ids)["state"].count()
            avg_duration = float(run_lengths.mean()) if not run_lengths.empty else 1.0
            persistence = max(0.0, min(1.0, 1.0 - (1.0 / avg_duration))) if avg_duration > 0 else 0.0
            return pd.DataFrame(
                [
                    {
                        "candidate_state": "computed_sequence",
                        "entity_family": "custom",
                        "observed_run_count": len(run_lengths),
                        "average_duration_periods": round(avg_duration, 2),
                        "persistence_score": round(persistence, 4),
                        "exit_frequency": round(1.0 - persistence, 4),
                        "stability_category": "custom_computed",
                        "non_signal": True,
                    }
                ]
            )
    return pd.DataFrame(DEFAULT_PERSISTENCE_DATA)


def build_state_persistence_diagnostics_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build state persistence diagnostics report dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = calculate_state_persistence_placeholder()
    summary = summarize_state_persistence_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_persistence_diagnostics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state persistence diagnostics."""
    mean_score = float(df["persistence_score"].mean()) if not df.empty and "persistence_score" in df.columns else 0.0
    mean_dur = float(df["average_duration_periods"].mean()) if not df.empty and "average_duration_periods" in df.columns else 0.0
    return {
        "total_analyzed_states": len(df),
        "mean_persistence_score": round(mean_score, 4),
        "mean_duration_periods": round(mean_dur, 2),
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_prediction": False,
        "contains_trading_signal": False,
    }
