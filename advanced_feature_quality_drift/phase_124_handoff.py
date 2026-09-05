"""Phase 123 to Phase 124 Handoff Report.

Prepares formal handoff specifications from Phase 123 (Feature Quality and Drift Diagnostics)
to Phase 124 (Feature Store Integration Expansion), guaranteeing clean, traceable,
metadata-rich, and non-destructive integration.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)

HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "item_feature_quality_manifest",
        "topic": "feature_quality_manifest_readiness",
        "requirement": "Feature quality manifest must provide column-level missingness, inf, zero-variance, and duplicate flags.",
        "status": "READY",
    },
    {
        "item_id": "item_factor_quality_manifest",
        "topic": "factor_quality_manifest_readiness",
        "requirement": "Factor-level quality manifest must cover all 10 factor families with aggregated readiness scores.",
        "status": "READY",
    },
    {
        "item_id": "item_validation_aware_metadata",
        "topic": "validation_aware_feature_store_metadata",
        "requirement": "Feature Store schemas must persist validation status and no-lookahead timestamps alongside feature data.",
        "status": "READY",
    },
    {
        "item_id": "item_quality_score_storage",
        "topic": "quality_score_storage_requirements",
        "requirement": "Feature Store must index dimension-specific quality scores within [0, 1] without signal interpretation.",
        "status": "READY",
    },
    {
        "item_id": "item_drift_score_storage",
        "topic": "drift_score_storage_requirements",
        "requirement": "Feature Store must support storage of baseline vs current distribution drift statistics and stability scores.",
        "status": "READY",
    },
    {
        "item_id": "item_manual_review_blocker_storage",
        "topic": "manual_review_blocker_storage",
        "requirement": "Blocker flags must be queryable in Feature Store to prevent ingestion of unreviewed corrupt features.",
        "status": "READY",
    },
    {
        "item_id": "item_namespace_schema_storage",
        "topic": "namespace_and_schema_storage_requirements",
        "requirement": "Strict namespace prefixing and absence of target/label tokens must be enforced upon feature registration.",
        "status": "READY",
    },
    {
        "item_id": "item_source_preservation",
        "topic": "source_preservation_requirements",
        "requirement": "Raw feature matrices and underlying provider data must remain immutable and preserved.",
        "status": "READY",
    },
    {
        "item_id": "item_no_auto_overwrite",
        "topic": "no_auto_overwrite_requirement",
        "requirement": "Automated imputation, destructive cleaning, and source overwriting are strictly prohibited.",
        "status": "READY",
    },
    {
        "item_id": "item_non_signal_metadata",
        "topic": "no_signal_metadata_requirement",
        "requirement": "All stored manifests and features must carry explicit non_signal=True metadata tags.",
        "status": "READY",
    },
    {
        "item_id": "item_phase_125_acceptance_prep",
        "topic": "phase_125_acceptance_dependencies",
        "requirement": "Manifests and audit logs must provide complete evidentiary lineage for final engine acceptance.",
        "status": "READY",
    },
]


def build_phase_124_feature_store_integration_handoff_report(
    profile: FeatureQualityDriftProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Phase 124 Feature Store integration handoff report."""
    active_profile = profile or get_default_feature_quality_drift_profile()

    records = []
    for item in HANDOFF_ITEMS:
        records.append({
            "item_id": item["item_id"],
            "topic": item["topic"],
            "requirement": item["requirement"],
            "status": item["status"],
            "source_phase": 123,
            "next_phase": 124,
            "target_final_phase": 160,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_phase_124_handoff(df)
    summary["active_profile"] = active_profile.name
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_phase_124_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from handoff DataFrame."""
    if df.empty:
        return {
            "total_items": 0,
            "ready_items": 0,
            "handoff_status": "BLOCKED",
            "source_phase": 123,
            "next_phase": 124,
            "target_final_phase": 160,
            "non_signal": True,
        }

    total_i = len(df)
    ready_i = int((df["status"] == "READY").sum()) if "status" in df.columns else 0

    return {
        "total_items": total_i,
        "ready_items": ready_i,
        "handoff_status": "READY" if ready_i == total_i else "PENDING",
        "source_phase": 123,
        "next_phase": 124,
        "target_final_phase": 160,
        "non_signal": True,
    }
