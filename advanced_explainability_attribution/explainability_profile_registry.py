# -*- coding: utf-8 -*-
"""Phase 143: Explainability Profile Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    PROFILES,
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_profile_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability profiles."""
    active_profile = profile or get_explainability_profile()

    rows: List[Dict[str, Any]] = []
    for name, prof in PROFILES.items():
        is_active = (name == active_profile.name)
        rows.append({
            "profile_name": prof.name,
            "display_name": prof.display_name,
            "description": prof.description,
            "current_phase": prof.current_phase,
            "target_final_phase": prof.target_final_phase,
            "next_phase": prof.next_phase,
            "is_active": is_active,
            "dry_run_default": prof.dry_run_default,
            "local_only": prof.local_only,
            "non_production": prof.non_production,
            "research_only": prof.research_only,
            "non_signal": True,
            "source_preserved": True,
            "min_readiness_score": prof.min_readiness_score,
            "allow_live_trading": prof.allow_live_trading,
            "allow_explainability_calculation": prof.allow_explainability_calculation,
            "allow_feature_attribution_calculation": prof.allow_feature_attribution_calculation,
            "allow_shap_execution": prof.allow_shap_execution,
            "allow_lime_execution": prof.allow_lime_execution,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_profiles(df)
    return df, summary


def summarize_explainability_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profile registry statistics."""
    total_profiles = len(df)
    active_row = df[df["is_active"] == True]
    active_name = active_row["profile_name"].iloc[0] if not active_row.empty else "unknown"

    return {
        "total_profiles": total_profiles,
        "active_profile": active_name,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
