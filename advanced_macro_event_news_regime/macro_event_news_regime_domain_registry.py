"""Phase 132: Macro/Event/News Regime Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)
from advanced_macro_event_news_regime.macro_event_news_regime_labels import (
    MACRO_EVENT_NEWS_REGIME_DOMAIN_LABELS,
)


def build_macro_event_news_regime_domain_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of all functional domains for Phase 132."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for idx, domain_label in enumerate(MACRO_EVENT_NEWS_REGIME_DOMAIN_LABELS):
        category = "core"
        if "macro" in domain_label:
            category = "macro"
        elif "event" in domain_label or "calendar" in domain_label:
            category = "event"
        elif "news" in domain_label:
            category = "news_metadata"
        elif "cross_asset" in domain_label or "transition" in domain_label:
            category = "linkage"
        elif "guard" in domain_label or "policy" in domain_label or "contract" in domain_label:
            category = "governance"
        elif "validation" in domain_label or "quality" in domain_label or "health" in domain_label or "safety" in domain_label:
            category = "assurance"

        rows.append(
            {
                "domain_index": idx + 1,
                "domain_label": domain_label,
                "category": category,
                "profile_name": p.profile_name,
                "non_signal": True,
                "source_preserved": True,
                "official_approval": False,
                "production_ready": False,
                "broker_ready": False,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_domains": len(df),
        "profile_name": p.profile_name,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_regime_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for domain registry DataFrame."""
    return {
        "total_domains": len(df),
        "categories": df["category"].nunique() if "category" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
