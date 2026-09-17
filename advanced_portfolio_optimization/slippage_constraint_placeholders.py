# -*- coding: utf-8 -*-
"""Phase 154: Slippage Constraint Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_slippage_constraint_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build slippage constraint placeholder registry."""
    records = [{
        "constraint_name": "slippage_constraint",
        "max_slippage_budget": 0.0030,
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
        "status": "constraint_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "constraint_name": "slippage_constraint",
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
    }
    return df, summary
