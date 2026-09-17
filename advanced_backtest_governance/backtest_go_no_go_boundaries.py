# -*- coding: utf-8 -*-
"""Phase 150: Backtest Go / No-Go Boundaries.

Defines allowable research progression activities (Go) versus strictly prohibited
production and execution actions (No-Go).
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    GO_NO_GO_BOUNDARY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

GO_ACTIVITIES: List[Dict[str, Any]] = [
    {
        "activity_name": "proceed_to_phase_151_benchmark_report_contracts",
        "category": "GO",
        "description": "Progress to Phase 151 benchmark comparison and strategy evaluation contracts under offline research boundaries.",
    },
    {
        "activity_name": "proceed_to_strategy_evaluation_report_contracts",
        "category": "GO",
        "description": "Design evaluation report templates, metric placeholders, and risk factor disclosure schemas.",
    },
    {
        "activity_name": "proceed_to_non_live_result_disclosure_design",
        "category": "GO",
        "description": "Draft local/offline reporting disclosures emphasizing empirical hypothesis framing and drawdowns.",
    },
]

NO_GO_ACTIVITIES: List[Dict[str, Any]] = [
    {
        "activity_name": "run_backtest",
        "category": "NO_GO",
        "description": "Running actual backtest execution engine across historical bars.",
    },
    {
        "activity_name": "run_benchmark",
        "category": "NO_GO",
        "description": "Executing real benchmark simulation or performance comparison calculations.",
    },
    {
        "activity_name": "calculate_metrics",
        "category": "NO_GO",
        "description": "Calculating actual numerical values for Sharpe, win-rate, CAGR, alpha, or drawdown.",
    },
    {
        "activity_name": "optimize_strategy",
        "category": "NO_GO",
        "description": "Running grid, random, or heuristic parameter optimization loops.",
    },
    {
        "activity_name": "approve_strategy",
        "category": "NO_GO",
        "description": "Granting formal strategy approval or sign-off for deployment.",
    },
    {
        "activity_name": "generate_signal",
        "category": "NO_GO",
        "description": "Emitting definitive buy/sell, long/short, or positioning recommendations.",
    },
    {
        "activity_name": "live_trading",
        "category": "NO_GO",
        "description": "Interfacing with live capital, exchange order routing, or position management.",
    },
    {
        "activity_name": "broker_execution",
        "category": "NO_GO",
        "description": "Connecting to broker APIs or submitting trading instructions.",
    },
    {
        "activity_name": "deploy_model",
        "category": "NO_GO",
        "description": "Deploying strategy models to production servers or container registries.",
    },
    {
        "activity_name": "performance_claim",
        "category": "NO_GO",
        "description": "Publishing guaranteed return, proven alpha, or production-ready performance assertions.",
    },
]

NO_GO_KEYWORDS = [
    "run_backtest",
    "run_benchmark",
    "calculate_metrics",
    "optimize_strategy",
    "approve_strategy",
    "generate_signal",
    "live_trading",
    "broker_execution",
    "deploy_model",
    "performance_claim",
    "live_trade",
    "broker_order",
    "send_order",
    "buy",
    "sell",
    "long",
    "short",
]


def validate_backtest_go_no_go_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Inspect request against Go / No-Go policy boundaries."""
    text = str(request).lower()
    blocked = False
    violating_tokens: List[str] = []

    for token in NO_GO_KEYWORDS:
        if token in text:
            blocked = True
            violating_tokens.append(token)

    decision = "NO_GO_BLOCKED" if blocked else "SAFE_GO_PERMITTED"
    return {
        "is_permitted": not blocked,
        "is_blocked": blocked,
        "decision": decision,
        "violating_tokens": violating_tokens,
        "policy_message": (
            f"Action blocked by No-Go policy: violating tokens {violating_tokens}. "
            "Real execution, metric calculation, and trading are forbidden."
            if blocked
            else "Action verified within Safe-Go research boundaries."
        ),
        "non_signal": True,
    }


def build_backtest_go_no_go_boundary_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Go / No-Go boundaries."""
    rows: List[Dict[str, Any]] = []
    for item in GO_ACTIVITIES:
        rows.append({
            "activity_name": item["activity_name"],
            "category": "GO",
            "permitted": True,
            "description": item["description"],
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    for item in NO_GO_ACTIVITIES:
        rows.append({
            "activity_name": item["activity_name"],
            "category": "NO_GO",
            "permitted": False,
            "description": item["description"],
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": GO_NO_GO_BOUNDARY_DOMAIN,
        "total_activities": len(df),
        "go_count": len(GO_ACTIVITIES),
        "no_go_count": len(NO_GO_ACTIVITIES),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "all_no_go_strictly_blocked": True,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
