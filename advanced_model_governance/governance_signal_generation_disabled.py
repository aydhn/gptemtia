# -*- coding: utf-8 -*-
"""Phase 144: Governance Signal Generation Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_SIGNAL_TERMS = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "recommendation",
]


def build_governance_signal_generation_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled signal generation."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "generate_signal", "is_disabled": True, "reason": "Signal generation is strictly disabled in governance phase."},
        {"action": "recommend_position", "is_disabled": True, "reason": "Trading recommendations are prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_signal_generation_disabled(df)
    return df, summary


def summarize_governance_signal_generation_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize signal generation disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "SIGNAL_GENERATION_DISABLED_ENFORCED",
    }


def validate_no_governance_signal_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any signal generation requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_SIGNAL_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Signal generation is prohibited in governance phase.",
    }
