# -*- coding: utf-8 -*-
"""Phase 154: Metric Calculation Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_metric_calculation_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build metric calculation disabled report table."""
    records = [{
        "component_name": "optimization_metric_calculation",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "calculate_sharpe, calculate_cvar, calculate_drawdown",
        "status": "execution_blocked_no_metric_calculation",
    }]
    df = pd.DataFrame(records)
    summary = {
        "metric_calculation_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_metric_calculation_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes numerical metric calculation."""
    text = str(request).lower()
    prohibited = ["calculate_sharpe", "calculate_cvar", "calculate_objective", "calculate_exposure", "calculate_frontier"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Metric calculation is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
