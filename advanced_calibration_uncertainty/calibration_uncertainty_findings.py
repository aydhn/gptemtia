# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Findings Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)
from advanced_calibration_uncertainty.calibration_uncertainty_models import (
    CalibrationUncertaintyFinding,
)

FINDING_TYPES = [
    "missing_calibration_contract",
    "missing_uncertainty_contract",
    "missing_candidate_dependency",
    "missing_ensemble_dependency",
    "missing_dataset_dependency",
    "missing_quality_gate",
    "probability_prediction_request_blocked",
    "calibration_fit_request_blocked",
    "calibration_transform_request_blocked",
    "uncertainty_estimation_request_blocked",
    "prediction_interval_request_blocked",
    "conformal_prediction_request_blocked",
    "metric_calculation_request_blocked",
    "artifact_request_blocked",
    "phase_142_readiness_blocker",
]

DEFAULT_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FIND_CALIB_001",
        "finding_type": "probability_prediction_request_blocked",
        "calibration_domain": "probability_prediction_disabled_domain",
        "severity_label": "INFO",
        "message": "Probability prediction execution blocked by policy; zero probabilities generated.",
        "recommendation": "Maintain strict non-execution policy during contract phase.",
    },
    {
        "finding_id": "FIND_UNCERT_002",
        "finding_type": "uncertainty_estimation_request_blocked",
        "calibration_domain": "uncertainty_execution_disabled_domain",
        "severity_label": "INFO",
        "message": "Uncertainty estimation execution blocked by policy; zero intervals computed.",
        "recommendation": "Inspect uncertainty method placeholders for Phase 142 drift readiness.",
    },
    {
        "finding_id": "FIND_AUDIT_003",
        "finding_type": "metric_calculation_request_blocked",
        "calibration_domain": "calibration_metric_placeholder_domain",
        "severity_label": "INFO",
        "message": "Calibration and uncertainty metrics are uncalculated placeholders.",
        "recommendation": "Perform manual review of metric formulas prior to evaluation phase.",
    },
]


def create_calibration_uncertainty_finding(
    finding_type: str,
    calibration_domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> CalibrationUncertaintyFinding:
    """Create a new finding item."""
    finding_id = f"FIND_{abs(hash(finding_type + message)) % 100000:05d}"
    return CalibrationUncertaintyFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        calibration_domain=calibration_domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
        non_signal=True,
    )


def build_calibration_uncertainty_findings_registry(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for calibration and uncertainty findings."""
    prof = profile or get_calibration_uncertainty_profile()
    rows = []
    for item in DEFAULT_FINDINGS:
        rows.append(
            {
                "finding_id": item["finding_id"],
                "finding_type": item["finding_type"],
                "calibration_domain": item["calibration_domain"],
                "severity_label": item["severity_label"],
                "message": item["message"],
                "recommendation": item["recommendation"],
                "manual_review_required": True,
                "is_critical": (item["severity_label"] == "CRITICAL"),
                "non_signal": True,
                "phase": prof.current_phase,
            }
        )

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_findings(df)
    return df, summary


def summarize_calibration_uncertainty_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize findings DataFrame."""
    critical_count = int(df["is_critical"].sum()) if not df.empty else 0
    return {
        "total_findings": len(df),
        "critical_findings": critical_count,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "manual_review_items": int(df["manual_review_required"].sum()) if not df.empty else 0,
    }
