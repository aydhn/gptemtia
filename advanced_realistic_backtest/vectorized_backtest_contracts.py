# -*- coding: utf-8 -*-
"""Phase 146: Vectorized Backtest Contracts.

Defines specifications for vectorized matrix backtesting with strict lag enforcement.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

VECTORIZED_CONTRACTS: List[Dict[str, Any]] = [
    {
        "component_name": "vectorized_signal_shift_contract",
        "description": "Sinyal matrisinin getiri matrisi ile caprazlanmadan once en az 1 bar (lag=1) otelenmesi zorunlulugu.",
        "enforcement_rule": "signal.shift(1)",
        "shift_direction": "POSITIVE_LAG_ONLY",
        "forbidden_pattern": "shift(-1)",
        "execution_allowed": False,
    },
    {
        "component_name": "vectorized_cost_deduction_contract",
        "description": "Portfoy donusumunde (turnover) komisyon ve kaymanin cikarilmasi sozlesmesi.",
        "enforcement_rule": "abs(weight - weight.shift(1)) * cost_rate",
        "shift_direction": "POSITIVE_LAG_ONLY",
        "forbidden_pattern": "future_cost_anticipation",
        "execution_allowed": False,
    },
    {
        "component_name": "vectorized_rebalance_matrix_contract",
        "description": "Duzenli araliklarla rebalance edilen agirlik matrisi tanimi.",
        "enforcement_rule": "normalize_weights_sum_to_one",
        "shift_direction": "NONE",
        "forbidden_pattern": "leverage_without_margin",
        "execution_allowed": False,
    },
]


def build_vectorized_backtest_contract_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of vectorized backtest contract specifications."""
    rows = []
    for c in VECTORIZED_CONTRACTS:
        rows.append(
            {
                "component_name": c["component_name"],
                "description": c["description"],
                "enforcement_rule": c["enforcement_rule"],
                "shift_direction": c["shift_direction"],
                "forbidden_pattern": c["forbidden_pattern"],
                "execution_allowed": c["execution_allowed"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_vectorized_backtest_contracts(df)
    return df, summary


def summarize_vectorized_backtest_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize vectorized contracts."""
    return {
        "total_vectorized_contracts": len(df),
        "all_execution_blocked": bool((~df["execution_allowed"]).all()) if not df.empty else True,
        "lag_one_enforced": True,
        "shift_minus_one_strictly_prohibited": True,
        "non_signal": True,
    }
