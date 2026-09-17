# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Dependencies Module.

Consolidates upstream phase dependencies required for benchmark and strategy evaluation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

CORE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_PHASE_146",
        "phase": 146,
        "name": "Realistic Backtest, Transaction Cost and Slippage Modeling",
        "status": "SATISFIED",
        "is_mandatory": True,
    },
    {
        "dependency_id": "DEP_PHASE_147",
        "phase": 147,
        "name": "Walk-Forward Validation and Out-of-Sample Benchmarking",
        "status": "SATISFIED",
        "is_mandatory": True,
    },
    {
        "dependency_id": "DEP_PHASE_148",
        "phase": 148,
        "name": "Stress Testing and Scenario Simulation",
        "status": "SATISFIED",
        "is_mandatory": True,
    },
    {
        "dependency_id": "DEP_PHASE_149",
        "phase": 149,
        "name": "Monte Carlo Robustness and Parameter Stability",
        "status": "SATISFIED",
        "is_mandatory": True,
    },
    {
        "dependency_id": "DEP_PHASE_150",
        "phase": 150,
        "name": "Backtest Governance and Bias Control",
        "status": "SATISFIED",
        "is_mandatory": True,
    },
]


def build_benchmark_evaluation_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of all core upstream dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in CORE_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "phase": d["phase"],
                "name": d["name"],
                "dependency_status": d["status"],
                "is_mandatory": d["is_mandatory"],
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_dependencies": len(df),
        "all_satisfied": bool((df["dependency_status"] == "SATISFIED").all()) if not df.empty else True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
