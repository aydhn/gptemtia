# -*- coding: utf-8 -*-
"""Phase 154: Max-Weight Constraint Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_max_weight_constraint_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build max-weight constraint placeholder registry."""
    records = [{
        "constraint_name": "max_weight_constraint",
        "default_max_weight": 0.20,
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
        "status": "constraint_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "constraint_name": "max_weight_constraint",
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
    }
    return df, summary
