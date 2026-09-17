# -*- coding: utf-8 -*-
"""Phase 151: Slippage-Adjusted Evaluation Report Contracts Module.

Defines reporting contracts for execution slippage and market impact frictions.
Ensures zero real metric calculation and zero trade recommendations.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SLIPPAGE_ADJUSTED_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

SLIPPAGE_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "SLIPPAGE_EVAL_FIXED_DYNAMIC",
        "contract_name": "Fixed and Dynamic Spread Slippage Contract",
        "model_ref": "phase_146_spread_based_slippage",
        "impact_metric": "slippage_adjusted_return_placeholder",
        "description": "Alış-satış makası genişlemesine bağlı kayma erozyonu değerlendirmesi.",
    },
    {
        "contract_id": "SLIPPAGE_EVAL_SQUARE_ROOT_IMPACT",
        "contract_name": "Non-Linear Market Impact Contract",
        "model_ref": "phase_146_square_root_market_impact",
        "impact_metric": "slippage_adjusted_return_placeholder",
        "description": "Emir büyüklüğüne bağlı doğrusal olmayan piyasa etkisi kayma değerlendirmesi.",
    },
    {
        "contract_id": "SLIPPAGE_EVAL_VOLATILITY_SCALED",
        "contract_name": "Volatility Scaled Slippage Contract",
        "model_ref": "phase_146_volatility_dependent_slippage",
        "impact_metric": "slippage_adjusted_return_placeholder",
        "description": "Yüksek volatilite koşullarında artan kayma maliyeti sözleşmesi.",
    },
    {
        "contract_id": "SLIPPAGE_EVAL_ADV_PARTICIPATION",
        "contract_name": "ADV Liquidity Constraint Slippage Contract",
        "model_ref": "phase_150_liquidity_realism_governance",
        "impact_metric": "slippage_adjusted_return_placeholder",
        "description": "Günlük ortalama hacim katılım sınırlarının aşılması durumundaki kayma cezası.",
    },
]


def build_slippage_adjusted_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of slippage-adjusted evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in SLIPPAGE_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "model_ref": c["model_ref"],
                "impact_metric": c["impact_metric"],
                "description": c["description"],
                "metric_calculation_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_SLIPPAGE_ADJUSTED_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_calculation_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
