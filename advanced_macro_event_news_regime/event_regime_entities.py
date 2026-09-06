"""Phase 132: Event Regime Entity Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_EVENT_ENTITIES = [
    {
        "event_id": "event_fomc_rate_decision",
        "event_name": "FOMC Rate Decision & Statement",
        "entity_type": "calendar_event",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "critical",
        "pre_event_window_minutes": 120,
        "post_event_window_minutes": 240,
    },
    {
        "event_id": "event_us_cpi_release",
        "event_name": "US CPI Scheduled Release",
        "entity_type": "scheduled_release",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "high",
        "pre_event_window_minutes": 60,
        "post_event_window_minutes": 120,
    },
    {
        "event_id": "event_us_nfp_actual",
        "event_name": "US NFP Actual Publication Timestamp",
        "entity_type": "actual_release",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "high",
        "pre_event_window_minutes": 60,
        "post_event_window_minutes": 120,
    },
    {
        "event_id": "event_ecb_monetary_policy",
        "event_name": "ECB Monetary Policy Decision",
        "entity_type": "event_window",
        "country_code": "EU",
        "currency_code": "EUR",
        "importance_level": "critical",
        "pre_event_window_minutes": 90,
        "post_event_window_minutes": 180,
    },
    {
        "event_id": "event_pre_fomc_quiet_window",
        "event_name": "Pre-FOMC Blackout Regime Window",
        "entity_type": "pre_event_window",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "medium",
        "pre_event_window_minutes": 1440,
        "post_event_window_minutes": 0,
    },
    {
        "event_id": "event_post_cpi_absorption_window",
        "event_name": "Post-CPI Market Digestion Window",
        "entity_type": "post_event_window",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "medium",
        "pre_event_window_minutes": 0,
        "post_event_window_minutes": 360,
    },
    {
        "event_id": "event_gdp_quarterly_lag_tracker",
        "event_name": "Quarterly GDP Release Lag Entity",
        "entity_type": "release_lag",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "medium",
        "pre_event_window_minutes": 0,
        "post_event_window_minutes": 0,
    },
    {
        "event_id": "event_importance_tier_classification",
        "event_name": "Economic Calendar Importance Tier Hierarchy",
        "entity_type": "event_importance",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "importance_level": "info",
        "pre_event_window_minutes": 0,
        "post_event_window_minutes": 0,
    },
    {
        "event_id": "event_jurisdiction_country_map",
        "event_name": "Macro Economic Jurisdiction Country Registry",
        "entity_type": "event_country",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "importance_level": "info",
        "pre_event_window_minutes": 0,
        "post_event_window_minutes": 0,
    },
    {
        "event_id": "event_currency_exposure_map",
        "event_name": "Major FX Pair Economic Currency Registry",
        "entity_type": "event_currency",
        "country_code": "GLOBAL",
        "currency_code": "MULTI",
        "importance_level": "info",
        "pre_event_window_minutes": 0,
        "post_event_window_minutes": 0,
    },
]


def build_event_regime_entity_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of economic calendar and event regime entities."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_EVENT_ENTITIES:
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
        "total_event_entities": len(df),
        "entity_types": df["entity_type"].unique().tolist(),
        "importance_levels": df["importance_level"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_event_regime_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for event regime entities."""
    return {
        "total_event_entities": len(df),
        "entity_types": df["entity_type"].nunique() if "entity_type" in df.columns else 0,
        "critical_events": int((df["importance_level"] == "critical").sum()) if "importance_level" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
