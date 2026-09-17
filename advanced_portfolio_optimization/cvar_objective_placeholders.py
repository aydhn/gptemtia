# -*- coding: utf-8 -*-
"""Phase 154: CVaR Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_cvar_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build CVaR objective placeholder registry."""
    records = [{
        "objective_name": "cvar_objective",
        "confidence_level_alpha": 0.95,
        "loss_scenarios_ref": "loss_scenarios_matrix_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "cvar_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
