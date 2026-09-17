# -*- coding: utf-8 -*-
"""Phase 155: Risk Reporting Forbidden Column Policies."""

from typing import Any, Dict, List, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile
from .risk_reporting_models import RiskReportingGuardItem


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
    "actual_risk_report",
    "actual_exposure",
    "exposure_value",
    "gross_exposure",
    "net_exposure",
    "concentration_ratio",
    "leverage",
    "margin",
    "var",
    "expected_shortfall",
    "actual_var",
    "actual_expected_shortfall",
    "limit_breach",
    "breach_alert",
    "risk_alert",
    "live_alert",
    "dashboard",
    "portfolio_adjustment",
    "rebalance",
    "hedge",
    "de_risk",
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


def build_risk_reporting_forbidden_column_policy_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for forbidden column policy."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = []
    for c in FORBIDDEN_COLUMNS:
        rows.append({
            "forbidden_column": c,
            "policy": "STRICT_BLOCK",
            "reason": "Forbidden in Phase 155 contract layer",
            "current_phase": profile.current_phase,
            "target_final_phase": profile.target_final_phase,
            "next_phase": profile.next_phase,
        })
    df = pd.DataFrame(rows)
    return df, {"forbidden_column_count": len(df), "all_blocked": True}


def validate_risk_reporting_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that given list of columns contains no forbidden terms."""
    violations = []
    for col in column_names:
        c_lower = col.lower()
        if any(f == c_lower or f"_{f}" in c_lower or f"{f}_" in c_lower for f in FORBIDDEN_COLUMNS):
            violations.append(col)

    return {
        "is_valid": len(violations) == 0,
        "violations": violations,
        "action": "BLOCK" if violations else "ALLOW",
    }
