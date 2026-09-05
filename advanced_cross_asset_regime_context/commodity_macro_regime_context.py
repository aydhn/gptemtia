"""Phase 131: Commodity/Macro Regime Context Registry.

Defines non-signal regime context mappings connecting commodity symbols to macroeconomic
indicators (inflation hedges, economic growth demand, interest rates, release lag, transitions).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

COMMODITY_MACRO_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "context_id": "cmdm_inf_xauusd_cpi",
        "context_name": "Gold to US CPI Inflation Regime Context",
        "context_category": "commodity_inflation_context",
        "commodity_entity": "cmd_xauusd",
        "macro_entity": "macro_us_cpi",
        "description": "Historical inflation hedge sensitivity context without directional forecast.",
        "readiness_score": 0.91,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "cmdm_growth_copper_gdp",
        "context_name": "Copper to Global GDP Growth Regime Context",
        "context_category": "commodity_growth_context",
        "commodity_entity": "cmd_copper",
        "macro_entity": "macro_us_gdp",
        "description": "Industrial metal economic expansion/contraction regime linkage.",
        "readiness_score": 0.86,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "cmdm_growth_brent_gdp",
        "context_name": "Brent Crude to GDP Growth Regime Context",
        "context_category": "commodity_growth_context",
        "commodity_entity": "cmd_brent",
        "macro_entity": "macro_us_gdp",
        "description": "Energy consumption regime sensitivity mapping.",
        "readiness_score": 0.87,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "cmdm_rate_xauusd_fedfunds",
        "context_name": "Gold to Fed Funds Real Rate Pressure Context",
        "context_category": "commodity_rate_context",
        "commodity_entity": "cmd_xauusd",
        "macro_entity": "macro_us_fedfunds",
        "description": "Opportunity cost regime backdrop for non-yielding bullion.",
        "readiness_score": 0.89,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "cmdm_release_copper_release_lag",
        "context_name": "Copper Macro Release Lag Guard Context",
        "context_category": "commodity_macro_release_context",
        "commodity_entity": "cmd_copper",
        "macro_entity": "macro_us_gdp",
        "description": "Verification that macro releases respect publication delays.",
        "readiness_score": 0.90,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "cmdm_trans_xauusd_macro_state",
        "context_name": "Gold to Macro Regime Transition Alignment",
        "context_category": "commodity_macro_transition_context",
        "commodity_entity": "cmd_xauusd",
        "macro_entity": "macro_us_cpi",
        "description": "Transition alignment between inflation regime shifts and precious metal volatility.",
        "readiness_score": 0.85,
        "requires_no_lookahead": True,
    },
]


def build_commodity_macro_regime_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Commodity/Macro regime context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in COMMODITY_MACRO_CONTEXT_RECORDS:
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
    summary = summarize_commodity_macro_regime_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_commodity_macro_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize Commodity/Macro regime context records."""
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
