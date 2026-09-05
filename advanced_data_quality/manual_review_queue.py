from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import (
    ManualReviewItem,
    QualityFinding,
    build_manual_review_id,
)


def create_manual_review_item(finding: QualityFinding) -> ManualReviewItem:
    review_id = build_manual_review_id(finding.finding_id)
    # Safe suggestions: non-destructive actions only
    suggested = finding.recommendation or "Inspect record manually; queue for Phase 113 Normalization."
    return ManualReviewItem(
        review_id=review_id,
        finding_id=finding.finding_id,
        dataset_type=finding.dataset_type,
        provider_name=finding.provider_name,
        priority=finding.severity_label,
        review_reason=finding.message,
        suggested_action=suggested,
        destructive_action_allowed=False,
        status_label="quality_manual_review_required",
    )


def build_manual_review_queue(
    findings_df: pd.DataFrame,
    profile: DataQualityProfile
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    if findings_df is None or len(findings_df) == 0:
        df = pd.DataFrame(columns=[
            "review_id", "finding_id", "dataset_type", "provider_name", "priority",
            "review_reason", "suggested_action", "destructive_action_allowed", "status_label"
        ])
        return df, summarize_manual_review_queue(df)

    # Filter findings requiring manual review
    if "manual_review_required" in findings_df.columns:
        reviewable = findings_df[findings_df["manual_review_required"] == True]
    else:
        reviewable = findings_df

    items: List[Dict[str, Any]] = []
    for _, row in reviewable.iterrows():
        f = QualityFinding(
            finding_id=str(row.get("finding_id", "")),
            rule_id=str(row.get("rule_id", "")),
            finding_type=str(row.get("finding_type", "")),
            dataset_type=str(row.get("dataset_type", "")),
            provider_name=str(row.get("provider_name", "")),
            field_name=str(row.get("field_name", "")),
            severity_label=str(row.get("severity_label", "quality_medium")),
            status_label=str(row.get("status_label", "quality_manual_review_required")),
            message=str(row.get("message", "")),
            recommendation=str(row.get("recommendation", "")),
            future_phase_owner=str(row.get("future_phase_owner", "Phase 113")),
            manual_review_required=bool(row.get("manual_review_required", True)),
        )
        item = create_manual_review_item(f)
        items.append(item.to_dict())

    df = pd.DataFrame.from_records(items)
    # Ensure destructive_action_allowed is strictly False
    if "destructive_action_allowed" in df.columns:
        df["destructive_action_allowed"] = False

    summary = summarize_manual_review_queue(df)
    return df, summary


def summarize_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or len(df) == 0:
        return {
            "total_items": 0,
            "critical_priority": 0,
            "high_priority": 0,
            "medium_priority": 0,
            "low_priority": 0,
            "destructive_action_allowed_any": False,
            "current_phase": 112,
            "target_final_phase": 160,
        }

    prio_counts = df["priority"].value_counts().to_dict() if "priority" in df.columns else {}
    return {
        "total_items": len(df),
        "critical_priority": prio_counts.get("quality_critical", 0),
        "high_priority": prio_counts.get("quality_high", 0),
        "medium_priority": prio_counts.get("quality_medium", 0),
        "low_priority": prio_counts.get("quality_low", 0),
        "destructive_action_allowed_any": bool(df["destructive_action_allowed"].any()) if "destructive_action_allowed" in df.columns else False,
        "providers": sorted(list(df["provider_name"].unique())) if "provider_name" in df.columns else [],
        "current_phase": 112,
        "target_final_phase": 160,
    }
