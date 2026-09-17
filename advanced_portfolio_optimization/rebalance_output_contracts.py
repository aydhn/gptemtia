# -*- coding: utf-8 -*-
"""Phase 154: Rebalance Output Contracts."""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_rebalance_output_contract_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build rebalance output contracts table."""
    records = [{
        "output_contract_name": "rebalance_output_contract",
        "contains_rebalance_orders": False,
        "contains_order_quantities": False,
        "contains_trade_instructions": False,
        "contract_validation_status": "rebalance_contract_ready",
        "manual_review_required": True,
    }]
    df = pd.DataFrame(records)
    summary = {
        "output_contract_name": "rebalance_output_contract",
        "zero_orders_generated": True,
        "contract_ready": True,
    }
    return df, summary
