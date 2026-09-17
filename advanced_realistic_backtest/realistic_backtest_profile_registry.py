# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest Profile Registry.

Builds and summarizes operational backtest profile metadata.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import (
    PROFILES,
    RealisticBacktestProfile,
)


def build_realistic_backtest_profile_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of all realistic backtest profiles."""
    rows = []
    for p in PROFILES.values():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "default_language": p.default_language,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_real_order": p.allow_real_order,
                "allow_investment_advice": p.allow_investment_advice,
                "allow_signal_generation": p.allow_signal_generation,
                "allow_directional_claim": p.allow_directional_claim,
                "allow_optimizer_execution": p.allow_optimizer_execution,
                "allow_walk_forward_execution": p.allow_walk_forward_execution,
                "allow_benchmark_execution": p.allow_benchmark_execution,
                "allow_stress_test_execution": p.allow_stress_test_execution,
                "allow_monte_carlo_execution": p.allow_monte_carlo_execution,
                "allow_model_training": p.allow_model_training,
                "allow_model_predict": p.allow_model_predict,
                "allow_performance_claim": p.allow_performance_claim,
                "min_readiness_score": p.min_readiness_score,
                "is_active": (p.profile_name == profile.profile_name),
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_realistic_backtest_profiles(df, profile)
    return df, summary


def summarize_realistic_backtest_profiles(
    df: pd.DataFrame, profile: RealisticBacktestProfile
) -> Dict[str, Any]:
    """Summarize the backtest profile registry."""
    return {
        "active_profile": profile.profile_name,
        "total_profiles": len(df),
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "live_trading_allowed": False,
        "broker_integration_allowed": False,
        "optimizer_execution_allowed": False,
        "walk_forward_allowed": False,
        "benchmark_allowed": False,
        "model_training_allowed": False,
        "non_signal": True,
    }


summarize_realistic_backtest_profile_registry = summarize_realistic_backtest_profiles
