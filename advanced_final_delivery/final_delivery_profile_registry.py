# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Profile Registry.

Builds and summarizes the registry of active configuration profiles for Phase 160.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    PROFILES,
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_DELIVERY_PROFILE_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)


def build_final_delivery_profile_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build the final delivery profile registry DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

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
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_real_order": p.allow_real_order,
            "allow_investment_advice": p.allow_investment_advice,
            "allow_signal_generation": p.allow_signal_generation,
            "allow_system_execution": p.allow_system_execution,
            "allow_release_deployment": p.allow_release_deployment,
            "allow_production_deployment": p.allow_production_deployment,
            "allow_model_training": p.allow_model_training,
            "allow_prediction_generation": p.allow_prediction_generation,
            "non_signal": True,
            "domain": FINAL_DELIVERY_PROFILE_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "next_phase": active_profile.next_phase,
        "profile_count": len(rows),
        "all_non_production": bool(df["non_production"].all()),
        "all_local_only": bool(df["local_only"].all()),
        "all_dry_run": bool(df["dry_run_default"].all()),
        "all_no_live": not bool(df["allow_live_trading"].any()),
        "all_no_broker": not bool(df["allow_broker_integration"].any()),
        "domain": FINAL_DELIVERY_PROFILE_DOMAIN,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def summarize_final_delivery_profiles(df: pd.DataFrame) -> Dict:
    """Summarize profile registry."""
    return {
        "total_profiles": len(df),
        "profiles": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
