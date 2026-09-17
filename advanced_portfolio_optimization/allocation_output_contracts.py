# -*- coding: utf-8 -*-
"""Phase 154: Allocation Output Contracts."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_allocation_output_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build allocation output contracts table."""
    records = [{
        "output_contract_name": "allocation_output_contract",
        "contains_capital_allocation": False,
        "contains_currency_allocation": False,
        "contains_position_sizes": False,
        "contract_validation_status": "allocation_constraint_ready",
        "manual_review_required": True,
    }]
    df = pd.DataFrame(records)
    summary = {
        "output_contract_name": "allocation_output_contract",
        "zero_capital_allocation": True,
        "contract_ready": True,
    }
    return df, summary
