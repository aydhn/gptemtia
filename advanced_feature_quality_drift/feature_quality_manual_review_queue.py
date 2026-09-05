"""Phase 123 Feature Quality Manual Review Queue.

Queues feature quality violations for human analyst inspection, explicitly prohibiting
automated deletion, automatic source overwrites, or live trade approvals.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def build_feature_quality_manual_review_queue(
    profile: FeatureQualityDriftProfile | None = None,
    findings_df: pd.DataFrame | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Filter quality findings requiring manual human review into a structured queue."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    if findings_df is not None and not findings_df.empty:
        review_items = findings_df[findings_df["manual_review_required"]]
        for _, row in review_items.iterrows():
            records.append({
                "queue_id": f"qmr_{len(records)+1}",
                "finding_id": row.get("finding_id", "unknown"),
                "source_table": row.get("source_table", "unknown"),
                "feature_column": row.get("feature_column", "general"),
                "severity": row.get("severity", "quality_medium"),
                "issue_description": row.get("issue_description", ""),
                "action_guideline": "Inspect upstream pipeline logic; do NOT perform automatic imputation or deletion",
                "auto_fix_forbidden": True,
                "auto_drop_forbidden": True,
                "production_approval_forbidden": True,
                "non_signal": True,
            })

    if not records:
        records.append({
            "queue_id": "qmr_nominal_empty",
            "finding_id": "none",
            "source_table": "quality_queue",
            "feature_column": "none",
            "severity": "quality_info",
            "issue_description": "No blocking quality issues pending manual review.",
            "action_guideline": "Queue is currently clear; continue scheduled routine audits",
            "auto_fix_forbidden": True,
            "auto_drop_forbidden": True,
            "production_approval_forbidden": True,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_feature_quality_manual_review_queue(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_quality_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary from feature quality manual review queue DataFrame."""
    if df.empty:
        return {
            "total_queued_items": 0,
            "critical_items_count": 0,
            "high_items_count": 0,
            "status": "diagnostic_pass",
            "manual_review_pending": False,
        }

    total_q = len(df) if not (len(df) == 1 and df.iloc[0]["queue_id"] == "qmr_nominal_empty") else 0
    crit_q = int((df["severity"] == "quality_critical").sum()) if "severity" in df.columns else 0
    high_q = int((df["severity"] == "quality_high").sum()) if "severity" in df.columns else 0

    return {
        "total_queued_items": total_q,
        "critical_items_count": crit_q,
        "high_items_count": high_q,
        "status": "diagnostic_fail" if (crit_q + high_q) > 0 else "diagnostic_pass",
        "manual_review_pending": total_q > 0,
    }
