# -*- coding: utf-8 -*-
"""Phase 153: Portfolio Forbidden Column Policies Module.

Defines forbidden column names and patterns for portfolio construction datasets.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from .portfolio_construction_config import PortfolioConstructionProfile
from .portfolio_construction_labels import (
    PORTFOLIO_GUARD_DOMAIN,
    PORTFOLIO_CONTRACT_READY,
)

FORBIDDEN_PORTFOLIO_COLUMNS = [
    "api_key",
    "secret_key",
    "access_token",
    "password",
    "broker_account_number",
    "broker_pin",
    "future_return",
    "forward_pnl",
    "live_order_id",
    "broker_order_response",
    "real_fill_price",
]


def build_portfolio_forbidden_column_policy_registry(
    profile: PortfolioConstructionProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of forbidden column policies."""
    rows = []
    for col in FORBIDDEN_PORTFOLIO_COLUMNS:
        rows.append({
            "forbidden_column_pattern": col,
            "policy_rule": "STRICT_FORBIDDEN",
            "reason": "Security credential, lookahead leakage, or live broker artifact.",
            "current_phase": profile.current_phase,
            "contract_only": True,
            "non_production": True,
            "is_enforced": True,
            "status": PORTFOLIO_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "domain": PORTFOLIO_GUARD_DOMAIN,
        "guard_category": "forbidden_column_policies",
        "active_profile": profile.profile_name,
        "total_forbidden_rules": len(df),
        "status": PORTFOLIO_CONTRACT_READY,
    }
    return df, summary


def validate_portfolio_forbidden_columns(columns: List[str]) -> Dict[str, Any]:
    """Check a list of columns against forbidden column policies."""
    violations = []
    for col in columns:
        c_low = str(col).lower()
        for forbidden in FORBIDDEN_PORTFOLIO_COLUMNS:
            if forbidden in c_low:
                violations.append(col)
                break

    is_clean = len(violations) == 0
    return {
        "is_clean": is_clean,
        "violations_detected": not is_clean,
        "violations": violations,
        "status": "PASS" if is_clean else "BLOCKED_BY_FORBIDDEN_COLUMN_POLICY",
        "contract_only": True,
    }
