# -*- coding: utf-8 -*-
"""Phase 150: Backtest Report Disclaimers.

Standardized regulatory and methodological disclaimers for Phase 150.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    RESULT_REPORTING_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

DISCLAIMER_TEXT = (
    "Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. "
    "Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness "
    "değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, "
    "benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, "
    "dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, "
    "performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, "
    "scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider "
    "API çağrısı değildir."
)

REPORT_DISCLAIMERS: List[Dict[str, Any]] = [
    {
        "disclaimer_id": "DISC_CORE_01",
        "title": "Core Non-Execution Disclaimer",
        "language": "tr",
        "text": DISCLAIMER_TEXT,
        "mandatory": True,
    },
    {
        "disclaimer_id": "DISC_CORE_02_EN",
        "title": "International Research Disclaimer",
        "language": "en",
        "text": (
            "This report is a Phase 150 Backtest Governance and Bias Control artifact. "
            "It does not constitute trade signals, live orders, broker integration, investment advice, "
            "actual backtest execution, benchmark execution, or performance guarantees. "
            "All metrics remain uncalculated research placeholders."
        ),
        "mandatory": True,
    },
]


def build_backtest_report_disclaimer_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for report disclaimers."""
    rows: List[Dict[str, Any]] = []
    for d in REPORT_DISCLAIMERS:
        rows.append({
            "disclaimer_id": d["disclaimer_id"],
            "title": d["title"],
            "language": d["language"],
            "text": d["text"],
            "mandatory": d["mandatory"],
            "phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": RESULT_REPORTING_DOMAIN,
        "subdomain": "report_disclaimers",
        "total_disclaimers": len(df),
        "mandatory_count": len(df),
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
