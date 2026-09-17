# -*- coding: utf-8 -*-
"""Phase 146: Cash and Position Accounting Contracts.

Defines specifications for cash balances, collateral allocation, and position ledgers.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

CASH_POSITION_RULES: List[Dict[str, Any]] = [
    {
        "ledger_component": "cash_balance_ledger",
        "description": "Nakit bakiye hareketleri, komisyon odemeleri ve gerceklesmis PnL mutabakat defteri.",
        "requires_real_money": False,
    },
    {
        "ledger_component": "margin_collateral_ledger",
        "description": "Acik pozisyonlar icin baglanan baslangic ve surdurme teminati defteri.",
        "requires_real_money": False,
    },
    {
        "ledger_component": "position_inventory_ledger",
        "description": "Varlik bazinda acik lot, ortalama maliyet ve acilis zaman damgasi defteri.",
        "requires_real_money": False,
    },
]


def build_cash_position_accounting_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of cash and position accounting contracts."""
    rows = []
    for r in CASH_POSITION_RULES:
        rows.append(
            {
                "ledger_component": r["ledger_component"],
                "description": r["description"],
                "requires_real_money": r["requires_real_money"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_cash_position_accounting_contracts(df)
    return df, summary


def summarize_cash_position_accounting_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cash and position accounting contracts."""
    return {
        "total_ledger_components": len(df),
        "zero_real_money_involved": bool((~df["requires_real_money"]).all()) if not df.empty else True,
        "non_signal": True,
    }
