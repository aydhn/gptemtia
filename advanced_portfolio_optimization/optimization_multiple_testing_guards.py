# -*- coding: utf-8 -*-
"""Phase 154: Multiple Testing Guards."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_multiple_testing_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build multiple testing guard registry."""
    records = [{
        "guard_name": "optimization_multiple_testing_guard",
        "description": "Coklu test yanliligi, rastlantisal alfa ve backtest overfitting engeli",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_multiple_testing_guard",
        "is_active": True,
    }
    return df, summary
