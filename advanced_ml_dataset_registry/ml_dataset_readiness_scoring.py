# -*- coding: utf-8 -*-
"""
Phase 137 - Advanced ML Dataset Contracts and Experiment Registry
Readiness scoring module.

Calculates composite contract readiness score (0-1) for dataset governance.
The score is strictly a contract-completeness indicator, NOT a trade signal,
NOT a production approval, and NOT a training authorization.
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    AdvancedMlDatasetProfile,
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_models import (
    MlDatasetReadinessScore,
)


def classify_ml_dataset_readiness_score(score: float) -> str:
    """Classify the readiness score into descriptive governance category."""
    if score >= 0.85:
        return "READY_FOR_LOCAL_ML_CONTRACTS"
    elif score >= 0.65:
        return "CONTRACT_READY_WITH_WARNINGS"
    elif score >= 0.45:
        return "PLACEHOLDER_CONTRACTS_ACTIVE"
    else:
        return "BLOCKED_BY_SAFETY_CONTRACTS"


def calculate_ml_dataset_readiness_score(
    findings_df: pd.DataFrame,
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> MlDatasetReadinessScore:
    """Calculate composite readiness score based on findings and profile parameters."""
    p = profile or get_default_advanced_ml_dataset_profile()

    total_findings = len(findings_df) if findings_df is not None else 0
    critical_findings = 0
    warning_findings = 0

    if findings_df is not None and not findings_df.empty and "severity_label" in findings_df.columns:
        critical_findings = int((findings_df["severity_label"] == "CRITICAL").sum())
        warning_findings = int((findings_df["severity_label"] == "WARNING").sum())

    base_score = 1.0
    deduction = (critical_findings * 0.25) + (warning_findings * 0.10)
    score = max(0.0, min(1.0, base_score - deduction))

    label = classify_ml_dataset_readiness_score(score)

    return MlDatasetReadinessScore(
        score=score,
        label=label,
        total_findings=total_findings,
        critical_findings=critical_findings,
        warning_findings=warning_findings,
        non_signal=True,
        production_ready=False,
        broker_ready=False,
        training_approved=False,
        dataset_materialization_approved=False,
    )


def build_ml_dataset_readiness_score_report(
    profile: Optional[AdvancedMlDatasetProfile] = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build DataFrame and summary for the readiness score report."""
    p = profile or get_default_advanced_ml_dataset_profile()
    from advanced_ml_dataset_registry.ml_dataset_findings import (
        build_ml_dataset_findings_registry,
    )

    findings_df, _ = build_ml_dataset_findings_registry(p)
    readiness = calculate_ml_dataset_readiness_score(findings_df, p)

    row = {
        "readiness_score": readiness.score,
        "classification_label": readiness.label,
        "total_findings": readiness.total_findings,
        "critical_findings": readiness.critical_findings,
        "warning_findings": readiness.warning_findings,
        "min_required_score": getattr(p, "min_readiness_score", 0.45),
        "is_minimum_passed": readiness.score >= getattr(p, "min_readiness_score", 0.45),
        "non_signal": readiness.non_signal,
        "production_ready": readiness.production_ready,
        "broker_ready": readiness.broker_ready,
        "training_approved": readiness.training_approved,
        "dataset_materialization_approved": readiness.dataset_materialization_approved,
    }

    df = pd.DataFrame([row])
    summary = summarize_ml_dataset_readiness_scores(df)
    return df, summary


def summarize_ml_dataset_readiness_scores(df: pd.DataFrame) -> Dict:
    """Summarize readiness score DataFrame."""
    first_row = df.iloc[0].to_dict() if not df.empty else {}
    return {
        "readiness_score": first_row.get("readiness_score", 1.0),
        "classification": first_row.get("classification_label", "READY_FOR_LOCAL_ML_CONTRACTS"),
        "is_minimum_passed": first_row.get("is_minimum_passed", True),
        "training_approved": False,
        "dataset_materialization_approved": False,
        "production_ready": False,
        "broker_ready": False,
        "non_signal": True,
    }
