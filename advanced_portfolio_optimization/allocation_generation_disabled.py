# -*- coding: utf-8 -*-
"""Phase 154: Allocation Generation Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_allocation_generation_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build allocation generation disabled report table."""
    records = [{
        "component_name": "allocation_generation",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "generate_allocation, allocate_capital",
        "status": "execution_blocked_no_allocation_generation",
    }]
    df = pd.DataFrame(records)
    summary = {
        "allocation_generation_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_allocation_generation_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes real capital allocation."""
    text = str(request).lower()
    prohibited = ["generate_allocation", "allocate_capital", "actual_allocation"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Allocation generation is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
