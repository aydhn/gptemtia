# -*- coding: utf-8 -*-
"""Phase 144: Governance Model Registry Write Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_REGISTRY_TERMS = [
    "write_model_registry",
    "mlflow",
    "register_model",
    "publish_model",
    "log_model",
]


def build_governance_model_registry_write_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled model registry writes."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "write_model_registry", "is_disabled": True, "reason": "Model registry write permanently blocked in non-production layer."},
        {"action": "mlflow_logging", "is_disabled": True, "reason": "External tracking / registry services are disabled."},
        {"action": "publish_model_weights", "is_disabled": True, "reason": "Zero weight materialization or export permitted."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_model_registry_write_disabled(df)
    return df, summary


def summarize_governance_model_registry_write_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model registry write disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "WRITE_DISABLED_ENFORCED",
    }


def validate_no_model_registry_write_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any model registry write requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_REGISTRY_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Model registry writes are prohibited.",
    }
