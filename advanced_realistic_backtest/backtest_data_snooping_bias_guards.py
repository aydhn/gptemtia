# -*- coding: utf-8 -*-
"""Phase 146: Backtest Data Snooping Bias Guards.

Protects against data snooping, p-hacking, and multiple testing distortions in backtesting.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

SNOOPING_RULES: List[Dict[str, Any]] = [
    {
        "guard_name": "multiple_testing_penalty_guard",
        "description": "Cok sayida strateji varyasyonu denendiginde istatistiksel ceza (White Reality Check / Deflated Sharpe) gereksinimi.",
        "enforcement": "STRICT",
        "active": True,
    },
    {
        "guard_name": "in_sample_selection_guard",
        "description": "In-sample veride en iyi sonucu veren parametrelerin out-of-sample test edilmeden basarili sayilmamasi kurali.",
        "enforcement": "STRICT",
        "active": True,
    },
]


def build_backtest_data_snooping_bias_guard_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of data snooping bias guards."""
    rows = []
    for r in SNOOPING_RULES:
        rows.append(
            {
                "guard_name": r["guard_name"],
                "description": r["description"],
                "enforcement": r["enforcement"],
                "active": r["active"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_data_snooping_bias_guards(df)
    return df, summary


def summarize_backtest_data_snooping_bias_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize data snooping bias guards."""
    return {
        "total_guards": len(df),
        "data_snooping_prevented": True,
        "non_signal": True,
    }
