# -*- coding: utf-8 -*-
"""Phase 154: Constraint Metric Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_constraint_metric_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build constraint metric placeholders table."""
    records = [{
        "metric_name": "constraint_violation_placeholder",
        "description": "Kisit ihlal miktari yer tutucusu",
        "is_placeholder": True,
        "actual_value": None,
        "is_calculated": False,
        "status": "metric_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "metric_name": "constraint_violation_placeholder",
        "is_placeholder": True,
        "is_calculated": False,
    }
    return df, summary
