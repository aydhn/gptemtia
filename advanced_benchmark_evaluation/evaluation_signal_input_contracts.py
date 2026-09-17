# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Signal Input Contracts Module.

Defines rules for strategy signal inputs during offline evaluation.
Explicitly clarifies that signal inputs are research models, NOT live orders.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_DEPENDENCY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

SIGNAL_INPUT_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "SIG_INP_RESEARCH_MODEL_HYPOTHESIS",
        "signal_type": "empirical_alpha_hypothesis",
        "boundary_rule": "Signals represent unproven hypotheses for research only; no trade recommendation",
        "description": "Araştırma sinyali ampirik hipotez giriş sözleşmesi.",
    },
    {
        "contract_id": "SIG_INP_NON_EXECUTION_LOCK",
        "signal_type": "offline_target_positions",
        "boundary_rule": "Zero order dispatch, zero broker connectivity; execution locked",
        "description": "Sinyallerin canlı emre dönüştürülmesini engelleyen kilit sözleşmesi.",
    },
    {
        "contract_id": "SIG_INP_POSITION_SIZING_DISQUALIFICATION",
        "signal_type": "weight_allocation",
        "boundary_rule": "Zero capital allocation or portfolio construction authority",
        "description": "Sinyallerin sermaye tahsisi veya portföy ağırlığı olarak kullanılmasını engelleyen sözleşme.",
    },
]


def build_evaluation_signal_input_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of evaluation signal input contracts."""
    rows: List[Dict[str, Any]] = []

    for c in SIGNAL_INPUT_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "signal_type": c["signal_type"],
                "boundary_rule": c["boundary_rule"],
                "description": c["description"],
                "live_dispatch_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_DEPENDENCY_DOMAIN,
        "total_contracts": len(df),
        "all_dispatch_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
