# -*- coding: utf-8 -*-
"""Phase 148: Stressed Drawdown Placeholders.

Provides specifications and registry for stressed maximum drawdown and underwater duration placeholders.
Formula metadata only; metric_calculated=False, no actual calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESSED_DRAWDOWN_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "stressed_max_drawdown_placeholder",
        "metric_category": "STRESSED_DRAWDOWN",
        "description": "Şok altındaki maksimum sermaye kaybı (Maximum Drawdown) yer tutucusu.",
        "formula_spec": "MaxDD_stress = max_t (Peak_Nav - Nav_t_stress) / Peak_Nav",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_drawdown_duration_placeholder",
        "metric_category": "STRESSED_DRAWDOWN",
        "description": "Şok altındaki su altı süresi (Underwater Duration) yer tutucusu.",
        "formula_spec": "Duration_stress = t_recovery - t_peak",
        "benchmark_relative": False,
    },
]


def build_stressed_drawdown_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stressed drawdown placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESSED_DRAWDOWN_SPECS:
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
        "total_stressed_drawdown_placeholders": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
