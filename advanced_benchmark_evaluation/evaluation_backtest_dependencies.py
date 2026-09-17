# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Backtest Dependencies Module.

Links Phase 151 evaluation contracts to Phase 146 realistic backtest contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BACKTEST_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_146_ENGINE_CONTRACTS",
        "phase_source": 146,
        "contract_source": "advanced_realistic_backtest.backtest_engine_contracts",
        "status": "SATISFIED",
        "description": "Gerçekçi backtest motoru sözleşmeleri (event-driven, portfolio, multi-asset).",
    },
    {
        "dependency_id": "DEP_146_COST_MODELS",
        "phase_source": 146,
        "contract_source": "advanced_realistic_backtest.commission_models",
        "status": "SATISFIED",
        "description": "Kademeli komisyon ve borsa ücreti modelleri sözleşmesi.",
    },
    {
        "dependency_id": "DEP_146_SLIPPAGE_MODELS",
        "phase_source": 146,
        "contract_source": "advanced_realistic_backtest.slippage_models",
        "status": "SATISFIED",
        "description": "Doğrusal olmayan piyasa etkisi ve makas tabanlı kayma modelleri sözleşmesi.",
    },
]


def build_evaluation_backtest_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of backtest dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in BACKTEST_DEPENDENCIES:
        rows.append(
            {
                "dependency_id": d["dependency_id"],
                "phase_source": d["phase_source"],
                "contract_source": d["contract_source"],
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
