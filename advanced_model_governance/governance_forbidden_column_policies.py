# -*- coding: utf-8 -*-
"""Phase 144: Governance Forbidden Column Policies."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

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
    "probability",
    "production_ready",
    "broker_ready",
    "approved",
    "live_trading_ready",
    "release_approved",
    "deployment_status",
    "model_registry_uri",
    "model_artifact_path",
    "performance_claim",
    "accuracy_claim",
    "sharpe_claim",
    "win_rate_claim",
    "future_return",
    "forward_return",
    "next_return",
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


def build_governance_forbidden_column_policy_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for forbidden column policies."""
    prof = profile or get_model_governance_profile()
    records = []
    for col in FORBIDDEN_COLUMNS_LIST:
        records.append({
            "forbidden_column": col,
            "policy_action": "DROP_OR_REJECT",
            "phase": prof.current_phase,
            "is_strictly_enforced": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_governance_forbidden_column_policies(df)
    return df, summary


def summarize_governance_forbidden_column_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize forbidden column policies."""
    return {
        "total_forbidden_columns": len(df),
        "all_strictly_enforced": bool(df["is_strictly_enforced"].all()),
        "status": "FORBIDDEN_COLUMN_POLICIES_ACTIVE",
    }


def validate_governance_forbidden_columns(column_names: List[str]) -> Dict[str, Any]:
    """Validate that given column names contain no forbidden columns."""
    violations = []
    for c in column_names:
        c_clean = str(c).lower().strip()
        if c_clean in FORBIDDEN_COLUMNS_LIST:
            violations.append(c)

    is_valid = len(violations) == 0
    return {
        "is_valid": is_valid,
        "violations": violations,
        "status": "PASS" if is_valid else "FAIL_FORBIDDEN_COLUMNS_FOUND",
    }
