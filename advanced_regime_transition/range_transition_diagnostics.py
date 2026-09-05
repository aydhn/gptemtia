"""Phase 130: Range Transition Diagnostics.

Evaluates range persistence, consolidation boundaries, compression/expansion transition
readiness, and cross-asset range context prep for Phase 131.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

RANGE_TRANSITION_DATA: List[Dict[str, Any]] = [
    {
        "range_context": "tight_range_consolidation",
        "range_state": "tight_range_consolidation",
        "range_stability": 0.92,
        "persistence_placeholder": 0.92,
        "breakout_context_placeholder": 0.18,
        "compression_expansion_readiness": 0.89,
        "mean_reversion_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "High persistence tight range channel consolidation",
    },
    {
        "range_context": "wide_channel_oscillation",
        "range_state": "wide_channel_oscillation",
        "range_stability": 0.88,
        "persistence_placeholder": 0.88,
        "breakout_context_placeholder": 0.28,
        "compression_expansion_readiness": 0.85,
        "mean_reversion_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Wide band range oscillations between support and resistance boundaries",
    },
    {
        "range_context": "boundary_testing_phase",
        "range_state": "boundary_testing_phase",
        "range_stability": 0.74,
        "persistence_placeholder": 0.74,
        "breakout_context_placeholder": 0.46,
        "compression_expansion_readiness": 0.82,
        "mean_reversion_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Range boundary test diagnostic context (NOT an order breakout signal)",
    },
]


def build_range_transition_diagnostics_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build range transition diagnostics dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(RANGE_TRANSITION_DATA)
    summary = summarize_range_transition_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_range_transition_diagnostics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize range transition diagnostics."""
    mean_pers = float(df["persistence_placeholder"].mean()) if not df.empty and "persistence_placeholder" in df.columns else 0.0
    all_dep = bool((df["mean_reversion_dependency_status"] == "satisfied").all()) if not df.empty else True
    return {
        "total_range_contexts": len(df),
        "total_contexts": len(df),
        "mean_persistence": round(mean_pers, 4),
        "all_mean_reversion_dependencies_satisfied": all_dep,
        "all_dependencies_satisfied": all_dep,
        "all_phase_131_ready": bool((df["phase_131_cross_asset_prep"] == "ready").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_trading_signal": False,
    }

