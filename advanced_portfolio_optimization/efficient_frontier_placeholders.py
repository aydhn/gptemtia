# -*- coding: utf-8 -*-
"""Phase 154: Efficient Frontier Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_efficient_frontier_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build efficient frontier placeholder registry."""
    records = [{
        "curve_name": "efficient_frontier_curve",
        "num_frontier_points": 0,
        "is_placeholder": True,
        "frontier_calculated": False,
        "actual_frontier_points": None,
        "status": "frontier_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "curve_name": "efficient_frontier_curve",
        "is_placeholder": True,
        "frontier_calculated": False,
    }
    return df, summary
