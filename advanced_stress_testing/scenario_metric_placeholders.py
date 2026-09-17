# -*- coding: utf-8 -*-
"""Phase 148: Scenario Metric Placeholders.

Provides specifications and registry for scenario-specific metric placeholders
(Survival Probability, Drawdown Recovery Time, Worst Case Loss, Liquidity Drain).
Formula metadata only; metric_calculated=False, no actual calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

SCENARIO_METRIC_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "scenario_survival_placeholder",
        "metric_category": "SURVIVAL",
        "description": "Senaryo Hayatta Kalma Oranı yer tutucusu (Marjın tükenmeme olasılığı).",
        "formula_spec": "P_survival = 1 - P(Nav_t <= Min_Margin)",
        "benchmark_relative": False,
    },
    {
        "metric_name": "scenario_drawdown_recovery_time_placeholder",
        "metric_category": "RECOVERY",
        "description": "Senaryo Drawdown Toparlanma Süresi yer tutucusu.",
        "formula_spec": "T_recovery = min{t > t_trough : Nav_t >= Nav_peak}",
        "benchmark_relative": False,
    },
    {
        "metric_name": "scenario_worst_case_loss_placeholder",
        "metric_category": "EXTREME_LOSS",
        "description": "Senaryo En Kötü Durum Kaybı (Worst-Case Peak-to-Trough) yer tutucusu.",
        "formula_spec": "L_worst = min_t(Nav_t - Nav_0) / Nav_0",
        "benchmark_relative": False,
    },
    {
        "metric_name": "scenario_liquidity_drain_placeholder",
        "metric_category": "LIQUIDITY_RISK",
        "description": "Senaryo Likidite Tüketim Oranı yer tutucusu.",
        "formula_spec": "D_liquidity = (Available_Cash - Margin_Req) / Total_Capital",
        "benchmark_relative": False,
    },
]


def build_scenario_metric_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of scenario metric placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in SCENARIO_METRIC_SPECS:
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
        "total_scenario_metrics": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "zero_performance_claims": not bool(df["performance_claim_generated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
