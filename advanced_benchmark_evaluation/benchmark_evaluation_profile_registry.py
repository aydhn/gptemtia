# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Profile Registry Module.

Builds and summarizes active benchmark evaluation profiles with strict negative invariant guarantees.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    BenchmarkEvaluationProfile,
    PROFILES,
    get_benchmark_evaluation_profile,
    list_benchmark_evaluation_profiles,
)
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_EVALUATION_PROFILE_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)


def build_benchmark_evaluation_profile_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all benchmark evaluation profiles."""
    active_prof = profile or get_benchmark_evaluation_profile()
    rows: List[Dict[str, Any]] = []

    for name, p in PROFILES.items():
        rows.append(
            {
                "profile_name": p.profile_name,
                "description": p.description,
                "domain": LABEL_BENCHMARK_EVALUATION_PROFILE_DOMAIN,
                "current_phase": p.current_phase,
                "target_final_phase": p.target_final_phase,
                "next_phase": p.next_phase,
                "dry_run_default": p.dry_run_default,
                "local_only": p.local_only,
                "non_production": p.non_production,
                "research_only": p.research_only,
                "allow_live_trading": p.allow_live_trading,
                "allow_broker_integration": p.allow_broker_integration,
                "allow_backtest_execution": p.allow_backtest_execution,
                "allow_benchmark_execution": p.allow_benchmark_execution,
                "allow_metric_calculation": p.allow_metric_calculation,
                "allow_result_claim": p.allow_result_claim,
                "allow_performance_claim": p.allow_performance_claim,
                "allow_strategy_approval": p.allow_strategy_approval,
                "min_readiness_score": p.min_readiness_score,
                "is_active": p.profile_name == active_prof.profile_name,
                "status": STATUS_EVALUATION_CONTRACT_READY,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_benchmark_evaluation_profiles(df, active_prof)
    return df, summary


def summarize_benchmark_evaluation_profiles(
    df: pd.DataFrame,
    active_profile: BenchmarkEvaluationProfile | None = None,
) -> Dict[str, Any]:
    """Summarize profile registry status."""
    active_name = (
        active_profile.profile_name
        if active_profile
        else "balanced_local_benchmark_evaluation_contracts"
    )
    return {
        "domain": LABEL_BENCHMARK_EVALUATION_PROFILE_DOMAIN,
        "total_profiles": len(df),
        "active_profile": active_name,
        "all_dry_run": bool(df["dry_run_default"].all()) if not df.empty else True,
        "all_local_only": bool(df["local_only"].all()) if not df.empty else True,
        "all_non_production": bool(df["non_production"].all()) if not df.empty else True,
        "all_live_trading_prohibited": not bool(df["allow_live_trading"].any()) if not df.empty else True,
        "all_broker_prohibited": not bool(df["allow_broker_integration"].any()) if not df.empty else True,
        "all_backtest_prohibited": not bool(df["allow_backtest_execution"].any()) if not df.empty else True,
        "all_benchmark_prohibited": not bool(df["allow_benchmark_execution"].any()) if not df.empty else True,
        "all_claims_prohibited": not bool(df["allow_result_claim"].any()) if not df.empty else True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
