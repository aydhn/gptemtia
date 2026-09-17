# -*- coding: utf-8 -*-
"""Phase 151: Cost Impact Summary Placeholders Module.

Defines placeholders summarizing commission drag, fee erosion, and turnover friction.
Strictly uncalculated and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_COST_IMPACT_SUMMARY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

COST_IMPACT_ITEMS: List[Dict[str, Any]] = [
    {
        "impact_id": "COST_IMP_GROSS_VS_NET",
        "title": "Gross vs Net Return Friction Gap Placeholder",
        "category": "performance_erosion",
        "description": "Brüt getiri ile komisyon düşülmüş net getiri arasındaki fark yer tutucusu.",
    },
    {
        "impact_id": "COST_IMP_TURNOVER_DRAG",
        "title": "Portfolio Turnover vs Cumulative Fee Drag Placeholder",
        "category": "turnover_friction",
        "description": "İşlem hacmi ve portföy devir hızının yarattığı kümülatif maliyet yükü yer tutucusu.",
    },
    {
        "impact_id": "COST_IMP_SWAP_CARRY",
        "title": "Cumulative Overnight Financing / Swap Impact Placeholder",
        "category": "carry_cost",
        "description": "Uzun süreli pozisyon taşımada faiz ve swap giderlerinin getiriye etkisi yer tutucusu.",
    },
]


def build_cost_impact_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of cost impact summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in COST_IMPACT_ITEMS:
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
        "domain": LABEL_COST_IMPACT_SUMMARY_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
