# -*- coding: utf-8 -*-
"""Phase 154: Live Trading Disabled Report & Policy."""

from typing import Dict, Tuple, Union
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile


def build_optimization_live_trading_disabled_report(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build live trading disabled report table."""
    records = [{
        "component_name": "optimization_live_trading",
        "is_disabled": True,
        "enforcement_mechanism": "runtime_policy_lock",
        "prohibited_actions": "live_trade, execute_order, connect_exchange",
        "status": "execution_blocked_no_live_trading",
    }]
    df = pd.DataFrame(records)
    summary = {
        "live_trading_disabled": True,
        "runtime_policy_lock_active": True,
    }
    return df, summary


def validate_no_optimization_live_trading_request(request: Union[dict, str]) -> Dict:
    """Ensure no request invokes live trading."""
    text = str(request).lower()
    prohibited = ["live_trade", "execute_order", "real_order", "connect_exchange"]
    blocked = any(p in text for p in prohibited)
    return {
        "blocked": blocked,
        "prohibited_detected": [p for p in prohibited if p in text],
        "message": "Live trading is strictly blocked by Phase 154 policy" if blocked else "OK",
    }
