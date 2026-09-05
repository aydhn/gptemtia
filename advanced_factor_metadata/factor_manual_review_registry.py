"""Phase 122 Factor Manual Review Registry.

Queues edge cases, placeholder factors, and boundary verifications for human inspection.
Non-destructive: rejects auto-deletion, silent dropping, or destructive modifications.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_MANUAL_REVIEW_REQUIRED
from advanced_factor_metadata.factor_metadata_models import (
    FactorManualReviewItem,
    build_factor_manual_review_id,
)

MANUAL_REVIEW_REASONS: List[Dict[str, Any]] = [
    {
        "factor_name": "factor_quote_spread_context_placeholder",
        "factor_family": "quote_microstructure",
        "review_reason": "Microstructure data availability and liquidity provider coverage verification.",
        "suggested_action": "Verify tick data source timestamps before unflagging placeholder.",
    },
    {
        "factor_name": "factor_macro_surprise_placeholder_context",
        "factor_family": "macro_context",
        "review_reason": "Consensus estimate feed stability and release lag verification.",
        "suggested_action": "Ensure economic calendar consensus source maintains zero lookahead.",
    },
    {
        "factor_name": "factor_news_freshness_placeholder_context",
        "factor_family": "news_attention",
        "review_reason": "Metadata-only boundary review and half-life decay parameter calibration.",
        "suggested_action": "Audit news headline feeds to guarantee zero article body or web scraping.",
    },
    {
        "factor_name": "factor_cross_domain_context_placeholder",
        "factor_family": "cross_asset_context",
        "review_reason": "Cross-domain matrix dimension verification across heterogeneous session hours.",
        "suggested_action": "Validate backward asof join alignment across non-synchronous asset calendars.",
    },
    {
        "factor_name": "factor_regime_prep_placeholder",
        "factor_family": "regime_prep",
        "review_reason": "Pre-flight review of candidate inputs for Phase 126+ regime classification.",
        "suggested_action": "Hold as non-executing candidate factor until Phase 126 regime engine is active.",
    },
    {
        "factor_name": "factor_composite_context_placeholder",
        "factor_family": "composite",
        "review_reason": "Composite placeholder boundary review to prevent accidental strategy generation.",
        "suggested_action": "Confirm composite factors remain pure research metadata containers.",
    },
]


def build_factor_manual_review_registry(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Manual Review Registry DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    items: List[Dict[str, Any]] = []
    for r in MANUAL_REVIEW_REASONS:
        item = FactorManualReviewItem(
            review_id=build_factor_manual_review_id(r["factor_name"], r["review_reason"]),
            factor_name=r["factor_name"],
            factor_family=r["factor_family"],
            review_reason=r["review_reason"],
            suggested_action=r["suggested_action"],
            destructive_action_allowed=False,
            status_label=FACTOR_MANUAL_REVIEW_REQUIRED,
        )
        items.append(item.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_review_items": len(items),
        "destructive_action_allowed": False,
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "non_signal": True,
        "status": FACTOR_MANUAL_REVIEW_REQUIRED,
    }
    return df, summary


def summarize_factor_manual_review_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor manual review registry DataFrame."""
    return {
        "total_items": len(df),
        "destructive_action_allowed": False,
        "status": FACTOR_MANUAL_REVIEW_REQUIRED,
        "non_signal": True,
    }
