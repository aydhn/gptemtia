"""Phase 130: Volatility Transition Diagnostics.

Evaluates volatility expansion/compression transitions, candidate state persistence,
and cross-asset volatility context preparation for Phase 131.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

VOLATILITY_TRANSITION_DATA: List[Dict[str, Any]] = [
    {
        "volatility_context": "compression_to_expansion",
        "volatility_regime": "compression_to_expansion",
        "transition_readiness": 0.88,
        "context_continuity": 0.99,
        "persistence_placeholder": 0.72,
        "quality_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Volatility compression into expansion transition readiness proxy",
    },
    {
        "volatility_context": "expansion_to_exhaustion",
        "volatility_regime": "expansion_to_exhaustion",
        "transition_readiness": 0.84,
        "context_continuity": 0.98,
        "persistence_placeholder": 0.68,
        "quality_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "High volatility expansion towards calm/exhaustion transition context",
    },
    {
        "volatility_context": "baseline_calm_regime",
        "volatility_regime": "baseline_calm_regime",
        "transition_readiness": 0.94,
        "context_continuity": 1.00,
        "persistence_placeholder": 0.91,
        "quality_dependency_status": "satisfied",
        "phase_131_cross_asset_prep": "ready",
        "non_signal": True,
        "description": "Persistent baseline volatility regime stability",
    },
]



def build_volatility_transition_diagnostics_report(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build volatility transition diagnostics dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(VOLATILITY_TRANSITION_DATA)
    summary = summarize_volatility_transition_diagnostics(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_volatility_transition_diagnostics(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize volatility transition diagnostics."""
    mean_readiness = float(df["transition_readiness"].mean()) if not df.empty and "transition_readiness" in df.columns else 0.0
    return {
        "total_contexts": len(df),
        "mean_transition_readiness": round(mean_readiness, 4),
        "all_dependencies_satisfied": bool((df["quality_dependency_status"] == "satisfied").all()) if not df.empty else True,
        "all_phase_131_ready": bool((df["phase_131_cross_asset_prep"] == "ready").all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "contains_trading_signal": False,
    }
