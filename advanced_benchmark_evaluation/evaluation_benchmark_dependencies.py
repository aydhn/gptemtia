# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Benchmark Dependencies Module.

Defines benchmark baseline and universe source dependencies for relative evaluation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_BENCH_PASSIVE_BUY_HOLD",
        "benchmark_type": "buy_and_hold",
        "source": "advanced_benchmark_evaluation.benchmark_baseline_report_contracts",
        "status": "SATISFIED",
        "description": "Pasif Buy & Hold referans stratejisi bağımlılığı.",
    },
    {
        "dependency_id": "DEP_BENCH_CASH_RISK_FREE",
        "benchmark_type": "risk_free_cash",
        "source": "advanced_benchmark_evaluation.benchmark_baseline_report_contracts",
        "status": "SATISFIED",
        "description": "Risksiz nakit getiri referansı bağımlılığı.",
    },
    {
        "dependency_id": "DEP_BENCH_COMMODITY_FX_UNIVERSE",
        "benchmark_type": "multi_asset_universe",
        "source": "advanced_benchmark_evaluation.benchmark_universe_report_contracts",
        "status": "SATISFIED",
        "description": "Emtia ve FX standart gösterge evreni bağımlılığı.",
    },
]


def build_evaluation_benchmark_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of benchmark dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in BENCHMARK_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "benchmark_type": d["benchmark_type"],
                "source": d["source"],
                "dependency_status": d["status"],
                "description": d["description"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_dependencies": len(df),
        "all_satisfied": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
