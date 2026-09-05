from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile


def build_manual_review_normalization_queue(
    findings_df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records: List[Dict[str, Any]] = []

    if not findings_df.empty and "manual_review_required" in findings_df.columns:
        manual_findings = findings_df[findings_df["manual_review_required"] == True]
        for idx, row in manual_findings.iterrows():
            fid = row.get("finding_id", f"unknown_finding_{idx}")
            records.append({
                "queue_id": f"queue_{fid}",
                "finding_id": fid,
                "rule_id": row.get("rule_id", "unknown_rule"),
                "dataset_type": row.get("dataset_type", "dataset_unknown"),
                "source_field": row.get("source_field", ""),
                "original_value_repr": row.get("original_value_repr", ""),
                "severity_label": row.get("severity_label", "normalization_medium"),
                "suggested_action": "manual inspect; lineage record in Phase 114; benchmark mapping in Phase 115",
                "destructive_action_allowed": False,
                "source_preserved": True,
                "lineage_required": True,
                "status_label": "normalization_manual_review_required",
            })

    df = pd.DataFrame.from_records(records)
    summary = summarize_manual_review_normalization_queue(df)
    return df, summary


def summarize_manual_review_normalization_queue(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_queued_items": len(df),
        "destructive_actions_prevented": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "source_preserved_all": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "lineage_required_all": bool(df["lineage_required"].all()) if "lineage_required" in df.columns and len(df) > 0 else True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
