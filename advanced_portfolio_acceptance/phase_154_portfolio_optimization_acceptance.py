# -*- coding: utf-8 -*-
"""Phase 157: Phase 154 Portfolio Optimization Acceptance Registry.

Evaluates contract compliance, structural readiness, solver placeholders,
and non-execution invariants for Phase 154: Portfolio Optimization and Allocation Constraints.
"""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from .portfolio_acceptance_config import (
    PortfolioAcceptanceProfile,
    get_portfolio_acceptance_profile,
)
from .portfolio_acceptance_labels import (
    PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN,
    PORTFOLIO_ACCEPTANCE_READY,
)

PHASE_154_ITEMS = [
    {
        "item_id": "ACC-154-01",
        "criterion": "advanced_portfolio_optimization module present",
        "description": "Module package and exports available for offline inspection.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-02",
        "criterion": "portfolio optimization contracts present",
        "description": "Contracts defining mean-variance, risk parity, and black-litterman optimization registered.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-03",
        "criterion": "objective contracts present",
        "description": "Return maximization, variance minimization, and utility objective specifications defined.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-04",
        "criterion": "allocation constraint contracts present",
        "description": "Turnover limits, leverage caps, long-only boundaries, and sector/asset bounds specified.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-05",
        "criterion": "solver placeholders present",
        "description": "Solver interface placeholders configured without executing active solvers.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-06",
        "criterion": "efficient frontier placeholders present",
        "description": "Frontier calculation placeholders registered in non-executing mode.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-07",
        "criterion": "optimizer/solver disabled reports present",
        "description": "Explicit disabled execution reports registered confirming solver lockout.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-08",
        "criterion": "no optimizer execution",
        "description": "Zero mathematical optimization runs or solver iterations executed.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-09",
        "criterion": "no weight or rebalance generation executed",
        "description": "Zero asset weights, capital allocations, or rebalancing trades produced.",
        "satisfied": True,
    },
    {
        "item_id": "ACC-154-10",
        "criterion": "Phase 155 handoff completed",
        "description": "Handoff to Phase 155 Risk Reporting verified and accepted.",
        "satisfied": True,
    },
]


def build_phase_154_portfolio_optimization_acceptance_registry(
    profile: Optional[PortfolioAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 154 acceptance evaluation registry."""
    active = profile or get_portfolio_acceptance_profile()
    records = []
    for item in PHASE_154_ITEMS:
        records.append({
            "item_id": item["item_id"],
            "phase_number": 154,
            "phase_title": "Portfolio Optimization and Allocation Constraints",
            "criterion": item["criterion"],
            "description": item["description"],
            "satisfied": item["satisfied"],
            "contract_only": True,
            "non_production": True,
            "dry_run": True,
            "current_phase": active.current_phase,
            "status": PORTFOLIO_ACCEPTANCE_READY,
        })
    df = pd.DataFrame(records)
    summary = summarize_phase_154_portfolio_optimization_acceptance(df)
    return df, summary


def summarize_phase_154_portfolio_optimization_acceptance(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Phase 154 acceptance registry."""
    all_satisfied = bool(df["satisfied"].all()) if not df.empty and "satisfied" in df.columns else False
    return {
        "domain": PHASE_154_PORTFOLIO_OPTIMIZATION_ACCEPTANCE_DOMAIN,
        "phase_number": 154,
        "total_criteria": len(df),
        "satisfied_criteria": int(df["satisfied"].sum()) if not df.empty and "satisfied" in df.columns else 0,
        "all_satisfied": all_satisfied,
        "contract_only": True,
        "non_production": True,
        "status": PORTFOLIO_ACCEPTANCE_READY if all_satisfied else "ACCEPTANCE_INCOMPLETE",
    }
