"""Phase 133: Regime Validation Acceptance Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_regime_validation_acceptance.regime_validation_acceptance_config import (
    PROFILES,
    RegimeValidationAcceptanceProfile,
    get_default_regime_validation_acceptance_profile,
)


def build_regime_validation_acceptance_profile_registry(
    profile: Optional[RegimeValidationAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of operational profiles for Phase 133."""
    active_profile = profile or get_default_regime_validation_acceptance_profile()
    rows = []
    for name, p in PROFILES.items():
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
                "min_acceptance_score": p.min_acceptance_score,
                "is_active": (p.profile_name == active_profile.profile_name),
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 133,
        "target_final_phase": 160,
        "next_phase": 134,
        "all_non_signal": True,
        "all_source_preserved": True,
        "zero_model_training": True,
        "zero_trading_signals": True,
    }
    return df, summary


def summarize_regime_validation_acceptance_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for profile registry DataFrame."""
    return {
        "total_profiles": len(df),
        "active_profiles": int(df["is_active"].sum()) if "is_active" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns else True,
    }
