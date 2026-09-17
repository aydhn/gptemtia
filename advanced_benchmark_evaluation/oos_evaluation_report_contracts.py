# -*- coding: utf-8 -*-
"""Phase 151: Out-of-Sample (OOS) Evaluation Report Contracts Module.

Defines reporting contracts for untouched sealed holdout period evaluation.
Strictly prohibits peeking, multiple passes, and performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_OOS_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

OOS_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "OOS_EVAL_SEALED_HOLDOUT",
        "contract_name": "Sealed Holdout Period Evaluation Contract",
        "isolation_level": "sealed_quarantine",
        "upstream_phase_ref": "phase_147_oos_benchmarking",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Hiç dokunulmamış mühürlü test dönemi değerlendirme raporu sözleşmesi.",
    },
    {
        "contract_id": "OOS_EVAL_SINGLE_PASS_DISCIPLINE",
        "contract_name": "Single-Pass OOS Discipline Contract",
        "isolation_level": "single_pass_only",
        "upstream_phase_ref": "phase_150_oos_governance",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "OOS veri üzerinde tek geçiş kuralını ve tekrar kullanım yasağını denetleyen sözleşme.",
    },
    {
        "contract_id": "OOS_EVAL_DEGRADATION_FACTOR",
        "contract_name": "OOS Performance Haircut and Degradation Contract",
        "isolation_level": "haircut_adjusted",
        "upstream_phase_ref": "phase_150_data_snooping_bias_controls",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Örneklem içi ve örneklem dışı sapmaya uygulanan iskonto sözleşmesi.",
    },
    {
        "contract_id": "OOS_EVAL_CROSS_VALIDATION_DIVERGENCE",
        "contract_name": "CV vs OOS Divergence Evaluation Contract",
        "isolation_level": "cross_validation_comparison",
        "upstream_phase_ref": "phase_147_oos_benchmarking",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Çapraz doğrulama ile OOS arasındaki varyans farkını inceleyen sözleşme.",
    },
]


def build_oos_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of out-of-sample (OOS) evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in OOS_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "isolation_level": c["isolation_level"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "metric_placeholder_ref": c["metric_placeholder_ref"],
                "description": c["description"],
                "execution_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_OOS_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_execution_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
