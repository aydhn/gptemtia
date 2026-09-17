# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Monte Carlo Dependencies Module.

Links Phase 151 evaluation contracts to Phase 149 Monte Carlo robustness & parameter stability contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

MONTE_CARLO_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_149_BOOTSTRAP_CONTRACTS",
        "phase_source": 149,
        "contract_source": "advanced_monte_carlo_robustness.bootstrap_contracts",
        "status": "SATISFIED",
        "description": "Blok bootstrap ve durağan yeniden örnekleme sözleşmeleri.",
    },
    {
        "dependency_id": "DEP_149_PARAMETER_STABILITY",
        "phase_source": 149,
        "contract_source": "advanced_monte_carlo_robustness.parameter_stability_contracts",
        "status": "SATISFIED",
        "description": "Parametre plato ve pertürbasyon duyarlılığı sözleşmeleri.",
    },
    {
        "dependency_id": "DEP_149_ROBUSTNESS_ENVELOPES",
        "phase_source": 149,
        "contract_source": "advanced_monte_carlo_robustness.robustness_envelopes",
        "status": "SATISFIED",
        "description": "Monte Carlo güven aralıkları ve kuyruk riski dağılım zarfları sözleşmesi.",
    },
]


def build_evaluation_monte_carlo_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of Monte Carlo dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in MONTE_CARLO_DEPENDENCIES:
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
