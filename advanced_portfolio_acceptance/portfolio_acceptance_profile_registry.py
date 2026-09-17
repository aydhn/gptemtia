# -*- coding: utf-8 -*-
"""Phase 157: Portfolio Acceptance Profile Registry.

Builds and summarizes the profile registry for Phase 157 Portfolio Acceptance.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
    list_portfolio_acceptance_profiles,
)
from .portfolio_acceptance_labels import (
    PORTFOLIO_ACCEPTANCE_PROFILE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)


def build_portfolio_acceptance_profile_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of configured portfolio acceptance profiles."""
    active = profile or get_portfolio_acceptance_profile()
    profiles = list_portfolio_acceptance_profiles()

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
            "allow_portfolio_construction": p.allow_portfolio_construction,
            "allow_portfolio_optimization": p.allow_portfolio_optimization,
            "allow_risk_reporting_execution": p.allow_risk_reporting_execution,
            "allow_scenario_execution": p.allow_scenario_execution,
            "allow_drawdown_control_execution": p.allow_drawdown_control_execution,
            "is_active": (p.profile_name == active.profile_name),
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })

    df = pd.DataFrame(records)
    summary = summarize_portfolio_acceptance_profile_registry(df, active)
    return df, summary


def summarize_portfolio_acceptance_profile_registry(
    df: pd.DataFrame,
    active_profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Dict[str, Any]:
    """Summarize portfolio acceptance profile registry DataFrame."""
    active_name = active_profile.profile_name if active_profile else (
        df.loc[df["is_active"], "profile_name"].iloc[0] if not df.empty and "is_active" in df.columns else "unknown"
    )
    return {
        "domain": PORTFOLIO_ACCEPTANCE_PROFILE_DOMAIN,
        "total_profiles": len(df),
        "active_profile": active_name,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_live_trading_disabled": not bool(df["allow_live_trading"].any()) if not df.empty else True,
        "status": PORTFOLIO_ACCEPTANCE_READY,
    }
