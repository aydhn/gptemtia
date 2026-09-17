# -*- coding: utf-8 -*-
"""Phase 154: Overfitting Guards."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_overfitting_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build overfitting guard registry."""
    records = [{
        "guard_name": "optimization_overfitting_guard",
        "description": "Portfoy optimizasyonunda asiri uyum ve serbest parametre patlamasi engeli",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_overfitting_guard",
        "is_active": True,
    }
    return df, summary
