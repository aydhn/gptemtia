"""Phase 132: Release Lag Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_RELEASE_LAGS = [
    {
        "lag_id": "lag_us_gdp",
        "indicator_id": "macro_us_real_gdp_qoq",
        "reference_period": "quarterly",
        "nominal_lag_days": 30,
        "max_tolerated_lag_days": 60,
        "lag_category": "high_lag_context",
        "requires_asof_backward_guard": True,
    },
    {
        "lag_id": "lag_us_cpi",
        "indicator_id": "macro_us_cpi_yoy",
        "reference_period": "monthly",
        "nominal_lag_days": 14,
        "max_tolerated_lag_days": 25,
        "lag_category": "medium_lag_context",
        "requires_asof_backward_guard": True,
    },
    {
        "lag_id": "lag_us_nfp",
        "indicator_id": "macro_us_nfp",
        "reference_period": "monthly",
        "nominal_lag_days": 7,
        "max_tolerated_lag_days": 15,
        "lag_category": "low_lag_context",
        "requires_asof_backward_guard": True,
    },
    {
        "lag_id": "lag_cn_pmi",
        "indicator_id": "macro_cn_manufacturing_pmi",
        "reference_period": "monthly",
        "nominal_lag_days": 1,
        "max_tolerated_lag_days": 5,
        "lag_category": "minimal_lag_context",
        "requires_asof_backward_guard": True,
    },
]


def build_release_lag_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of release lag regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_RELEASE_LAGS:
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
        "total_release_lag_entries": len(df),
        "mean_lag_days": float(df["nominal_lag_days"].mean()) if "nominal_lag_days" in df.columns else 0.0,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_release_lag_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for release lag context."""
    return {
        "total_lag_entries": len(df),
        "max_nominal_lag": int(df["nominal_lag_days"].max()) if "nominal_lag_days" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
