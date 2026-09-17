# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Limitation Placeholders Module.

Defines placeholders documenting benchmark baseline constraints and mismatch risks.
Zero performance claims and zero strategy approvals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_LIMITATIONS: List[Dict[str, Any]] = [
    {
        "limitation_id": "BENCH_LIM_LEVERAGE_MISMATCH",
        "title": "Unlevered Benchmark vs Levered Strategy Mismatch",
        "category": "leverage_mismatch",
        "description": "Pasif benchmarkın kaldıraçsız, stratejinin ise marjinli işlem yapması durumundaki sapma uyarısı.",
    },
    {
        "limitation_id": "BENCH_LIM_REBALANCING_FRICTION",
        "title": "Theoretical vs Realizable Benchmark Rebalancing Friction",
        "category": "rebalancing_friction",
        "description": "Sepet benchmarkın maliyetsiz yeniden dengeleme varsayımının yarattığı sapma uyarısı.",
    },
    {
        "limitation_id": "BENCH_LIM_UNIVERSE_SURVIVORSHIP",
        "title": "Static vs Dynamic Benchmark Universe Composition",
        "category": "universe_limitation",
        "description": "Benchmark evreninin tarihsel bileşen değişimlerini ne ölçüde yansıttığına dair sınır.",
    },
]


def build_benchmark_limitation_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of benchmark limitation placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in BENCHMARK_LIMITATIONS:
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
        "domain": LABEL_BENCHMARK_BASELINE_REPORT_DOMAIN,
        "total_limitations": len(df),
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
