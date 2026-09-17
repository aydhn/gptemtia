# -*- coding: utf-8 -*-
"""Phase 154: Rebalance Claim Guards."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_rebalance_claim_guard_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build rebalance claim guard registry."""
    records = [{
        "guard_name": "optimization_rebalance_claim_guard",
        "description": "Rebalance emri ve islem talimati iddialarini engelleme",
        "is_active": True,
        "action_on_violation": "BLOCK",
    }]
    df = pd.DataFrame(records)
    summary = {
        "guard_name": "optimization_rebalance_claim_guard",
        "is_active": True,
    }
    return df, summary


def validate_rebalance_claim_request(request: Union[dict, str]) -> Dict:
    """Detect and block prohibited rebalance requests."""
    text = str(request).lower()
    prohibited = ["rebalance_order", "generate_rebalance", "rebalance_portfolio", "execute_rebalance"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Rebalance claims strictly blocked" if blocked else "OK",
    }
