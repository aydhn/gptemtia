# -*- coding: utf-8 -*-
"""Phase 146: Event-Driven Backtest Contracts.

Defines specifications for discrete-event backtesting loops (tick, bar, signal, order, fill events).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

EVENT_DRIVEN_CONTRACTS: List[Dict[str, Any]] = [
    {
        "event_type": "MARKET_DATA_EVENT",
        "description": "Zaman damgali yeni fiyat veya bar verisi olusumu.",
        "handler_interface": "on_market_data(event: MarketDataEvent)",
        "lookahead_check": "timestamp <= current_sim_time",
        "execution_allowed": False,
    },
    {
        "event_type": "SIGNAL_INPUT_EVENT",
        "description": "Stratejiden gelen sinyal istegi bildirim olayi.",
        "handler_interface": "on_signal(event: SignalEvent)",
        "lookahead_check": "signal_time <= current_sim_time",
        "execution_allowed": False,
    },
    {
        "event_type": "ORDER_CREATION_EVENT",
        "description": "Simulasyon ici emir olusturma olayi.",
        "handler_interface": "on_order_create(event: OrderEvent)",
        "lookahead_check": "order_time >= current_sim_time",
        "execution_allowed": False,
    },
    {
        "event_type": "ORDER_FILL_EVENT",
        "description": "Fiyat ve kayma kurallarina gore emir eslesme olayi.",
        "handler_interface": "on_fill(event: FillEvent)",
        "lookahead_check": "fill_time > order_time",
        "execution_allowed": False,
    },
    {
        "event_type": "POSITION_UPDATE_EVENT",
        "description": "Pozisyon ve bakiye guncelleme olayi.",
        "handler_interface": "on_position_update(event: PositionEvent)",
        "lookahead_check": "update_time >= fill_time",
        "execution_allowed": False,
    },
]


def build_event_driven_backtest_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of event-driven backtest contract specifications."""
    rows = []
    for c in EVENT_DRIVEN_CONTRACTS:
        rows.append(
            {
                "event_type": c["event_type"],
                "description": c["description"],
                "handler_interface": c["handler_interface"],
                "lookahead_check": c["lookahead_check"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_event_driven_backtest_contracts(df)
    return df, summary


def summarize_event_driven_backtest_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize event-driven contracts."""
    return {
        "total_event_contracts": len(df),
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "event_types": df["event_type"].tolist() if not df.empty else [],
        "non_signal": True,
    }
