# -*- coding: utf-8 -*-
"""Phase 154: Optimization Result Output Contracts."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_result_output_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build optimization result output contracts table."""
    records = [{
        "output_contract_name": "optimization_result_output_contract",
        "contains_actual_weights": False,
        "contains_actual_allocation": False,
        "contains_actual_objective_value": False,
        "contains_solver_result": False,
        "contract_validation_status": "optimization_contract_ready",
        "manual_review_required": True,
    }]
    df = pd.DataFrame(records)
    summary = {
        "output_contract_name": "optimization_result_output_contract",
        "zero_actual_weights": True,
        "contract_ready": True,
    }
    return df, summary
