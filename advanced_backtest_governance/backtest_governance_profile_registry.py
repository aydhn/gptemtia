# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Profile Registry.

Builds and summarizes the catalog of backtest governance profiles.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import (
    BacktestGovernanceProfile,
    list_backtest_governance_profiles,
)
from advanced_backtest_governance.backtest_governance_labels import (
    BACKTEST_GOVERNANCE_PROFILE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)


def summarize_backtest_governance_profiles(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the registered backtest governance profiles."""
    return {
        "domain": BACKTEST_GOVERNANCE_PROFILE_DOMAIN,
        "total_profiles": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_local_only": bool((df["local_only"] == True).all()) if not df.empty else True,
        "all_non_production": bool((df["non_production"] == True).all()) if not df.empty else True,
        "all_executions_disabled": bool((df["allow_backtest_execution"] == False).all()) if not df.empty else True,
        "all_live_trading_disabled": bool((df["allow_live_trading"] == False).all()) if not df.empty else True,
        "non_signal": True,
    }


def build_backtest_governance_profile_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for all governance profiles."""
    profiles = list_backtest_governance_profiles()
    rows: List[Dict[str, Any]] = []
    for p in profiles:
        rows.append({
            "profile_name": p.profile_name,
            "description": p.description,
            "current_phase": p.current_phase,
            "target_final_phase": p.target_final_phase,
            "next_phase": p.next_phase,
            "local_only": p.local_only,
            "non_production": p.non_production,
            "dry_run_default": p.dry_run_default,
            "research_only": p.research_only,
            "allow_live_trading": p.allow_live_trading,
            "allow_broker_integration": p.allow_broker_integration,
            "allow_backtest_execution": p.allow_backtest_execution,
            "allow_metric_calculation": p.allow_metric_calculation,
            "allow_result_claim": p.allow_result_claim,
            "allow_performance_claim": p.allow_performance_claim,
            "allow_strategy_approval": p.allow_strategy_approval,
            "min_readiness_score": p.min_readiness_score,
            "lookahead_guard_strictness": p.lookahead_guard_strictness,
            "survivorship_policy_mode": p.survivorship_policy_mode,
            "snooping_penalty_rate": p.snooping_penalty_rate,
            "max_allowable_multiple_tests": p.max_allowable_multiple_tests,
            "non_signal": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_profiles(df)
    summary["active_profile"] = profile.profile_name
    return df, summary
