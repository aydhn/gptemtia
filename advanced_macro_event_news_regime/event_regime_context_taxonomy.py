"""Phase 132: Event Regime Context Taxonomy."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_EVENT_TAXONOMIES = [
    {
        "taxonomy_id": "event_tax_scheduled",
        "taxonomy_name": "scheduled_event_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Pre-scheduled calendar publication timestamps and intervals.",
        "parent_category": "calendar_scheduling",
    },
    {
        "taxonomy_id": "event_tax_actual_release",
        "taxonomy_name": "actual_release_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Actual observed publication timestamp for lookahead-free backward join.",
        "parent_category": "calendar_scheduling",
    },
    {
        "taxonomy_id": "event_tax_pre_event",
        "taxonomy_name": "pre_event_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Pre-event regime buffer window prior to major high-importance releases.",
        "parent_category": "window_context",
    },
    {
        "taxonomy_id": "event_tax_post_event",
        "taxonomy_name": "post_event_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Post-event regime buffer window following data publication.",
        "parent_category": "window_context",
    },
    {
        "taxonomy_id": "event_tax_release_lag",
        "taxonomy_name": "release_lag_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Difference between economic reference period end and release date.",
        "parent_category": "lag_context",
    },
    {
        "taxonomy_id": "event_tax_importance",
        "taxonomy_name": "event_importance_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Hierarchy of release significance (low, medium, high, critical).",
        "parent_category": "importance_context",
    },
    {
        "taxonomy_id": "event_tax_event_window",
        "taxonomy_name": "event_window_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Composite event window boundaries encompassing pre, release, and post phases.",
        "parent_category": "window_context",
    },
    {
        "taxonomy_id": "event_tax_recurring",
        "taxonomy_name": "recurring_event_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Periodically recurring release event series (monthly, quarterly).",
        "parent_category": "calendar_scheduling",
    },
    {
        "taxonomy_id": "event_tax_delay_placeholder",
        "taxonomy_name": "unexpected_delay_placeholder_context",
        "domain": "event_context_taxonomy_domain",
        "description": "Diagnostics placeholder for releases delayed beyond scheduled time.",
        "parent_category": "anomaly_context",
    },
]


def build_event_regime_context_taxonomy_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build taxonomy registry DataFrame for event regime context."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_EVENT_TAXONOMIES:
        row = dict(item)
        row["profile_name"] = p.profile_name
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        rows.append(row)
    df = pd.DataFrame(rows)
    summary = {
        "total_event_taxonomies": len(df),
        "domains": df["domain"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_event_regime_context_taxonomy(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for event context taxonomy."""
    return {
        "total_taxonomies": len(df),
        "parent_categories": df["parent_category"].nunique() if "parent_category" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
