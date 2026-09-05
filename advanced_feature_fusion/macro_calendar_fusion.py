"""Macro and Economic Calendar Cross-Domain Fusion.

Integrates macroeconomic series with calendar release event context.
Strictly non-signal, backward-only join, research use only.
"""

from typing import Any, Dict, Optional
import pandas as pd
from advanced_feature_fusion.fusion_asof_join_policies import safe_fusion_asof_join_backward
from advanced_feature_fusion.no_lookahead_fusion_guard import validate_no_future_fusion_join, validate_no_forbidden_fusion_columns


def fuse_macro_with_calendar(
    macro_df: pd.DataFrame,
    calendar_df: pd.DataFrame,
    macro_timestamp_col: str = "timestamp",
    calendar_release_col: str = "release_timestamp",
    by: Optional[str] = "macro_indicator_id",
    calendar_by: Optional[str] = "event_macro_indicator_id",
) -> pd.DataFrame:
    """Safely fuse macroeconomic base records with calendar release events using backward-only asof join.

    Base records (macro_df) are matched with the most recent prior calendar release event.
    """
    if macro_df.empty:
        return macro_df.copy()
    if calendar_df.empty:
        return macro_df.copy()

    # Pre-validation
    validate_no_forbidden_fusion_columns(macro_df)
    validate_no_forbidden_fusion_columns(calendar_df)

    # Rename calendar_by to match by if both provided and different
    cal_copy = calendar_df.copy()
    join_by = by
    if by and calendar_by and by != calendar_by:
        if calendar_by in cal_copy.columns:
            cal_copy[by] = cal_copy[calendar_by]

    fused = safe_fusion_asof_join_backward(
        left_df=macro_df,
        right_df=cal_copy,
        left_on=macro_timestamp_col,
        right_on=calendar_release_col,
        by=join_by,
    )

    validate_no_future_fusion_join(fused, base_timestamp_col=macro_timestamp_col, release_timestamp_col=calendar_release_col)
    validate_no_forbidden_fusion_columns(fused)

    return fused


def get_macro_calendar_fusion_summary() -> Dict[str, Any]:
    """Summary of Macro-Calendar fusion specification."""
    return {
        "fusion_type": "macro_calendar_cross_domain",
        "description": "Cross-fuses macro timeseries with economic calendar releases via backward-only asof join.",
        "join_direction": "backward",
        "no_lookahead_guaranteed": True,
        "is_signal": False,
        "policy": "release_timestamp <= macro_timestamp",
    }
