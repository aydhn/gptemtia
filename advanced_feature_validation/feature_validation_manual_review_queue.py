"""Manual Review Queue for Phase 121 Feature Validation Layer.

Collects validation findings that require human inspection and prescribes non-destructive review steps.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_validation.feature_validation_config import (
    FeatureValidationProfile,
    get_default_feature_validation_profile,
)

SAFE_RECOMMENDATIONS: List[str] = [
    "inspect timestamp ordering",
    "inspect release lag policy",
    "inspect forbidden column source",
    "inspect namespace collision",
    "inspect missingness",
    "inspect duplicate feature",
    "inspect metadata-only boundary",
    "inspect no-lookahead source",
]

PROHIBITED_RECOMMENDATIONS: List[str] = [
    "auto-delete",
    "auto-overwrite",
    "auto-fill production data",
    "enable scraping",
    "generate signal",
    "approve production",
    "approve broker readiness",
]


def build_feature_validation_manual_review_queue(
    findings_df: pd.DataFrame | None = None,
    profile: FeatureValidationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manual review queue DataFrame from validation findings."""
    active_profile = profile or get_default_feature_validation_profile()

    records = []
    if findings_df is not None and not findings_df.empty:
        review_items = findings_df[findings_df.get("manual_review_required", True)]
        for _, row in review_items.iterrows():
            finding_type = str(row.get("finding_type", "general_anomaly")).lower()
            rec = "inspect no-lookahead source"
            if "timestamp" in finding_type or "order" in finding_type:
                rec = "inspect timestamp ordering"
            elif "lag" in finding_type or "release" in finding_type:
                rec = "inspect release lag policy"
            elif "forbidden" in finding_type:
                rec = "inspect forbidden column source"
            elif "namespace" in finding_type:
                rec = "inspect namespace collision"
            elif "missing" in finding_type:
                rec = "inspect missingness"
            elif "duplicate" in finding_type:
                rec = "inspect duplicate feature"
            elif "news" in finding_type or "metadata" in finding_type:
                rec = "inspect metadata-only boundary"

            records.append({
                "finding_id": row.get("finding_id", ""),
                "feature_or_matrix_name": row.get("feature_or_matrix_name", ""),
                "severity_label": row.get("severity_label", "validation_medium"),
                "status_label": "validation_manual_review_required",
                "recommended_action": rec,
                "destructive_action_allowed": False,
                "auto_remediation_blocked": True,
            })
    else:
        # Default placeholder item
        records.append({
            "finding_id": "review_sample_placeholder",
            "feature_or_matrix_name": "context_matrix_placeholder",
            "severity_label": "validation_info",
            "status_label": "validation_pass",
            "recommended_action": "inspect timestamp ordering",
            "destructive_action_allowed": False,
            "auto_remediation_blocked": True,
        })

    df = pd.DataFrame(records)
    summary = {
        "active_profile": active_profile.name,
        "queue_size": len(records),
        "destructive_action_allowed": False,
        "auto_remediation_blocked": True,
        "non_signal": True,
        "safe_recommendations_enforced": True,
    }
    return df, summary


def summarize_feature_validation_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    return {
        "queue_size": len(df),
        "status": "validation_pass" if len(df) <= 1 else "validation_manual_review_required",
        "destructive_actions_blocked": True,
        "auto_remediation_blocked": True,
    }


_GLOBAL_REVIEW_QUEUE: List[Dict[str, Any]] = []


def clear_manual_review_queue() -> None:
    """Clear all items from the manual review queue."""
    global _GLOBAL_REVIEW_QUEUE
    _GLOBAL_REVIEW_QUEUE.clear()


def get_manual_review_queue() -> List[Dict[str, Any]]:
    """Return all items currently in the manual review queue."""
    return list(_GLOBAL_REVIEW_QUEUE)


def add_to_manual_review_queue(
    finding_id: str,
    column_name: str,
    reason: str,
    recommended_action: str = "inspect manually",
) -> Dict[str, Any]:
    """Add a finding to the manual review queue."""
    item = {
        "finding_id": finding_id,
        "column_name": column_name,
        "reason": reason,
        "recommended_action": recommended_action,
        "status": "PENDING_REVIEW",
        "destructive_action_allowed": False,
    }
    _GLOBAL_REVIEW_QUEUE.append(item)
    return item


def get_manual_review_summary() -> Dict[str, Any]:
    """Return summary of manual review queue."""
    total = len(_GLOBAL_REVIEW_QUEUE)
    pending = sum(1 for item in _GLOBAL_REVIEW_QUEUE if item.get("status") == "PENDING_REVIEW")
    return {
        "total_items": total,
        "pending_review": pending,
        "destructive_action_allowed": False,
        "current_phase": 121,
    }

