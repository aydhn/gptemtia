"""Phase 130: State Transition Frequency.

Diagnostic report detailing frequency of regime transitions across candidate states.
Strictly offline, non-signal, zero-predictive calculation.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

DEFAULT_FREQUENCY_DATA: List[Dict[str, Any]] = [
    {
        "source_state": "volatility_compression",
        "target_state": "volatility_expansion",
        "transition_count": 24,
        "empirical_frequency": 0.57,
        "sample_size": 42,
        "non_signal": True,
    },
    {
        "source_state": "volatility_compression",
        "target_state": "range_bound_consolidation",
        "transition_count": 18,
        "empirical_frequency": 0.43,
        "sample_size": 42,
        "non_signal": True,
    },
    {
        "source_state": "volatility_expansion",
        "target_state": "volatility_compression",
        "transition_count": 20,
        "empirical_frequency": 0.71,
        "sample_size": 28,
        "non_signal": True,
    },
    {
        "source_state": "volatility_expansion",
        "target_state": "trend_persistent_bullish",
        "transition_count": 8,
        "empirical_frequency": 0.29,
        "sample_size": 28,
        "non_signal": True,
    },
    {
        "source_state": "range_bound_consolidation",
        "target_state": "volatility_compression",
        "transition_count": 35,
        "empirical_frequency": 0.64,
        "sample_size": 55,
        "non_signal": True,
    },
    {
        "source_state": "range_bound_consolidation",
        "target_state": "trend_persistent_bearish",
        "transition_count": 20,
        "empirical_frequency": 0.36,
        "sample_size": 55,
        "non_signal": True,
    },
]


def calculate_transition_frequency_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-signal empirical transition frequency placeholder."""
    if df is not None and not df.empty and "source_state" in df.columns and "target_state" in df.columns:
        counts = df.groupby(["source_state", "target_state"]).size().reset_index(name="transition_count")
        totals = counts.groupby("source_state")["transition_count"].transform("sum")
        counts["empirical_frequency"] = (counts["transition_count"] / totals).round(4)
        counts["sample_size"] = totals
        counts["non_signal"] = True
        return counts
    return pd.DataFrame(DEFAULT_FREQUENCY_DATA)


def build_state_transition_frequency_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition frequency report dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = calculate_transition_frequency_placeholder()
    summary = summarize_state_transition_frequency(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_transition_frequency(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state transition frequency diagnostics."""
    total_trans = int(df["transition_count"].sum()) if not df.empty and "transition_count" in df.columns else 0
    return {
        "total_transition_pairs": len(df),
        "total_transitions_observed": total_trans,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_prediction": False,
        "contains_predictive_score": False,
        "contains_trading_signal": False,
    }

