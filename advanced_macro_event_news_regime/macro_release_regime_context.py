"""Phase 132: Macro Release Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_MACRO_RELEASE_CONTEXTS = [
    {
        "release_context_id": "rel_ctx_us_cpi",
        "context_name": "scheduled_release_context",
        "indicator_id": "macro_us_cpi_yoy",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "high",
        "scheduled_time_utc": "13:30:00",
        "release_day_of_month": 12,
        "release_lag_days": 14,
    },
    {
        "release_context_id": "rel_ctx_us_nfp",
        "context_name": "actual_release_context",
        "indicator_id": "macro_us_nfp",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "high",
        "scheduled_time_utc": "13:30:00",
        "release_day_of_month": 5,
        "release_lag_days": 7,
    },
    {
        "release_context_id": "rel_ctx_fomc_statement",
        "context_name": "release_timestamp_context",
        "indicator_id": "macro_us_fed_funds_rate",
        "country_code": "US",
        "currency_code": "USD",
        "importance_level": "critical",
        "scheduled_time_utc": "19:00:00",
        "release_day_of_month": 18,
        "release_lag_days": 0,
    },
    {
        "release_context_id": "rel_ctx_eu_hicp",
        "context_name": "release_country_currency_context",
        "indicator_id": "macro_eu_hicp_yoy",
        "country_code": "EU",
        "currency_code": "EUR",
        "importance_level": "high",
        "scheduled_time_utc": "10:00:00",
        "release_day_of_month": 16,
        "release_lag_days": 16,
    },
    {
        "release_context_id": "rel_ctx_cn_pmi",
        "context_name": "release_importance_context",
        "indicator_id": "macro_cn_manufacturing_pmi",
        "country_code": "CN",
        "currency_code": "CNY",
        "importance_level": "high",
        "scheduled_time_utc": "01:30:00",
        "release_day_of_month": 31,
        "release_lag_days": 1,
    },
]


def build_macro_release_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro release regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_MACRO_RELEASE_CONTEXTS:
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
        "total_release_contexts": len(df),
        "countries": df["country_code"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_release_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for macro release context."""
    return {
        "total_release_contexts": len(df),
        "mean_lag_days": float(df["release_lag_days"].mean()) if "release_lag_days" in df.columns else 0.0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
