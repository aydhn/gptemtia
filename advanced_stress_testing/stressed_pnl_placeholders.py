# -*- coding: utf-8 -*-
"""Phase 148: Stressed PnL Placeholders.

Provides specifications and registry for stressed PnL computation placeholders.
Formula metadata only; metric_calculated=False, no actual PnL calculation.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESSED_PNL_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "stressed_realized_pnl_placeholder",
        "metric_category": "STRESSED_PNL",
        "description": "Kriz senaryosu altında gerçekleşen kâr/zarar yer tutucusu.",
        "formula_spec": "PnL_realized_stress = sum((Exit_P_stress - Entry_P) * Qty) - Friction_stress",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_unrealized_pnl_placeholder",
        "metric_category": "STRESSED_PNL",
        "description": "Kriz anındaki açık pozisyonların anlık değer düşüş kâr/zarar yer tutucusu.",
        "formula_spec": "PnL_unrealized_stress = sum((Mark_P_stress - Cost_Basis) * Position_Qty)",
        "benchmark_relative": False,
    },
]


def build_stressed_pnl_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stressed PnL placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESSED_PNL_SPECS:
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
        "total_stressed_pnl_placeholders": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
