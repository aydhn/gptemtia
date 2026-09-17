# -*- coding: utf-8 -*-
"""Phase 151: Regime Performance Summary Placeholders Module.

Defines placeholders for reporting strategy behavior stratified across regimes.
All metrics are uncalculated.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_REGIME_AWARE_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

REGIME_PERFORMANCE_ITEMS: List[Dict[str, Any]] = [
    {
        "regime_summary_id": "REG_SUM_BULL_TREND",
        "regime_state": "bullish_trending",
        "title": "Bullish Trend Market State Performance Placeholder",
        "description": "Güçlü yukarı yönlü trend rejiminde getiri ve risk davranışı özeti.",
    },
    {
        "regime_summary_id": "REG_SUM_BEAR_TREND",
        "regime_state": "bearish_trending",
        "title": "Bearish Trend Market State Performance Placeholder",
        "description": "Aşağı yönlü trend rejiminde sermaye koruma veya kısa pozisyon davranışı özeti.",
    },
    {
        "regime_summary_id": "REG_SUM_HIGH_VOL",
        "regime_state": "high_volatility",
        "title": "High Volatility Regime Performance Placeholder",
        "description": "Piyasa çalkantısı ve yüksek volatilite rejiminde risk profili özeti.",
    },
    {
        "regime_summary_id": "REG_SUM_LOW_VOL_RANGE",
        "regime_state": "low_volatility_ranging",
        "title": "Low Volatility Range-Bound Regime Performance Placeholder",
        "description": "Düşük oynaklıklı yatay piyasa rejiminde sahte sinyal (whipsaw) direnci özeti.",
    },
]


def build_regime_performance_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of regime performance summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for item in REGIME_PERFORMANCE_ITEMS:
        rows.append(
            {
                "regime_summary_id": item["regime_summary_id"],
                "regime_state": item["regime_state"],
                "title": item["title"],
                "description": item["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_REGIME_AWARE_EVALUATION_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
