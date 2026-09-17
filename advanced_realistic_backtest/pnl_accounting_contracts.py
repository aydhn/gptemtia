# -*- coding: utf-8 -*-
"""Phase 146: PnL Accounting Contracts.

Defines specifications for realized and unrealized PnL accounting conventions.
Does NOT compute real PnL or balance figures.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

PNL_CONTRACTS: List[Dict[str, Any]] = [
    {
        "accounting_rule": "unrealized_pnl_contract",
        "description": "Acik pozisyonlar icin anlik piyasa degerine (Mark-to-Market) gore gerceklesmemis kar/zarar.",
        "formula_spec": "(current_market_price - avg_entry_price) * position_size",
        "real_pnl_calculated": False,
    },
    {
        "accounting_rule": "realized_pnl_contract",
        "description": "Kapanan pozisyonlar icin maliyetler cikarildiktan sonraki gerceklesmis net kar/zarar.",
        "formula_spec": "(exit_price - entry_price) * closed_size - (entry_costs + exit_costs)",
        "real_pnl_calculated": False,
    },
]


def build_pnl_accounting_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of PnL accounting contracts."""
    rows = []
    for c in PNL_CONTRACTS:
        rows.append(
            {
                "accounting_rule": c["accounting_rule"],
                "description": c["description"],
                "formula_spec": c["formula_spec"],
                "real_pnl_calculated": c["real_pnl_calculated"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_pnl_accounting_contracts(df)
    return df, summary


def summarize_pnl_accounting_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize PnL accounting contracts."""
    return {
        "total_pnl_contracts": len(df),
        "zero_real_pnl_calculated": bool((~df["real_pnl_calculated"]).all()) if not df.empty else True,
        "cost_deduction_mandatory": True,
        "non_signal": True,
    }
