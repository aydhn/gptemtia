# -*- coding: utf-8 -*-
"""Phase 150: Backtest Forbidden Column Policies.

Enforces absolute prohibition against columns representing trade signals,
future returns, calculated actual performance metrics, approval claims,
and raw unstructured text/embeddings.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_backtest_governance.backtest_governance_config import BacktestGovernanceProfile
from advanced_backtest_governance.backtest_governance_labels import (
    SAFETY_DOMAIN,
    STATUS_GOVERNANCE_CONTRACT_READY,
)

FORBIDDEN_COLUMNS: List[str] = [
    # Signals and trade recommendations
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
    # Lookahead and future returns
    "future_return",
    "forward_return",
    "next_return",
    "lookahead_return",
    "realized_future_pnl",
    "future_pnl",
    # Unrealistic execution assumptions
    "perfect_fill",
    "zero_cost",
    "zero_slippage",
    # Realized metric calculations
    "actual_sharpe",
    "actual_win_rate",
    "actual_alpha",
    "actual_return",
    "actual_drawdown",
    # Claims and approvals
    "performance_claim",
    "strategy_approved",
    "production_ready",
    "broker_ready",
    # Leakage markers
    "leak",
    "leakage",
    # Raw text / scraping / sentiment / embeddings
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


def validate_backtest_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate a list of column names against the forbidden column policy."""
    violating_columns: List[str] = []
    for col in column_names:
        c_clean = col.lower().strip()
        for forbidden in FORBIDDEN_COLUMNS:
            if forbidden == c_clean or forbidden in c_clean:
                violating_columns.append(col)
                break

    is_clean = len(violating_columns) == 0
    return {
        "is_clean": is_clean,
        "is_blocked": not is_clean,
        "violating_columns": violating_columns,
        "decision": "PASS" if is_clean else "BLOCKED_BY_FORBIDDEN_COLUMN_POLICY",
        "policy_message": (
            "Forbidden column audit passed cleanly."
            if is_clean
            else f"Forbidden columns detected: {violating_columns}. Operation blocked by safety policy."
        ),
        "non_signal": True,
    }


def build_backtest_forbidden_column_policy_registry(
    profile: BacktestGovernanceProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for forbidden column policies."""
    rows: List[Dict[str, Any]] = []
    for col in FORBIDDEN_COLUMNS:
        rows.append({
            "column_name": col,
            "policy": "STRICTLY_FORBIDDEN",
            "enforcement": "BLOCKING_ZERO_TOLERANCE",
            "non_signal": True,
            "local_only": True,
            "phase": profile.current_phase,
        })
    df = pd.DataFrame(rows)
    summary = {
        "domain": SAFETY_DOMAIN,
        "subdomain": "forbidden_column_policies",
        "total_forbidden_columns": len(df),
        "all_strictly_forbidden": True,
        "status": STATUS_GOVERNANCE_CONTRACT_READY,
        "non_signal": True,
        "local_only": True,
    }
    return df, summary
