# -*- coding: utf-8 -*-
"""Phase 146: Realistic Execution Assumptions.

Defines foundational realism assumptions that eliminate naive backtesting biases
(no instant zero-slippage fills, mandatory spread, latency awareness).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile

REALISTIC_ASSUMPTIONS: List[Dict[str, Any]] = [
    {
        "assumption_name": "no_instant_fill_assumption",
        "category": "TIMING",
        "description": "Emirler sinyal uretildigi anda aninda sifir gecikmeyle dolmaz; en erken sonraki bar/tick fiyati kullanilir.",
        "enforced": True,
    },
    {
        "assumption_name": "spread_cost_required_assumption",
        "category": "COST",
        "description": "Alis-satis makasi asla sifir kabul edilemez; islem fiyati daima ask veya bid uzerinden veya yarim spread eklenerek hesaplanir.",
        "enforced": True,
    },
    {
        "assumption_name": "slippage_required_assumption",
        "category": "FRICTION",
        "description": "Her islemde piyasa oynakligina veya islem hacmine gore kayma (slippage) payi kesilmelidir.",
        "enforced": True,
    },
    {
        "assumption_name": "latency_placeholder_required_assumption",
        "category": "LATENCY",
        "description": "Emir iletiminde fiziksel ag ve borsa sirasi gecikmesi (latency) hesaba katilmalidir.",
        "enforced": True,
    },
    {
        "assumption_name": "partial_fill_possible_assumption",
        "category": "LIQUIDITY",
        "description": "Piyasa derinligi yetersiz oldugunda tek barda tam dolum gerceklesmeyebilir, kismi dolum mumkundur.",
        "enforced": True,
    },
    {
        "assumption_name": "rejected_order_possible_assumption",
        "category": "RISK",
        "description": "Teminat yetersizligi veya tavan/taban limitlerinde emirlerin reddedilmesi gercekci bir olasiliktir.",
        "enforced": True,
    },
    {
        "assumption_name": "liquidity_constraint_possible_assumption",
        "category": "LIQUIDITY",
        "description": "Islem buyuklugu bar veya gunluk hacmin kucuk bir yuzdesi ile sinirlandirilmalidir (%10 max ADV).",
        "enforced": True,
    },
    {
        "assumption_name": "no_live_execution_assumption",
        "category": "SAFETY",
        "description": "Simulasyon ortami canli piyasa ve broker baglantilarindan tamamen yalitilmistir.",
        "enforced": True,
    },
]


def build_realistic_execution_assumption_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of realistic execution assumptions."""
    rows = []
    for a in REALISTIC_ASSUMPTIONS:
        rows.append(
            {
                "assumption_name": a["assumption_name"],
                "category": a["category"],
                "description": a["description"],
                "enforced": a["enforced"],
                "is_active": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_realistic_execution_assumptions(df)
    return df, summary


def summarize_realistic_execution_assumptions(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize realistic execution assumptions."""
    return {
        "total_assumptions": len(df),
        "all_enforced": bool(df["enforced"].all()) if not df.empty else True,
        "naive_backtest_prevented": True,
        "non_signal": True,
    }
