"""Phase 123 Feature Drift Manual Review Queue.

Queues distribution drift and stability alerts for research inspection, ensuring drift
findings are never directly routed into trading strategies or automated order systems.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def build_feature_drift_manual_review_queue(
    profile: FeatureQualityDriftProfile | None = None,
    drift_findings_df: pd.DataFrame | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Filter drift findings requiring manual review into a structured queue."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    if drift_findings_df is not None and not drift_findings_df.empty:
        review_items = drift_findings_df[drift_findings_df["manual_review_required"]]
        for _, row in review_items.iterrows():
            records.append({
                "queue_id": f"dmr_{len(records)+1}",
                "finding_id": row.get("finding_id", "unknown"),
                "source_table": row.get("source_table", "unknown"),
                "feature_column": row.get("feature_column", "general"),
                "severity": row.get("severity", "drift_medium"),
                "drift_description": row.get("drift_description", ""),
                "action_guideline": "Inspect baseline window and feature distribution; do NOT interpret as trade signal",
                "trade_signal_generation_forbidden": True,
                "strategy_rule_generation_forbidden": True,
                "non_signal": True,
            })

    if not records:
        records.append({
            "queue_id": "dmr_nominal_empty",
            "finding_id": "none",
            "source_table": "drift_queue",
            "feature_column": "none",
            "severity": "drift_info",
            "drift_description": "No blocking drift issues pending manual review.",
            "action_guideline": "Queue is currently clear; continue scheduled routine audits",
            "trade_signal_generation_forbidden": True,
            "strategy_rule_generation_forbidden": True,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_feature_drift_manual_review_queue(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_drift_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary from feature drift manual review queue DataFrame."""
    if df.empty:
        return {
            "total_queued_items": 0,
            "critical_drift_items": 0,
            "high_drift_items": 0,
            "status": "diagnostic_pass",
            "manual_review_pending": False,
        }

    total_q = len(df) if not (len(df) == 1 and df.iloc[0]["queue_id"] == "dmr_nominal_empty") else 0
    crit_q = int((df["severity"] == "drift_critical").sum()) if "severity" in df.columns else 0
    high_q = int((df["severity"] == "drift_high").sum()) if "severity" in df.columns else 0

    return {
        "total_queued_items": total_q,
        "critical_drift_items": crit_q,
        "high_drift_items": high_q,
        "status": "diagnostic_fail" if (crit_q + high_q) > 0 else "diagnostic_pass",
        "manual_review_pending": total_q > 0,
    }
