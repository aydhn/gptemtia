# -*- coding: utf-8 -*-
"""Phase 154: Maximum Sharpe Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_maximum_sharpe_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build maximum Sharpe objective placeholder registry."""
    records = [{
        "objective_name": "max_sharpe_objective",
        "risk_free_rate_ref": "rf_rate_stub",
        "expected_return_ref": "mu_expected_returns_stub",
        "covariance_matrix_ref": "sigma_covariance_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "max_sharpe_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
