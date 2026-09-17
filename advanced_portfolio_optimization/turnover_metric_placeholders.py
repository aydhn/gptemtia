# -*- coding: utf-8 -*-
"""Phase 154: Turnover Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_turnover_metric_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build turnover and cost impact metric placeholders table."""
    records = [
        {
            "metric_name": "turnover_placeholder",
            "description": "Portfoy devir hizi yuzdesi yer tutucusu",
            "is_placeholder": True,
            "actual_value": None,
            "is_calculated": False,
        },
        {
            "metric_name": "transaction_cost_impact_placeholder",
            "description": "Islem maliyeti etki yuzdesi yer tutucusu",
            "is_placeholder": True,
            "actual_value": None,
            "is_calculated": False,
        },
        {
            "metric_name": "slippage_impact_placeholder",
            "description": "Kayma etki yuzdesi yer tutucusu",
            "is_placeholder": True,
            "actual_value": None,
            "is_calculated": False,
        },
    ]
    df = pd.DataFrame(records)
    summary = {
        "metric_count": len(records),
        "all_metrics_placeholders": True,
        "zero_metrics_calculated": True,
    }
    return df, summary
