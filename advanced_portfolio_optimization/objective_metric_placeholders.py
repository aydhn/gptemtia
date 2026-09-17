# -*- coding: utf-8 -*-
"""Phase 154: Objective Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_objective_metric_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build objective metric placeholders table."""
    records = [{
        "metric_name": "objective_function_value_placeholder",
        "description": "Amac fonksiyonu degeri yer tutucusu",
        "is_placeholder": True,
        "actual_value": None,
        "is_calculated": False,
        "status": "metric_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "metric_name": "objective_function_value_placeholder",
        "is_placeholder": True,
        "is_calculated": False,
    }
    return df, summary
