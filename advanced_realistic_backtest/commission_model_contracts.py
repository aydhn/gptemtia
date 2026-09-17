# -*- coding: utf-8 -*-
"""Phase 146: Commission Model Contracts.

Defines specifications for broker commission structures (per-lot, percentage basis points, tiered).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

COMMISSION_MODELS: List[Dict[str, Any]] = [
    {
        "commission_model_name": "fixed_per_lot_commission",
        "category": "PER_LOT",
        "description": "Her kontrat veya lot basina sabit komisyon tutari (orn: $2.00 / lot).",
        "formula": "lots * fixed_cost_per_lot",
        "default_value": 2.0,
        "currency": "USD",
        "execution_allowed": False,
    },
    {
        "commission_model_name": "percentage_bps_commission",
        "category": "PERCENTAGE_BPS",
        "description": "Islem nosyonel degeri uzerinden baz puan (bps) oraninda komisyon (orn: 2 bps).",
        "formula": "notional_value * (bps / 10000.0)",
        "default_value": 2.0,
        "currency": "USD",
        "execution_allowed": False,
    },
    {
        "commission_model_name": "tiered_volume_commission",
        "category": "TIERED",
        "description": "Aylik islem hacmine gore kademeli azalan komisyon baremi sozlesmesi.",
        "formula": "piecewise_volume_tier(monthly_volume)",
        "default_value": 1.5,
        "currency": "USD",
        "execution_allowed": False,
    },
    {
        "commission_model_name": "minimum_ticket_commission",
        "category": "MINIMUM_FEE",
        "description": "Islem basina asgari komisyon bariyeri (orn: min $1.00 per trade).",
        "formula": "max(calculated_commission, min_ticket_fee)",
        "default_value": 1.0,
        "currency": "USD",
        "execution_allowed": False,
    },
]


def build_commission_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of commission model contracts."""
    rows = []
    for c in COMMISSION_MODELS:
        rows.append(
            {
                "commission_model_name": c["commission_model_name"],
                "category": c["category"],
                "description": c["description"],
                "formula": c["formula"],
                "default_value": c["default_value"],
                "currency": c["currency"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_commission_model_contracts(df)
    return df, summary


def summarize_commission_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize commission model contracts."""
    return {
        "total_commission_models": len(df),
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
    }
