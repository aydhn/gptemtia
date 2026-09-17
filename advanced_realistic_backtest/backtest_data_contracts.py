# -*- coding: utf-8 -*-
"""Phase 146: Backtest Data Contracts.

Defines point-in-time and schema contracts for historical market data ingestion.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

DATA_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "ohlcv_bar_data_contract",
        "description": "Zaman damgali OHLCV bar verisi (Open, High, Low, Close, Volume).",
        "required_columns": ["timestamp", "open", "high", "low", "close", "volume"],
        "point_in_time_enforced": True,
        "monotonic_timestamp": True,
    },
    {
        "contract_name": "bid_ask_quote_data_contract",
        "description": "Zaman damgali teklif ve talep verisi (Bid, Ask, BidSize, AskSize).",
        "required_columns": ["timestamp", "bid", "ask", "bid_size", "ask_size"],
        "point_in_time_enforced": True,
        "monotonic_timestamp": True,
    },
]


def build_backtest_data_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of backtest data contracts."""
    rows = []
    for d in DATA_CONTRACTS:
        rows.append(
            {
                "contract_name": d["contract_name"],
                "description": d["description"],
                "required_columns": str(d["required_columns"]),
                "point_in_time_enforced": d["point_in_time_enforced"],
                "monotonic_timestamp": d["monotonic_timestamp"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_data_contracts(df)
    return df, summary


def summarize_backtest_data_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest data contracts."""
    return {
        "total_data_contracts": len(df),
        "point_in_time_enforced": bool(df["point_in_time_enforced"].all()) if not df.empty else True,
        "monotonic_timestamp_enforced": bool(df["monotonic_timestamp"].all()) if not df.empty else True,
        "non_signal": True,
    }
