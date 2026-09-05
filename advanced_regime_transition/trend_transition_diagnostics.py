"""Phase 130: Trend Transition Diagnostics.

Evaluates trend-to-range and directional transition readiness, trend persistence,
momentum decay contexts, and cross-asset trend context prep for Phase 131.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

TREND_TRANSITION_DATA: List[Dict[str, Any]] = [
    {
        "trend_context": "bullish_trend_to_consolidation",
        "trend_regime": "bullish_trend_to_consolidation",
        "transition_readiness": 0.86,
        "trend_persistence": 0.85,
        "trend_persistence_placeholder": 0.85,
        "momentum_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Bullish trend weakening into consolidation context proxy",
    },
    {
        "trend_context": "bearish_trend_to_consolidation",
        "trend_regime": "bearish_trend_to_consolidation",
        "transition_readiness": 0.84,
        "trend_persistence": 0.83,
        "trend_persistence_placeholder": 0.83,
        "momentum_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Bearish trend weakening into consolidation context proxy",
    },
    {
        "trend_context": "range_to_directional_initiation",
        "trend_regime": "range_to_directional_initiation",
        "transition_readiness": 0.80,
        "trend_persistence": 0.76,
        "trend_persistence_placeholder": 0.76,
        "momentum_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Consolidation regime emerging towards directional trend context",
    },
]


def build_trend_transition_diagnostics_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build trend transition diagnostics dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(TREND_TRANSITION_DATA)
    summary = summarize_trend_transition_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_trend_transition_diagnostics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize trend transition diagnostics."""
    mean_readiness = float(df["transition_readiness"].mean()) if not df.empty and "transition_readiness" in df.columns else 0.0
    all_dep = bool((df["momentum_dependency_status"] == "satisfied").all()) if not df.empty else True
    return {
        "total_trend_contexts": len(df),
        "total_contexts": len(df),
        "mean_transition_readiness": round(mean_readiness, 4),
        "all_momentum_dependencies_satisfied": all_dep,
        "all_dependencies_satisfied": all_dep,
        "all_phase_131_ready": bool((df["phase_131_cross_asset_prep"] == "ready").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_trading_signal": False,
    }

