# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Findings registry builder.

Manages audit findings and governance notifications for ML dataset contracts.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_models import (
    MlDatasetFinding,
)

BASE_FINDINGS = [
    {
        "finding_id": "FIND-137-01",
        "finding_type": "materialization_request_blocked",
        "dataset_domain": "dataset_contract_domain",
        "severity_label": "INFO",
        "message": "Physical dataset materialization is prohibited in Phase 137 by design.",
        "recommendation": "Maintain contracts as metadata schemas only.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
    {
        "finding_id": "FIND-137-02",
        "finding_type": "target_label_request_blocked",
        "dataset_domain": "target_label_disabled_policy_domain",
        "severity_label": "INFO",
        "message": "Target and label generation are blocked by contract; no forward returns permitted.",
        "recommendation": "Enforce target-label disabled policy until future phases.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
    {
        "finding_id": "FIND-137-03",
        "finding_type": "training_request_blocked",
        "dataset_domain": "training_harness_disabled_domain",
        "severity_label": "INFO",
        "message": "Model training harness is disabled in Phase 137; deferred to Phase 138 dry-run harness.",
        "recommendation": "Preserve zero-training invariants throughout Phase 137.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
    {
        "finding_id": "FIND-137-04",
        "finding_type": "prediction_request_blocked",
        "dataset_domain": "prediction_disabled_domain",
        "severity_label": "INFO",
        "message": "Model inference and prediction execution are strictly disabled.",
        "recommendation": "Ensure no forward inferences or signals are produced.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
    {
        "finding_id": "FIND-137-05",
        "finding_type": "artifact_persistence_blocked",
        "dataset_domain": "artifact_disabled_domain",
        "severity_label": "INFO",
        "message": "Model registry writes and binary artifact persistence are prohibited.",
        "recommendation": "Only persist audit and contract governance metadata.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
    {
        "finding_id": "FIND-137-06",
        "finding_type": "phase_138_readiness_blocker",
        "dataset_domain": "phase_138_handoff_domain",
        "severity_label": "INFO",
        "message": "Phase 138 dry-run training harness requires explicit non-signal handoff acceptance.",
        "recommendation": "Review handoff deliverables and verify compliance.",
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_forbidden": True,
    },
]


def create_ml_dataset_finding(
    finding_type: str,
    dataset_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> MlDatasetFinding:
    """Create a structured audit finding item."""
    import uuid
    f_id = f"FIND-{uuid.uuid4().hex[:6].upper()}"
    return MlDatasetFinding(
        finding_id=f_id,
        finding_type=finding_type,
        dataset_domain=dataset_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
        auto_fix_forbidden=True,
    )


def build_ml_dataset_findings_registry(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for ML dataset findings."""
    p = profile or get_default_advanced_ml_dataset_profile()
    df = pd.DataFrame(BASE_FINDINGS)
    summary = summarize_ml_dataset_findings(df)
    return df, summary


def summarize_ml_dataset_findings(df: pd.DataFrame) -> Dict:
    """Summarize dataset findings."""
    critical_count = int((df["severity_label"] == "CRITICAL").sum()) if "severity_label" in df.columns else 0
    warning_count = int((df["severity_label"] == "WARNING").sum()) if "severity_label" in df.columns else 0
    info_count = int((df["severity_label"] == "INFO").sum()) if "severity_label" in df.columns else 0
    return {
        "total_findings": len(df),
        "critical_findings": critical_count,
        "warning_findings": warning_count,
        "info_findings": info_count,
        "manual_review_required": True,
        "non_signal": True,
        "auto_fix_allowed": False,
    }
