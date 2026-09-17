# -*- coding: utf-8 -*-
"""Phase 149: Monte Carlo Forbidden Column Policies Module.

Defines the comprehensive list of forbidden column names to quarantine signals,
targets, predictions, future leaks, actual Monte Carlo returns, and raw text.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_monte_carlo_robustness.monte_carlo_config import MonteCarloProfile
from advanced_monte_carlo_robustness.monte_carlo_labels import (
    BIAS_GUARD_DOMAIN,
    MONTE_CARLO_CONTRACT_READY,
)

FORBIDDEN_COLUMNS = [
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
    "monte_carlo_return",
    "actual_monte_carlo_return",
    "monte_carlo_drawdown",
    "actual_monte_carlo_drawdown",
    "monte_carlo_sharpe",
    "monte_carlo_win_rate",
    "actual_var",
    "actual_expected_shortfall",
    "parameter_optimum",
    "optimized_parameter",
    "best_parameter",
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


def validate_monte_carlo_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Inspect column names against the quarantine policy."""
    violations: List[str] = []
    for col in column_names:
        col_clean = str(col).strip().lower()
        if col_clean in FORBIDDEN_COLUMNS:
            violations.append(col)
        else:
            for f in FORBIDDEN_COLUMNS:
                if f in col_clean:
                    violations.append(col)
                    break

    # deduplicate
    violations = sorted(list(set(violations)))
    return {
        "valid": len(violations) == 0,
        "violations": violations,
        "violations_count": len(violations),
        "status": "PASS" if len(violations) == 0 else "FAIL_FORBIDDEN_COLUMNS_DETECTED",
    }


def build_monte_carlo_forbidden_column_policy_registry(
    profile: MonteCarloProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the forbidden column policy registry DataFrame and summary."""
    rows: List[Dict[str, Any]] = []
    for col in FORBIDDEN_COLUMNS:
        rows.append(
            {
                "forbidden_column": col,
                "policy": "STRICT_QUARANTINE",
                "reason": "Prevents signals, targets, lookahead, actual metrics, or raw text leaks.",
                "profile_name": profile.profile_name,
                "current_phase": profile.current_phase,
                "status": "ACTIVE",
                "domain": BIAS_GUARD_DOMAIN,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "domain": BIAS_GUARD_DOMAIN,
        "total_forbidden_columns": len(df),
        "all_active": True,
        "profile_name": profile.profile_name,
        "status": MONTE_CARLO_CONTRACT_READY,
    }
    return df, summary
