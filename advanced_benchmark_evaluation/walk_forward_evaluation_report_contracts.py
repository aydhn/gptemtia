# -*- coding: utf-8 -*-
"""Phase 151: Walk-Forward Evaluation Report Contracts Module.

Defines reporting contracts for dynamic walk-forward window stability.
Ensures zero simulation execution and zero performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_WALK_FORWARD_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

WALK_FORWARD_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "WF_EVAL_ROLLING_WINDOW",
        "contract_name": "Rolling Window Walk-Forward Evaluation Contract",
        "window_mode": "rolling",
        "upstream_phase_ref": "phase_147_walk_forward",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Kayan pencereler üzerinden adım bazlı OOS stabilite raporu sözleşmesi.",
    },
    {
        "contract_id": "WF_EVAL_EXPANDING_WINDOW",
        "contract_name": "Expanding Window Walk-Forward Evaluation Contract",
        "window_mode": "expanding",
        "upstream_phase_ref": "phase_147_walk_forward",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Genişleyen geçmiş veri pencereleri üzerinde OOS performansı değerlendirme sözleşmesi.",
    },
    {
        "contract_id": "WF_EVAL_PURGED_EMBARGOED",
        "contract_name": "Purged and Embargoed Walk-Forward Evaluation Contract",
        "window_mode": "purged_embargoed",
        "upstream_phase_ref": "phase_147_walk_forward",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Etiket sızıntısını önleyen arındırma ve ambargo tamponlu walk-forward sözleşmesi.",
    },
    {
        "contract_id": "WF_EVAL_STEP_DEGRADATION",
        "contract_name": "Step Degradation Ratio Evaluation Contract",
        "window_mode": "in_sample_vs_out_of_sample_ratio",
        "upstream_phase_ref": "phase_150_split_governance",
        "metric_placeholder_ref": "oos_stability_placeholder",
        "description": "Eğitim seti ile doğrulama adımları arasındaki bozulma oranını inceleyen sözleşme.",
    },
]


def build_walk_forward_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of walk-forward evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in WALK_FORWARD_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "window_mode": c["window_mode"],
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
        "domain": LABEL_WALK_FORWARD_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_execution_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
