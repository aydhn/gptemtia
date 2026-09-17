# -*- coding: utf-8 -*-
"""Phase 154: Rebalance Constraint Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_rebalance_constraint_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build rebalance constraint placeholder registry."""
    records = [{
        "constraint_name": "rebalance_constraint",
        "minimum_weight_deviation_trigger": 0.02,
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_rebalance_generated": False,
        "status": "constraint_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "constraint_name": "rebalance_constraint",
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_rebalance_generated": False,
    }
    return df, summary
