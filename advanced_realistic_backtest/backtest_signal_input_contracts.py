# -*- coding: utf-8 -*-
"""Phase 146: Backtest Signal Input Contracts.

Defines strategy/signal interface specifications for future backtests.
Does NOT generate real signals, targets, labels, or predictions.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

SIGNAL_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_name": "target_weight_signal_contract",
        "interface_spec": "get_target_weights(timestamp, features) -> Dict[symbol, weight]",
        "description": "Portfoy hedef agirlik arayuzu sozlesmesi (-1.0 ile +1.0 arasi hedef agirliklar).",
        "real_signal_generated": False,
        "prediction_included": False,
        "target_included": False,
    },
    {
        "contract_name": "discrete_order_signal_contract",
        "interface_spec": "generate_sim_orders(timestamp, portfolio_state) -> List[OrderRequest]",
        "description": "Ayrık emir uretim arayuzu sozlesmesi (yalniz simulasyon icin).",
        "real_signal_generated": False,
        "prediction_included": False,
        "target_included": False,
    },
]


def build_backtest_signal_input_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of signal input contracts."""
    rows = []
    for s in SIGNAL_INPUT_CONTRACTS:
        rows.append(
            {
                "contract_name": s["contract_name"],
                "interface_spec": s["interface_spec"],
                "description": s["description"],
                "real_signal_generated": s["real_signal_generated"],
                "prediction_included": s["prediction_included"],
                "target_included": s["target_included"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_signal_input_contracts(df)
    return df, summary


def summarize_backtest_signal_input_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize signal input contracts."""
    return {
        "total_signal_contracts": len(df),
        "zero_real_signals_generated": bool((~df["real_signal_generated"]).all()) if not df.empty else True,
        "zero_predictions_included": bool((~df["prediction_included"]).all()) if not df.empty else True,
        "zero_targets_included": bool((~df["target_included"]).all()) if not df.empty else True,
        "non_signal": True,
    }
