"""Phase 127: Regime Matrix Manual Review Queue.

Manages non-destructive audit items for human review without automated purging,
imputation, signal generation, or model execution.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_matrix.regime_matrix_config import (
    RegimeMatrixProfile,
    get_default_regime_matrix_profile,
)

QUEUE_ITEMS_DEFINITION: List[Dict[str, Any]] = [
    {
        "item_id": "rev_001_source_phase_coverage",
        "finding_type": "missing_source_phase_input",
        "affected_entity": "fx_pair_and_commodity",
        "severity": "MEDIUM",
        "description": "Verify that all 9 upstream source phases are present and synced in local lake.",
        "recommended_action": "Inspect upstream Phase 117-126 artifacts; do NOT auto-delete missing records.",
    },
    {
        "item_id": "review_gap_brent_wti_spread",
        "finding_type": "unresolved_validation_dependency",
        "affected_entity": "cross_asset_spread",
        "severity": "LOW",
        "description": "Confirm Phase 121 validation pass before publishing composite research matrix.",
        "recommended_action": "Audit Phase 121 validation report; do NOT auto-drop features.",
    },
    {
        "item_id": "rev_003_quality_dependency",
        "finding_type": "unresolved_quality_dependency",
        "affected_entity": "macro_indicator_time_series",
        "severity": "MEDIUM",
        "description": "Verify rolling missingness ratio remains under 0.05 threshold.",
        "recommended_action": "Review quality diagnostics report; do NOT perform auto-imputation.",
    },
    {
        "item_id": "rev_004_timestamp_order",
        "finding_type": "unresolved_timestamp_alignment",
        "affected_entity": "calendar_event_fusion",
        "severity": "HIGH",
        "description": "Audit asof join direction to confirm zero forward or future return linkage.",
        "recommended_action": "Verify backward-only asof join policy; do NOT alter timestamp values manually.",
    },
    {
        "item_id": "rev_005_news_metadata_boundary",
        "finding_type": "unresolved_news_metadata_only_boundary",
        "affected_entity": "news_metadata_tag",
        "severity": "HIGH",
        "description": "Inspect news tags to verify zero raw HTML, full text, or scraping content.",
        "recommended_action": "Quarantine suspicious text payloads; do NOT enable web scraping.",
    },
    {
        "item_id": "rev_006_forbidden_column_audit",
        "finding_type": "forbidden_column_risk",
        "affected_entity": "all_matrices",
        "severity": "HIGH",
        "description": "Scan matrix column headers for buy/sell/signal/target/prediction substrings.",
        "recommended_action": "Rename or quarantine conflicting column names; do NOT generate signals.",
    },
    {
        "item_id": "rev_007_state_dataset_schema",
        "finding_type": "state_dataset_schema_ambiguity",
        "affected_entity": "state_candidate_contexts",
        "severity": "LOW",
        "description": "Ensure candidate contexts are treated as structural research flags, not labels.",
        "recommended_action": "Verify no_target_label_prediction invariant; do NOT train models or cluster.",
    },
    {
        "item_id": "rev_008_phase_128_readiness",
        "finding_type": "phase_128_readiness_review",
        "affected_entity": "handoff_specification",
        "severity": "MEDIUM",
        "description": "Audit handoff prerequisites for Phase 128 rule-free labeling and unsupervised prep.",
        "recommended_action": "Validate handoff manifest checklist; do NOT issue official production approval.",
    },
]


def build_regime_matrix_manual_review_queue(
    profile: Optional[RegimeMatrixProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the regime matrix manual review queue."""
    p = profile or get_default_regime_matrix_profile()

    rows = []
    for item in QUEUE_ITEMS_DEFINITION:
        i_copy = item.copy()
        i_copy["current_phase"] = p.current_phase
        i_copy["target_final_phase"] = p.target_final_phase
        i_copy["next_phase"] = p.next_phase
        i_copy["destructive_action_allowed"] = False
        i_copy["auto_fix_allowed"] = False
        i_copy["auto_drop_allowed"] = False
        i_copy["non_signal"] = True
        i_copy["source_preserved"] = True
        i_copy["status"] = "PENDING_REVIEW"
        rows.append(i_copy)

    df = pd.DataFrame(rows)
    summary = summarize_regime_matrix_manual_review_queue(df)
    return df, summary


def summarize_regime_matrix_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    pending_count = int((df["status"] == "PENDING_REVIEW").sum()) if not df.empty else len(df)
    return {
        "total_review_items": len(df),
        "total_items": len(df),
        "pending_items": pending_count,
        "finding_types": df["finding_type"].tolist() if not df.empty else [],
        "all_destructive_disallowed": bool((~df["destructive_action_allowed"]).all()) if not df.empty else True,
        "all_auto_fix_disallowed": bool((~df["auto_fix_allowed"]).all()) if not df.empty else True,
        "all_auto_drop_disallowed": bool((~df["auto_drop_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "status": "REVIEW_QUEUE_ACTIVE",
    }


MANUAL_REVIEW_ITEMS = QUEUE_ITEMS_DEFINITION


def is_valid_manual_review_item(item_id: str) -> bool:
    """Check if manual review item id is defined."""
    return any(item["item_id"] == item_id for item in MANUAL_REVIEW_ITEMS)

