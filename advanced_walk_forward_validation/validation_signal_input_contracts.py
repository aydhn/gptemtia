# -*- coding: utf-8 -*-
"""Phase 147: Validation Signal Input Contracts.

Specifications linking theoretical strategy signals to validation pipelines.
Strictly disallows converting signals into live execution or trade recommendations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

SIGNAL_CONTRACTS: List[Dict[str, Any]] = [
    {
        "signal_contract_id": "SIG-147-01",
        "signal_source": "Phase 146 Realistic Backtest Signals",
        "live_order_allowed": False,
        "investment_advice_allowed": False,
        "description": "Dogrulama amacli teorik sinyal girdi arayuzu.",
    },
    {
        "signal_contract_id": "SIG-147-02",
        "signal_source": "Passive Benchmark Signal Stream",
        "live_order_allowed": False,
        "investment_advice_allowed": False,
        "description": "Karsilastirma amacli pasif referans sinyal akisi.",
    },
]


def build_validation_signal_input_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for validation signal input contracts."""
    rows = []
    for s in SIGNAL_CONTRACTS:
        rows.append(
            {
                "signal_contract_id": s["signal_contract_id"],
                "signal_source": s["signal_source"],
                "live_order_allowed": s["live_order_allowed"],
                "investment_advice_allowed": s["investment_advice_allowed"],
                "description": s["description"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_signal_contracts": len(df),
        "zero_live_orders": True,
        "zero_investment_advice": True,
        "non_signal": True,
    }
    return df, summary
