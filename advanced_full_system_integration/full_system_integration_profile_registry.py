# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration Profile Registry.

Builds and summarizes the profile registry for full-system integration contracts.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import (
    FullSystemIntegrationProfile,
    list_full_system_integration_profiles,
)
from .full_system_integration_models import FullSystemIntegrationProfileItem


def build_full_system_integration_profile_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all full-system integration profiles."""
    profiles = list_full_system_integration_profiles()
    items = []
    for p in profiles:
        item = FullSystemIntegrationProfileItem(
            profile_name=p.profile_name,
            description=p.description,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            min_readiness_score=p.min_readiness_score,
            non_signal=True,
            dry_run=p.dry_run_default,
            local_only=p.local_only,
            non_production=p.non_production,
            broker_ready=False,
            production_ready=False,
            live_trading_ready=False,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = summarize_full_system_integration_profiles(df, profile)
    return df, summary


def summarize_full_system_integration_profiles(
    df: pd.DataFrame, profile: FullSystemIntegrationProfile
) -> Dict[str, Any]:
    """Summarize profile registry metadata."""
    return {
        "active_profile": profile.profile_name,
        "total_profiles": len(df),
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "next_phase": profile.next_phase,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_dry_run": bool(df["dry_run"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_broker_ready_false": not bool(df["broker_ready"].any()) if not df.empty else True,
        "all_production_ready_false": not bool(df["production_ready"].any()) if not df.empty else True,
        "all_live_ready_false": not bool(df["live_trading_ready"].any()) if not df.empty else True,
        "status": "full_system_integration_ready",
    }
