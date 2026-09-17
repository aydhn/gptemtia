# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Profile Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
    list_backtest_acceptance_profiles,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    BACKTEST_ACCEPTANCE_PROFILE_DOMAIN,
    ACCEPTANCE_READY,
)


def build_backtest_acceptance_profile_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary of configured backtest acceptance profiles."""
    active = profile or get_backtest_acceptance_profile()
    profiles = list_backtest_acceptance_profiles(enabled_only=False)

    records = []
    for p in profiles:
        records.append({
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
            "enabled": p.enabled,
            "is_active": (p.profile_name == active.profile_name),
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": BACKTEST_ACCEPTANCE_PROFILE_DOMAIN,
        "active_profile": active.profile_name,
        "total_profiles": len(profiles),
        "enabled_profiles": len([p for p in profiles if p.enabled]),
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "all_dry_run": all(p.dry_run_default for p in profiles),
        "all_local_only": all(p.local_only for p in profiles),
        "all_non_production": all(p.non_production for p in profiles),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
