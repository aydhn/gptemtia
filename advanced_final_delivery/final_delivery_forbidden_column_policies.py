# -*- coding: utf-8 -*-
"""Phase 160: Final Delivery Forbidden Column Policies.

Enforces strict bans on forbidden columns including signals, targets, future returns,
leakage terms, raw HTML/text, embeddings, and credentials.
"""

from typing import Dict, List, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_BOUNDARY_DOMAIN,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
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
    "live_signal",
    "broker_order",
    "order_quantity",
    "portfolio_weight",
    "allocation",
    "position_size",
    "risk_budget",
    "scenario_pnl",
    "actual_drawdown",
    "var",
    "expected_shortfall",
    "performance_claim",
    "strategy_approved",
    "portfolio_approved",
    "production_ready",
    "broker_ready",
    "live_ready",
    "official_approval",
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
    "api_key",
    "token",
    "secret",
]


def build_final_delivery_forbidden_column_policy_registry(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build forbidden column policy DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    rows = []
    for col_name in FORBIDDEN_COLUMNS:
        rows.append({
            "forbidden_column": col_name,
            "prohibited": True,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "domain": FINAL_BOUNDARY_DOMAIN,
            "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "active_profile": active_profile.profile_name,
        "forbidden_column_count": len(rows),
        "all_prohibited": True,
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
    }
    return df, summary


def validate_final_delivery_forbidden_columns(column_names: List[str]) -> dict:
    """Validate a list of column names against forbidden policies."""
    violations = []
    col_names_lower = [str(c).lower().strip() for c in column_names]

    for col in col_names_lower:
        for f_col in FORBIDDEN_COLUMNS:
            if col == f_col or col.startswith(f"{f_col}_") or col.endswith(f"_{f_col}"):
                violations.append(col)
                break

    valid = len(violations) == 0
    return {
        "valid": valid,
        "violations": violations,
        "violation_count": len(violations),
        "status": FULL_ADVANCED_BOT_FINAL_DELIVERY_READY if valid else "FORBIDDEN_COLUMNS_DETECTED",
    }
