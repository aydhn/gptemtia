# -*- coding: utf-8 -*-
"""Phase 154: Turnover Minimization Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_turnover_minimization_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build turnover minimization objective placeholder registry."""
    records = [{
        "objective_name": "turnover_minimization_objective",
        "initial_weights_ref": "w_0_initial_weights_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "turnover_minimization_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
