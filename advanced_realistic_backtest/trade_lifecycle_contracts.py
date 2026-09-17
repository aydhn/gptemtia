# -*- coding: utf-8 -*-
"""Phase 146: Trade Lifecycle Contracts.

Defines state transition specifications for trades (CREATED -> SUBMITTED -> FILLED -> CLOSED).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

TRADE_STATES: List[Dict[str, Any]] = [
    {"state": "CREATED", "allowed_next_states": ["SUBMITTED", "REJECTED"], "description": "Emir sinyal uzerine olusturuldu."},
    {"state": "SUBMITTED", "allowed_next_states": ["ACKNOWLEDGED", "REJECTED", "CANCELLED"], "description": "Emir simulasyon motoruna iletildi."},
    {"state": "ACKNOWLEDGED", "allowed_next_states": ["PARTIALLY_FILLED", "FILLED", "CANCELLED"], "description": "Emir deftere yazildi."},
    {"state": "PARTIALLY_FILLED", "allowed_next_states": ["PARTIALLY_FILLED", "FILLED", "CANCELLED"], "description": "Emir kismi olarak gerceklesti."},
    {"state": "FILLED", "allowed_next_states": ["CLOSED"], "description": "Emir tamamen gerceklesti."},
    {"state": "CANCELLED", "allowed_next_states": [], "description": "Emir iptal edildi."},
    {"state": "REJECTED", "allowed_next_states": [], "description": "Emir kurallar geregi reddedildi."},
    {"state": "CLOSED", "allowed_next_states": [], "description": "Pozisyon baglantisi kapandi."},
]


def build_trade_lifecycle_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of trade lifecycle contracts."""
    rows = []
    for s in TRADE_STATES:
        rows.append(
            {
                "state": s["state"],
                "allowed_next_states": str(s["allowed_next_states"]),
                "description": s["description"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_trade_lifecycle_contracts(df)
    return df, summary


def summarize_trade_lifecycle_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize trade lifecycle contracts."""
    return {
        "total_trade_states": len(df),
        "terminal_states": ["CANCELLED", "REJECTED", "CLOSED"],
        "non_signal": True,
    }
