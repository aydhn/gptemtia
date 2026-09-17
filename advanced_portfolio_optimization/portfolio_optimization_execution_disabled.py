# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Execution Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_portfolio_optimization_execution_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build portfolio optimization execution disabled report table."""
    records = [{
        "component_name": "portfolio_optimization_execution",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "solve, optimize, compute_weights, allocate",
        "status": "execution_blocked_no_portfolio_optimization",
    }]
    df = pd.DataFrame(records)
    summary = {
        "portfolio_optimization_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_portfolio_optimization_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes real portfolio optimization."""
    text = str(request).lower()
    prohibited = ["optimize_portfolio", "run_optimizer", "execute_optimizer", "solve_portfolio"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Portfolio optimization execution is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
