# -*- coding: utf-8 -*-
"""Phase 154: Transaction Cost Constraint Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_transaction_cost_constraint_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build transaction cost constraint placeholder registry."""
    records = [{
        "constraint_name": "transaction_cost_constraint",
        "max_transaction_cost_budget": 0.0050,
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
        "status": "constraint_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "constraint_name": "transaction_cost_constraint",
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
    }
    return df, summary
