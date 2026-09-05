"""Phase 129: Market Behavior Diagnostics Profile Registry.

Builds a DataFrame and summary of operational profiles and non-signal constraints.
"""

from typing import Optional, Tuple
import pandas as pd

from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES,
    MarketBehaviorDiagnosticsProfile,
    get_market_behavior_diagnostics_profile,
)


def build_market_behavior_diagnostics_profile_registry(
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> Tuple[pd.DataFrame, dict]:
    """Build DataFrame and metadata summary of operational profiles."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()

    rows = []
    for name, p in MARKET_BEHAVIOR_DIAGNOSTICS_PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "min_quality_score": p.min_quality_score,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_quality_as_signal": p.allow_quality_as_signal,
                "allow_behavior_as_signal": p.allow_behavior_as_signal,
                "allow_candidate_state_as_signal": p.allow_candidate_state_as_signal,
                "allow_model_training": p.allow_model_training,
                "allow_clustering_execution": p.allow_clustering_execution,
                "allow_unsupervised_execution": p.allow_unsupervised_execution,
                "allow_target_label_generation": p.allow_target_label_generation,
                "allow_prediction_generation": p.allow_prediction_generation,
                "allow_source_overwrite": p.allow_source_overwrite,
                "allow_auto_destructive_cleaning": p.allow_auto_destructive_cleaning,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_market_behavior_diagnostics_profiles(df, profile)
    return df, summary


def summarize_market_behavior_diagnostics_profiles(
    df: pd.DataFrame,
    profile: Optional[MarketBehaviorDiagnosticsProfile] = None,
) -> dict:
    """Summarize operational profiles inventory."""
    if profile is None:
        profile = get_market_behavior_diagnostics_profile()
    return {
        "active_profile": profile.profile_name,
        "total_profiles": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "non_signal": True,
        "all_non_signal": True,
        "source_preserved": True,
        "clustering_executed": False,
        "model_training_executed": False,
    }

