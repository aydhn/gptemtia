# -*- coding: utf-8 -*-
"""Phase 150: Backtest Governance Manual Review Queue Module.

Compiles manual review tasks ensuring human governance before advancing to Phase 151.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    MANUAL_REVIEW_GATE_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

MANUAL_REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "MRQ_150_01",
        "title": "Review Backtest Governance Contracts",
        "category": "contract_governance",
        "inspection_focus": "Verify all 7 backtest governance contracts are defined without active simulation permissions.",
    },
    {
        "review_id": "MRQ_150_02",
        "title": "Review Lookahead and Survivorship Bias Controls",
        "category": "bias_control",
        "inspection_focus": "Ensure timestamp ordering and point-in-time universe preservation rules are enforced.",
    },
    {
        "review_id": "MRQ_150_03",
        "title": "Review Data Snooping and Overfitting Guards",
        "category": "bias_control",
        "inspection_focus": "Verify strict hypothesis pre-registration and test set quarantine discipline.",
    },
    {
        "review_id": "MRQ_150_04",
        "title": "Review Multiple Testing and Parameter Fishing Policies",
        "category": "statistical_rigor",
        "inspection_focus": "Check family-wise error adjustments and parameter penalty documentation.",
    },
    {
        "review_id": "MRQ_150_05",
        "title": "Review Transaction Cost, Slippage, and Realism Settings",
        "category": "execution_realism",
        "inspection_focus": "Ensure commission tiers, bid-ask spreads, and liquidity thresholds are realistic.",
    },
    {
        "review_id": "MRQ_150_06",
        "title": "Review Split Discipline, Purge/Embargo, and Walk-Forward",
        "category": "time_series_integrity",
        "inspection_focus": "Verify purge and embargo windows prevent autocorrelation leakage across folds.",
    },
    {
        "review_id": "MRQ_150_07",
        "title": "Review Stress Testing and Monte Carlo Robustness Linkage",
        "category": "stress_monte_carlo",
        "inspection_focus": "Confirm crisis catalogs and bootstrap protocols are linked as research contracts.",
    },
    {
        "review_id": "MRQ_150_08",
        "title": "Review Metric and Performance Claim Boundaries",
        "category": "claim_boundary",
        "inspection_focus": "Confirm all return, Sharpe, alpha, and strategy approval claims remain blocked.",
    },
    {
        "review_id": "MRQ_150_09",
        "title": "Review Disabled Execution and Safety Boundaries",
        "category": "safety_boundary",
        "inspection_focus": "Verify live trading, broker APIs, optimizers, and model fitting are strictly disabled.",
    },
    {
        "review_id": "MRQ_150_10",
        "title": "Review Phase 151 Handoff Prerequisites",
        "category": "handoff_readiness",
        "inspection_focus": "Confirm readiness for Phase 151 Benchmark Comparison and Strategy Evaluation.",
    },
]


def summarize_backtest_governance_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the manual review queue."""
    return {
        "domain": MANUAL_REVIEW_GATE_DOMAIN,
        "total_review_items": len(df),
        "pending_review_count": len(df),
        "all_pending_manual_review": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }


def build_backtest_governance_manual_review_queue(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the manual review queue DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for item in MANUAL_REVIEW_ITEMS:
        rows.append({
            "review_id": item["review_id"],
            "title": item["title"],
            "category": item["category"],
            "inspection_focus": item["inspection_focus"],
            "status": "PENDING_MANUAL_REVIEW",
            "safe_resolution": "Inspect contract specifications and metadata definitions without executing live orders.",
            "profile_name": profile.profile_name,
            "current_phase": profile.current_phase,
            "non_signal": True,
            "local_only": True,
        })
    df = pd.DataFrame(rows)
    summary = summarize_backtest_governance_manual_review_queue(df)
    summary["profile_name"] = profile.profile_name
    return df, summary
