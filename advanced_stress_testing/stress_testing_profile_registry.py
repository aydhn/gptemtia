# -*- coding: utf-8 -*-
"""Phase 148: Stress Testing Profile Registry.

Builds and summarizes operational profiles for the stress testing contract layer.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import (
    PROFILES,
    StressTestingProfile,
    list_stress_testing_profiles,
)
from advanced_stress_testing.stress_testing_models import StressTestingProfileItem


def build_stress_testing_profile_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all configured stress testing profiles."""
    profiles = list_stress_testing_profiles()
    rows: List[Dict[str, Any]] = []
    for p in profiles:
        item = StressTestingProfileItem(
            profile_name=p.profile_name,
            description=p.description,
            current_phase=p.current_phase,
            target_final_phase=p.target_final_phase,
            next_phase=p.next_phase,
            local_only=p.local_only,
            dry_run=p.dry_run_default,
            non_production=p.non_production,
            non_signal=True,
            broker_ready=False,
            production_ready=False,
            live_trading_ready=False,
            official_approval=False,
            min_readiness_score=p.min_readiness_score,
        )
        rows.append(
            {
                "profile_name": item.profile_name,
                "description": item.description,
                "current_phase": item.current_phase,
                "target_final_phase": item.target_final_phase,
                "next_phase": item.next_phase,
                "local_only": item.local_only,
                "dry_run": item.dry_run,
                "non_production": item.non_production,
                "non_signal": item.non_signal,
                "broker_ready": item.broker_ready,
                "production_ready": item.production_ready,
                "live_trading_ready": item.live_trading_ready,
                "official_approval": item.official_approval,
                "min_readiness_score": item.min_readiness_score,
                "is_active": p.profile_name == profile.profile_name,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": profile.profile_name,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "zero_broker_ready": not bool(df["broker_ready"].any()) if not df.empty else True,
        "zero_production_ready": not bool(df["production_ready"].any()) if not df.empty else True,
        "zero_live_trading_ready": not bool(df["live_trading_ready"].any()) if not df.empty else True,
    }
    return df, summary
