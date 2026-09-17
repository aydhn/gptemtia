# -*- coding: utf-8 -*-
"""Phase 151: Strategy Limitation Placeholders Module.

Defines placeholders documenting structural, data, and execution limitations of evaluated strategies.
Ensures transparent risk disclosure without strategy approval.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRATEGY_LIMITATIONS: List[Dict[str, Any]] = [
    {
        "limitation_id": "STRAT_LIM_REGIME_DEPENDENCE",
        "title": "Unfavorable Market Regime Fragility Limitation",
        "category": "regime_limitation",
        "description": "Stratejinin optimize edilmediği veya test edilmediği rejimlerdeki kırılganlık bildirimi.",
    },
    {
        "limitation_id": "STRAT_LIM_CAPACITY_CONSTRAINTS",
        "title": "Strategy Capacity and Asset Liquidity Limitation",
        "category": "capacity_limitation",
        "description": "Yüksek sermaye tahsisinde piyasa etkisinin getiriyi eritme riski bildirimi.",
    },
    {
        "limitation_id": "STRAT_LIM_STATIONARITY_ASSUMPTION",
        "title": "Non-Stationarity and Structural Shift Limitation",
        "category": "statistical_limitation",
        "description": "Piyasa dinamiklerinin ve parametre ilişkilerinin zamanla değişebileceğine dair kısıt.",
    },
]


def build_strategy_limitation_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of strategy limitation placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in STRATEGY_LIMITATIONS:
        rows.append(
            {
                "limitation_id": item["limitation_id"],
                "title": item["title"],
                "category": item["category"],
                "description": item["description"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
        "total_limitations": len(df),
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
