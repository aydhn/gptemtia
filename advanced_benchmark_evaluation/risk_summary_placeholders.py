# -*- coding: utf-8 -*-
"""Phase 151: Risk Summary Placeholders Module.

Defines placeholders for drawdown, tail risk, and downside deviation reporting.
Zero real calculation is performed.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_RISK_SUMMARY_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

RISK_SUMMARY_ITEMS: List[Dict[str, Any]] = [
    {
        "risk_id": "RISK_MAX_DRAWDOWN",
        "title": "Maximum Drawdown and Underwater Profile Placeholder",
        "risk_type": "drawdown_profile",
        "description": "Zirveden dibe azami kayıp ve toparlanma süresi (recovery time) yer tutucusu.",
    },
    {
        "risk_id": "RISK_VALUE_AT_RISK",
        "title": "Parametric and Historical Value at Risk (VaR) Placeholder",
        "risk_type": "tail_risk",
        "description": "%95 ve %99 güven aralığında günlük ve dönemsel Riske Maruz Değer yer tutucusu.",
    },
    {
        "risk_id": "RISK_EXPECTED_SHORTFALL",
        "title": "Conditional Value at Risk / Expected Shortfall (ES) Placeholder",
        "risk_type": "tail_risk",
        "description": "VaR eşiğini aşan aşırı kayıpların beklenen ortalaması yer tutucusu.",
    },
    {
        "risk_id": "RISK_DOWNSIDE_DEVIATION",
        "title": "Downside Semi-Variance and Deviation Placeholder",
        "risk_type": "downside_volatility",
        "description": "Yalnızca negatif getirilerin oluşturduğu asimetrik risk varyansı yer tutucusu.",
    },
]


def build_risk_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of risk summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for r in RISK_SUMMARY_ITEMS:
        rows.append(
            {
                "risk_id": r["risk_id"],
                "title": r["title"],
                "risk_type": r["risk_type"],
                "description": r["description"],
                "is_calculated": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_RISK_SUMMARY_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
