"""Phase 132: Pre-Event Regime Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_PRE_EVENT_CONTEXTS = [
    {
        "pre_event_id": "pre_fomc_anticipation",
        "event_id": "event_fomc_rate_decision",
        "buffer_minutes": 120,
        "anticipation_tier": "heightened_uncertainty_context",
        "liquidity_adjustment_flag": True,
        "description": "Pre-FOMC window where price discovery regime typically exhibits compression.",
    },
    {
        "pre_event_id": "pre_cpi_anticipation",
        "event_id": "event_us_cpi_release",
        "buffer_minutes": 60,
        "anticipation_tier": "data_sensitive_context",
        "liquidity_adjustment_flag": True,
        "description": "Pre-CPI data release regime window.",
    },
    {
        "pre_event_id": "pre_nfp_anticipation",
        "event_id": "event_us_nfp_actual",
        "buffer_minutes": 60,
        "anticipation_tier": "data_sensitive_context",
        "liquidity_adjustment_flag": True,
        "description": "Pre-NFP employment release window.",
    },
]


def build_pre_event_regime_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of pre-event regime contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_PRE_EVENT_CONTEXTS:
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
        "total_pre_event_contexts": len(df),
        "mean_pre_buffer_mins": float(df["buffer_minutes"].mean()) if "buffer_minutes" in df.columns else 0.0,
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_pre_event_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for pre-event context."""
    return {
        "total_pre_events": len(df),
        "anticipation_tiers": df["anticipation_tier"].nunique() if "anticipation_tier" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
