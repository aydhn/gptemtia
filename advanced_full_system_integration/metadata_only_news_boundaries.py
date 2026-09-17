# -*- coding: utf-8 -*-
"""Phase 158: Metadata-Only News Boundaries.

Prohibits storing or processing copyrighted full news articles or scraped HTML bodies.
"""

from typing import Any, Dict, Tuple
import pandas as pd

from .full_system_integration_config import FullSystemIntegrationProfile
from .full_system_integration_models import SystemBoundaryItem

NEWS_RULES = [
    ("NMD-001", "news_metadata_boundary", "no_full_text_storage", "storage", False, "Storing full text or article bodies is strictly prohibited."),
    ("NMD-002", "news_metadata_boundary", "no_scraped_html_storage", "storage", False, "Storing raw scraped HTML or page dumps is prohibited."),
    ("NMD-003", "news_metadata_boundary", "no_vector_embedding_storage", "storage", False, "Storing heavy embedding vectors is prohibited."),
    ("NMD-004", "news_metadata_boundary", "allow_metadata_headers_only", "pipeline", True, "Only headline, timestamp, source, and category metadata are permitted."),
]


def build_metadata_only_news_boundary_registry(
    profile: FullSystemIntegrationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build metadata-only news boundary registry DataFrame and summary."""
    items = []
    for bid, btype, rname, atype, is_allowed, reason in NEWS_RULES:
        item = SystemBoundaryItem(
            boundary_id=bid,
            boundary_type=btype,
            rule_name=rname,
            action_type=atype,
            is_allowed=is_allowed,
            reason=reason,
        )
        items.append(item.__dict__)

    df = pd.DataFrame(items)
    summary = {
        "active_profile": profile.profile_name,
        "total_rules": len(df),
        "prohibited_actions_count": int((df["is_allowed"] == False).sum()),
        "allowed_actions_count": int((df["is_allowed"] == True).sum()),
        "status": "full_system_integration_ready",
        "non_signal": True,
    }
    return df, summary
