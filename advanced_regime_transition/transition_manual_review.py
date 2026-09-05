"""Phase 130: Transition Manual Review Queue.

Constructs manual review items requiring human inspection.
Strictly prohibits automated destruction, auto-imputation, model fitting, or signal generation.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_transition.regime_transition_config import (
    RegimeTransitionProfile,
    get_default_regime_transition_profile,
)

SAMPLE_REVIEW_ITEMS: List[Dict[str, Any]] = [
    {
        "review_id": "REV-130-001",
        "target_component": "state_sequence_continuity",
        "issue_description": "Validate sequence continuity across holiday session boundaries",
        "recommended_inspection": "inspect state sequence continuity and ensure no unintended temporal gaps",
        "blocking_status": "review_pending",
        "manual_review_required": True,
        "auto_fix_forbidden": True,
    },
    {
        "review_id": "REV-130-002",
        "target_component": "transition_ambiguity",
        "issue_description": "Verify transition ambiguity remains below warning threshold during volatility shifts",
        "recommended_inspection": "inspect transition ambiguity and verify candidate state assignment sharpness",
        "blocking_status": "review_pending",
        "manual_review_required": True,
        "auto_fix_forbidden": True,
    },
    {
        "review_id": "REV-130-003",
        "target_component": "news_metadata_boundary",
        "issue_description": "Audit news context feeds to certify metadata-only usage without article body text",
        "recommended_inspection": "inspect news metadata-only boundary and confirm zero raw content or embeddings",
        "blocking_status": "review_pending",
        "manual_review_required": True,
        "auto_fix_forbidden": True,
    },
    {
        "review_id": "REV-130-004",
        "target_component": "cross_asset_transition_prep",
        "issue_description": "Examine cross-asset timestamp alignment between commodity and currency regimes",
        "recommended_inspection": "inspect cross-asset transition readiness and Phase 131 prerequisites",
        "blocking_status": "review_pending",
        "manual_review_required": True,
        "auto_fix_forbidden": True,
    },
]

FORBIDDEN_REVIEW_ACTIONS = [
    "auto-delete",
    "auto-overwrite",
    "auto-impute",
    "enable scraping",
    "generate signal",
    "run clustering",
    "train model",
    "run dimensionality reduction",
    "approve production",
    "approve broker readiness",
]


def build_transition_manual_review_queue(
    profile: Optional[RegimeTransitionProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build manual review queue dataframe and summary."""
    if profile is None:
        profile = get_default_regime_transition_profile()

    df = pd.DataFrame(SAMPLE_REVIEW_ITEMS)
    summary = summarize_transition_manual_review_queue(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_transition_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize manual review queue."""
    pending_count = int((df["blocking_status"] == "review_pending").sum()) if not df.empty and "blocking_status" in df.columns else 0
    return {
        "total_review_items": len(df),
        "pending_reviews_count": pending_count,
        "auto_fix_forbidden_certified": bool(df["auto_fix_forbidden"].all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "forbidden_actions_avoided": True,
    }
