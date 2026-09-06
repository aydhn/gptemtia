"""Phase 132: Macro/Event/News Cross-Asset Context Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_macro_event_news_regime.macro_event_news_regime_config import (
    MacroEventNewsRegimeProfile,
    get_macro_event_news_regime_profile,
)

DEFAULT_CROSS_ASSET_CONTEXTS = [
    {
        "cross_asset_context_id": "casset_macro_fx_rate_diff",
        "context_name": "macro_fx_sensitivity_context",
        "target_asset_class": "forex",
        "related_indicator_id": "macro_us_fed_funds_rate",
        "sensitivity_level": "high",
        "transmission_channel": "monetary_policy_yield_differential",
        "description": "Interest rate differential sensitivity context for major currency pairs.",
    },
    {
        "cross_asset_context_id": "casset_macro_comm_growth",
        "context_name": "macro_commodity_sensitivity_context",
        "target_asset_class": "commodities",
        "related_indicator_id": "macro_cn_manufacturing_pmi",
        "sensitivity_level": "high",
        "transmission_channel": "global_manufacturing_demand",
        "description": "Global manufacturing demand sensitivity context for industrial commodities.",
    },
    {
        "cross_asset_context_id": "casset_event_fx_fomc",
        "context_name": "event_fx_context",
        "target_asset_class": "forex",
        "related_indicator_id": "event_fomc_rate_decision",
        "sensitivity_level": "critical",
        "transmission_channel": "fomc_scheduled_window",
        "description": "FOMC scheduled event window cross-impact context on EUR/USD.",
    },
    {
        "cross_asset_context_id": "casset_event_comm_cpi",
        "context_name": "event_commodity_context",
        "target_asset_class": "commodities",
        "related_indicator_id": "event_us_cpi_release",
        "sensitivity_level": "high",
        "transmission_channel": "inflation_repricing_gold_oil",
        "description": "US CPI release event window cross-impact context on Gold and Crude Oil.",
    },
    {
        "cross_asset_context_id": "casset_news_fx_meta",
        "context_name": "news_fx_metadata_context",
        "target_asset_class": "forex",
        "related_indicator_id": "news_asset_tag_eurusd",
        "sensitivity_level": "medium",
        "transmission_channel": "thematic_topic_volume",
        "description": "News metadata attention context across currency markets.",
    },
    {
        "cross_asset_context_id": "casset_news_comm_meta",
        "context_name": "news_commodity_metadata_context",
        "target_asset_class": "commodities",
        "related_indicator_id": "news_asset_tag_gold",
        "sensitivity_level": "medium",
        "transmission_channel": "thematic_topic_volume",
        "description": "News metadata attention context across precious metals and energy.",
    },
    {
        "cross_asset_context_id": "casset_macro_transition_dep",
        "context_name": "macro_cross_asset_transition_dependency",
        "target_asset_class": "multi_asset",
        "related_indicator_id": "macro_us_cpi_yoy",
        "sensitivity_level": "high",
        "transmission_channel": "joint_regime_state_transition",
        "description": "Cross-asset regime transition alignment dependency for Phase 130/131 coupling.",
    },
]


def build_macro_event_news_cross_asset_context_registry(
    profile: Optional[MacroEventNewsRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry DataFrame of macro/event/news cross-asset contexts."""
    p = profile or get_macro_event_news_regime_profile()
    rows = []
    for item in DEFAULT_CROSS_ASSET_CONTEXTS:
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
        "total_cross_asset_contexts": len(df),
        "target_asset_classes": df["target_asset_class"].unique().tolist(),
        "all_non_signal": True,
        "all_source_preserved": True,
    }
    return df, summary


def summarize_macro_event_news_cross_asset_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Return summary dictionary for cross-asset context registry."""
    return {
        "total_contexts": len(df),
        "asset_classes": df["target_asset_class"].nunique() if "target_asset_class" in df.columns else 0,
        "all_non_signal": bool(df["non_signal"].all()) if "non_signal" in df.columns else True,
    }
