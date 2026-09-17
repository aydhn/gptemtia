# -*- coding: utf-8 -*-
"""Phase 146: Position Lifecycle Contracts.

Defines state transition specifications for positions (FLAT -> OPENING -> OPEN -> ADJUSTING -> CLOSING -> CLOSED).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

POSITION_STATES: List[Dict[str, Any]] = [
    {"state": "FLAT", "allowed_next_states": ["OPENING"], "description": "Sifir pozisyon, piyasa maruziyeti yok."},
    {"state": "OPENING", "allowed_next_states": ["OPEN", "FLAT"], "description": "Giris emri iletildi, dolum bekleniyor."},
    {"state": "OPEN", "allowed_next_states": ["ADJUSTING", "CLOSING"], "description": "Pozisyon aktif olarak tasiniyor."},
    {"state": "ADJUSTING", "allowed_next_states": ["OPEN"], "description": "Pozisyona ekleme veya kismi cikis yapiliyor."},
    {"state": "CLOSING", "allowed_next_states": ["CLOSED", "OPEN"], "description": "Pozisyon kapatma emri iletildi."},
    {"state": "CLOSED", "allowed_next_states": ["FLAT"], "description": "Pozisyon tamamen kapandi ve PnL gerceklesti."},
]


def build_position_lifecycle_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of position lifecycle contracts."""
    rows = []
    for s in POSITION_STATES:
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
    summary = summarize_position_lifecycle_contracts(df)
    return df, summary


def summarize_position_lifecycle_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize position lifecycle contracts."""
    return {
        "total_position_states": len(df),
        "zero_live_positions_opened": True,
        "non_signal": True,
    }
