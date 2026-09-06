"""Phase 134: Macro / Event / News Regime Store Catalog.

Connects Phase 132 macro indicator, calendar event, and news metadata context
to the FeatureStore catalog, enforcing strict metadata-only news purity.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    MACRO_EVENT_NEWS_STORE_CATALOG_DOMAIN,
    REGIME_STORE_READY,
    STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
)

CANONICAL_MACRO_EVENT_NEWS_ITEMS: List[Dict[str, Any]] = [
    {
        "store_catalog_name": "macro_release_regime_context",
        "store_entity_type": STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "source_report_ref": "reports/output/advanced_macro_event_news_regime/report_balanced_local_macro_event_news_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_macro_event_news_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "economic_calendar_event_regime_context",
        "store_entity_type": STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "source_report_ref": "reports/output/advanced_macro_event_news_regime/report_balanced_local_macro_event_news_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_macro_event_news_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
    {
        "store_catalog_name": "news_metadata_regime_context",
        "store_entity_type": STORE_ENTITY_MACRO_EVENT_NEWS_CONTEXT,
        "source_phase": 132,
        "source_component": "advanced_macro_event_news_regime",
        "source_report_ref": "reports/output/advanced_macro_event_news_regime/report_balanced_local_macro_event_news_regime_context.json",
        "validation_acceptance_ref": "phase_133_gate_macro_event_news_pass",
        "no_lookahead_accepted": True,
        "metadata_only_news_accepted": True,
        "source_preserved": True,
        "non_signal": True,
        "manual_review_required": False,
        "production_ready": False,
        "broker_ready": False,
    },
]


def build_macro_event_news_regime_store_catalog(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct DataFrame and summary for macro/event/news regime store catalog."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(CANONICAL_MACRO_EVENT_NEWS_ITEMS)
    summary = {
        "domain": MACRO_EVENT_NEWS_STORE_CATALOG_DOMAIN,
        "total_items": len(df),
        "active_profile": active_profile.profile_name,
        "source_phase": 132,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "all_non_signal": bool((df["non_signal"] == True).all()),
        "all_metadata_only_news": bool((df["metadata_only_news_accepted"] == True).all()),
        "all_source_preserved": bool((df["source_preserved"] == True).all()),
        "production_ready": False,
        "broker_ready": False,
        "status": REGIME_STORE_READY,
    }
    return df, summary


def summarize_macro_event_news_regime_store_catalog(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize macro/event/news catalog DataFrame."""
    return {
        "total_items": len(df),
        "catalog_names": df["store_catalog_name"].tolist() if not df.empty else [],
        "all_metadata_only_news": bool((df["metadata_only_news_accepted"] == True).all()) if not df.empty else True,
        "all_non_signal": bool((df["non_signal"] == True).all()) if not df.empty else True,
    }
