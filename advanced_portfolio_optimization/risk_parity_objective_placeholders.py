# -*- coding: utf-8 -*-
"""Phase 154: Risk Parity Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_risk_parity_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build risk parity objective placeholder registry."""
    records = [{
        "objective_name": "risk_parity_objective",
        "covariance_matrix_ref": "sigma_covariance_stub",
        "risk_budget_vector_ref": "b_target_risk_budget_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "risk_parity_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
