# -*- coding: utf-8 -*-
"""Phase 141: Calibration & Uncertainty Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_calibration_uncertainty.calibration_uncertainty_config import (
    CalibrationUncertaintyProfile,
    get_calibration_uncertainty_profile,
)
from advanced_calibration_uncertainty.calibration_uncertainty_models import (
    CalibrationUncertaintyReadinessScore,
)
from advanced_calibration_uncertainty.calibration_uncertainty_findings import (
    build_calibration_uncertainty_findings_registry,
)


def classify_calibration_uncertainty_readiness_score(score: float) -> str:
    """Classify readiness score into governance state."""
    if score >= 0.85:
        return "READY_FOR_PHASE_142_DRIFT_MONITORING_HANDOFF"
    elif score >= 0.60:
        return "READY_FOR_CALIBRATION_UNCERTAINTY_DRY_RUN"
    elif score >= 0.45:
        return "READY_WITH_RESERVATIONS"
    return "BLOCKED_BY_GOVERNANCE"


def calculate_calibration_uncertainty_readiness_score(
    findings_df: Optional[pd.DataFrame] = None,
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> CalibrationUncertaintyReadinessScore:
    """Calculate composite readiness score bounded in [0.0, 1.0]."""
    prof = profile or get_calibration_uncertainty_profile()
    if findings_df is None:
        findings_df, _ = build_calibration_uncertainty_findings_registry(prof)

    total_findings = len(findings_df)
    critical_blockers = int(findings_df["is_critical"].sum()) if not findings_df.empty and "is_critical" in findings_df.columns else 0

    base_score = 1.0
    deduction = critical_blockers * 0.30
    final_score = max(0.0, min(1.0, base_score - deduction))

    meets_threshold = bool(final_score >= prof.min_readiness_score)
    classification = classify_calibration_uncertainty_readiness_score(final_score)

    return CalibrationUncertaintyReadinessScore(
        readiness_score=final_score,
        classification=classification,
        meets_threshold=meets_threshold,
        total_findings=total_findings,
        critical_blockers=critical_blockers,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        official_approval=False,
    )


def build_calibration_uncertainty_readiness_score_report(
    profile: Optional[CalibrationUncertaintyProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build report DataFrame and summary for readiness score."""
    prof = profile or get_calibration_uncertainty_profile()
    score_obj = calculate_calibration_uncertainty_readiness_score(profile=prof)

    rows = [
        {
            "readiness_score": score_obj.readiness_score,
            "classification": score_obj.classification,
            "meets_threshold": score_obj.meets_threshold,
            "min_threshold": prof.min_readiness_score,
            "total_findings": score_obj.total_findings,
            "critical_blockers": score_obj.critical_blockers,
            "non_signal": score_obj.non_signal,
            "production_ready": score_obj.production_ready,
            "broker_ready": score_obj.broker_ready,
            "official_approval": score_obj.official_approval,
            "phase": prof.current_phase,
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_calibration_uncertainty_readiness_scores(df)
    return df, summary


def summarize_calibration_uncertainty_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness score DataFrame."""
    if df.empty:
        return {"readiness_score": 0.0, "meets_threshold": False, "classification": "EMPTY"}
    row = df.iloc[0]
    return {
        "readiness_score": float(row["readiness_score"]),
        "classification": str(row["classification"]),
        "meets_threshold": bool(row["meets_threshold"]),
        "production_ready": bool(row["production_ready"]),
        "broker_ready": bool(row["broker_ready"]),
        "all_non_signal": bool(df["non_signal"].all()),
    }
