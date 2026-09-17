# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Profile Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PROFILES,
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)


def build_portfolio_scenario_control_profile_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 156 configuration profiles."""
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()

    rows = []
    for p_name, p in PROFILES.items():
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "dry_run_default": p.dry_run_default,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_scenario_execution": p.allow_scenario_execution,
            "allow_drawdown_control_execution": p.allow_drawdown_control_execution,
            "allow_portfolio_control_action": p.allow_portfolio_control_action,
            "min_readiness_score": p.min_readiness_score,
            "enabled": p.enabled,
        })

    df = pd.DataFrame(rows)
    summary = {
        "total_profiles": len(df),
        "active_profile": profile.profile_name,
        "current_phase": profile.current_phase,
        "target_final_phase": profile.target_final_phase,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_zero_live_trading": bool((~df["allow_live_trading"]).all()) if not df.empty else True,
    }
    return df, summary
