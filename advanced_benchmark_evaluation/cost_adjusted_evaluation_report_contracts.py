# -*- coding: utf-8 -*-
"""Phase 151: Cost-Adjusted Evaluation Report Contracts Module.

Defines reporting contracts for performance net of commissions, exchange fees,
and financing/carry costs. Zero real metric calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_COST_ADJUSTED_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

COST_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "COST_EVAL_COMMISSION_IMPACT",
        "contract_name": "Tiered Commission Impact Report Contract",
        "cost_type": "broker_commission",
        "realism_model_ref": "phase_146_tiered_volume_commission",
        "metric_placeholder_ref": "cost_adjusted_return_placeholder",
        "description": "Kademeli komisyon maliyetlerinin getiriye etkisini değerlendiren sözleşme.",
    },
    {
        "contract_id": "COST_EVAL_EXCHANGE_REGULATORY_FEES",
        "contract_name": "Exchange and Regulatory Fee Impact Contract",
        "cost_type": "exchange_fees",
        "realism_model_ref": "phase_146_regulatory_exchange_fee",
        "metric_placeholder_ref": "cost_adjusted_return_placeholder",
        "description": "Borsa ve takas ücretlerinin getiri erozyonunu inceleyen sözleşme.",
    },
    {
        "contract_id": "COST_EVAL_FINANCING_CARRY",
        "contract_name": "Financing and Carry Cost Contract",
        "cost_type": "overnight_carry",
        "realism_model_ref": "phase_146_overnight_swap_carry",
        "metric_placeholder_ref": "cost_adjusted_return_placeholder",
        "description": "Gecelik taşıma ve faiz farkı (swap/roll) maliyetleri değerlendirme sözleşmesi.",
    },
    {
        "contract_id": "COST_EVAL_NET_SURVIVAL_THRESHOLD",
        "contract_name": "Net Profitability Friction Barrier Contract",
        "cost_type": "all_in_friction",
        "realism_model_ref": "phase_150_execution_realism",
        "metric_placeholder_ref": "cost_adjusted_return_placeholder",
        "description": "Stratejinin toplam sürtünme maliyetlerini aşma eşiğini inceleyen sözleşme.",
    },
]


def build_cost_adjusted_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of cost-adjusted evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in COST_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "cost_type": c["cost_type"],
                "realism_model_ref": c["realism_model_ref"],
                "metric_placeholder_ref": c["metric_placeholder_ref"],
                "description": c["description"],
                "metric_calculation_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_COST_ADJUSTED_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_calculation_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
