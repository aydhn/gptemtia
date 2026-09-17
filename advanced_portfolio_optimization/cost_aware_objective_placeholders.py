# -*- coding: utf-8 -*-
"""Phase 154: Cost-Aware Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_cost_aware_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build cost-aware objective placeholder registry."""
    records = [{
        "objective_name": "cost_aware_objective",
        "linear_cost_coefficient_ref": "c_transaction_cost_stub",
        "initial_weights_ref": "w_0_initial_weights_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "cost_aware_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
