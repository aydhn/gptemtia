# -*- coding: utf-8 -*-
"""Phase 154: Mean-Variance Objective Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_mean_variance_objective_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build mean-variance objective placeholder registry."""
    records = [{
        "objective_name": "mean_variance_objective",
        "risk_aversion_parameter": "lambda_risk_aversion",
        "expected_return_vector_ref": "mu_expected_returns_stub",
        "covariance_matrix_ref": "sigma_covariance_stub",
        "is_placeholder": True,
        "actual_objective_calculated": None,
        "is_calculated": False,
        "actual_weights_generated": False,
        "status": "objective_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "objective_name": "mean_variance_objective",
        "is_placeholder": True,
        "is_calculated": False,
        "actual_weights_generated": False,
    }
    return df, summary
