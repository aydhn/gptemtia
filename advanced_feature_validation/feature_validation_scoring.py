"""Feature Validation Scoring Engine.

Calculates normalized 0.0-1.0 feature validation scores based on findings severity.
Strictly an internal research hygiene metric; never an official approval or trade signal.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)
from advanced_feature_validation.feature_validation_models import (
    FeatureValidationScore,
    build_feature_validation_score_id,
)


def classify_feature_validation_score(
    score: float, profile: FeatureValidationProfile | None = None
) -> str:
    """Classify validation score into standard validation status label."""
    p = profile or get_default_feature_validation_profile()
    min_score = p.min_validation_score

    if score >= 0.85:
        return "validation_pass"
    elif score >= min_score:
        return "validation_pass_with_warnings"
    else:
        return "validation_fail"


def calculate_feature_validation_score(
    findings_df: pd.DataFrame | None,
    matrix_name: str,
    profile: FeatureValidationProfile | None = None,
) -> FeatureValidationScore:
    """Calculate validation score based on findings penalty deduction."""
    p = profile or get_default_feature_validation_profile()
    score_id = build_feature_validation_score_id(matrix_name)

    critical = 0
    high = 0
    medium = 0
    review_count = 0

    if findings_df is not None and not findings_df.empty:
        if "severity_label" in findings_df.columns:
            critical = int((findings_df["severity_label"] == "validation_critical").sum())
            high = int((findings_df["severity_label"] == "validation_high").sum())
            medium = int((findings_df["severity_label"] == "validation_medium").sum())
        if "manual_review_required" in findings_df.columns:
            review_count = int(findings_df["manual_review_required"].sum())

    # Penalty calculation: Start at 1.0, deduct based on severity
    raw_score = 1.0 - (critical * 0.40 + high * 0.20 + medium * 0.05)
    score = max(0.0, min(1.0, raw_score))

    status = classify_feature_validation_score(score, p)

    return FeatureValidationScore(
        score_id=score_id,
        matrix_name=matrix_name,
        validation_score=round(score, 4),
        status_label=status,
        critical_findings=critical,
        high_findings=high,
        medium_findings=medium,
        manual_review_count=review_count,
        official_approval=False,
        production_ready=False,
        notes="Internal quality score. Zero signal, non-production, no official approval.",
    )


def build_feature_validation_score_report(
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build summary score report for standard feature matrices."""
    active_profile = profile or get_default_feature_validation_profile()

    matrices = [
        "technical_indicator_matrix",
        "multi_window_feature_grid",
        "cross_asset_aligned_matrix",
        "macro_calendar_news_fusion_matrix",
    ]

    records = []
    for m in matrices:
        score_obj = calculate_feature_validation_score(None, m, active_profile)
        records.append(score_obj.to_dict())

    df = pd.DataFrame(records)
    avg_score = float(df["validation_score"].mean()) if not df.empty else 1.0

    summary = {
        "active_profile": active_profile.name,
        "total_matrices_scored": len(records),
        "average_validation_score": round(avg_score, 4),
        "all_passed": all(r["status_label"] in ("validation_pass", "validation_pass_with_warnings") for r in records),
        "official_approval_claim": False,
        "production_ready_claim": False,
        "non_signal": True,
    }
    return df, summary


def summarize_feature_validation_scores(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize scores DataFrame."""
    return {
        "matrices_scored": len(df),
        "avg_score": float(df["validation_score"].mean()) if "validation_score" in df else 1.0,
        "min_score": float(df["validation_score"].min()) if "validation_score" in df else 1.0,
        "max_score": float(df["validation_score"].max()) if "validation_score" in df else 1.0,
        "official_approval": False,
        "production_ready": False,
    }


def compute_feature_validation_scores(
    lookahead_score: float = 1.0,
    forbidden_column_score: float = 1.0,
    integrity_score: float = 1.0,
    numeric_sanity_score: float = 1.0,
    completeness_score: float = 1.0,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Compute overall feature validation score and status."""
    weights = {
        "lookahead": 0.30,
        "forbidden_column": 0.25,
        "integrity": 0.15,
        "numeric_sanity": 0.15,
        "completeness": 0.15,
    }
    overall = (
        lookahead_score * weights["lookahead"]
        + forbidden_column_score * weights["forbidden_column"]
        + integrity_score * weights["integrity"]
        + numeric_sanity_score * weights["numeric_sanity"]
        + completeness_score * weights["completeness"]
    )
    overall = round(max(0.0, min(1.0, float(overall))), 4)
    is_passing = bool(overall >= 0.80 and lookahead_score >= 0.99 and forbidden_column_score >= 0.99)

    return {
        "overall_score": overall,
        "lookahead_score": lookahead_score,
        "forbidden_column_score": forbidden_column_score,
        "integrity_score": integrity_score,
        "numeric_sanity_score": numeric_sanity_score,
        "completeness_score": completeness_score,
        "is_passing": is_passing,
        "current_phase": 121,
    }


def get_score_grade(score: float) -> str:
    """Map numeric score to letter grade."""
    if score >= 0.95:
        return "A+"
    elif score >= 0.85:
        return "A"
    elif score >= 0.75:
        return "B"
    elif score >= 0.65:
        return "C"
    elif score >= 0.50:
        return "D"
    else:
        return "F"


def get_scoring_summary(scores: Dict[str, Any]) -> Dict[str, Any]:
    """Return structured scoring summary."""
    overall = scores.get("overall_score", 1.0)
    grade = get_score_grade(overall)
    return {
        "current_phase": 121,
        "target_final_phase": 160,
        "overall_score": overall,
        "grade": grade,
        "is_passing": scores.get("is_passing", True),
        "scores": scores,
    }

