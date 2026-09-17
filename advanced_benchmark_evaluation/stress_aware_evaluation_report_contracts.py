# -*- coding: utf-8 -*-
"""Phase 151: Stress-Aware Evaluation Report Contracts Module.

Defines reporting contracts evaluating strategy behavior under extreme stress and historical shocks.
Zero real stress simulation execution and zero capital allocation claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRESS_AWARE_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRESS_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "STRESS_EVAL_HISTORICAL_CRISIS",
        "contract_name": "Historical Crisis Shock Evaluation Contract",
        "scenario_type": "historical_replay",
        "upstream_phase_ref": "phase_148_stress_testing",
        "metric_placeholder_ref": "stress_resilience_placeholder",
        "description": "2008 Küresel Finans Krizi, 2020 Covid ve Negatif Petrol krizleri altındaki değerlendirme.",
    },
    {
        "contract_id": "STRESS_EVAL_HYPOTHETICAL_SHOCK",
        "contract_name": "Hypothetical Stagflation and Supply Choke Contract",
        "scenario_type": "hypothetical_simulation",
        "upstream_phase_ref": "phase_148_stress_testing",
        "metric_placeholder_ref": "stress_resilience_placeholder",
        "description": "Stagflasyon 2.0 ve boğaz tıkanıklığı varsayımsal krizleri altındaki değerlendirme.",
    },
    {
        "contract_id": "STRESS_EVAL_LIQUIDITY_FREEZE",
        "contract_name": "Liquidity Freeze and Spread Widening Contract",
        "scenario_type": "liquidity_crisis",
        "upstream_phase_ref": "phase_148_stress_testing",
        "metric_placeholder_ref": "stress_resilience_placeholder",
        "description": "Derinlik yarılanması ve makas patlaması altındaki kayıp inceleme sözleşmesi.",
    },
    {
        "contract_id": "STRESS_EVAL_CORRELATION_BREAKDOWN",
        "contract_name": "Cross-Asset Correlation Breakdown Contract",
        "scenario_type": "correlation_shock",
        "upstream_phase_ref": "phase_148_stress_testing",
        "metric_placeholder_ref": "stress_resilience_placeholder",
        "description": "Geleneksel korunma (hedging) ve varlık korelasyonlarının çöküşü altındaki değerlendirme.",
    },
]


def build_stress_aware_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of stress-aware evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in STRESS_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "scenario_type": c["scenario_type"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "metric_placeholder_ref": c["metric_placeholder_ref"],
                "description": c["description"],
                "simulation_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_STRESS_AWARE_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_simulation_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
