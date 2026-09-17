# -*- coding: utf-8 -*-
"""Phase 151: Robustness Metric Placeholders Module.

Defines uncalculated metric placeholders for OOS stability, stress resilience,
Monte Carlo robustness, and parameter sensitivity.
Zero real calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

ROBUSTNESS_METRIC_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "metric_name": "oos_stability_placeholder",
        "category": "out_of_sample_stability",
        "formula_spec": "oos_annualized_return / is_annualized_return",
        "target_role": "oos_retention_ratio_hypothesis",
        "description": "Örneklem dışı performansın örneklem içine oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "stress_resilience_placeholder",
        "category": "stress_resilience",
        "formula_spec": "min_nav_under_stress / baseline_nav",
        "target_role": "capital_preservation_under_shock_hypothesis",
        "description": "Kriz senaryoları altındaki sermaye erozyonu yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "monte_carlo_robustness_placeholder",
        "category": "resampling_stability",
        "formula_spec": "5th_percentile_drawdown / median_drawdown",
        "target_role": "bootstrap_worst_case_ratio_hypothesis",
        "description": "Monte Carlo yeniden örneklemesindeki en kötü %5'lik yol oranı yer tutucusu (hesaplanmamış).",
    },
    {
        "metric_name": "parameter_stability_placeholder",
        "category": "parameter_sensitivity",
        "formula_spec": "min(perturbed_returns) / nominal_return",
        "target_role": "plateau_fragility_ratio_hypothesis",
        "description": "Parametre pertürbasyonlarında performansın korunma oranı yer tutucusu (hesaplanmamış).",
    },
]


def build_robustness_metric_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of robustness metric placeholders."""
    rows: List[Dict[str, Any]] = []

    for m in ROBUSTNESS_METRIC_PLACEHOLDERS:
        rows.append(
            {
                "metric_name": m["metric_name"],
                "category": m["category"],
                "formula_spec": m["formula_spec"],
                "target_role": m["target_role"],
                "description": m["description"],
                "is_calculated": False,
                "actual_value": None,
                "performance_claim_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_MONTE_CARLO_ROBUSTNESS_EVALUATION_DOMAIN,
        "total_metrics": len(df),
        "all_uncalculated": True,
        "all_claims_blocked": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
