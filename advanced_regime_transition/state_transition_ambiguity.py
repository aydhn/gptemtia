"""Phase 130: State Transition Ambiguity.

Calculates ambiguity metrics during regime transition boundaries.
Helps detect unsharp or conflicting candidate regime assignments without producing trade signals.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

DEFAULT_AMBIGUITY_DATA: List[Dict[str, Any]] = [
    {
        "transition_boundary": "vol_compression -> vol_expansion",
        "boundary_type": "volatility",
        "sample_points": 35,
        "mean_ambiguity_score": 0.28,
        "high_ambiguity_fraction": 0.14,
        "is_acceptable": True,
        "non_signal": True,
    },
    {
        "transition_boundary": "bullish_trend -> range_bound",
        "boundary_type": "trend_range",
        "sample_points": 45,
        "mean_ambiguity_score": 0.36,
        "high_ambiguity_fraction": 0.20,
        "is_acceptable": True,
        "non_signal": True,
    },
    {
        "transition_boundary": "bearish_trend -> range_bound",
        "boundary_type": "trend_range",
        "sample_points": 40,
        "mean_ambiguity_score": 0.34,
        "high_ambiguity_fraction": 0.18,
        "is_acceptable": True,
        "non_signal": True,
    },
    {
        "transition_boundary": "range_bound -> breakout_context",
        "boundary_type": "breakout_context",
        "sample_points": 25,
        "mean_ambiguity_score": 0.44,
        "high_ambiguity_fraction": 0.32,
        "is_acceptable": True,
        "non_signal": True,
    },
]


def calculate_transition_ambiguity_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-signal transition ambiguity placeholder."""
    if df is not None and not df.empty and "ambiguity_score" in df.columns:
        out_df = df.copy()
        mean_amb = float(out_df["ambiguity_score"].mean())
        high_frac = float((out_df["ambiguity_score"] > 0.50).mean())
        return pd.DataFrame(
            [
                {
                    "transition_boundary": "custom_computed_boundary",
                    "boundary_type": "custom",
                    "sample_points": len(out_df),
                    "mean_ambiguity_score": round(mean_amb, 4),
                    "high_ambiguity_fraction": round(high_frac, 4),
                    "is_acceptable": high_frac < 0.35,
                    "non_signal": True,
                }
            ]
        )
    return pd.DataFrame(DEFAULT_AMBIGUITY_DATA)


def build_state_transition_ambiguity_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition ambiguity report dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = calculate_transition_ambiguity_placeholder()
    summary = summarize_state_transition_ambiguity(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_transition_ambiguity(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state transition ambiguity diagnostics."""
    mean_amb = float(df["mean_ambiguity_score"].mean()) if not df.empty and "mean_ambiguity_score" in df.columns else 0.0
    return {
        "total_boundaries_analyzed": len(df),
        "total_ambiguity_records": len(df),
        "overall_mean_ambiguity": round(mean_amb, 4),
        "all_acceptable": bool(df["is_acceptable"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_prediction": False,
        "contains_predictive_score": False,
        "contains_trading_signal": False,
    }

