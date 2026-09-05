"""Phase 131: Cross-Asset Regime Entity Registry.

Defines canonical multi-domain entities (FX pairs, commodity symbols, macro indicators,
calendar events, news metadata tags, regime families, candidate state contexts, transition contexts).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

CANONICAL_ENTITIES: List[Dict[str, Any]] = [
    # FX Pairs
    {
        "entity_id": "fx_eurusd",
        "entity_name": "EUR/USD Currency Pair",
        "entity_type": "fx_pair",
        "domain": "fx",
        "base_currency_or_asset": "EUR",
        "quote_or_benchmark": "USD",
        "source_phase": 107,
        "readiness_status": "ready",
    },
    {
        "entity_id": "fx_usdjpy",
        "entity_name": "USD/JPY Currency Pair",
        "entity_type": "fx_pair",
        "domain": "fx",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "JPY",
        "source_phase": 107,
        "readiness_status": "ready",
    },
    {
        "entity_id": "fx_gbpusd",
        "entity_name": "GBP/USD Currency Pair",
        "entity_type": "fx_pair",
        "domain": "fx",
        "base_currency_or_asset": "GBP",
        "quote_or_benchmark": "USD",
        "source_phase": 107,
        "readiness_status": "ready",
    },
    {
        "entity_id": "fx_audusd",
        "entity_name": "AUD/USD Currency Pair",
        "entity_type": "fx_pair",
        "domain": "fx",
        "base_currency_or_asset": "AUD",
        "quote_or_benchmark": "USD",
        "source_phase": 107,
        "readiness_status": "ready",
    },
    {
        "entity_id": "fx_usdtry",
        "entity_name": "USD/TRY Currency Pair",
        "entity_type": "fx_pair",
        "domain": "fx",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "TRY",
        "source_phase": 107,
        "readiness_status": "ready",
    },
    # Commodity Symbols
    {
        "entity_id": "cmd_xauusd",
        "entity_name": "Gold Spot Commodity",
        "entity_type": "commodity_symbol",
        "domain": "commodity",
        "base_currency_or_asset": "XAU",
        "quote_or_benchmark": "USD",
        "source_phase": 108,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cmd_xagusd",
        "entity_name": "Silver Spot Commodity",
        "entity_type": "commodity_symbol",
        "domain": "commodity",
        "base_currency_or_asset": "XAG",
        "quote_or_benchmark": "USD",
        "source_phase": 108,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cmd_brent",
        "entity_name": "Brent Crude Oil",
        "entity_type": "commodity_symbol",
        "domain": "commodity",
        "base_currency_or_asset": "BRENT",
        "quote_or_benchmark": "USD",
        "source_phase": 108,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cmd_wti",
        "entity_name": "WTI Crude Oil",
        "entity_type": "commodity_symbol",
        "domain": "commodity",
        "base_currency_or_asset": "WTI",
        "quote_or_benchmark": "USD",
        "source_phase": 108,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cmd_copper",
        "entity_name": "Copper Industrial Metal",
        "entity_type": "commodity_symbol",
        "domain": "commodity",
        "base_currency_or_asset": "COPPER",
        "quote_or_benchmark": "USD",
        "source_phase": 108,
        "readiness_status": "ready",
    },
    # Macro Indicators
    {
        "entity_id": "macro_us_fedfunds",
        "entity_name": "US Federal Funds Target Rate",
        "entity_type": "macro_indicator",
        "domain": "macro",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "PERCENT",
        "source_phase": 109,
        "readiness_status": "ready",
    },
    {
        "entity_id": "macro_us_cpi",
        "entity_name": "US Consumer Price Index YoY",
        "entity_type": "macro_indicator",
        "domain": "macro",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "INDEX",
        "source_phase": 109,
        "readiness_status": "ready",
    },
    {
        "entity_id": "macro_us_gdp",
        "entity_name": "US Real GDP Growth QoQ Annualized",
        "entity_type": "macro_indicator",
        "domain": "macro",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "PERCENT",
        "source_phase": 109,
        "readiness_status": "ready",
    },
    {
        "entity_id": "macro_eu_hicp",
        "entity_name": "Eurozone Harmonised Index of Consumer Prices",
        "entity_type": "macro_indicator",
        "domain": "macro",
        "base_currency_or_asset": "EUR",
        "quote_or_benchmark": "INDEX",
        "source_phase": 109,
        "readiness_status": "ready",
    },
    # Calendar Events
    {
        "entity_id": "cal_fomc_decision",
        "entity_name": "FOMC Interest Rate Decision Event",
        "entity_type": "calendar_event",
        "domain": "calendar",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "SCHEDULED_RELEASE",
        "source_phase": 110,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cal_us_nfp",
        "entity_name": "US Non-Farm Payrolls Release Event",
        "entity_type": "calendar_event",
        "domain": "calendar",
        "base_currency_or_asset": "USD",
        "quote_or_benchmark": "SCHEDULED_RELEASE",
        "source_phase": 110,
        "readiness_status": "ready",
    },
    {
        "entity_id": "cal_ecb_decision",
        "entity_name": "ECB Monetary Policy Decision Event",
        "entity_type": "calendar_event",
        "domain": "calendar",
        "base_currency_or_asset": "EUR",
        "quote_or_benchmark": "SCHEDULED_RELEASE",
        "source_phase": 110,
        "readiness_status": "ready",
    },
    # News Metadata Tags
    {
        "entity_id": "news_central_bank_rate",
        "entity_name": "Central Bank Interest Rate Topic Tag",
        "entity_type": "news_metadata_tag",
        "domain": "news_metadata",
        "base_currency_or_asset": "GLOBAL",
        "quote_or_benchmark": "TOPIC_TAG",
        "source_phase": 111,
        "readiness_status": "ready",
    },
    {
        "entity_id": "news_geopolitical_tension",
        "entity_name": "Geopolitical Tension Topic Tag",
        "entity_type": "news_metadata_tag",
        "domain": "news_metadata",
        "base_currency_or_asset": "GLOBAL",
        "quote_or_benchmark": "TOPIC_TAG",
        "source_phase": 111,
        "readiness_status": "ready",
    },
    {
        "entity_id": "news_energy_supply",
        "entity_name": "Energy Supply Shock Topic Tag",
        "entity_type": "news_metadata_tag",
        "domain": "news_metadata",
        "base_currency_or_asset": "GLOBAL",
        "quote_or_benchmark": "TOPIC_TAG",
        "source_phase": 111,
        "readiness_status": "ready",
    },
    # Regime Families
    {
        "entity_id": "regime_volatility_family",
        "entity_name": "Volatility Regime Family",
        "entity_type": "regime_family",
        "domain": "regime_foundation",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "VOL_STATE",
        "source_phase": 126,
        "readiness_status": "ready",
    },
    {
        "entity_id": "regime_trend_family",
        "entity_name": "Trend Regime Family",
        "entity_type": "regime_family",
        "domain": "regime_foundation",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "TREND_STATE",
        "source_phase": 126,
        "readiness_status": "ready",
    },
    {
        "entity_id": "regime_range_family",
        "entity_name": "Range & Consolidation Regime Family",
        "entity_type": "regime_family",
        "domain": "regime_foundation",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "RANGE_STATE",
        "source_phase": 126,
        "readiness_status": "ready",
    },
    # Candidate State Contexts
    {
        "entity_id": "candidate_high_vol",
        "entity_name": "High Volatility Candidate Context",
        "entity_type": "candidate_state_context",
        "domain": "candidate_state",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "THRESHOLD_CONTEXT",
        "source_phase": 128,
        "readiness_status": "ready",
    },
    {
        "entity_id": "candidate_trending",
        "entity_name": "Persistent Trend Candidate Context",
        "entity_type": "candidate_state_context",
        "domain": "candidate_state",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "DIRECTION_CONTEXT",
        "source_phase": 128,
        "readiness_status": "ready",
    },
    # Transition Contexts
    {
        "entity_id": "trans_compression_to_expansion",
        "entity_name": "Volatility Compression to Expansion Sequence",
        "entity_type": "transition_context",
        "domain": "regime_transition",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "TRANSITION_STATE",
        "source_phase": 130,
        "readiness_status": "ready",
    },
    {
        "entity_id": "trans_trend_exhaustion",
        "entity_name": "Trend Exhaustion to Range Sequence",
        "entity_type": "transition_context",
        "domain": "regime_transition",
        "base_currency_or_asset": "MULTI_ASSET",
        "quote_or_benchmark": "TRANSITION_STATE",
        "source_phase": 130,
        "readiness_status": "ready",
    },
]


def build_cross_asset_regime_entity_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build canonical multi-domain entity registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in CANONICAL_ENTITIES:
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
    summary = summarize_cross_asset_regime_entities(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_cross_asset_regime_entities(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize cross-asset regime entity distributions and safety flags."""
    type_counts = df["entity_type"].value_counts().to_dict() if not df.empty else {}
    domain_counts = df["domain"].value_counts().to_dict() if not df.empty else {}
    return {
        "total_entities": len(df),
        "entity_types": type_counts,
        "domains": domain_counts,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "all_source_preserved": bool(df["source_preserved"].all()) if not df.empty else True,
        "zero_target_or_prediction": True,
        "zero_trading_recommendations": True,
    }
