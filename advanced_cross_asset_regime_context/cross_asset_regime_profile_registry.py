"""Phase 131: Cross-Asset Regime Profile Registry.

Builds and registers operational profiles for Cross-Asset Regime Context Expansion.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CROSS_ASSET_REGIME_PROFILES,
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)


def build_cross_asset_regime_profile_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for registered cross-asset regime profiles."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for name, p in CROSS_ASSET_REGIME_PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "default_language": p.default_language,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "min_context_score": p.min_context_score,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
                "contains_target_or_prediction": False,
                "contains_trading_recommendation": False,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_context_as_signal": p.allow_context_as_signal,
                "allow_correlation_as_signal": p.allow_correlation_as_signal,
                "allow_divergence_as_signal": p.allow_divergence_as_signal,
                "allow_model_training": p.allow_model_training,
                "allow_clustering_execution": p.allow_clustering_execution,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": profile.profile_name,
        "current_phase": 131,
        "target_final_phase": 160,
        "next_phase": 132,
        "all_local_only": bool(df["local_only"].all()),
        "all_non_production": bool(df["non_production"].all()),
        "all_research_only": bool(df["research_only"].all()),
        "all_non_signal": True,
        "zero_trading_allowed": True,
        "zero_model_training": True,
    }
    return df, summary
