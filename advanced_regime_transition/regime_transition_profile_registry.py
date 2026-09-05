"""Phase 130: Regime Transition Profile Registry.

Builds registry table of available operational profiles for Phase 130.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    REGIME_TRANSITION_PROFILES,
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)


def build_regime_transition_profile_registry(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build dataframe and summary of all registered regime transition profiles."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    rows = []
    for name, p in REGIME_TRANSITION_PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "min_stability_score": p.min_stability_score,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_transition_as_signal": p.allow_transition_as_signal,
                "allow_stability_as_signal": p.allow_stability_as_signal,
                "allow_model_training": p.allow_model_training,
                "allow_clustering_execution": p.allow_clustering_execution,
                "non_signal": True,
                "source_preserved": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": profile.profile_name,
        "total_profiles": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_research_only": bool(df["research_only"].all()),
        "all_non_signal": True,
        "zero_trading_allowed": bool(not df["allow_live_trading"].any()),
        "zero_clustering_allowed": bool(not df["allow_clustering_execution"].any()),
    }
    return df, summary
