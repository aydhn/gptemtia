# -*- coding: utf-8 -*-
"""Phase 151: Monte Carlo Result Summary Placeholders Module.

Defines placeholders summarizing resampling distributions, quantile envelopes, and path variances.
Zero real simulation is executed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

MONTE_CARLO_RESULT_ITEMS: List[Dict[str, Any]] = [
    {
        "mc_summary_id": "MC_SUM_CONFIDENCE_INTERVAL",
        "title": "Bootstrap 90%/95% Confidence Interval Summary Placeholder",
        "category": "quantile_envelope",
        "description": "Blok bootstrap getiri ve drawdown güven aralıkları özeti yer tutucusu.",
    },
    {
        "mc_summary_id": "MC_SUM_PERMUTATION_VARIANCE",
        "title": "Trade Permutation Sequence Variance Placeholder",
        "category": "sequence_luck",
        "description": "İşlem sıralamasının tesadüfi olmasından kaynaklanan kümülatif PnL saçılım özeti.",
    },
    {
        "mc_summary_id": "MC_SUM_WORST_PATH_PROFILE",
        "title": "Worst 5th Percentile Resampled Path Profile Placeholder",
        "category": "tail_scenario",
        "description": "Yeniden örneklenen en kötü %5'lik patikadaki sermaye tüketimi özeti.",
    },
]


def build_monte_carlo_result_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of Monte Carlo result summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in MONTE_CARLO_RESULT_ITEMS:
        rows.append(
            {
                "mc_summary_id": item["mc_summary_id"],
                "title": item["title"],
                "category": item["category"],
                "description": item["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
