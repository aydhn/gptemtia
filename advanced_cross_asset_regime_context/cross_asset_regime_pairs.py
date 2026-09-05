"""Phase 131: Cross-Asset Regime Pair Registry.

Defines canonical entity pair relationships across FX, commodities, macro indicators,
calendar events, news metadata, and regime transition sequences.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CANONICAL_PAIRS: List[Dict[str, Any]] = [
    {
        "pair_id": "pair_fx_eurusd_to_cmd_xauusd",
        "left_entity_id": "fx_eurusd",
        "left_entity_type": "fx_pair",
        "right_entity_id": "cmd_xauusd",
        "right_entity_type": "commodity_symbol",
        "relationship_category": "fx_pair_to_commodity_symbol",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_fx_audusd_to_cmd_copper",
        "left_entity_id": "fx_audusd",
        "left_entity_type": "fx_pair",
        "right_entity_id": "cmd_copper",
        "right_entity_type": "commodity_symbol",
        "relationship_category": "fx_pair_to_commodity_symbol",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_fx_usdjpy_to_cmd_xauusd",
        "left_entity_id": "fx_usdjpy",
        "left_entity_type": "fx_pair",
        "right_entity_id": "cmd_xauusd",
        "right_entity_type": "commodity_symbol",
        "relationship_category": "fx_pair_to_commodity_symbol",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_cmd_xauusd_to_macro_us_cpi",
        "left_entity_id": "cmd_xauusd",
        "left_entity_type": "commodity_symbol",
        "right_entity_id": "macro_us_cpi",
        "right_entity_type": "macro_indicator",
        "relationship_category": "commodity_symbol_to_macro_indicator",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_release_lag_guarded",
    },
    {
        "pair_id": "pair_cmd_brent_to_macro_us_gdp",
        "left_entity_id": "cmd_brent",
        "left_entity_type": "commodity_symbol",
        "right_entity_id": "macro_us_gdp",
        "right_entity_type": "macro_indicator",
        "relationship_category": "commodity_symbol_to_macro_indicator",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_release_lag_guarded",
    },
    {
        "pair_id": "pair_fx_eurusd_to_macro_us_fedfunds",
        "left_entity_id": "fx_eurusd",
        "left_entity_type": "fx_pair",
        "right_entity_id": "macro_us_fedfunds",
        "right_entity_type": "macro_indicator",
        "relationship_category": "fx_pair_to_macro_indicator",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_release_lag_guarded",
    },
    {
        "pair_id": "pair_fx_eurusd_to_macro_eu_hicp",
        "left_entity_id": "fx_eurusd",
        "left_entity_type": "fx_pair",
        "right_entity_id": "macro_eu_hicp",
        "right_entity_type": "macro_indicator",
        "relationship_category": "fx_pair_to_macro_indicator",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_release_lag_guarded",
    },
    {
        "pair_id": "pair_macro_us_fedfunds_to_cal_fomc_decision",
        "left_entity_id": "macro_us_fedfunds",
        "left_entity_type": "macro_indicator",
        "right_entity_id": "cal_fomc_decision",
        "right_entity_type": "calendar_event",
        "relationship_category": "macro_indicator_to_calendar_event",
        "timestamp_alignment_policy": "utc_event_window_alignment",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_cal_fomc_decision_to_news_central_bank_rate",
        "left_entity_id": "cal_fomc_decision",
        "left_entity_type": "calendar_event",
        "right_entity_id": "news_central_bank_rate",
        "right_entity_type": "news_metadata_tag",
        "relationship_category": "calendar_event_to_news_metadata_tag",
        "timestamp_alignment_policy": "utc_metadata_window_alignment",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_fx_eurusd_to_cross_asset_context",
        "left_entity_id": "fx_eurusd",
        "left_entity_type": "fx_pair",
        "right_entity_id": "regime_volatility_family",
        "right_entity_type": "cross_asset_context",
        "relationship_category": "fx_pair_to_cross_asset_context",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_cmd_xauusd_to_cross_asset_context",
        "left_entity_id": "cmd_xauusd",
        "left_entity_type": "commodity_symbol",
        "right_entity_id": "regime_range_family",
        "right_entity_type": "cross_asset_context",
        "relationship_category": "commodity_symbol_to_cross_asset_context",
        "timestamp_alignment_policy": "utc_backward_asof",
        "asof_join_policy": "backward_exact_or_prior",
    },
    {
        "pair_id": "pair_regime_volatility_to_transition_context",
        "left_entity_id": "regime_volatility_family",
        "left_entity_type": "regime_family",
        "right_entity_id": "trans_compression_to_expansion",
        "right_entity_type": "transition_context",
        "relationship_category": "regime_family_to_transition_context",
        "timestamp_alignment_policy": "utc_sequence_continuity",
        "asof_join_policy": "backward_exact_or_prior",
    },
]


def build_cross_asset_regime_pair_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build canonical multi-asset regime pair registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CANONICAL_PAIRS:
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
    summary = summarize_cross_asset_regime_pairs(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_regime_pairs(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset pair registry metrics and safety compliance."""
    category_counts = df["relationship_category"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_pairs": len(df),
        "relationship_categories": category_counts,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_target_or_prediction": True,
        "zero_trading_recommendations": True,
        "zero_arbitrage_claims": True,
    }
