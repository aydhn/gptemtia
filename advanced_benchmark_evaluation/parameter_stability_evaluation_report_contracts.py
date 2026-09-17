# -*- coding: utf-8 -*-
"""Phase 151: Parameter Stability Evaluation Report Contracts Module.

Defines reporting contracts evaluating parameter sensitivity and plateau smoothness.
Zero parameter optimization, zero curve-fitting sweeps, and zero strategy approvals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_PARAMETER_STABILITY_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

PARAMETER_STABILITY_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "PARAM_EVAL_PLATEAU_SMOOTHNESS",
        "contract_name": "Parameter Plateau Smoothness Evaluation Contract",
        "stability_focus": "plateau_neighborhood",
        "upstream_phase_ref": "phase_149_parameter_stability",
        "metric_placeholder_ref": "parameter_stability_placeholder",
        "description": "Parametre komşuluğunda keskin performans çöküşü yerine yumuşak plato varlığı sözleşmesi.",
    },
    {
        "contract_id": "PARAM_EVAL_PERTURBATION_SENSITIVITY",
        "contract_name": "Parameter Perturbation Sensitivity Contract",
        "stability_focus": "perturbation_tolerance",
        "upstream_phase_ref": "phase_149_parameter_stability",
        "metric_placeholder_ref": "parameter_stability_placeholder",
        "description": "Parametrelere uygulanan %10-%20 tedirginlik altındaki esneklik değerlendirmesi.",
    },
    {
        "contract_id": "PARAM_EVAL_CLIFF_RISK_FRAGILITY",
        "contract_name": "Cliff-Risk and Overfitting Fragility Contract",
        "stability_focus": "cliff_detection",
        "upstream_phase_ref": "phase_150_bias_controls",
        "metric_placeholder_ref": "parameter_stability_placeholder",
        "description": "Uçurum riski (cliff risk) ve dar parametre optimizasyonu aşırı uyumunu inceleyen sözleşme.",
    },
    {
        "contract_id": "PARAM_EVAL_PREREGISTERED_HYPOTHESIS",
        "contract_name": "Pre-Registered Parameter Hypothesis Contract",
        "stability_focus": "pre_registered_priors",
        "upstream_phase_ref": "phase_150_governance_contracts",
        "metric_placeholder_ref": "parameter_stability_placeholder",
        "description": "Parametrelerin geriye dönük veri uydurma değil, önceden tescilli ampirik hipoteze dayanması.",
    },
]


def build_parameter_stability_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of parameter stability evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in PARAMETER_STABILITY_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "stability_focus": c["stability_focus"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "metric_placeholder_ref": c["metric_placeholder_ref"],
                "description": c["description"],
                "optimization_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_PARAMETER_STABILITY_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_optimization_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
