# -*- coding: utf-8 -*-
"""Phase 154: Rebalance Generation Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_rebalance_generation_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build rebalance generation disabled report table."""
    records = [{
        "component_name": "rebalance_generation",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "rebalance, generate_rebalance, generate_orders",
        "status": "execution_blocked_no_rebalance_generation",
    }]
    df = pd.DataFrame(records)
    summary = {
        "rebalance_generation_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_rebalance_generation_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes rebalance generation."""
    text = str(request).lower()
    prohibited = ["generate_rebalance", "rebalance_portfolio", "execute_rebalance", "generate_orders"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Rebalance generation is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
