# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Comparison Summary Placeholders Module.

Defines summary placeholders for benchmark comparison reports.
Strictly uncalculated and contains zero performance claims.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_SUMMARY_PLACEHOLDER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

BENCHMARK_SUMMARY_PLACEHOLDERS: List[Dict[str, Any]] = [
    {
        "placeholder_id": "SUM_BENCHMARK_EXECUTIVE",
        "title": "Executive Benchmark Comparison Summary Placeholder",
        "section": "executive_summary",
        "template_text": "[PLACEHOLDER: Baseline stratejiler ile görece karşılaştırma özeti]",
    },
    {
        "placeholder_id": "SUM_BENCHMARK_RELATIVE_EXPOSURE",
        "title": "Systematic Market Exposure and Beta Summary Placeholder",
        "section": "systematic_risk",
        "template_text": "[PLACEHOLDER: Benchmark beta ve sistematik risk ayrıştırma özeti]",
    },
    {
        "placeholder_id": "SUM_BENCHMARK_TRACKING_DIAGNOSTICS",
        "title": "Tracking Error and Active Risk Summary Placeholder",
        "section": "tracking_diagnostics",
        "template_text": "[PLACEHOLDER: Benchmark sapma volatilitesi ve artık getiri özeti]",
    },
    {
        "placeholder_id": "SUM_BENCHMARK_CAPTURE_RATIO",
        "title": "Bull/Bear Market Participation Summary Placeholder",
        "section": "market_capture",
        "template_text": "[PLACEHOLDER: Yükseliş ve düşüş evrelerinde benchmark katılım özeti]",
    },
]


def build_benchmark_comparison_summary_placeholder_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of benchmark comparison summary placeholders."""
    rows: List[Dict[str, Any]] = []

    for p in BENCHMARK_SUMMARY_PLACEHOLDERS:
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
