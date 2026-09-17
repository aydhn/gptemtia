# -*- coding: utf-8 -*-
"""Phase 151: Monte Carlo Robustness Evaluation Report Contracts Module.

Defines reporting contracts evaluating robustness against resampled paths and permutations.
Ensures zero bootstrap simulation execution and zero performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

MONTE_CARLO_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "MC_EVAL_BLOCK_BOOTSTRAP_ENVELOPE",
        "contract_name": "Block Bootstrap Envelope Evaluation Contract",
        "resampling_mode": "block_bootstrap",
        "upstream_phase_ref": "phase_149_monte_carlo",
        "metric_placeholder_ref": "monte_carlo_robustness_placeholder",
        "description": "Zaman serisi otokorelasyonunu koruyan blok bootstrap güven aralıkları sözleşmesi.",
    },
    {
        "contract_id": "MC_EVAL_TRADE_ORDER_PERMUTATION",
        "contract_name": "Trade Order Permutation Drawdown Contract",
        "resampling_mode": "trade_permutation",
        "upstream_phase_ref": "phase_149_monte_carlo",
        "metric_placeholder_ref": "monte_carlo_robustness_placeholder",
        "description": "İşlem sırası şansını ortadan kaldıran permütasyon azami drawdown sözleşmesi.",
    },
    {
        "contract_id": "MC_EVAL_RESIDUAL_RESAMPLING",
        "contract_name": "Residual Resampling Path Variance Contract",
        "resampling_mode": "residual_resampling",
        "upstream_phase_ref": "phase_149_monte_carlo",
        "metric_placeholder_ref": "monte_carlo_robustness_placeholder",
        "description": "Model artıkları yeniden örnekleme ve getiri yolu varyansı değerlendirmesi.",
    },
    {
        "contract_id": "MC_EVAL_TAIL_RISK_DISTRIBUTION",
        "contract_name": "Tail Risk Distribution and Extreme Quantile Contract",
        "resampling_mode": "quantile_envelope",
        "upstream_phase_ref": "phase_149_monte_carlo",
        "metric_placeholder_ref": "monte_carlo_robustness_placeholder",
        "description": "Monte Carlo dağılımının %95 ve %99 kuyruk riski (VaR/ES) zarfları sözleşmesi.",
    },
]


def build_monte_carlo_robustness_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of Monte Carlo robustness evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in MONTE_CARLO_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "resampling_mode": c["resampling_mode"],
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
        "domain": LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_execution_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
