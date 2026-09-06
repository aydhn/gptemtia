"""Phase 132: Macro/Event/News Manual Review Queue (Non-Destructive Governance)."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

PROHIBITED_ACTIONS: List[str] = [
    "auto-delete",
    "auto-overwrite",
    "auto-impute",
    "enable scraping",
    "download article body",
    "generate sentiment",
    "generate embedding",
    "generate signal",
    "train model",
    "approve production",
    "approve broker readiness",
]

DEFAULT_REVIEW_ITEMS = [
    {
        "review_id": "rev_001_inspect_release_ts",
        "category": "timestamp_verification",
        "issue_description": "Verify high-importance indicator release timestamps match official publication records.",
        "safe_recommendation": "inspect macro release timestamp",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_002_inspect_actual_alignment",
        "category": "lookahead_verification",
        "issue_description": "Audit scheduled vs actual publication timestamps for potential clock drifts.",
        "safe_recommendation": "inspect scheduled/actual release alignment",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_003_inspect_release_lag",
        "category": "lag_verification",
        "issue_description": "Validate indicator reporting lag horizons are strictly respected in backward asof joins.",
        "safe_recommendation": "inspect release lag context",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_004_inspect_event_windows",
        "category": "window_verification",
        "issue_description": "Inspect pre-event and post-event window parameter settings across critical events.",
        "safe_recommendation": "inspect event window boundaries",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_005_inspect_metadata_boundary",
        "category": "news_safety_verification",
        "issue_description": "Ensure no full article text, HTML tags, or sentiment scores enter the registry.",
        "safe_recommendation": "inspect news metadata-only boundary",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_006_inspect_forbidden_fields",
        "category": "news_field_audit",
        "issue_description": "Perform string scanning to verify complete exclusion of raw article content.",
        "safe_recommendation": "inspect forbidden news content fields",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_007_inspect_cross_asset_dep",
        "category": "cross_asset_verification",
        "issue_description": "Confirm macro-FX and macro-Commodity linkages maintain consistent schema keys.",
        "safe_recommendation": "inspect cross-asset macro sensitivity dependency",
        "status": "pending_analyst_review",
    },
    {
        "review_id": "rev_008_inspect_phase_133_blockers",
        "category": "handoff_verification",
        "issue_description": "Assess all acceptance criteria prerequisites prior to Phase 133 validation sign-off.",
        "safe_recommendation": "inspect Phase 133 blockers",
        "status": "pending_analyst_review",
    },
]


def build_macro_event_news_manual_review_queue(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build review queue DataFrame enforcing safe human inspection without auto-fixes."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_REVIEW_ITEMS:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["prohibited_actions"] = list(PROHIBITED_ACTIONS)
        row["auto_action_permitted"] = False
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_review_items": len(df),
        "categories": df["category"].unique().tolist(),
        "prohibited_actions_enforced": True,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_manual_review_queue(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for manual review queue."""
    return {
        "total_reviews": len(df),
        "pending_reviews": int((df["status"] == "pending_analyst_review").sum()) if "status" in df.columns else 0,
        "prohibited_actions_count": len(PROHIBITED_ACTIONS),
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
