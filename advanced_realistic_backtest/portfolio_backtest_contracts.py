# -*- coding: utf-8 -*-
"""Phase 146: Portfolio Backtest Contracts.

Defines specifications for portfolio-level capital allocation, asset weights, and exposure limits.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

PORTFOLIO_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "PORT-01",
        "contract_name": "capital_allocation_contract",
        "description": "Portfoy sermayesinin varliklar ve nakit arasinda tahsisi kurali.",
        "max_leverage": 1.0,
        "cash_buffer_min": 0.05,
        "execution_allowed": False,
    },
    {
        "contract_id": "PORT-02",
        "contract_name": "asset_weight_constraint_contract",
        "description": "Tekil varlik basina maksimum pozisyon agirligi siniri (%25 max).",
        "max_single_weight": 0.25,
        "min_single_weight": 0.0,
        "execution_allowed": False,
    },
    {
        "contract_id": "PORT-03",
        "contract_name": "turnover_constraint_contract",
        "description": "Asiri islem ve yuksek maliyet olusumunu onleyen portfoy devir hizi siniri.",
        "max_daily_turnover": 0.50,
        "rebalance_frequency": "DAILY",
        "execution_allowed": False,
    },
]


def build_portfolio_backtest_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of portfolio backtest contracts."""
    rows = []
    for c in PORTFOLIO_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "description": c["description"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_portfolio_backtest_contracts(df)
    return df, summary


def summarize_portfolio_backtest_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize portfolio contracts."""
    return {
        "total_portfolio_contracts": len(df),
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
    }
