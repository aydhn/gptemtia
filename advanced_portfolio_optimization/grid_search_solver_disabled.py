# -*- coding: utf-8 -*-
"""Phase 154: Grid Search Solver Disabled Registry.

Strictly prohibits exhaustive grid-search weight optimization to prevent
data snooping, combinatorial explosion, and pseudo-optimization.
"""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_grid_search_solver_disabled_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build grid search solver disabled registry."""
    records = [{
        "component_name": "grid_search_solver",
        "is_disabled": True,
        "reason": "Exhaustive grid-search weight generation leads to severe overfitting and multiple-testing bias",
        "policy": "BLOCK_ALL_GRID_SEARCH_REQUESTS",
        "status": "execution_blocked_no_solver",
    }]
    df = pd.DataFrame(records)
    summary = {
        "grid_search_disabled": True,
        "policy_active": True,
    }
    return df, summary


def validate_no_grid_search_solver_request(request: Union[dict, str]) -> dict:
    """Validate that request does not ask for grid-search solver."""
    text = str(request).lower()
    prohibited = ["grid_search", "exhaustive_search", "weight_grid", "brute_force_allocation"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Grid-search optimization is strictly prohibited by governance policy" if blocked else "OK",
    }
