"""Phase 130: State Transition Stability.

Calculates multi-dimensional transition stability metrics combining persistence,
low transition ambiguity, and continuity into an aggregate stability diagnostics index.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

DEFAULT_STABILITY_DATA: List[Dict[str, Any]] = [
    {
        "regime_family": "volatility_regimes",
        "persistence_component": 0.82,
        "ambiguity_component": 0.28,
        "continuity_component": 0.99,
        "stability_score": 0.84,
        "stability_tier": "high_stability",
        "non_signal": True,
    },
    {
        "regime_family": "trend_regimes",
        "persistence_component": 0.86,
        "ambiguity_component": 0.32,
        "continuity_component": 0.99,
        "stability_score": 0.85,
        "stability_tier": "high_stability",
        "non_signal": True,
    },
    {
        "regime_family": "range_regimes",
        "persistence_component": 0.90,
        "ambiguity_component": 0.35,
        "continuity_component": 0.99,
        "stability_score": 0.86,
        "stability_tier": "high_stability",
        "non_signal": True,
    },
    {
        "regime_family": "macro_event_regimes",
        "persistence_component": 0.58,
        "ambiguity_component": 0.42,
        "continuity_component": 0.98,
        "stability_score": 0.68,
        "stability_tier": "moderate_stability",
        "non_signal": True,
    },
    {
        "regime_family": "cross_asset_regimes",
        "persistence_component": 0.78,
        "ambiguity_component": 0.34,
        "continuity_component": 0.99,
        "stability_score": 0.81,
        "stability_tier": "high_stability",
        "non_signal": True,
    },
]


def calculate_transition_stability_placeholder(
    df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Calculate non-signal transition stability placeholder."""
    if df is not None and not df.empty and "persistence" in df.columns and "ambiguity" in df.columns:
        out_df = df.copy()
        out_df["continuity"] = out_df.get("continuity", 1.0)
        # formula: 0.4 * persistence + 0.3 * (1 - ambiguity) + 0.3 * continuity
        out_df["stability_score"] = (
            0.4 * out_df["persistence"]
            + 0.3 * (1.0 - out_df["ambiguity"])
            + 0.3 * out_df["continuity"]
        ).round(4)
        out_df["non_signal"] = True
        return out_df
    return pd.DataFrame(DEFAULT_STABILITY_DATA)


def build_state_transition_stability_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build transition stability report dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = calculate_transition_stability_placeholder()
    summary = summarize_state_transition_stability(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_state_transition_stability(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize state transition stability diagnostics."""
    mean_stab = float(df["stability_score"].mean()) if not df.empty and "stability_score" in df.columns else 0.0
    return {
        "total_regime_families": len(df),
        "total_regimes": len(df),
        "mean_stability_score": round(mean_stab, 4),
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_prediction": False,
        "contains_trading_signal": False,
    }

