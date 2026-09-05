"""Phase 124 Feature Store Integration Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    list_feature_store_integration_profiles,
    get_default_feature_store_integration_profile,
)


def build_feature_store_integration_profile_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store integration profiles."""
    active_profile = profile or get_default_feature_store_integration_profile()
    profiles = list_feature_store_integration_profiles(enabled_only=False)

    records = []
    for p in profiles:
        records.append({
            "profile_name": p.name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "research_only": p.research_only,
            "min_readiness_score": p.min_readiness_score,
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_store_as_signal": p.allow_store_as_signal,
            "allow_source_overwrite": p.allow_source_overwrite,
            "allow_auto_imputation": p.allow_auto_imputation,
            "allow_auto_feature_drop": p.allow_auto_feature_drop,
            "enabled": p.enabled,
            "is_active": p.name == active_profile.name,
        })

    df = pd.DataFrame(records)
    summary = {
        "total_profiles": len(records),
        "active_profile": active_profile.name,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "non_signal": True,
        "source_preserved": True,
        "destructive_action_allowed": False,
    }
    return df, summary


def summarize_feature_store_integration_profile_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profile registry."""
    if df.empty:
        return {"total_profiles": 0, "active_profile": "none", "non_signal": True}
    active_mask = df.get("is_active", False)
    active_name = df.loc[active_mask, "profile_name"].iloc[0] if active_mask.any() else "unknown"
    return {
        "total_profiles": len(df),
        "active_profile": active_name,
        "non_signal": bool(not any(df.get("allow_store_as_signal", [False]))),
        "source_preserved": bool(not any(df.get("allow_source_overwrite", [False]))),
        "destructive_action_allowed": False,
    }
