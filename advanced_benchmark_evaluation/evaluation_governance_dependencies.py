# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Governance Dependencies Module.

Links Phase 151 evaluation contracts to Phase 150 backtest governance & bias control contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

GOVERNANCE_DEPENDENCIES: List[Dict[str, Any]] = [
    {
        "dependency_id": "DEP_150_BIAS_CONTROLS",
        "phase_source": 150,
        "contract_source": "advanced_backtest_governance.backtest_bias_control_contracts",
        "status": "SATISFIED",
        "description": "Lookahead, survivorship, data snooping ve multiple testing yanlılık kontrolleri.",
    },
    {
        "dependency_id": "DEP_150_CLAIM_BOUNDARIES",
        "phase_source": 150,
        "contract_source": "advanced_backtest_governance.backtest_performance_claim_boundaries",
        "status": "SATISFIED",
        "description": "Performans ve sonuç iddialarını engelleyen kesin sınırlar.",
    },
    {
        "dependency_id": "DEP_150_MANUAL_REVIEW_GATES",
        "phase_source": 150,
        "contract_source": "advanced_backtest_governance.backtest_manual_review_gates",
        "status": "SATISFIED",
        "description": "Zorunlu insan denetimi (human-in-the-loop) inceleme kapıları sözleşmesi.",
    },
]


def build_evaluation_governance_dependency_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of governance dependencies."""
    rows: List[Dict[str, Any]] = []

    for d in GOVERNANCE_DEPENDENCIES:
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
