# -*- coding: utf-8 -*-
"""Phase 151: Strategy Evaluation Summary Placeholders Module.

Defines summary placeholders for strategy evaluation reports.
Strictly uncalculated and contains zero performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STRATEGY_SUMMARY_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "SUM_STRATEGY_EXECUTIVE",
        "title": "Executive Strategy Evaluation Summary Placeholder",
        "section": "executive_summary",
        "template_text": "[PLACEHOLDER: Çevrimdışı strateji ampirik hipotezi ve model mimarisi özeti]",
    },
    {
        "placeholder_id": "SUM_STRATEGY_REGIME_COVERAGE",
        "title": "Regime Performance Stratification Placeholder",
        "section": "regime_performance",
        "template_text": "[PLACEHOLDER: Volatilite ve trend rejimlerine göre ayrıştırılmış özet]",
    },
    {
        "placeholder_id": "SUM_STRATEGY_FRICTION_EROSION",
        "title": "Friction and Slippage Drag Summary Placeholder",
        "section": "friction_analysis",
        "template_text": "[PLACEHOLDER: Komisyon ve kayma kaynaklı getiri erozyonu özeti]",
    },
    {
        "placeholder_id": "SUM_STRATEGY_OOS_STABILITY",
        "title": "Out-of-Sample Stability and Walk-Forward Summary Placeholder",
        "section": "oos_stability",
        "template_text": "[PLACEHOLDER: Örneklem dışı dönem ve adım stabilitesi özeti]",
    },
]


def build_strategy_evaluation_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of strategy evaluation summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for p in STRATEGY_SUMMARY_PLACEHOLDERS:
        rows.append(
            {
                "placeholder_id": p["placeholder_id"],
                "title": p["title"],
                "section": p["section"],
                "template_text": p["template_text"],
                "is_calculated": False,
                "performance_claim_allowed": False,
                "strategy_approval_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
        "total_placeholders": len(df),
        "all_uncalculated": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
