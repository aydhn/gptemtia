# -*- coding: utf-8 -*-
"""Phase 148: Stress Metric Placeholders.

Provides specifications and registry for stress test risk metric placeholders
(Stressed Return, Stressed Volatility, Stressed VaR, Stressed Expected Shortfall).
Formula metadata only; metric_calculated=False, no actual calculation or performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressMetricPlaceholder

STRESS_METRIC_SPECS: List[Dict[str, Any]] = [
    {
        "metric_name": "stressed_return_placeholder",
        "metric_category": "STRESS_PERFORMANCE",
        "description": "Şok altındaki portföy getirisi yer tutucusu.",
        "formula_spec": "R_stress = sum(w_i * (R_i + delta_R_i)) - total_stress_friction",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_volatility_placeholder",
        "metric_category": "STRESS_RISK",
        "description": "Şok altındaki portföy oynaklığı yer tutucusu.",
        "formula_spec": "sigma_stress = sqrt(w.T * Sigma_stress * w)",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_var_placeholder",
        "metric_category": "TAIL_RISK",
        "description": "Stresli Riske Maruz Değer (Stressed Value-at-Risk 99%) yer tutucusu.",
        "formula_spec": "VaR_99_stress = quantile(L_stress, 0.99)",
        "benchmark_relative": False,
    },
    {
        "metric_name": "stressed_expected_shortfall_placeholder",
        "metric_category": "TAIL_RISK",
        "description": "Stresli Beklenen Kayıp (Stressed Expected Shortfall / CVaR) yer tutucusu.",
        "formula_spec": "ES_99_stress = E[L_stress | L_stress >= VaR_99_stress]",
        "benchmark_relative": False,
    },
]


def build_stress_metric_placeholder_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of stress metric placeholders."""
    rows: List[Dict[str, Any]] = []
    for spec in STRESS_METRIC_SPECS:
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
        "total_stress_metrics": len(df),
        "all_calculation_blocked": not bool(df["metric_calculated"].any()) if not df.empty else True,
        "zero_performance_claims": not bool(df["performance_claim_generated"].any()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
