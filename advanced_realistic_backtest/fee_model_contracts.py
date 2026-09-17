# -*- coding: utf-8 -*-
"""Phase 146: Fee Model Contracts.

Defines specifications for exchange, regulatory, and clearing fees.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

FEE_MODELS: List[Dict[str, Any]] = [
    {
        "fee_model_name": "exchange_clearing_fee",
        "category": "EXCHANGE",
        "description": "Borsa takas ve tescil ucreti sozlesmesi (orn: CME/ICE per-trade fee).",
        "formula": "contracts * exchange_fee_per_contract",
        "default_rate": 0.50,
        "currency": "USD",
        "execution_allowed": False,
    },
    {
        "fee_model_name": "regulatory_transaction_fee",
        "category": "REGULATORY",
        "description": "Regulasyon (NFA/SEC vb.) islem ucreti sozlesmesi.",
        "formula": "notional_value * regulatory_rate",
        "default_rate": 0.000022,
        "currency": "USD",
        "execution_allowed": False,
    },
]


def build_fee_model_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of fee model contracts."""
    rows = []
    for f in FEE_MODELS:
        rows.append(
            {
                "fee_model_name": f["fee_model_name"],
                "category": f["category"],
                "description": f["description"],
                "formula": f["formula"],
                "default_rate": f["default_rate"],
                "currency": f["currency"],
                "execution_allowed": f["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_fee_model_contracts(df)
    return df, summary


def summarize_fee_model_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize fee model contracts."""
    return {
        "total_fee_models": len(df),
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "non_signal": True,
    }
