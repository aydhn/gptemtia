# -*- coding: utf-8 -*-
"""Phase 151: Regime-Aware Evaluation Report Contracts Module.

Defines reporting contracts conditioned on distinct market regimes (volatility, trend, liquidity, macro).
Zero real metric calculation and zero strategy approval.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_REGIME_AWARE_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

REGIME_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "REGIME_EVAL_VOLATILITY",
        "contract_name": "Volatility Regime Stratified Evaluation Contract",
        "regime_axis": "volatility_regimes",
        "upstream_phase_ref": "phase_135_regime_acceptance",
        "metric_placeholder_ref": "strategy_evaluation_metric_placeholders",
        "description": "Yüksek ve düşük oynaklık rejimlerinde strateji davranış sözleşmesi.",
    },
    {
        "contract_id": "REGIME_EVAL_TREND",
        "contract_name": "Trend vs Mean-Reverting Regime Evaluation Contract",
        "regime_axis": "trend_states",
        "upstream_phase_ref": "phase_135_regime_acceptance",
        "metric_placeholder_ref": "strategy_evaluation_metric_placeholders",
        "description": "Trendli ve yatay bant piyasa rejimlerinde ayrıştırılmış değerlendirme sözleşmesi.",
    },
    {
        "contract_id": "REGIME_EVAL_LIQUIDITY",
        "contract_name": "Liquidity Stress Regime Evaluation Contract",
        "regime_axis": "liquidity_spread_states",
        "upstream_phase_ref": "phase_135_regime_acceptance",
        "metric_placeholder_ref": "cost_adjusted_metric_placeholders",
        "description": "Likidite daralması ve makas genişlemesi rejimlerinde strateji performansı inceleme sözleşmesi.",
    },
    {
        "contract_id": "REGIME_EVAL_MACRO",
        "contract_name": "Macro Economic Regime Evaluation Contract",
        "regime_axis": "macro_states",
        "upstream_phase_ref": "phase_132_macro_event_regime",
        "metric_placeholder_ref": "relative_performance_metric_placeholders",
        "description": "Enflasyon, faiz ve büyüme makro döngüleri altındaki strateji sözleşmesi.",
    },
]


def build_regime_aware_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of regime-aware evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in REGIME_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "regime_axis": c["regime_axis"],
                "upstream_phase_ref": c["upstream_phase_ref"],
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
        "domain": LABEL_REGIME_AWARE_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_calculation_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
