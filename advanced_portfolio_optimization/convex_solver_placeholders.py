# -*- coding: utf-8 -*-
"""Phase 154: Convex Solver Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_convex_solver_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build convex solver placeholder registry."""
    records = [{
        "solver_name": "convex_solver",
        "solver_backend": "osqp_or_clarabel_interface_stub",
        "convergence_tolerance": 1e-6,
        "is_placeholder": True,
        "solver_executed": False,
        "actual_weights_generated": False,
        "status": "solver_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "solver_name": "convex_solver",
        "is_placeholder": True,
        "solver_executed": False,
        "actual_weights_generated": False,
    }
    return df, summary
