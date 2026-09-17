# -*- coding: utf-8 -*-
"""Phase 139 GPU Training Readiness Scoring."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_gpu_training_governance.gpu_training_governance_config import (
    GpuTrainingGovernanceProfile,
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_governance_models import (
    GpuTrainingReadinessScore,
)


def classify_gpu_training_readiness_score(score: float) -> str:
    """Classify readiness score into governance tiers."""
    if score >= 0.85:
        return "READY_FOR_GPU_RESOURCE_GOVERNANCE_DRY_RUN"
    elif score >= 0.70:
        return "READY_WITH_MONITORED_POLICIES"
    elif score >= 0.45:
        return "READY_WITH_REVIEW_REQUIRED"
    return "BLOCKED_BY_GOVERNANCE_GAPS"


def calculate_gpu_training_readiness_score(
    findings_df: pd.DataFrame, profile: Optional[GpuTrainingGovernanceProfile] = None
) -> GpuTrainingReadinessScore:
    """Calculate readiness score based on findings and profile constraints."""
    active_profile = profile or get_default_gpu_training_governance_profile()

    base_score = 1.0
    deductions = 0.0

    if not findings_df.empty and "severity_label" in findings_df.columns:
        critical_count = int((findings_df["severity_label"] == "CRITICAL").sum())
        high_count = int((findings_df["severity_label"] == "HIGH").sum())
        medium_count = int((findings_df["severity_label"] == "MEDIUM").sum())

        deductions += critical_count * 0.30
        deductions += high_count * 0.15
        deductions += medium_count * 0.05

    final_score = max(0.0, min(1.0, base_score - deductions))
    classification = classify_gpu_training_readiness_score(final_score)
    meets_threshold = final_score >= active_profile.min_readiness_score

    return GpuTrainingReadinessScore(
        score=round(final_score, 4),
        classification=classification,
        meets_threshold=meets_threshold,
        current_phase=139,
        target_final_phase=160,
        next_phase=140,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        official_approval=False,
        real_training_approved=False,
        performance_claim_generated=False,
        details={
            "base_score": base_score,
            "deductions": round(deductions, 4),
            "min_required_score": active_profile.min_readiness_score,
        },
    )


def build_gpu_training_readiness_score_report(
    profile: Optional[GpuTrainingGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build readiness score report DataFrame and summary."""
    active_profile = profile or get_default_gpu_training_governance_profile()
    from advanced_gpu_training_governance.gpu_training_findings import (
        build_gpu_training_findings_registry,
    )

    findings_df, _ = build_gpu_training_findings_registry(active_profile)
    readiness = calculate_gpu_training_readiness_score(findings_df, active_profile)

    rows = [
        {
            "score": readiness.score,
            "classification": readiness.classification,
            "meets_threshold": readiness.meets_threshold,
            "current_phase": readiness.current_phase,
            "target_final_phase": readiness.target_final_phase,
            "next_phase": readiness.next_phase,
            "non_signal": True,
            "production_ready": False,
            "broker_ready": False,
            "official_approval": False,
            "real_training_approved": False,
            "performance_claim_generated": False,
            "active_profile": active_profile.name,
        }
    ]

    df = pd.DataFrame(rows)
    summary = summarize_gpu_training_readiness_scores(df)
    summary["active_profile"] = active_profile.name
    return df, summary


def summarize_gpu_training_readiness_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize readiness scores DataFrame."""
    if df.empty:
        return {"readiness_score": 0.0, "meets_threshold": False, "non_signal": True}
    row = df.iloc[0]
    return {
        "readiness_score": float(row.get("score", 0.0)),
        "classification": str(row.get("classification", "UNKNOWN")),
        "meets_threshold": bool(row.get("meets_threshold", False)),
        "production_ready": False,
        "broker_ready": False,
        "real_training_approved": False,
        "current_phase": 139,
        "non_signal": True,
    }
