# -*- coding: utf-8 -*-
"""Phase 151: Evaluation Forbidden Column Policies Module.

Comprehensive policy and quarantine engine rejecting forbidden columns across
signals, predictions, lookahead returns, claims, approvals, news text, and embeddings.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_CLAIM_GUARD_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

FORBIDDEN_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    "actual_sharpe",
    "actual_win_rate",
    "actual_alpha",
    "actual_beta",
    "actual_return",
    "actual_drawdown",
    "information_ratio",
    "actual_information_ratio",
    "performance_claim",
    "result_claim",
    "strategy_approved",
    "approved_strategy",
    "capital_allocation",
    "portfolio_construction",
    "position_sizing",
    "production_ready",
    "broker_ready",
    "leak",
    "leakage",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "page_html",
    "html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_evaluation_forbidden_column_policy_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of forbidden column policies."""
    rows: List[Dict[str, Any]] = []

    for col in FORBIDDEN_COLUMNS:
        rows.append(
            {
                "forbidden_column": col,
                "policy": "STRICT_PROHIBITION_AND_QUARANTINE",
                "reason": "Prevents signals, claims, leakage, or unapproved execution",
                "is_enforced": True,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_CLAIM_GUARD_DOMAIN,
        "total_forbidden_columns": len(df),
        "all_enforced": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary


def validate_evaluation_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect column names against the forbidden column policy list."""
    detected: List[str] = []
    for col in column_names:
        c_lower = str(col).lower()
        for forbidden in FORBIDDEN_COLUMNS:
            if c_lower == forbidden or c_lower.startswith(f"{forbidden}_") or c_lower.endswith(f"_{forbidden}"):
                detected.append(col)
                break

    is_clean = len(detected) == 0
    return {
        "is_clean": is_clean,
        "violations_count": len(detected),
        "detected_columns": detected,
        "status": "PASS" if is_clean else "BLOCKED_BY_FORBIDDEN_COLUMN_POLICY",
        "policy_action": "ALLOW" if is_clean else "QUARANTINE_OR_REJECT",
        "non_signal": True,
    }
