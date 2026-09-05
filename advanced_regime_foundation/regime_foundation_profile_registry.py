"""Phase 126: Regime Foundation Profile Registry.

Builds operational profile registry DataFrame and summary metadata.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_foundation.regime_foundation_config import (
    REGIME_FOUNDATION_PROFILES,
    RegimeFoundationProfile,
    get_default_regime_foundation_profile,
)


def build_regime_foundation_profile_registry(
    profile: Optional[RegimeFoundationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime foundation profiles."""
    active_profile = profile or get_default_regime_foundation_profile()

    rows = []
    for p_name, prof in REGIME_FOUNDATION_PROFILES.items():
        rows.append(
            {
                "profile_name": prof.profile_name,
                "description": prof.description,
                "current_phase": prof.current_phase,
                "target_final_phase": prof.target_final_phase,
                "next_phase": prof.next_phase,
                "dry_run_default": prof.dry_run_default,
                "local_only": prof.local_only,
                "non_production": prof.non_production,
                "research_only": prof.research_only,
                "allow_live_trading": prof.allow_live_trading,
                "allow_broker_integration": prof.allow_broker_integration,
                "allow_real_order": prof.allow_real_order,
                "allow_investment_advice": prof.allow_investment_advice,
                "allow_regime_as_signal": prof.allow_regime_as_signal,
                "allow_directional_claim": prof.allow_directional_claim,
                "allow_model_training": prof.allow_model_training,
                "allow_clustering_execution": prof.allow_clustering_execution,
                "min_readiness_score": prof.min_readiness_score,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "total_profiles": len(df),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "all_local_only": bool((df["local_only"] == True).all()),
        "all_non_production": bool((df["non_production"] == True).all()),
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "all_model_training_disabled": bool((df["allow_model_training"] == False).all()),
        "all_clustering_disabled": bool((df["allow_clustering_execution"] == False).all()),
        "official_approval": False,
        "production_ready": False,
        "broker_ready": False,
    }
    return df, summary
