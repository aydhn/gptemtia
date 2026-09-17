# -*- coding: utf-8 -*-
"""Phase 151: Report Disclaimers Module.

Defines legal, methodological, and non-trading disclaimers for Phase 151.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_REPORT_DISCLAIMER_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

STANDARD_DISCLAIMER_TEXT = (
    "Bu çıktı Phase 151 Benchmark Comparison and Strategy Evaluation Reports raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark/evaluation/readiness/"
    "strategy-evaluation değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, "
    "gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, "
    "model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek "
    "Sharpe/win-rate/return/alpha/beta/drawdown hesaplama, performans garantisi, strategy approval, "
    "capital allocation, portfolio construction, position sizing, model deployment, model registry write, "
    "model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/"
    "vector kullanımı veya gerçek provider API çağrısı değildir."
)

REPORT_DISCLAIMERS: List[Dict[str, Any]] = [
    {
        "disclaimer_id": "DISC_OFFICIAL_RESEARCH",
        "title": "Official Phase 151 Research Disclaimer",
        "category": "legal_operational",
        "text": STANDARD_DISCLAIMER_TEXT,
    },
    {
        "disclaimer_id": "DISC_ZERO_METRIC_CALCULATION",
        "title": "Uncalculated Metric Placeholder Notice",
        "category": "methodological",
        "text": (
            "Bu rapordaki tüm metrikler hesaplanmamış sözleşme yer tutucularıdır. "
            "Gerçek piyasa simülasyonu, getiri veya risk oranı hesaplanmamıştır. "
            "Herhangi bir ampirik getiri veya başarı garantisi ima edilemez."
        ),
    },
    {
        "disclaimer_id": "DISC_NON_PRODUCTION_BOUNDARY",
        "title": "Strict Non-Production Boundary Notice",
        "category": "safety_boundary",
        "text": (
            "Bu katman yalnızca yerel ve çevrimdışı araştırma sözleşmelerini tanımlar. "
            "Aracı kurum API bağlantısı veya canlı piyasa emir yürütmesi kesinlikle engellenmiştir."
        ),
    },
]


def build_report_disclaimer_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of report disclaimers."""
    rows: List[Dict[str, Any]] = []

    for d in REPORT_DISCLAIMERS:
        rows.append(
            {
                "disclaimer_id": d["disclaimer_id"],
                "title": d["title"],
                "category": d["category"],
                "text": d["text"],
                "is_mandatory": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_REPORT_DISCLAIMER_DOMAIN,
        "total_disclaimers": len(df),
        "all_mandatory": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
