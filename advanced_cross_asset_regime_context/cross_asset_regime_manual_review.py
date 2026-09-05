"""Phase 131: Cross-Asset Regime Manual Review Queue.

Defines non-destructive human review items for cross-asset context evaluation.
Strictly prohibits destructive actions, auto-imputation, auto-feature-drop, scraping,
signal generation, and machine learning model execution.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

MANUAL_REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "rev_inspect_entity_mapping",
        "category": "entity_audit",
        "severity": "low",
        "title": "Inspect Cross-Asset Entity Mapping",
        "description": "Review consistency of currency identifiers, commodity symbol codes, and benchmark indicators.",
        "suggested_action": "inspect cross-asset entity mapping and preserve raw identifier provenance",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_timestamp_alignment",
        "category": "temporal_audit",
        "severity": "medium",
        "title": "Inspect Timestamp Alignment and Monotonicity",
        "description": "Ensure observation timestamps across disjoint market trading calendars remain strictly aligned in UTC.",
        "suggested_action": "inspect timestamp alignment and verify backward-looking temporal order",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_backward_asof",
        "category": "join_policy_audit",
        "severity": "medium",
        "title": "Inspect Backward Asof Policy",
        "description": "Verify asof merges enforce direction='backward' and never pull future tick quotes.",
        "suggested_action": "inspect backward asof policy and confirm zero forward-join leakage",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_divergence_convergence",
        "category": "relationship_audit",
        "severity": "low",
        "title": "Inspect Divergence and Convergence Context",
        "description": "Confirm that divergence and convergence records remain descriptive diagnostics and are never interpreted as pairs trades.",
        "suggested_action": "inspect divergence/convergence context and verify non-signal documentation",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_news_metadata_boundary",
        "category": "compliance_audit",
        "severity": "high",
        "title": "Inspect News Metadata-Only Boundary",
        "description": "Verify that zero full article text, HTML scraping, or NLP embeddings enter cross-asset pipelines.",
        "suggested_action": "inspect news metadata-only boundary and enforce text-free constraints",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_macro_calendar_dependency",
        "category": "macro_dependency_audit",
        "severity": "medium",
        "title": "Inspect Macro/Calendar Dependency",
        "description": "Confirm release lag parameters accommodate unannounced publication postponements.",
        "suggested_action": "inspect macro/calendar dependency and verify publication lag guards",
        "blocking_for_phase_132": False,
    },
    {
        "item_id": "rev_inspect_phase_132_blockers",
        "category": "handoff_gate",
        "severity": "medium",
        "title": "Inspect Phase 132 Handoff Readiness",
        "description": "Audit readiness of macro/event/news context contracts prior to Phase 132 expansion.",
        "suggested_action": "inspect Phase 132 blockers and verify non-signal handoff criteria",
        "blocking_for_phase_132": False,
    },
]


def build_cross_asset_regime_manual_review_queue(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manual review queue dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in MANUAL_REVIEW_ITEMS:
        row = dict(item)
        row["destructive_action_allowed"] = False
        row["auto_fix_allowed"] = False
        row["auto_drop_allowed"] = False
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_cross_asset_manual_review_queue(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    categories = df["category"].value_counts().to_dict() if not df.empty else {}
    severities = df["severity"].value_counts().to_dict() if not df.empty else {}
    blocking = int(df["blocking_for_phase_132"].sum()) if not df.empty else 0
    return {
        "total_review_items": len(df),
        "categories": categories,
        "severities": severities,
        "blocking_for_phase_132_count": blocking,
        "destructive_action_allowed": False,
        "auto_fix_allowed": False,
        "auto_drop_allowed": False,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
    }
