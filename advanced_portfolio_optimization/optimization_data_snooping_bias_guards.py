# -*- coding: utf-8 -*-
"""Phase 154: Data Snooping Bias Guards."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_data_snooping_bias_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build data snooping bias guard registry."""
    records = [{
        "guard_name": "optimization_data_snooping_bias_guard",
        "description": "Portfoy optimizasyonunda veri gozetleme ve gecmise bakarak parametre secimi engeli",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_data_snooping_bias_guard",
        "is_active": True,
    }
    return df, summary
