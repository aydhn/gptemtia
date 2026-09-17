# -*- coding: utf-8 -*-
"""Phase 152: Backtest Acceptance Scope Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_backtest_acceptance.backtest_acceptance_config import (
    BacktestAcceptanceProfile,
    get_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    BACKTEST_ACCEPTANCE_SCOPE_DOMAIN,
    ACCEPTANCE_READY,
)

SCOPE_ITEMS: List[Dict[str, Any]] = [
    {
        "scope_id": "SCP-152-01",
        "scope_name": "phase_146_152_block_acceptance",
        "description": "Consolidated acceptance of Phases 146-152 backtest/benchmark/robustness block.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-02",
        "scope_name": "local_offline_governance",
        "description": "Enforce local and offline execution without remote service calls.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-03",
        "scope_name": "dry_run_validation_contracts",
        "description": "Verify dry-run compliance and contract existence across all sub-components.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-04",
        "scope_name": "non_production_boundary_enforcement",
        "description": "Enforce non-production, research-only boundaries on all outputs.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-05",
        "scope_name": "no_live_trading_or_broker_orders",
        "description": "Strict prohibition of live trading or broker order routing.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-06",
        "scope_name": "no_real_backtest_execution",
        "description": "Prohibit execution of real backtesting loops or PnL generation.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-07",
        "scope_name": "no_real_benchmark_execution",
        "description": "Prohibit execution of real benchmark simulations or tracking error calculations.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-08",
        "scope_name": "no_real_metric_calculation",
        "description": "Prohibit calculation of Sharpe, drawdown, win-rate, alpha, beta, VaR, or returns.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-09",
        "scope_name": "no_strategy_approval_or_capital_allocation",
        "description": "Prohibit strategy approval, capital allocation, portfolio construction, and position sizing.",
        "in_scope": True,
        "is_safe": True,
    },
    {
        "scope_id": "SCP-152-10",
        "scope_name": "phase_153_handoff_preparation",
        "description": "Provide clean handoff to Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting.",
        "in_scope": True,
        "is_safe": True,
    },
]


def build_backtest_acceptance_scope_registry(
    profile: Optional[BacktestAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for backtest acceptance scope items."""
    active = profile or get_backtest_acceptance_profile()

    records = []
    for item in SCOPE_ITEMS:
        records.append({
            "scope_id": item["scope_id"],
            "scope_name": item["scope_name"],
            "description": item["description"],
            "in_scope": item["in_scope"],
            "is_safe": item["is_safe"],
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "local_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": BACKTEST_ACCEPTANCE_SCOPE_DOMAIN,
        "active_profile": active.profile_name,
        "total_scope_items": len(records),
        "in_scope_count": len([r for r in records if r["in_scope"]]),
        "all_safe": all(r["is_safe"] for r in records),
        "non_signal": True,
        "status": "ACCEPTED",
    }
    return df, summary
