# -*- coding: utf-8 -*-
"""Phase 158: Forbidden Column System Policies.

Maintains the system-wide blacklist of prohibited columns (signals, lookahead, leaks, credentials).
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile

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


def build_forbidden_column_system_policy_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build forbidden column system policy DataFrame and summary."""
    records = []
    for idx, col in enumerate(FORBIDDEN_COLUMNS, start=1):
        category = "leakage" if "future" in col or "lookahead" in col or "pnl" in col else (
            "signal" if col in ["signal", "buy", "sell", "long", "short", "position", "recommendation", "live_signal"] else (
                "ml_target" if col in ["target", "label", "prediction"] else (
                    "portfolio_risk" if col in ["order_quantity", "portfolio_weight", "allocation", "position_size", "risk_budget", "scenario_pnl", "actual_drawdown", "var", "expected_shortfall"] else (
                        "claim_approval" if col in ["performance_claim", "strategy_approved", "portfolio_approved", "production_ready", "broker_ready", "live_ready"] else (
                            "security" if col in ["api_key", "token", "secret"] else "content_heavy"
                        )
                    )
                )
            )
        )
        records.append({
            "policy_id": f"FCP-{idx:03d}",
            "column_name": col,
            "category": category,
            "is_forbidden": True,
            "status": "ENFORCED",
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": profile.profile_name,
        "total_forbidden_columns": len(df),
        "all_enforced": bool(df["is_forbidden"].all()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary


def validate_system_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate whether provided column names contain any forbidden items."""
    found_forbidden = []
    lower_map = {c.lower(): c for c in column_names}

    for f_col in FORBIDDEN_COLUMNS:
        if f_col in lower_map:
            found_forbidden.append(lower_map[f_col])

    is_clean = len(found_forbidden) == 0
    return {
        "is_clean": is_clean,
        "forbidden_columns_found": found_forbidden,
        "total_checked": len(column_names),
        "non_signal": True,
    }
