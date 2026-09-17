# -*- coding: utf-8 -*-
"""Phase 147: Benchmark Baseline Contracts.

Defines passive baseline specifications for strategy comparison.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

BASELINE_SPECS: List[Dict[str, Any]] = [
    {
        "baseline_id": "BASE-01",
        "baseline_name": "cash_zero_risk_baseline",
        "benchmark_type": "CASH",
        "rebalance_freq": "DAILY",
        "transaction_cost": False,
        "description": "Portfoyun nakit tutuldugu risksiz getiri tabani.",
    },
    {
        "baseline_id": "BASE-02",
        "baseline_name": "buy_and_hold_asset_baseline",
        "benchmark_type": "BUY_HOLD",
        "rebalance_freq": "NONE",
        "transaction_cost": True,
        "description": "Ilk bar alinip son bara kadar tasinan varlik baselini.",
    },
    {
        "baseline_id": "BASE-03",
        "baseline_name": "equal_weight_basket_baseline",
        "benchmark_type": "EQUAL_WEIGHT",
        "rebalance_freq": "MONTHLY",
        "transaction_cost": True,
        "description": "Sepetteki varliklarin her ay esit agirliga rebalance edildigi baseline.",
    },
]


def build_benchmark_baseline_contract_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark baseline contract registry."""
    rows = []
    for b in BASELINE_SPECS:
        rows.append(
            {
                "baseline_id": b["baseline_id"],
                "baseline_name": b["baseline_name"],
                "benchmark_type": b["benchmark_type"],
                "rebalance_freq": b["rebalance_freq"],
                "transaction_cost": b["transaction_cost"],
                "description": b["description"],
                "execution_enabled": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_baselines": len(df),
        "all_execution_disabled": True,
        "non_signal": True,
    }
    return df, summary
