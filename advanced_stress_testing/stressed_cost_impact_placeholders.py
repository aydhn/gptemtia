# -*- coding: utf-8 -*-
"""Phase 148: Stressed Cost Impact Placeholders.

Provides specifications and registry for combined friction, slippage, and spread shock cost impact placeholders.
Formula metadata only; metric_calculated=False, no actual calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESSED_COST_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "total_stressed_friction_impact_placeholder",
        "metric_category": "FRICTION_IMPACT",
        "description": "Kriz anında artan komisyon, spread ve slippage'ın toplam getiriye negatif etkisi yer tutucusu.",
        "formula_spec": "Friction_Impact = Commission_stress + Slippage_stress + Spread_stress",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_drag_ratio_placeholder",
        "metric_category": "FRICTION_IMPACT",
        "description": "Stresli sürtünme maliyetinin brüt getiriye oranı (Drag Ratio) yer tutucusu.",
        "formula_spec": "Drag_Ratio_stress = Friction_Impact / Gross_Return_Abs",
        "benchmark_relative": False,
    },
]


def build_stressed_cost_impact_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stressed cost impact placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESSED_COST_SPECS:
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
        "total_cost_impact_placeholders": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
