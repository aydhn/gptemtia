# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Stress Dependencies Module.

Links Phase 151 evaluation contracts to Phase 148 stress testing & scenario simulation contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRESS_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_148_SCENARIO_CATALOG",
        "phase_source": 148,
        "contract_source": "advanced_stress_testing.stress_scenario_contracts",
        "status": "SATISFIED",
        "description": "Tarihsel ve varsayımsal kriz senaryoları kataloğu sözleşmesi.",
    },
    {
        "dependency_id": "DEP_148_SHOCK_MODELS",
        "phase_source": 148,
        "contract_source": "advanced_stress_testing.volatility_shock_placeholders",
        "status": "SATISFIED",
        "description": "Volatilite patlaması ve likidite donması şok modelleri sözleşmesi.",
    },
    {
        "dependency_id": "DEP_148_CORRELATION_SHOCKS",
        "phase_source": 148,
        "contract_source": "advanced_stress_testing.correlation_breakdown_placeholders",
        "status": "SATISFIED",
        "description": "Çapraz varlık korelasyon çöküşü şok sözleşmeleri.",
    },
]


def build_evaluation_stress_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of stress testing dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in STRESS_DEPENDENCIES:
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
