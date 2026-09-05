"""Phase 130: State Transition Continuity.

Provides diagnostic continuity metrics evaluating gaps, missing timestamps,
and sequence consistency in candidate regime time series.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

DEFAULT_CONTINUITY_DATA: List[Dict[str, Any]] = [
    {
        "entity_family": "fx_major",
        "expected_intervals": 1000,
        "observed_intervals": 995,
        "gap_count": 5,
        "continuity_ratio": 0.995,
        "is_continuous": True,
        "non_signal": True,
    },
    {
        "entity_family": "commodity_energy",
        "expected_intervals": 1000,
        "observed_intervals": 988,
        "gap_count": 12,
        "continuity_ratio": 0.988,
        "is_continuous": True,
        "non_signal": True,
    },
    {
        "entity_family": "commodity_metals",
        "expected_intervals": 1000,
        "observed_intervals": 992,
        "gap_count": 8,
        "continuity_ratio": 0.992,
        "is_continuous": True,
        "non_signal": True,
    },
    {
        "entity_family": "macro_events",
        "expected_intervals": 120,
        "observed_intervals": 118,
        "gap_count": 2,
        "continuity_ratio": 0.983,
        "is_continuous": True,
        "non_signal": True,
    },
]


def calculate_transition_continuity_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-signal transition continuity placeholder."""
    if df is not None and not df.empty and "is_valid" in df.columns:
        out_df = df.copy()
        valid_count = int(out_df["is_valid"].sum())
        total_count = len(out_df)
        ratio = round(valid_count / total_count, 4) if total_count > 0 else 1.0
        return pd.DataFrame(
            [
                {
                    "entity_family": "custom_computed",
                    "expected_intervals": total_count,
                    "observed_intervals": valid_count,
                    "gap_count": total_count - valid_count,
                    "continuity_ratio": ratio,
                    "is_continuous": ratio >= 0.95,
                    "non_signal": True,
                }
            ]
        )
    return pd.DataFrame(DEFAULT_CONTINUITY_DATA)


def build_state_transition_continuity_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition continuity report dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = calculate_transition_continuity_placeholder()
    summary = summarize_state_transition_continuity(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_transition_continuity(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state transition continuity diagnostics."""
    mean_ratio = float(df["continuity_ratio"].mean()) if not df.empty and "continuity_ratio" in df.columns else 0.0
    return {
        "total_entity_families": len(df),
        "total_sequences": len(df),
        "mean_continuity_ratio": round(mean_ratio, 4),
        "all_continuous": bool(df["is_continuous"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_prediction": False,
        "contains_trading_signal": False,
    }

