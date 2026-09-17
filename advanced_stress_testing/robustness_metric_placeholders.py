# -*- coding: utf-8 -*-
"""Phase 148: Robustness Metric Placeholders.

Provides specifications and registry for strategy robustness and fragility metric placeholders.
Formula metadata only; metric_calculated=False, no performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

ROBUSTNESS_METRIC_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "scenario_robustness_score_placeholder",
        "metric_category": "ROBUSTNESS",
        "description": "Farklı stres senaryolarındaki hayatta kalma ve performans koruma skoru yer tutucusu.",
        "formula_spec": "Robustness = mean(Scenario_Survivability_i) * (1 - Std(Loss_i))",
        "benchmark_relative": False,
    },
    {
        "metric_name": "cross_scenario_stability_index_placeholder",
        "metric_category": "STABILITY",
        "description": "Senaryolar arası sonuç varyansı ve stabilite indeksi yer tutucusu.",
        "formula_spec": "Stability = 1 / (1 + variance(Stressed_Drawdowns))",
        "benchmark_relative": False,
    },
    {
        "metric_name": "parameter_fragility_score_placeholder",
        "metric_category": "FRAGILITY",
        "description": "Küçük girdi ve parametre değişimlerinde stres sonucunun bozulma hassasiyeti yer tutucusu.",
        "formula_spec": "Fragility = max(|d(Stressed_Loss) / d(Param_k)|)",
        "benchmark_relative": False,
    },
]


def build_robustness_metric_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of robustness metric placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in ROBUSTNESS_METRIC_SPECS:
        placeholder = StressMetricPlaceholder(
            metric_name=spec["metric_name"],
            metric_category=spec["metric_category"],
            description=spec["description"],
            formula_spec=spec["formula_spec"],
            benchmark_relative=spec["benchmark_relative"],
            metric_calculated=False,
            performance_claim_generated=False,
            non_signal=True,
        )
        rows.append(
            {
                "metric_name": placeholder.metric_name,
                "metric_category": placeholder.metric_category,
                "description": placeholder.description,
                "formula_spec": placeholder.formula_spec,
                "benchmark_relative": placeholder.benchmark_relative,
                "metric_calculated": placeholder.metric_calculated,
                "performance_claim_generated": placeholder.performance_claim_generated,
                "non_signal": placeholder.non_signal,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_robustness_metrics": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "zero_performance_claims": not bool(df["performance_claim_generated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
