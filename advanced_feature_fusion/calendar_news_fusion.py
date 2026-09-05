"""Calendar and News Metadata Cross-Domain Fusion.

Integrates economic calendar events with news metadata (event linkage, tags, timestamps).
Strictly metadata-only, non-signal, backward-only join, research use only.
"""

from typing import Any, Dict, Optional
import pandas as pd
from advanced_feature_fusion.fusion_asof_join_policies import safe_fusion_asof_join_backward
from advanced_feature_fusion.no_lookahead_fusion_guard import (
    validate_no_future_fusion_join,
    validate_no_forbidden_fusion_columns,
    validate_no_full_article_columns,
)
from advanced_feature_fusion.news_metadata_only_fusion_policies import validate_news_metadata_only_dataframe


def fuse_calendar_with_news_metadata(
    calendar_df: pd.DataFrame,
    news_metadata_df: pd.DataFrame,
    calendar_timestamp_col: str = "release_timestamp",
    news_published_col: str = "published_timestamp",
    by: Optional[str] = "event_id",
    news_by: Optional[str] = "event_linkage_id",
) -> pd.DataFrame:
    """Safely fuse calendar event base records with news metadata using backward-only asof join.

    Ensures strictly metadata only (no full text, no scraping) and no lookahead.
    """
    if calendar_df.empty:
        return calendar_df.copy()
    if news_metadata_df.empty:
        return calendar_df.copy()

    # Pre-validation
    validate_no_forbidden_fusion_columns(calendar_df)
    validate_no_forbidden_fusion_columns(news_metadata_df)
    validate_no_full_article_columns(news_metadata_df)
    validate_news_metadata_only_dataframe(news_metadata_df)

    news_copy = news_metadata_df.copy()
    join_by = by
    if by and news_by and by != news_by:
        if news_by in news_copy.columns:
            news_copy[by] = news_copy[news_by]

    fused = safe_fusion_asof_join_backward(
        left_df=calendar_df,
        right_df=news_copy,
        left_on=calendar_timestamp_col,
        right_on=news_published_col,
        by=join_by,
    )

    validate_no_future_fusion_join(fused, base_timestamp_col=calendar_timestamp_col, release_timestamp_col=news_published_col)
    validate_no_forbidden_fusion_columns(fused)
    validate_no_full_article_columns(fused)

    return fused


def get_calendar_news_fusion_summary() -> Dict[str, Any]:
    """Summary of Calendar-News metadata fusion specification."""
    return {
        "fusion_type": "calendar_news_metadata_cross_domain",
        "description": "Cross-fuses economic calendar events with news metadata linkage via backward-only asof join.",
        "join_direction": "backward",
        "strictly_metadata_only": True,
        "no_lookahead_guaranteed": True,
        "is_signal": False,
        "policy": "news_published_timestamp <= calendar_release_timestamp",
    }
