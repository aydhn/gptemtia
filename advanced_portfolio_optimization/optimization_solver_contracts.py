# -*- coding: utf-8 -*-
"""Phase 154: Optimization Solver Contracts.

Defines interface specifications for convex and heuristic solvers.
Strictly offline, contract mode, zero execution.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

SOLVER_CATALOG = [
    (
        "convex_solver",
        "convex_quadratic_programming",
        "Konveks kuadratik ve koni programlama arayuzu sozlesmesi",
        ["mean_variance_objective", "min_variance_objective", "cvar_objective", "cost_aware_objective"],
    ),
    (
        "heuristic_solver",
        "heuristic_evolutionary",
        "Sezgisel (risk parity, cardinality constrained) arayuz sozlesmesi",
        ["risk_parity_objective", "drawdown_minimization_objective", "regime_aware_objective"],
    ),
    (
        "grid_search_solver",
        "grid_search_prohibited",
        "Izgara aramali agirlik tarama cozucusu (KESIN ENGEL)",
        [],
    ),
]


def build_optimization_solver_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build registered solver contracts table."""
    records = []
    for name, s_type, desc, obj_list in SOLVER_CATALOG:
        is_disabled = (s_type == "grid_search_prohibited")
        records.append({
            "solver_name": name,
            "solver_type": s_type,
            "description": desc,
            "supported_objectives_count": len(obj_list),
            "is_placeholder": True,
            "solver_executed": False,
            "allows_execution": False,
            "is_disabled": is_disabled,
            "manual_review_required": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "solver_count": len(records),
        "all_solvers_placeholders": True,
        "zero_solvers_executed": True,
        "grid_search_disabled": True,
    }
    return df, summary


def validate_optimization_solver_contract(contract: dict) -> dict:
    """Validate solver contract invariants."""
    is_valid = True
    reasons = []
    if contract.get("allows_execution", False) is True:
        is_valid = False
        reasons.append("allows_execution must be False")
    if contract.get("solver_executed", False) is True:
        is_valid = False
        reasons.append("solver_executed must be False")
    return {
        "solver_name": contract.get("solver_name", "unknown"),
        "is_valid": is_valid,
        "reasons": reasons,
    }
