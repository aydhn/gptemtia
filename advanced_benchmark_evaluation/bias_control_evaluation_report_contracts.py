# -*- coding: utf-8 -*-
"""Phase 151: Bias-Control Evaluation Report Contracts Module.

Defines reporting contracts verifying bias mitigations across lookahead,
survivorship, data-snooping, overfitting, and benchmark selection.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BIAS_CONTROL_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "BIAS_EVAL_LOOKAHEAD_AUDIT",
        "contract_name": "Lookahead and Leakage Prevention Evaluation Contract",
        "bias_category": "lookahead_bias",
        "upstream_phase_ref": "phase_150_lookahead_bias_controls",
        "description": "Zaman serisi sıralaması, negatif shift yasağı ve asof join sızıntısızlığı denetimi.",
    },
    {
        "contract_id": "BIAS_EVAL_SURVIVORSHIP_AUDIT",
        "contract_name": "Survivorship Bias Reconstitution Evaluation Contract",
        "bias_category": "survivorship_bias",
        "upstream_phase_ref": "phase_150_survivorship_bias_controls",
        "description": "Kote-dışı kalmış varlıkların ve tarihsel evren bileşenlerinin korunumu denetimi.",
    },
    {
        "contract_id": "BIAS_EVAL_DATA_SNOOPING_AUDIT",
        "contract_name": "Data Snooping and Multiple Testing Haircut Contract",
        "bias_category": "data_snooping_bias",
        "upstream_phase_ref": "phase_150_data_snooping_bias_controls",
        "description": "Deneme sayısı takibi ve çoklu hipotez testleri istatistiki ceza standartları.",
    },
    {
        "contract_id": "BIAS_EVAL_OVERFITTING_AUDIT",
        "contract_name": "Overfitting and Degrees of Freedom Control Contract",
        "bias_category": "overfitting_bias",
        "upstream_phase_ref": "phase_150_overfitting_bias_controls",
        "description": "Serbestlik derecesi oranı ve IS/OOS varyans uçurumu denetimi sözleşmesi.",
    },
    {
        "contract_id": "BIAS_EVAL_BENCHMARK_SELECTION_AUDIT",
        "contract_name": "Benchmark Selection Bias Control Contract",
        "bias_category": "benchmark_selection_bias",
        "upstream_phase_ref": "phase_150_benchmark_selection_bias_controls",
        "description": "Benchmarkın sonradan amaca uygun seçilmesini engelleyen ön taahhütlü referans denetimi.",
    },
]


def build_bias_control_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of bias-control evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in BIAS_CONTROL_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "bias_category": c["bias_category"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "description": c["description"],
                "enforcement_active": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_contracts": len(df),
        "all_enforcements_active": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
