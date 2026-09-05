"""Cross-domain context fusion engine.

Safely merges base aligned market feature dataframes (FX, Commodities)
with Macroeconomic indicators, Calendar events, and News metadata.
Strictly non-signal, metadata-only, backward-only asof join, no lookahead.
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


def fuse_cross_domain_context(
    base_df: pd.DataFrame,
    macro_df: Optional[pd.DataFrame] = None,
    calendar_df: Optional[pd.DataFrame] = None,
    news_metadata_df: Optional[pd.DataFrame] = None,
    timestamp_col: str = "timestamp",
    macro_release_col: str = "macro_release_timestamp",
    calendar_release_col: str = "calendar_release_timestamp",
    news_published_col: str = "news_published_timestamp",
) -> pd.DataFrame:
    """Safely fuse base aligned market feature dataframe with macro, calendar, and news metadata.

    All joins are strictly backward-in-time asof joins.
    """
    if base_df.empty:
        return base_df.copy()

    validate_no_forbidden_fusion_columns(base_df)
    fused = base_df.copy()

    # 1. Macro fusion
    if macro_df is not None and not macro_df.empty:
        validate_no_forbidden_fusion_columns(macro_df)
        m_col = macro_release_col if macro_release_col in macro_df.columns else "timestamp"
        fused = safe_fusion_asof_join_backward(
            left_df=fused,
            right_df=macro_df,
            left_on=timestamp_col,
            right_on=m_col,
        )
        validate_no_future_fusion_join(fused, base_timestamp_col=timestamp_col, release_timestamp_col=m_col)
        validate_no_forbidden_fusion_columns(fused)

    # 2. Calendar fusion
    if calendar_df is not None and not calendar_df.empty:
        validate_no_forbidden_fusion_columns(calendar_df)
        c_col = calendar_release_col if calendar_release_col in calendar_df.columns else "release_timestamp"
        if c_col not in calendar_df.columns and "timestamp" in calendar_df.columns:
            c_col = "timestamp"
        fused = safe_fusion_asof_join_backward(
            left_df=fused,
            right_df=calendar_df,
            left_on=timestamp_col,
            right_on=c_col,
        )
        validate_no_future_fusion_join(fused, base_timestamp_col=timestamp_col, release_timestamp_col=c_col)
        validate_no_forbidden_fusion_columns(fused)

    # 3. News metadata fusion
    if news_metadata_df is not None and not news_metadata_df.empty:
        validate_no_forbidden_fusion_columns(news_metadata_df)
        validate_no_full_article_columns(news_metadata_df)
        validate_news_metadata_only_dataframe(news_metadata_df)
        n_col = news_published_col if news_published_col in news_metadata_df.columns else "published_timestamp"
        if n_col not in news_metadata_df.columns and "timestamp" in news_metadata_df.columns:
            n_col = "timestamp"
        fused = safe_fusion_asof_join_backward(
            left_df=fused,
            right_df=news_metadata_df,
            left_on=timestamp_col,
            right_on=n_col,
        )
        validate_no_future_fusion_join(fused, base_timestamp_col=timestamp_col, release_timestamp_col=n_col)
        validate_no_forbidden_fusion_columns(fused)
        validate_no_full_article_columns(fused)

    return fused


def get_cross_domain_context_fusion_summary() -> Dict[str, Any]:
    """Summary of cross-domain context fusion engine."""
    return {
        "engine": "cross_domain_context_fusion",
        "purpose": "Multi-domain context representation linking FX/Commodity with Macro, Calendar, and News metadata.",
        "join_policy": "backward_only_asof",
        "no_lookahead": True,
        "is_signal": False,
        "strictly_metadata_only": True,
        "research_only": True,
    }
