# -*- coding: utf-8 -*-
"""Phase 154: Currency Exposure Constraint Placeholders."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_currency_exposure_constraint_placeholder_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build currency exposure constraint placeholder registry."""
    records = [{
        "constraint_name": "currency_exposure_constraint",
        "single_currency_ceiling": 0.30,
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
        "status": "constraint_contract_only",
    }]
    df = pd.DataFrame(records)
    summary = {
        "constraint_name": "currency_exposure_constraint",
        "is_placeholder": True,
        "is_enforced_live": False,
        "actual_weights_generated": False,
    }
    return df, summary
