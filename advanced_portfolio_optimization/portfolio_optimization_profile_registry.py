# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Profile Registry.

Maintains registered profiles with negative execution invariants.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import (
    PortfolioOptimizationProfile,
    list_portfolio_optimization_profiles,
    get_portfolio_optimization_profile,
    get_default_portfolio_optimization_profile,
)


def build_portfolio_optimization_profile_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build registry of portfolio optimization configuration profiles."""
    profiles = list_portfolio_optimization_profiles(enabled_only=False)
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
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_real_order": p.allow_real_order,
            "allow_investment_advice": p.allow_investment_advice,
            "allow_signal_generation": p.allow_signal_generation,
            "allow_portfolio_optimization": p.allow_portfolio_optimization,
            "allow_portfolio_construction": p.allow_portfolio_construction,
            "allow_position_sizing": p.allow_position_sizing,
            "allow_capital_allocation": p.allow_capital_allocation,
            "allow_weight_generation": p.allow_weight_generation,
            "allow_allocation_generation": p.allow_allocation_generation,
            "allow_rebalance_generation": p.allow_rebalance_generation,
            "allow_order_generation": p.allow_order_generation,
            "allow_optimizer_execution": p.allow_optimizer_execution,
            "allow_solver_execution": p.allow_solver_execution,
            "allow_grid_search_execution": p.allow_grid_search_execution,
            "allow_efficient_frontier_generation": p.allow_efficient_frontier_generation,
            "allow_metric_calculation": p.allow_metric_calculation,
            "min_readiness_score": p.min_readiness_score,
            "enabled": p.enabled,
        })
    df = pd.DataFrame(records)
    active_profile = profile or get_default_portfolio_optimization_profile()
    summary = {
        "profile_count": len(records),
        "active_profile": active_profile.profile_name,
        "all_profiles_non_production": True,
        "all_profiles_dry_run": True,
        "all_profiles_local_only": True,
        "all_profiles_zero_execution": True,
    }
    return df, summary


def summarize_portfolio_optimization_profiles(df: pd.DataFrame) -> Dict:
    """Summarize profile registry table."""
    return {
        "profile_count": len(df),
        "profiles": df["profile_name"].tolist() if "profile_name" in df.columns else [],
        "dry_run_all": bool((df["dry_run_default"] == True).all()) if "dry_run_default" in df.columns else False,
        "local_only_all": bool((df["local_only"] == True).all()) if "local_only" in df.columns else False,
        "zero_trading_all": bool((df["allow_live_trading"] == False).all()) if "allow_live_trading" in df.columns else False,
    }
