# -*- coding: utf-8 -*-
"""Phase 147: Validation Forbidden Column Policies.

Policies defining and strictly detecting forbidden columns (signals, future returns,
targets, predictions, performance claims, full text, embeddings).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

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
    "oos_performance",
    "actual_sharpe",
    "actual_win_rate",
    "benchmark_alpha",
    "alpha_claim",
    "performance_claim",
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


def build_validation_forbidden_column_policy_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for forbidden column policy registry."""
    rows = []
    for col in FORBIDDEN_COLUMNS:
        rows.append(
            {
                "forbidden_column": col,
                "policy_level": "STRICT_FORBIDDEN",
                "action": "BLOCK_EXECUTION",
                "enforced": True,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_forbidden_columns": len(df),
        "all_enforced": True,
        "non_signal": True,
    }
    return df, summary


def validate_validation_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Check list of column names against forbidden list."""
    violations = []
    for col in column_names:
        c_clean = col.lower().strip()
        for forbidden in FORBIDDEN_COLUMNS:
            if forbidden == c_clean or forbidden in c_clean.split("_"):
                violations.append(col)
                break
    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violating_columns": violations,
        "total_columns_checked": len(column_names),
        "message": "Gecerli kolonlar" if is_valid else f"Yasakli kolonlar tespit edildi: {violations}",
        "non_signal": True,
    }
