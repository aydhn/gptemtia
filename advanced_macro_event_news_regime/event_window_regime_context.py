"""Phase 132: Event Window Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_EVENT_WINDOWS = [
    {
        "window_id": "win_fomc_complete_regime",
        "event_id": "event_fomc_rate_decision",
        "pre_window_mins": 120,
        "post_window_mins": 240,
        "total_window_mins": 360,
        "window_state": "active_window_context",
        "description": "FOMC rate announcement buffer window.",
    },
    {
        "window_id": "win_cpi_complete_regime",
        "event_id": "event_us_cpi_release",
        "pre_window_mins": 60,
        "post_window_mins": 120,
        "total_window_mins": 180,
        "window_state": "active_window_context",
        "description": "US CPI release buffer window.",
    },
    {
        "window_id": "win_nfp_complete_regime",
        "event_id": "event_us_nfp_actual",
        "pre_window_mins": 60,
        "post_window_mins": 120,
        "total_window_mins": 180,
        "window_state": "active_window_context",
        "description": "US NFP release buffer window.",
    },
    {
        "window_id": "win_ecb_complete_regime",
        "event_id": "event_ecb_monetary_policy",
        "pre_window_mins": 90,
        "post_window_mins": 180,
        "total_window_mins": 270,
        "window_state": "active_window_context",
        "description": "ECB policy decision buffer window.",
    },
]


def build_event_window_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of event window regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_EVENT_WINDOWS:
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
        "total_event_windows": len(df),
        "mean_window_duration": float(df["total_window_mins"].mean()) if "total_window_mins" in df.columns else 0.0,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_event_window_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for event window context."""
    return {
        "total_event_windows": len(df),
        "mean_total_mins": float(df["total_window_mins"].mean()) if "total_window_mins" in df.columns else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
