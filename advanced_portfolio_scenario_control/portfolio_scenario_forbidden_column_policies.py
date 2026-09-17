# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Forbidden Column Policies."""

from typing import Any, Dict, List, Tuple
import pandas as pd
from .portfolio_scenario_control_config import (
    PortfolioScenarioControlProfile,
    get_default_portfolio_scenario_control_profile,
)

FORBIDDEN_COLUMNS: List[str] = [
    "target_return", "forward_return", "future_loss", "real_pnl", "real_drawdown",
    "order_id", "broker_order_id", "execution_price", "live_signal", "trade_direction",
    "buy_signal", "sell_signal", "position_size_real", "rebalance_order", "hedge_order",
    "scraped_html", "full_text", "article_body", "raw_content", "api_key", "secret_key"
]

def build_portfolio_scenario_forbidden_column_policy_registry(
    profile: PortfolioScenarioControlProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if profile is None:
        profile = get_default_portfolio_scenario_control_profile()
    rows = [{"forbidden_column": col, "policy": "QUARANTINE_AND_REJECT", "status": "ENFORCED"} for col in FORBIDDEN_COLUMNS]
    df = pd.DataFrame(rows)
    summary = {
        "total_forbidden_columns": len(df),
        "all_enforced": True,
        "policy": "STRICT_FORBIDDEN_COLUMN_ENFORCEMENT"
    }
    return df, summary
