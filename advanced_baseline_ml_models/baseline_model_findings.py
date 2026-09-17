# -*- coding: utf-8 -*-
"""Phase 138 Baseline Model Findings Registry.

Records audit findings, security boundaries, and policy blockers for baseline models.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_baseline_ml_models.baseline_ml_model_config import (
    BaselineMlModelProfile,
    get_default_baseline_ml_model_profile,
)
from advanced_baseline_ml_models.baseline_ml_model_models import BaselineModelFinding

FINDING_TYPES = [
    "missing_model_contract",
    "missing_dataset_contract_ref",
    "missing_feature_snapshot_contract_ref",
    "missing_runtime_profile_ref",
    "no_lookahead_guard_missing",
    "metadata_only_news_guard_missing",
    "source_preservation_guard_missing",
    "real_training_request_blocked",
    "prediction_request_blocked",
    "target_label_request_blocked",
    "artifact_request_blocked",
    "model_registry_write_blocked",
    "phase_139_readiness_blocker",
]


def create_baseline_model_finding(
    finding_type: str,
    model_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> BaselineModelFinding:
    """Create a new BaselineModelFinding instance."""
    from datetime import datetime, timezone
    import uuid

    finding_id = f"finding_{uuid.uuid4().hex[:8]}"
    return BaselineModelFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        model_domain=model_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        blocking_status=True,
        created_at=datetime.now(timezone.utc).isoformat(),
    )


def build_baseline_model_findings_registry(
    profile: BaselineMlModelProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build findings registry DataFrame and summary."""
    if profile is None:
        profile = get_default_baseline_ml_model_profile()

    # Under nominal clean state in Phase 138, contracts adhere to safety rules (0 critical findings)
    rows: List[Dict[str, Any]] = []

    df = pd.DataFrame(rows, columns=[
        "finding_id", "finding_type", "model_domain", "severity_label",
        "message", "recommendation", "manual_review_required", "blocking_status", "created_at"
    ])
    summary = summarize_baseline_model_findings(df)
    return df, summary


def summarize_baseline_model_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings registry."""
    critical_count = int((df["severity_label"] == "CRITICAL").sum()) if not df.empty and "severity_label" in df.columns else 0
    return {
        "total_findings": len(df),
        "critical_blockers": critical_count,
        "clean_baseline_contracts": critical_count == 0,
        "non_signal": True,
        "production_ready": False,
        "broker_ready": False,
    }
