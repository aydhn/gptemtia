# -*- coding: utf-8 -*-
"""Phase 150: Benchmark Governance.

Governs benchmark baseline contracts and pre-commitment requirements under zero execution.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    BENCHMARK_GOVERNANCE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

BENCHMARK_GOVERNANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "governance_id": "BMK_GOV_01_PASSIVE_BUY_HOLD",
        "name": "passive_buy_and_hold_contract",
        "description": "Unleveraged buy-and-hold baseline of the underlying commodity/FX asset.",
        "requirement": "Pre-committed baseline that cannot be swapped ex-post.",
    },
    {
        "governance_id": "BMK_GOV_02_CASH_RISK_FREE",
        "name": "cash_and_risk_free_rate_contract",
        "description": "Cash baseline reflecting risk-free interest rate (SOFR/Fed Funds) carry.",
        "requirement": "Standard hurdle for excess return assessment.",
    },
    {
        "governance_id": "BMK_GOV_03_EQUAL_WEIGHT_UNIVERSE",
        "name": "equal_weighted_commodity_basket_contract",
        "description": "Equal-weighted basket baseline across evaluated asset universe.",
        "requirement": "Ensures cross-asset diversification context.",
    },
]


def build_benchmark_governance_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for benchmark governance."""
    rows: List[Dict[str, Any]] = []
    for item in BENCHMARK_GOVERNANCE_ITEMS:
        rows.append({
            "governance_id": item["governance_id"],
            "name": item["name"],
            "description": item["description"],
            "requirement": item["requirement"],
            "execution_allowed": False,
            "status": "GOVERNANCE_CONTRACT_READY",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": BENCHMARK_GOVERNANCE_DOMAIN,
        "total_benchmarks": len(df),
        "execution_disabled": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
