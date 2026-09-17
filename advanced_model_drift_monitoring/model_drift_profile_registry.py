# -*- coding: utf-8 -*-
"""Phase 142: Model Drift Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    PROFILES,
    ModelDriftProfile,
    get_model_drift_profile,
)


def build_model_drift_profile_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all model drift profiles."""
    active_profile = profile or get_model_drift_profile()
    rows = []
    for name, p in PROFILES.items():
        rows.append(
            {
                "profile_name": p.name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_signal_generation": p.allow_signal_generation,
                "allow_model_training": p.allow_model_training,
                "allow_probability_prediction": p.allow_probability_prediction,
                "allow_drift_calculation": p.allow_drift_calculation,
                "allow_drift_metric_calculation": p.allow_drift_metric_calculation,
                "allow_alerting": p.allow_alerting,
                "allow_retraining_trigger": p.allow_retraining_trigger,
                "allow_model_action": p.allow_model_action,
                "min_readiness_score": p.min_readiness_score,
                "is_active": (p.name == active_profile.name),
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_model_drift_profiles(df)
    return df, summary


def summarize_model_drift_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize profile registry DataFrame."""
    total_profiles = len(df)
    active_profile = df[df["is_active"]]["profile_name"].iloc[0] if not df.empty else "unknown"
    return {
        "total_profiles": total_profiles,
        "profiles": df["profile_name"].tolist() if not df.empty else [],
        "active_profile": active_profile,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_non_executing": True,
        "all_zero_calculation": bool((~df["allow_drift_calculation"]).all()) if not df.empty else True,
        "all_zero_drift_calculation": bool((~df["allow_drift_calculation"]).all()) if not df.empty else True,
        "all_zero_alerting": bool((~df["allow_alerting"]).all()) if not df.empty else True,
        "all_zero_retraining_trigger": bool((~df["allow_retraining_trigger"]).all()) if not df.empty else True,
        "all_zero_model_action": bool((~df["allow_model_action"]).all()) if not df.empty else True,
    }

