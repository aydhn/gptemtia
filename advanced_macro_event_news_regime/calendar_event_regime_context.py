"""Phase 132: Calendar Event Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_CALENDAR_EVENT_CONTEXTS = [
    {
        "calendar_context_id": "cal_ctx_fomc",
        "event_id": "event_fomc_rate_decision",
        "event_name": "FOMC Rate Decision",
        "jurisdiction": "US",
        "currency": "USD",
        "importance": "critical",
        "regular_schedule": "8_times_per_year",
        "event_window_minutes": 360,
    },
    {
        "calendar_context_id": "cal_ctx_us_cpi",
        "event_id": "event_us_cpi_release",
        "event_name": "US CPI Release",
        "jurisdiction": "US",
        "currency": "USD",
        "importance": "high",
        "regular_schedule": "monthly",
        "event_window_minutes": 180,
    },
    {
        "calendar_context_id": "cal_ctx_us_nfp",
        "event_id": "event_us_nfp_actual",
        "event_name": "US NFP Release",
        "jurisdiction": "US",
        "currency": "USD",
        "importance": "high",
        "regular_schedule": "first_friday_monthly",
        "event_window_minutes": 180,
    },
    {
        "calendar_context_id": "cal_ctx_ecb_decision",
        "event_id": "event_ecb_monetary_policy",
        "event_name": "ECB Monetary Policy Meeting",
        "jurisdiction": "EU",
        "currency": "EUR",
        "importance": "critical",
        "regular_schedule": "8_times_per_year",
        "event_window_minutes": 270,
    },
]


def build_calendar_event_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of calendar event regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_CALENDAR_EVENT_CONTEXTS:
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
        "total_calendar_events": len(df),
        "jurisdictions": df["jurisdiction"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_calendar_event_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for calendar event context."""
    return {
        "total_calendar_events": len(df),
        "critical_events": int((df["importance"] == "critical").sum()) if "importance" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
