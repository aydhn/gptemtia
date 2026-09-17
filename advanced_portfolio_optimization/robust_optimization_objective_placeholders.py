# -*- coding: utf-8 -*-
"""Phase 154: Robust Optimization Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_robust_optimization_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build robust optimization objective placeholder registry."""
    records = [{
        "objective_name": "robust_optimization_objective",
        "uncertainty_set_type": "ellipsoidal",
        "uncertainty_bound_delta": 0.10,
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "robust_optimization_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
