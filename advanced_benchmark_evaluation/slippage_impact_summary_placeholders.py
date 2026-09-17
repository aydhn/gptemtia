# -*- coding: utf-8 -*-
"""Phase 151: Slippage Impact Summary Placeholders Module.

Defines placeholders summarizing execution slippage, latency drag, and market impact.
Zero real calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SLIPPAGE_IMPACT_SUMMARY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

SLIPPAGE_IMPACT_ITEMS: List[Dict[str, Any]] = [
    {
        "impact_id": "SLIPPAGE_IMP_SPREAD_CROSS",
        "title": "Bid-Ask Half-Spread Crossing Cost Placeholder",
        "category": "spread_crossing",
        "description": "Piyasa emirlerinde alış-satış makasını geçmenin yarattığı maliyet özeti.",
    },
    {
        "impact_id": "SLIPPAGE_IMP_MARKET_IMPACT",
        "title": "Order Size Non-Linear Market Impact Drag Placeholder",
        "category": "order_book_impact",
        "description": "Emir büyüklüğünün tahta derinliğini tüketmesinden kaynaklanan fiyat kayması özeti.",
    },
    {
        "impact_id": "SLIPPAGE_IMP_LATENCY_DELAY",
        "title": "Execution Latency and Adverse Selection Drag Placeholder",
        "category": "latency_friction",
        "description": "Ağ ve eşleme gecikmesi kaynaklı aleyhte fiyat hareketi (adverse selection) özeti.",
    },
]


def build_slippage_impact_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of slippage impact summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in SLIPPAGE_IMPACT_ITEMS:
        rows.append(
            {
                "impact_id": item["impact_id"],
                "title": item["title"],
                "category": item["category"],
                "description": item["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_SLIPPAGE_IMPACT_SUMMARY_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
