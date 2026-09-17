# -*- coding: utf-8 -*-
"""Phase 154: Broker Execution Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_broker_execution_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build broker execution disabled report table."""
    records = [{
        "component_name": "optimization_broker_execution",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "broker_order, send_order, broker_api",
        "status": "execution_blocked_no_broker",
    }]
    df = pd.DataFrame(records)
    summary = {
        "broker_execution_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_broker_execution_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes broker execution."""
    text = str(request).lower()
    prohibited = ["broker_order", "send_order", "broker_api", "fix_protocol"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Broker execution is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
