# -*- coding: utf-8 -*-
"""Phase 154: Forbidden Column Policies.

Enforces quarantine on 52 forbidden column names to prevent signal leakage,
actual optimization weights, live orders, credentials, and full news text.
"""

from typing import Dict, List, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

FORBIDDEN_COLUMNS_LIST = [
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
    "actual_weight",
    "optimized_weight",
    "optimal_weight",
    "target_weight",
    "portfolio_weight",
    "allocation",
    "actual_allocation",
    "rebalance",
    "rebalance_order",
    "order_quantity",
    "position_size",
    "capital_allocation",
    "objective_value",
    "solver_result",
    "efficient_frontier",
    "risk_budget",
    "exposure_limit",
    "leverage",
    "margin",
    "investment_advice",
    "performance_claim",
    "strategy_approved",
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


def build_optimization_forbidden_column_policy_registry(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build forbidden column quarantine policy registry."""
    records = []
    for col in FORBIDDEN_COLUMNS_LIST:
        records.append({
            "forbidden_column_name": col,
            "policy_action": "QUARANTINE_AND_DROP",
            "is_active": True,
            "local_only": True,
            "non_production": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "forbidden_column_count": len(records),
        "policy_action_default": "QUARANTINE_AND_DROP",
        "all_policies_active": True,
    }
    return df, summary


def validate_optimization_forbidden_columns(column_names: List[str]) -> Dict:
    """Detect and report forbidden column names in a dataset."""
    detected = [c for c in column_names if c.lower() in [f.lower() for f in FORBIDDEN_COLUMNS_LIST]]
    return {
        "is_clean": len(detected) == 0,
        "detected_columns": detected,
        "forbidden_count": len(detected),
        "status": "VALIDATION_PASS" if len(detected) == 0 else "VALIDATION_FAIL_FORBIDDEN_COLUMNS",
    }


FORBIDDEN_OPTIMIZATION_COLUMNS = FORBIDDEN_COLUMNS_LIST


def is_forbidden_optimization_column(column_name: str) -> bool:
    """Check if a column name is in the forbidden optimization quarantine list."""
    col_lower = column_name.lower().strip()
    return col_lower in [f.lower() for f in FORBIDDEN_COLUMNS_LIST]

