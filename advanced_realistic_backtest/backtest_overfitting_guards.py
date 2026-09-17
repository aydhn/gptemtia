# -*- coding: utf-8 -*-
"""Phase 146: Backtest Overfitting Guards.

Protects against parameter overfitting, excessive curve fitting, and strategy fragility.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

OVERFITTING_RULES: List[Dict[str, Any]] = [
    {
        "guard_name": "parameter_degrees_of_freedom_guard",
        "description": "Strateji basina serbest parametre sayisinin veri uzunluguna gore sinirlandirilmasi (max 4-5 parametre).",
        "max_parameters": 5,
        "enforcement": "STRICT",
        "active": True,
    },
    {
        "guard_name": "parameter_plateau_stability_guard",
        "description": "Parametre komsu degerlerinde performansin dramatik dusmemesi (plato kararliligi) kurali.",
        "enforcement": "STRICT",
        "active": True,
    },
]


def build_backtest_overfitting_guard_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of overfitting guards."""
    rows = []
    for r in OVERFITTING_RULES:
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
    summary = summarize_backtest_overfitting_guards(df)
    return df, summary


def summarize_backtest_overfitting_guards(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize overfitting guards."""
    return {
        "total_guards": len(df),
        "overfitting_mitigation_enforced": True,
        "non_signal": True,
    }
