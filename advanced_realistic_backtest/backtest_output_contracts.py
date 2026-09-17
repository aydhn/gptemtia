# -*- coding: utf-8 -*-
"""Phase 146: Backtest Output Contracts.

Defines safe, non-signal output contracts for backtesting runs.
Explicitly excludes realized PnL, performance claims, Sharpe ratios, and trading signals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

ALLOWED_OUTPUT_FIELDS: List[Dict[str, Any]] = [
    {
        "field_name": "contract_validation_status",
        "data_type": "STRING",
        "description": "Backtest sozlesmelerinin gecerlilik durumu (PASS, REVIEW_REQUIRED, BLOCKED).",
        "is_safe": True,
    },
    {
        "field_name": "blocked_reason",
        "data_type": "STRING",
        "description": "Guvenlik veya politika geregi engellenme gerekcesi.",
        "is_safe": True,
    },
    {
        "field_name": "manual_review_required",
        "data_type": "BOOLEAN",
        "description": "Insan operator incelemesinin zorunlu olup olmadigi.",
        "is_safe": True,
    },
    {
        "field_name": "cost_model_contract_ready",
        "data_type": "BOOLEAN",
        "description": "Islem maliyeti model sozlesmesinin hazirlik durumu.",
        "is_safe": True,
    },
    {
        "field_name": "slippage_model_contract_ready",
        "data_type": "BOOLEAN",
        "description": "Fiyat kaymasi (slippage) model sozlesmesinin hazirlik durumu.",
        "is_safe": True,
    },
]


def build_backtest_output_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of permitted backtest output contracts."""
    rows = []
    for f in ALLOWED_OUTPUT_FIELDS:
        rows.append(
            {
                "field_name": f["field_name"],
                "data_type": f["data_type"],
                "description": f["description"],
                "is_safe": f["is_safe"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_output_contracts(df)
    return df, summary


def summarize_backtest_output_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest output contracts."""
    return {
        "total_output_fields": len(df),
        "all_fields_safe": bool(df["is_safe"].all()) if not df.empty else True,
        "pnl_output_prohibited": True,
        "performance_claim_prohibited": True,
        "trading_signal_prohibited": True,
        "non_signal": True,
    }
