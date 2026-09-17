# -*- coding: utf-8 -*-
"""Phase 154: Investment Advice Guards."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_investment_advice_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build investment advice guard registry."""
    records = [{
        "guard_name": "optimization_investment_advice_guard",
        "description": "Yatirim tavsiyesi, portfoy onayi ve getiri vaadi engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_investment_advice_guard",
        "is_active": True,
    }
    return df, summary


def validate_optimization_investment_advice_request(request: Union[dict, str]) -> Dict:
    """Detect and block investment advice attempts."""
    text = str(request).lower()
    prohibited = ["investment_advice", "portfolio_recommendation", "guaranteed_return", "optimal_portfolio"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Investment advice strictly blocked" if blocked else "OK",
    }
