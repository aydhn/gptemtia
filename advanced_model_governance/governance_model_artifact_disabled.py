# -*- coding: utf-8 -*-
"""Phase 144: Governance Model Artifact Disabled Report."""

from typing import Any, Dict, List, Optional, Tuple, Union
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

FORBIDDEN_ARTIFACT_TERMS = [
    "save_model",
    "pickle",
    "joblib.dump",
    "torch.save",
    "onnx_export",
]


def build_governance_model_artifact_disabled_report(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for disabled artifact persistence."""
    prof = profile or get_model_governance_profile()
    records = [
        {"action": "save_model_weights", "is_disabled": True, "reason": "Model weight serialization is permanently disabled."},
        {"action": "pickle_dump", "is_disabled": True, "reason": "Pickle serialization of models is prohibited."},
        {"action": "joblib_dump", "is_disabled": True, "reason": "Joblib artifact dumping is prohibited."},
    ]
    for r in records:
        r["status"] = "BLOCKED_BY_POLICY"
        r["phase"] = prof.current_phase

    df = pd.DataFrame(records)
    summary = summarize_governance_model_artifact_disabled(df)
    return df, summary


def summarize_governance_model_artifact_disabled(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model artifact disabled report."""
    return {
        "total_checks": len(df),
        "all_disabled": bool(df["is_disabled"].all()),
        "status": "ARTIFACT_DISABLED_ENFORCED",
    }


def validate_no_model_artifact_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate and intercept any model artifact persistence requests."""
    req_str = str(request).lower()
    violation = any(term in req_str for term in FORBIDDEN_ARTIFACT_TERMS)
    return {
        "request": str(request),
        "allowed": False,
        "blocked": True,
        "violation_detected": violation,
        "status": "BLOCKED_BY_POLICY",
        "message": "Model artifact persistence is prohibited.",
    }
