"""Phase 131: Macro/Calendar Cross-Asset Context Registry.

Defines non-signal cross-asset context records for macro release windows, scheduled
events, actual publication timestamps, and release lag guard boundaries.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

MACRO_CALENDAR_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "context_id": "mcal_rel_fomc_fedfunds",
        "context_name": "FOMC Rate Decision Release Calendar Context",
        "context_category": "macro_release_calendar_context",
        "macro_indicator": "macro_us_fedfunds",
        "calendar_event": "cal_fomc_decision",
        "description": "Mapping scheduled central bank interest rate announcement dates to regime timelines.",
        "readiness_score": 0.92,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "mcal_window_pre_post_fomc",
        "context_name": "Pre/Post Event Window Cross-Asset Volatility Context",
        "context_category": "macro_event_window_cross_asset_context",
        "macro_indicator": "macro_us_fedfunds",
        "calendar_event": "cal_fomc_decision",
        "description": "Pre-event compression and post-event realization window context across FX and Gold.",
        "readiness_score": 0.88,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "mcal_alignment_nfp_scheduled",
        "context_name": "Scheduled vs Actual Release Timestamp Alignment Context",
        "context_category": "scheduled_actual_release_alignment_context",
        "macro_indicator": "macro_us_cpi",
        "calendar_event": "cal_us_nfp",
        "description": "Audit trail verifying that actual publication timestamps do not leak into earlier bars.",
        "readiness_score": 0.94,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "mcal_lag_guard_cross_asset",
        "context_name": "Release Lag Guard Enforcement Context",
        "context_category": "release_lag_cross_asset_context",
        "macro_indicator": "macro_us_gdp",
        "calendar_event": "cal_fomc_decision",
        "description": "Explicit verification that lag-tolerant backward asof join is enforced.",
        "readiness_score": 0.93,
        "requires_no_lookahead": True,
    },
]


def build_macro_calendar_cross_asset_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Macro/Calendar cross-asset context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in MACRO_CALENDAR_CONTEXT_RECORDS:
        row = dict(item)
        row["non_signal"] = True
        row["source_preserved"] = True
        row["official_approval"] = False
        row["production_ready"] = False
        row["broker_ready"] = False
        row["contains_target_or_prediction"] = False
        row["contains_trading_recommendation"] = False
        rows.append(row)

    df = pd.DataFrame(rows)
    summary = summarize_macro_calendar_cross_asset_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_macro_calendar_cross_asset_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Macro/Calendar cross-asset context records."""
    cat_counts = df["context_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_records": len(df),
        "context_categories": cat_counts,
        "mean_readiness_score": float(df["readiness_score"].mean()) if not df.empty else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_trading_signals": True,
        "zero_predictions": True,
    }
