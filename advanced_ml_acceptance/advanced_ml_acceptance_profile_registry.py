# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
    list_advanced_ml_acceptance_profiles,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    ADVANCED_ML_ACCEPTANCE_PROFILE_DOMAIN,
    ACCEPTANCE_READY,
)


def build_advanced_ml_acceptance_profile_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for acceptance profiles."""
    active = profile or get_advanced_ml_acceptance_profile()
    profiles = list_advanced_ml_acceptance_profiles(enabled_only=True)

    records = []
    for p in profiles:
        records.append({
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
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_signal_generation": p.allow_signal_generation,
            "allow_backtest_execution": p.allow_backtest_execution,
            "allow_real_model_training": p.allow_real_model_training,
            "allow_model_predict": p.allow_model_predict,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": ADVANCED_ML_ACCEPTANCE_PROFILE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_profiles": len(df),
        "min_readiness_score": active.min_readiness_score,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_advanced_ml_acceptance_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profiles DataFrame."""
    return {
        "profile_count": len(df),
        "profiles": df["profile_name"].tolist() if not df.empty and "profile_name" in df.columns else [],
        "non_signal": True,
    }
