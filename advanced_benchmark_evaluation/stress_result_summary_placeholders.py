# -*- coding: utf-8 -*-
"""Phase 151: Stress Result Summary Placeholders Module.

Defines placeholders summarizing stress scenario resilience and tail losses.
Strictly uncalculated and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_STRESS_AWARE_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRESS_RESULT_ITEMS: List[Dict[str, Any]] = [
    {
        "stress_summary_id": "STRESS_SUM_GFC_2008",
        "scenario_name": "2008 Global Financial Crisis Shock",
        "severity": "extreme",
        "description": "2008 GFC kriz simülasyonu altında azami kayıp ve sermaye erozyonu yer tutucusu.",
    },
    {
        "stress_summary_id": "STRESS_SUM_COVID_2020",
        "scenario_name": "March 2020 Covid Liquidity Shock",
        "severity": "severe",
        "description": "Mart 2020 küresel likidite çöküşü altında strateji dayanıklılık özeti.",
    },
    {
        "stress_summary_id": "STRESS_SUM_OIL_NEGATIVE_2020",
        "scenario_name": "April 2020 Negative Oil Price Shock",
        "severity": "black_swan",
        "description": "Nisan 2020 WTI negatif fiyat şoku altında marjin ve teminat riski özeti.",
    },
    {
        "stress_summary_id": "STRESS_SUM_SUPPLY_CHAIN_CHOKE",
        "scenario_name": "Hypothetical Global Supply Chain Choke",
        "severity": "severe",
        "description": "Boğaz ve tedarik zinciri tıkanıklığı varsayımsal şoku altındaki risk özeti.",
    },
]


def build_stress_result_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of stress result summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in STRESS_RESULT_ITEMS:
        rows.append(
            {
                "stress_summary_id": item["stress_summary_id"],
                "scenario_name": item["scenario_name"],
                "severity": item["severity"],
                "description": item["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_STRESS_AWARE_EVALUATION_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
