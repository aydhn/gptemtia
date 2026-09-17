# -*- coding: utf-8 -*-
"""Phase 151: Benchmark Evaluation Manual Review Module.

Defines the manual review queue requiring operator inspection before Phase 152 handoff.
Strictly prohibits automated approvals, automated trading, or automated model optimization.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_FINDING_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

MANUAL_REVIEW_GATES: List[Dict[str, Any]] = [
    {
        "review_id": "REV_01_BENCHMARK_REPORT_CONTRACTS",
        "topic": "Benchmark Comparison Report Contracts",
        "inspection_focus": "Verify benchmark report templates maintain strictly zero execution logic.",
        "mandatory": True,
    },
    {
        "review_id": "REV_02_STRATEGY_EVALUATION_CONTRACTS",
        "topic": "Strategy Evaluation Report Contracts",
        "inspection_focus": "Verify strategy evaluation templates maintain zero strategy approval status.",
        "mandatory": True,
    },
    {
        "review_id": "REV_03_BENCHMARK_UNIVERSE_BASELINE",
        "topic": "Benchmark Universe & Baseline Definitions",
        "inspection_focus": "Ensure commodity & FX universes and Buy & Hold baselines are pre-committed.",
        "mandatory": True,
    },
    {
        "review_id": "REV_04_COST_SLIPPAGE_CONTRACTS",
        "topic": "Friction Realism Evaluation Contracts",
        "inspection_focus": "Confirm commission and market impact assumptions are explicitly defined.",
        "mandatory": True,
    },
    {
        "review_id": "REV_05_REGIME_STRESS_MONTE_CARLO",
        "topic": "Conditioned Evaluation Contracts",
        "inspection_focus": "Verify regime, stress, and Monte Carlo contract links are correctly wired.",
        "mandatory": True,
    },
    {
        "review_id": "REV_06_METRIC_PLACEHOLDERS",
        "topic": "Uncalculated Metric Placeholders",
        "inspection_focus": "Inspect all placeholders to verify actual_value is None and zero calculation occurs.",
        "mandatory": True,
    },
    {
        "review_id": "REV_07_CLAIM_APPROVAL_GUARDS",
        "topic": "Claim and Strategy Approval Guards",
        "inspection_focus": "Ensure all result/performance claims and capital allocation requests are blocked.",
        "mandatory": True,
    },
    {
        "review_id": "REV_08_DISABLED_EXECUTION_REPORTS",
        "topic": "Disabled Execution Enforcements",
        "inspection_focus": "Audit the 11 disabled execution reports for complete perimeter coverage.",
        "mandatory": True,
    },
    {
        "review_id": "REV_09_SOURCE_PRESERVATION",
        "topic": "Source Preservation & Metadata News",
        "inspection_focus": "Confirm raw data files are untouched and news bodies/embeddings are rejected.",
        "mandatory": True,
    },
    {
        "review_id": "REV_10_PHASE_152_HANDOFF_BLOCKERS",
        "topic": "Phase 152 Acceptance Handoff Prerequisites",
        "inspection_focus": "Verify all 10 handoff prerequisites are satisfied without operational leakage.",
        "mandatory": True,
    },
]


def build_benchmark_evaluation_manual_review_queue(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of manual review items."""
    rows: List[Dict[str, Any]] = []

    for g in MANUAL_REVIEW_GATES:
        rows.append(
            {
                "review_id": g["review_id"],
                "topic": g["topic"],
                "inspection_focus": g["inspection_focus"],
                "status": "PENDING_OPERATOR_REVIEW",
                "mandatory": g["mandatory"],
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_FINDING_DOMAIN,
        "total_review_items": len(df),
        "all_mandatory": bool(df["mandatory"].all()) if not df.empty else True,
        "pending_count": len(df),
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
