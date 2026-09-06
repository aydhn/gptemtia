"""Phase 134: Regime FeatureStore Profile Registry.

Builds and summarizes the catalog of supported FeatureStore profiles.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    PROFILES,
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
    validate_regime_featurestore_profiles,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_PROFILE_DOMAIN,
    REGIME_STORE_READY,
)


def build_regime_featurestore_profile_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular profile registry containing all configured profiles."""
    validate_regime_featurestore_profiles()
    active_profile = profile or get_regime_featurestore_profile()

    rows = []
    for p_name, p in PROFILES.items():
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "min_readiness_score": p.min_readiness_score,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "non_signal": True,
            "source_preserved": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
            "is_active": (p.profile_name == active_profile.profile_name),
            "status": REGIME_STORE_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": REGIME_FEATURESTORE_PROFILE_DOMAIN,
        "total_profiles": len(rows),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "status": REGIME_STORE_READY,
        "non_signal": True,
        "production_ready": False,
    }
    return df, summary


def summarize_regime_featurestore_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profile registry DataFrame."""
    return {
        "total_profiles": len(df),
        "profile_names": df["profile_name"].tolist() if not df.empty else [],
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
        "all_local_only": bool((df["local_only"] == True).all()) if not df.empty else True,
    }
