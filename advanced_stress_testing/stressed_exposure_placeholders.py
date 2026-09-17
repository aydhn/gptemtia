# -*- coding: utf-8 -*-
"""Phase 148: Stressed Exposure Placeholders.

Provides specifications and registry for gross/net leverage and tail risk exposure placeholders under stress.
Formula metadata only; metric_calculated=False, no actual calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESSED_EXPOSURE_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "stressed_gross_leverage_placeholder",
        "metric_category": "EXPOSURE",
        "description": "Şok altındaki brüt kaldıraç oranı (Gross Exposure / Equity) yer tutucusu.",
        "formula_spec": "Gross_Lev_stress = sum(|Pos_i * P_i_stress|) / Nav_stress",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_margin_utilization_placeholder",
        "metric_category": "EXPOSURE",
        "description": "Teminat çağrısı ve margin kullanım oranı yer tutucusu.",
        "formula_spec": "Margin_Util_stress = Required_Margin_stress / Nav_stress",
        "benchmark_relative": False,
    },
]


def build_stressed_exposure_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stressed exposure placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESSED_EXPOSURE_SPECS:
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
        "total_stressed_exposure_placeholders": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
