# -*- coding: utf-8 -*-
"""Phase 148: Stressed Liquidity Placeholders.

Provides specifications and registry for liquidity cost and days-to-liquidate placeholders under stress.
Formula metadata only; metric_calculated=False, no actual calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESSED_LIQUIDITY_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "days_to_liquidate_stressed_placeholder",
        "metric_category": "LIQUIDITY",
        "description": "Kriz anındaki hacim düşüşünde pozisyonu tasfiye etmek için gereken gün sayısı yer tutucusu.",
        "formula_spec": "DTL_stress = sum(Pos_Qty_i / (Daily_Vol_i * 0.20 * Participation_Rate))",
        "benchmark_relative": False,
    },
    {
        "metric_name": "liquidation_haircut_stressed_placeholder",
        "metric_category": "LIQUIDITY",
        "description": "Acil tasfiyede piyasa etkisi ve spread nedeniyle uğranacak sermaye iskontosu yer tutucusu.",
        "formula_spec": "Haircut_stress = Total_Impact_Cost / Portfolio_Nav",
        "benchmark_relative": False,
    },
]


def build_stressed_liquidity_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stressed liquidity placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESSED_LIQUIDITY_SPECS:
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
        "total_stressed_liquidity_placeholders": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
