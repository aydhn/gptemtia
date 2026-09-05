"""Phase 131: FX/Macro Regime Context Registry.

Defines non-signal regime context mappings connecting FX pairs to macroeconomic indicators
(interest rates, inflation metrics, growth dynamics, release events, transition alignment).
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_cross_asset_regime_context.cross_asset_regime_config import (
    CrossAssetRegimeProfile,
    get_default_cross_asset_regime_profile,
)

FX_MACRO_CONTEXT_RECORDS: List[Dict[str, Any]] = [
    {
        "context_id": "fxm_rate_eurusd_fedfunds",
        "context_name": "EUR/USD to Fed Funds Interest Rate Context",
        "context_category": "fx_rate_context",
        "fx_entity": "fx_eurusd",
        "macro_entity": "macro_us_fedfunds",
        "description": "Monetary policy stance differential backdrop without trade signaling.",
        "readiness_score": 0.89,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxm_rate_usdjpy_fedfunds",
        "context_name": "USD/JPY to Fed Funds Policy Rate Differential Context",
        "context_category": "fx_rate_context",
        "fx_entity": "fx_usdjpy",
        "macro_entity": "macro_us_fedfunds",
        "description": "Yield curve policy differential mapping.",
        "readiness_score": 0.88,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxm_cpi_eurusd_cpi",
        "context_name": "EUR/USD to US CPI Inflation Context",
        "context_category": "fx_inflation_context",
        "fx_entity": "fx_eurusd",
        "macro_entity": "macro_us_cpi",
        "description": "Inflation regime pressure mapping against EUR/USD volatility.",
        "readiness_score": 0.87,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxm_growth_eurusd_gdp",
        "context_name": "EUR/USD to US GDP Growth Context",
        "context_category": "fx_growth_context",
        "fx_entity": "fx_eurusd",
        "macro_entity": "macro_us_gdp",
        "description": "Economic cycle regime alignment without directional bias.",
        "readiness_score": 0.85,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxm_release_eurusd_release_lag",
        "context_name": "EUR/USD Macro Release Window Alignment Context",
        "context_category": "fx_macro_release_context",
        "fx_entity": "fx_eurusd",
        "macro_entity": "macro_us_cpi",
        "description": "Verification of publication timestamp <= observation timestamp boundary.",
        "readiness_score": 0.90,
        "requires_no_lookahead": True,
    },
    {
        "context_id": "fxm_trans_eurusd_macro_state",
        "context_name": "EUR/USD to Macro Regime Transition Alignment",
        "context_category": "fx_macro_transition_context",
        "fx_entity": "fx_eurusd",
        "macro_entity": "macro_us_fedfunds",
        "description": "Alignment of currency trend exhaustion with macro tightening cycle transitions.",
        "readiness_score": 0.84,
        "requires_no_lookahead": True,
    },
]


def build_fx_macro_regime_context_registry(
    profile: Optional[CrossAssetRegimeProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build FX/Macro regime context registry dataframe and summary."""
    if profile is None:
        profile = get_default_cross_asset_regime_profile()

    rows = []
    for item in FX_MACRO_CONTEXT_RECORDS:
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
    summary = summarize_fx_macro_regime_context(df)
    summary["active_profile"] = profile.profile_name
    return df, summary


def summarize_fx_macro_regime_context(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FX/Macro regime context records."""
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
