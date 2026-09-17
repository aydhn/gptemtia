# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Profile Registry.

Builds and summarizes operational profile configurations for Phase 147.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import (
    WalkForwardProfile,
    list_walk_forward_profiles,
)


def build_walk_forward_profile_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary metadata for walk-forward profiles."""
    profiles = list_walk_forward_profiles(enabled_only=False)
    rows = []
    for p in profiles:
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
                "min_readiness_score": p.min_readiness_score,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_optimizer_execution": p.allow_optimizer_execution,
                "allow_walk_forward_execution": p.allow_walk_forward_execution,
                "allow_benchmark_execution": p.allow_benchmark_execution,
                "allow_model_training": p.allow_model_training,
                "allow_prediction_generation": p.allow_prediction_generation,
                "allow_performance_claim": p.allow_performance_claim,
                "is_active": p.profile_name == profile.profile_name,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_walk_forward_profiles(df, profile)
    return df, summary


def summarize_walk_forward_profiles(
    df: pd.DataFrame, active_profile: WalkForwardProfile
) -> Dict[str, Any]:
    """Summarize walk-forward profile registry."""
    return {
        "total_profiles": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "zero_live_trading": not bool(df["allow_live_trading"].any()) if not df.empty else True,
        "zero_broker_integration": not bool(df["allow_broker_integration"].any()) if not df.empty else True,
        "zero_walk_forward_execution": not bool(df["allow_walk_forward_execution"].any()) if not df.empty else True,
        "zero_benchmark_execution": not bool(df["allow_benchmark_execution"].any()) if not df.empty else True,
        "non_signal": True,
    }
